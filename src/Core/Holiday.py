class Holiday:
    def __init__(self, start_date, duration, villa, transfer):
        self.start_date = start_date
        self.duration = duration

        self.villa = villa
        self.location = villa.location

        self.transfer = transfer

    @property
    def cost(self):
        return self.villa.cost + self.transfer.cost