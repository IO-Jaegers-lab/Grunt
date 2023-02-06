from io_jaegers.grunts.SystemState \
    import SystemState

from io_jaegers.grunts.Domain \
    import Domain


class Application:
    def __init__(self):
        self.states = SystemState()

        self.domain = Domain()
        self.domain.set_system_state(
            self.get_system_states()
        )

    def initialise(self):
        pass

    def execute(self):
        pass

    def garbage_collection(self):
        pass

    def tests(self):
        pass

    def get_system_states(self) -> SystemState:
        return self.states

    def set_system_states(
            self,
            value: SystemState
    ):
        self.states = value

    def get_domain(self) -> Domain:
        return self.domain

    def set_domain(
            self,
            value: Domain
    ) -> None:
        self.domain = value
