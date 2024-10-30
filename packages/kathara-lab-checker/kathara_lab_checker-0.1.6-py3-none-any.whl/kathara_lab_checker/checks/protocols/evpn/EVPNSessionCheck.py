import json

from Kathara.exceptions import MachineNotRunningError
from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab

from ...AbstractCheck import AbstractCheck
from ...CheckResult import CheckResult
from ....utils import get_output


class EVPNSessionCheck(AbstractCheck):
    def check(self, device_name: str, neighbor: str, lab: Lab) -> CheckResult:
        kathara_manager: Kathara = Kathara.get_instance()
        try:
            exec_output_gen = kathara_manager.exec(
                machine_name=device_name, command="vtysh -e 'show bgp summary json'", lab_hash=lab.hash
            )
        except MachineNotRunningError as e:
            return CheckResult(self.description, False, str(e))

        output = get_output(exec_output_gen)

        if output.startswith("ERROR:") or "exec failed" in output:
            return CheckResult(self.description, False, output)
        output = json.loads(output)
        if "l2VpnEvpn" in output:
            try:
                for peer_name, peer in output["l2VpnEvpn"]["peers"].items():
                    if neighbor == peer_name:
                        if peer["state"] == "Established":
                            return CheckResult(self.description, True, "OK")
                        else:
                            return CheckResult(
                                self.description,
                                False,
                                f"The session is configured but is in the {peer['state']} state",
                            )
            except KeyError:
                pass
            reason = f"The evpn session between {device_name} and {neighbor} is not up."

            return CheckResult(self.description, False, reason)

        else:
            return CheckResult(
                self.description, False, f"`l2VpnEvpn` address family not active for bgp on {device_name}"
            )

    def run(self, device_to_neighbours: dict[str, list[str]], lab: Lab) -> list[CheckResult]:
        results = []
        for device_name, neighbors in device_to_neighbours.items():
            self.logger.info(f"Checking that {device_name} has `address-family l2vpn evpn` activated...")
            for neighbor in neighbors:
                self.description = f"{device_name} has bgp peer {neighbor}"
                check_result = self.check(device_name, neighbor, lab)
                results.append(check_result)
        return results
