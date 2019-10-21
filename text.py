def error_print(*args: str):
    red = "\x1b[31m"
    result = ''
    default = "\x1b[39m"

    for text in args:
        result += red + text + ' '

    result += default

    print(result)


def warning_print(*args: str):
    yellow = "\x1b[33m"
    result = ''
    default = "\x1b[39m"

    for text in args:
        result += yellow + text + ' '

    result += default

    print(result)


class ColoredText(object):
    foreground_colors = {
        None: "\x1b[39m",
        'black': "\x1b[30m",
        'red': "\x1b[31m",
        'green': "\x1b[32m",
        'yellow': "\x1b[33m",
        'blue': "\x1b[34m",
        'magenta': "\x1b[35m",
        'cyan': "\x1b[36m",
        'light gray': "\x1b[37m",
        'dark gray': "\x1b[90m",
        'light red': "\x1b[91m",
        'light green': "\x1b[92m",
        'light yellow': "\x1b[93m",
        'light blue': "\x1b[94m",
        'light magenta': "\x1b[95m",
        'light cyan': "\x1b[96m",
        'white': "\x1b[97m"
    }
    background_colors = {
        None: "\x1b[49m",
        'black': "\x1b[40m",
        'red': "\x1b[41m",
        'green': "\x1b[42m",
        'yellow': "\x1b[43m",
        'blue': "\x1b[44m",
        'magenta': "\x1b[45m",
        'cyan': "\x1b[46m",
        'light gray': "\x1b[47m",
        'dark gray': "\x1b[100m",
        'light red': "\x1b[101m",
        'light green': "\x1b[102m",
        'light yellow': "\x1b[103m",
        'light blue': "\x1b[104m",
        'light magenta': "\x1b[105m",
        'light cyan': "\x1b[106m",
        'white': "\x1b[107m"
    }

    def __init__(self, text: str, text_color: str = None, background_color: str = None):
        self.text_color = text_color
        self.background_color = background_color
        if text_color is not None:
            self.text_color = self.text_color.lower()
        if background_color is not None:
            self.background_color = self.background_color.lower()
        self.text = f"{self.foreground_colors[self.text_color]}{self.background_colors[self.background_color]}{text}" \
            f"\x1b[49m\x1b[39m"

    def __str__(self):
        return self.text


class Table(object):
    def __init__(self, row_name, items):
        pass
