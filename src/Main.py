import datetime
import re

from InputProcessing.ChoiceProcessor import choice_processor
from InputProcessing.InputProcessor import input_processor

from Core.Customer import Customer
from Core.Holiday import Holiday
from Core.Order import Order
from Core.Transfer import Transfer
from Core.Villa import Villa

print("Welcome to 'Sunny-Days Villas'. This progam will create a report of pricing for your villa trip.\n")

location = choice_processor("Choose a location:", [1, 2, 3], ["Florida", "Spain", "Turkey"], int)
print(f"\nLocation: {location}\n")

stay = input_processor("How many days will you stay? ", lambda days: days > 0, int)
print(f"You will stay for {stay:,} days.\n")

bed_count = choice_processor("Choose a bed-count:", [2, 3, 4], [
    "2-Bed Villa",
    "3-Bed Villa",
    "4-Bed Villa"
], int)
print(f"\nBed Count: {bed_count}\n")

person_count = input_processor(f"How many people will occupy the villa (1 - {bed_count.parsed})? ",
                               lambda choice: 1 <= choice <= bed_count.parsed, int)
print(f"{person_count} person(s) will occupy your villa.")
print([f"You will pay an under-occupancy fee of £{10 * (bed_count.parsed - person_count) * stay:,.2f}.\n",
       "You will not pay an under-occupancy fee.\n"][bed_count.parsed == person_count])

hire = choice_processor("Choose a car hire or transfer:", [1, 2, 3, 4],
                        ["Small Car", "Large Car", "Transfer by Coach", "None"], int)
print(
    f"\nYou will {['hire a small car', 'hire a large car', 'perform a transfer by coach', 'not use this optional service'][hire.parsed - 1]}.\n")

name = input_processor("Enter your name: ", lambda name: re.match("^(?:[A-Z][a-z]+ )*[A-Z][a-z]+$", name))
print(f"You are: {name}\n")

address = input_processor("Enter your address (format: [number] [street]; [city], [country]): ",
                          lambda address: re.match(
                              r"^(?P<number>\d+) (?P<street>[A-Za-z ]+); ?(?P<city>[A-Za-z ]+), ?(?P<country>[A-Za-z ]+)$",
                              address))
print(f"Your address is: {address}.\n")

date_start = input_processor("What is your date of arrival (format: dd/mm/yyyy)? ",
                             lambda date: date > datetime.datetime.today(),
                             lambda date: datetime.datetime.strptime(date, "%d/%m/%Y"),
                             lambda date: re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", date))
print(f"You will arrive on {date_start:%d/%m/%Y}.\n")

order = Order(
    Customer(name, address),
    Holiday(date_start, stay,
            Villa(location, bed_count.parsed, person_count, stay),
            Transfer(hire.parsed, stay, person_count)
            )
)

print(f"Your order confirmation:{order.confirmation}")
