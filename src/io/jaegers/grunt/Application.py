from io.jaegers.grunt.SystemState \
    import SystemState

from io.jaegers.grunt.Domain \
    import Domain

from io.jaegers.grunt.Configuration \
    import Configuration


class Application:
    def __init__(self):
        self.states = SystemState()

        self.domain = Domain()
        self.domain.set_system_state(
            self.get_system_states()
        )

        self.configuration = Configuration()

    def initialise(self):
        pass

    def execute(self):
        while self.get_system_states()\
                  .IsToContinue():
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
