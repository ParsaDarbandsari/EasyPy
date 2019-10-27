from text import *

# title = ColoredText('Sample text graphic design with ColorText', 'red', 'yellow')
# rainbow_text = f"{ColoredText('C', 'red')}{ColoredText('O', 'yellow')}{ColoredText('L', 'green')}" \
#     f"{ColoredText('O', 'magenta')}{ColoredText('R', 'blue')}"
#
# print(title)
# print(f'Add some {rainbow_text} into your text using this awesome tool')

myTable = Table('colors')
myTable.add_column('colors', ['blue', 'purple', 'oz', 'magenta'])

print(myTable)
