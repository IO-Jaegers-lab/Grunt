class SystemState:
    def __init__(self):
        self.is_to_continue = False

    def IsToContinue(self) -> bool:
        return self.is_to_continue

    def set_is_to_continue(
            self,
            value: bool
    ):
        self.is_to_continue = value

    def flag_exit(self):
        self.set_is_to_continue(
            False
        )

