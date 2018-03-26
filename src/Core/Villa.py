class Villa:
    def __init__(self, location, bed_count, guest_count, duration):
        self.location = location
        self.bed_count = bed_count
        self.guess_count = guest_count
        self.duration = duration

        self.daily_cost = [25.5, 75, 99.95][bed_count - 2]

    @property
    def cost(self):
        return self.daily_cost * self.duration + self.under_occupancy_charge

    @property
    def under_occupancy_charge(self):
        return 10 * (self.bed_count - self.guess_count) * self.duration
