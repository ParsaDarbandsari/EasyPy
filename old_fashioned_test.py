from text import ColoredText

title = ColoredText('Sample text graphic design with ColorText', 'red', 'light Yellow')
rainbow_text = f"{ColoredText('C', 'red')}{ColoredText('O', 'yellow')}{ColoredText('L', 'green')}" \
    f"{ColoredText('O', 'magenta')}{ColoredText('R', 'blue')}"

print(title)
print(f'Add some {rainbow_text} into your text using this awesome tool')
