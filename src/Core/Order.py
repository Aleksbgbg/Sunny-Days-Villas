class Order:
    def __init__(self, customer, holiday):
        self.customer = customer
        self.holiday = holiday

    @property
    def cost(self):
        return self.holiday.cost

    @property
    def confirmation(self):
        return f"""
        Villa
            Bed-Count: {self.holiday.villa.bed_count}
            Daily Cost: £{self.holiday.villa.daily_cost:,.2f}
            
            Under-Occupancy Charge: £{self.holiday.villa.under_occupancy_charge:,.2f}
            
            Total Charge: £{self.holiday.villa.cost:,.2f}
        
        Transfer
            Type: {self.holiday.transfer.kind_string}
            Cost: £{["50 per day", "100 per day", "20 per person", "0"][self.holiday.transfer.kind - 1]}
            
            Total Charge: £{self.holiday.transfer.cost:,.2f}
        
        Sum: £{self.holiday.cost:,2f}
        """