from io_jaegers.grunts.SystemState \
    import SystemState


class Domain:
    def __init__(self):
        self.system_state = None

    def get_system_state(self) -> None | SystemState:
        return self.system_state

    def set_system_state(
            self,
            value: SystemState
    ):
        self.system_state = value