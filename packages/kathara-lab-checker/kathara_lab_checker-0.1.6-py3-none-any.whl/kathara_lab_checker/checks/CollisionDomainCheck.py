from Kathara.exceptions import LinkNotFoundError
from Kathara.model.Lab import Lab
from Kathara.model.Machine import Machine

from .AbstractCheck import AbstractCheck
from .CheckResult import CheckResult


class CollisionDomainCheck(AbstractCheck):
    def check(self, machine_t: Machine, lab: Lab) -> list[CheckResult]:

        results = []
        try:
            machine = lab.get_machine(machine_t.name)
            for iface_num, interface in machine.interfaces.items():
                self.description = f"Checking the collision domain attached to interface `eth{iface_num}` of `{machine_t.name}`"
                interface_t = machine_t.interfaces[iface_num]
                if interface_t.link.name != interface.link.name:
                    reason = (
                        f"Interface `{iface_num}` of device {machine_t.name} is connected to collision domain "
                        f"`{interface.link.name}` instead of `{interface_t.link.name}`"
                    )
                    results.append(CheckResult(self.description, False, reason))
                else:
                    results.append(CheckResult(self.description, True, "OK"))


        except LinkNotFoundError as e:
            results.append(CheckResult(self.description, False, str(e)))
        return results

    def run(self, template_machines: list[Machine], lab: Lab) -> list[CheckResult]:
        results = []
        for machine_t in template_machines:
            check_result = self.check(machine_t, lab)
            results.extend(check_result)
        return results
