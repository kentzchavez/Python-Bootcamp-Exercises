from prettytable import PrettyTable
from lib.pokemon_list import POKEDEX

# Initialize table
table = PrettyTable()

# Add rows
table.field_names = ["Pokemon Name", "Type"]
for x in POKEDEX:
    table.add_row([x['name'], x['type']])

# Customize Table Attributes
table.header_style = "upper"
table.align = 'l'
table.padding_width = 10

print(table)

"""
The next project is supposedly an OOP version of the coffee machine, but I believce that my coffee machine project from
Day 15 iis already implementing OOP, so I'll skip it :-).
"""