class ColorPrint(object):
    @staticmethod
    def error_print(*args: str):
        red = "\x1b[31m"
        result = ''
        default = "\x1b[39m"

        for text in args:
            result += red + text + ' '

        result += default

        print(result)

    @staticmethod
    def warning_print(*args: str):
        yellow = "\x1b[33m"
        result = ''
        default = "\x1b[39m"

        for text in args:
            result += yellow + text + ' '

        result += default

        print(result)
