import os

if os.name == 'nt':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception as e:
        print("Could not enable ANSI support:", e)

class ANSI:
    CSI = '\033['
    RESET = f"{CSI}0m"

    @staticmethod
    def rgb_color(r: int, g: int, b: int, is_background: bool = False) -> str:
        """Returns an ANSI code for a 24-bit RGB color, with an option for background."""
        code_type = '48' if is_background else '38'
        return f"{ANSI.CSI}{code_type};2;{r};{g};{b}m"
    
    @staticmethod
    def hex_to_rgb(hex_code: str) -> tuple:
        """Converts hex color to RGB tuple."""
        hex_code = hex_code.lstrip("#")
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

class ANSIBase:
    __slots__ = ['_entries']
    
    def __init__(self):
        self._entries = {}
    
    def __getattr__(self, name: str) -> str:
        """Retrieve color, background, or style by name or default to RESET."""
        return self._entries.get(name.upper(), ANSI.RESET)
    
    def add_entry(self, name: str, code: str):
        """Add a new entry in RGB or ANSI code format, including hex code support."""
        name = name.upper()
        if "," in code:
            rgb_values = tuple(map(int, code.split(",")))
            if len(rgb_values) == 3:
                self._entries[name] = ANSI.rgb_color(*rgb_values)
            else:
                raise ValueError("RGB code must have three comma-separated values.")
        elif code.startswith("#"):
            self._entries[name] = ANSI.rgb_color(*ANSI.hex_to_rgb(code))
        else:
            self._entries[name] = code



class Colors(ANSIBase):
    def __init__(self):
        super().__init__()
        self._entries.update({
            'BLACK': f"{ANSI.CSI}30m", 'RED': f"{ANSI.CSI}31m", 'GREEN': f"{ANSI.CSI}32m",
            'YELLOW': f"{ANSI.CSI}33m", 'BLUE': f"{ANSI.CSI}34m", 'MAGENTA': f"{ANSI.CSI}35m",
            'CYAN': f"{ANSI.CSI}36m", 'WHITE': f"{ANSI.CSI}37m",
            'LIGHT_BLACK': f"{ANSI.CSI}90m", 'LIGHT_RED': f"{ANSI.CSI}91m", 'LIGHT_GREEN': f"{ANSI.CSI}92m",
            'LIGHT_YELLOW': f"{ANSI.CSI}93m", 'LIGHT_BLUE': f"{ANSI.CSI}94m", 'LIGHT_MAGENTA': f"{ANSI.CSI}95m",
            'LIGHT_CYAN': f"{ANSI.CSI}96m", 'LIGHT_WHITE': f"{ANSI.CSI}97m",
            'ORANGE': f"{ANSI.CSI}38;5;208m", 'BRIGHT_RED': f"{ANSI.CSI}38;5;196m",
            'FOREST_GREEN': f"{ANSI.CSI}38;5;34m", 'DARK_GREEN': f"{ANSI.CSI}38;5;22m",
            'DARK_RED': f"{ANSI.CSI}38;5;88m", 'PEACH': f"{ANSI.CSI}38;5;210m",
            'PASTEL_YELLOW': f"{ANSI.CSI}38;5;228m", 'PASTEL_GREEN': f"{ANSI.CSI}38;5;120m",
            'PASTEL_PURPLE': f"{ANSI.CSI}38;5;141m", 'BURNT_ORANGE': f"{ANSI.CSI}38;5;130m",
            'ELECTRIC_BLUE': f"{ANSI.CSI}38;5;45m", 'BRIGHT_PINK': f"{ANSI.CSI}38;5;201m",
            'BRIGHT_ORANGE': f"{ANSI.CSI}38;5;214m", 'BRIGHT_TEAL': f"{ANSI.CSI}38;5;51m",
            'OLIVE': f"{ANSI.CSI}38;5;100m", 'DARK_SLATE': f"{ANSI.CSI}38;5;235m",
            'SOFT_LAVENDER': f"{ANSI.CSI}38;5;183m", 'SOFT_PINK': f"{ANSI.CSI}38;5;217m",
            'LIGHT_SKY_BLUE': f"{ANSI.CSI}38;5;153m", 'PALE_MINT_GREEN': f"{ANSI.CSI}38;5;121m",
            'GRAY_3': f"{ANSI.CSI}38;5;237m", 'GRAY_7': f"{ANSI.CSI}38;5;243m",
            'GRAY_11': f"{ANSI.CSI}38;5;247m", 'NEON_GREEN': f"{ANSI.CSI}38;5;46m",
            'NEON_YELLOW': f"{ANSI.CSI}38;5;226m"
        })

    def __getattr__(self, name: str):
        """Allow RGB and hex access via attribute."""
        if ',' in name:
            try:
                rgb_values = tuple(map(int, name.split(',')))
                if len(rgb_values) == 3:
                    return ANSI.rgb_color(*rgb_values)
            except ValueError:
                pass
        elif name.startswith('#'):
            return ANSI.rgb_color(*ANSI.hex_to_rgb(name))

        return super().__getattr__(name)


class Backgrounds(ANSIBase):
    def __init__(self):
        super().__init__()
        self._entries.update({
            'BLACK': f"{ANSI.CSI}40m", 'RED': f"{ANSI.CSI}41m", 'GREEN': f"{ANSI.CSI}42m",
            'YELLOW': f"{ANSI.CSI}43m", 'BLUE': f"{ANSI.CSI}44m", 'MAGENTA': f"{ANSI.CSI}45m",
            'CYAN': f"{ANSI.CSI}46m", 'WHITE': f"{ANSI.CSI}47m",
            'LIGHT_BLACK': f"{ANSI.CSI}100m", 'LIGHT_RED': f"{ANSI.CSI}101m",
            'LIGHT_GREEN': f"{ANSI.CSI}102m", 'LIGHT_YELLOW': f"{ANSI.CSI}103m",
            'LIGHT_BLUE': f"{ANSI.CSI}104m", 'LIGHT_MAGENTA': f"{ANSI.CSI}105m",
            'LIGHT_CYAN': f"{ANSI.CSI}106m", 'LIGHT_WHITE': f"{ANSI.CSI}107m"
        })

    def __getattr__(self, name: str):
        """Allow RGB and hex access via attribute for backgrounds."""
        if ',' in name:
            try:
                rgb_values = tuple(map(int, name.split(',')))
                if len(rgb_values) == 3:
                    return ANSI.rgb_color(*rgb_values, is_background=True)
            except ValueError:
                pass
        elif name.startswith('#'):
            return ANSI.rgb_color(*ANSI.hex_to_rgb(name), is_background=True)

        return super().__getattr__(name)


class Styles(ANSIBase):
    def __init__(self):
        super().__init__()
        self._entries.update({
            'BOLD': f"{ANSI.CSI}1m", 'DIM': f"{ANSI.CSI}2m", 'ITALIC': f"{ANSI.CSI}3m",
            'UNDERLINE': f"{ANSI.CSI}4m", 'BLINK': f"{ANSI.CSI}5m", 'REVERSE': f"{ANSI.CSI}7m",
            'HIDDEN': f"{ANSI.CSI}8m", 'RESET': ANSI.RESET
        })

Rcolor = Colors()
Rbackground = Backgrounds()
Rstyle = Styles()


def color_text(text: str, color: str = "", background: str = "", style: str = "") -> str:
    """Applies color, background, and style to text."""
    return f"{color}{background}{style}{text}{Rstyle.RESET}"

"""
print(f"{Rcolor.CYAN}This is cyan text{Rstyle.RESET}")
print(f"{Rstyle.BOLD}{Rcolor.RED}Bold Red Text{Rstyle.RESET}")
print(f"{Rbackground.LIGHT_BLUE}{Rcolor.WHITE}White on Light Blue Background{Rstyle.RESET}")

Rcolor.add_entry('CUSTOM_PURPLE', f"{ANSI.CSI}38;5;93m") # add customs colors, background and styles
Rbackground.add_entry('CUSTOM_BG_PURPLE', f"{ANSI.CSI}48;5;93m")
Rstyle.add_entry('DOUBLE_UNDERLINE', f"{ANSI.CSI}21m")

print(f"{Rcolor.CUSTOM_PURPLE}Custom Purple Text{Rstyle.RESET}")
print(f"{Rbackground.CUSTOM_BG_PURPLE}Text with Custom Purple Background{Rstyle.RESET}")
print(f"{Rstyle.DOUBLE_UNDERLINE}Double Underlined Text{Rstyle.RESET}")
"""
