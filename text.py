def error_print(*args: str):
    """
    Error print

    Just a pre-defined error print text method, prints a red version of you text
    """
    red = "\x1b[31m"
    result = ''
    default = "\x1b[39m"

    for text in args:
        result += red + text + ' '

    result += default

    print(result)


def warning_print(*args: str):
    """
    Warning Print

    Just a pre-defined warning print text method, prints a yellow version of you text
    """
    yellow = "\x1b[33m"
    result = ''
    default = "\x1b[39m"

    for text in args:
        result += yellow + text + ' '

    result += default

    print(result)


class ColoredText(object):
    """
    ColoredText

    an awesome tool for you to add colors to your text in python

    Text: The text that is going to be colored
    Text Color: text_color: The color's name
        NOTE: only the following colors are supported:
            Default (Default)
            black
            red
            green
            yellow
            blue
            magenta
            cyan
            light black
            light red
            light green
            light yellow
            light blue
            light cyan
            light gray
            dark gray
    Background Color: The Background color's name
        NOTE: only the following colors are supported:
            None (Default)
            black
            red
            green
            yellow
            blue
            magenta
            cyan
            light black
            light red
            light green
            light blue
            light cyan
            light gray
            dark yellow
            dark gray
    """
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
        'yellow': "\x1b[103m",
        'blue': "\x1b[44m",
        'magenta': "\x1b[45m",
        'cyan': "\x1b[46m",
        'dark yellow': "\x1b[43m",
        'dark gray': "\x1b[100m",
        'light red': "\x1b[101m",
        'light gray': "\x1b[47m",
        'light green': "\x1b[102m",
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
        self.text = text

    def __str__(self):
        """
        Returns The Finished Colored text
        """
        return f"{self.foreground_colors[self.text_color]}{self.background_colors[self.background_color]}{self.text}" \
            f"\x1b[49m\x1b[39m"


class Table(object):
    def __init__(self, table_name):
        self.table_info = {'table_name': table_name}

    def add_column(self, column_name: str, column_items: list):
        self.table_info.update({column_name: column_items})

    def __find_longest_value(self, column_name):
        longest_value = column_name
        other_values = self.table_info[column_name]

        for value in other_values:
            if len(longest_value) < len(value):
                longest_value = value

        return longest_value

    def calculate_spaces(self, word, max_length):
        return max_length - len(word)
    
    def adjust_spaces(self, word, max_length):
        required_spaces = self.calculate_spaces(word, max_length)
        return f"{word}{' ' * (required_spaces + 1)}"
    
    def border(self):
        return "|"
    
    def create_row(self, word, max_length):
        return f"{self.adjust_spaces(word, max_length)}{self.border()}\n"
    
    def separator(self, max_length):
        dashes = ""
        for i in range(max_length + 1):
            dashes = dashes + '-'
        
        return dashes
        
    def create_table(self):
        column_name = list(self.table_info.keys())[1]
        longest_item = self.__find_longest_value(column_name)
    
        table = self.create_row(column_name, len(longest_item))
        table += self.separator(len(longest_item)) + self.border() + "\n"
    
        for word in self.table_info[column_name]:
            table += self.create_row(word, len(longest_item))
    
        return table

    def __dict__(self):
        return self.table_info

    def __str__(self):
        return self.create_table()
