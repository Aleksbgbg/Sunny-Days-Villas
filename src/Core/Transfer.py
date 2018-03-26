class Transfer:
    def __init__(self, kind, duration, occupants):
        self.required = kind != 4

        self.kind = kind
        self.kind_string = ["Small Car", "Large Car", "Coach", "None"][kind - 1]

        self.duration = duration
        self.occupants = occupants

    @property
    def cost(self):
        if self.required:
            return [
                lambda transfer: 50 * transfer.duration,
                lambda transfer: 100 * transfer.duration,
                lambda transfer: 20 * transfer.occupants
            ][self.kind - 1](self)

        return 0