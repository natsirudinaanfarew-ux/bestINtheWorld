# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ContentCalendar
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"

    FG_COLORS = {
        'black': "\033[30m", 'red': "\033[31m", 'green': "\033[32m",
        'yellow': "\033[33m", 'blue': "\033[34m", 'magenta': "\033[35m",
        'cyan': "\033[36m", 'white': "\033[37m",
    }
    BG_COLORS = {
        'black': "\033[40m", 'red': "\033[41m", 'green': "\033[42m",
        'yellow': "\033[43m", 'blue': "\033[44m", 'magenta': "\033[45m",
        'cyan': "\033[46m", 'white': "\033[47m",
    }

    @staticmethod
    def enabled():
        return hasattr(Color, '_enabled') and Color._enabled

    @staticmethod
    def set_enabled(enabled):
        Color._enabled = enabled

    @staticmethod
    def colorize(text, fg=None, bg=None):
        if not Color.enabled():
            return text
        result = text
        if fg and fg in Color.FG_COLORS:
            result = Color.FG_COLORS[fg] + result
        if bg and bg in Color.BG_COLORS:
            result = Color.BG_COLORS[bg] + result
        return result + Color.RESET

    @staticmethod
    def styled(text, style=None, fg=None, bg=None):
        if not Color.enabled():
            return text
        result = text
        if style:
            if style == 'bold':
                result = Color.BOLD + result
            elif style == 'dim':
                result = Color.DIM + result
            elif style == 'underline':
                result = Color.UNDERLINE + result
            elif style == 'blink':
                result = Color.BLINK + result
            elif style == 'reverse':
                result = Color.REVERSE + result
            elif style == 'hidden':
                result = Color.HIDDEN + result
        if fg and fg in Color.FG_COLORS:
            result = Color.FG_COLORS[fg] + result
        if bg and bg in Color.BG_COLORS:
            result = Color.BG_COLORS[bg] + result
        return result + Color.RESET
