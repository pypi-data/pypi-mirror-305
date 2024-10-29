from .color import Rcolor, Rstyle, Rbackground
import time

class TextFormatter:
    def __init__(self):
        self.styles = []
        
    def apply(self, text: str) -> str:
        style_code = "".join(set(self.styles))
        return f"{style_code}{text}{Rstyle.RESET}{Rcolor.RESET}{Rbackground.RESET}"
    
    def color(self, color: str) -> 'TextFormatter':
        self.styles.append(color)
        return self
    
    def background(self, background: str) -> 'TextFormatter':
        self.styles.append(background)
        return self
    
    def style(self, style: str) -> 'TextFormatter':
        self.styles.append(style)
        return self
    
    def reset(self) -> 'TextFormatter':
        """Resets the current style settings."""
        self.styles.clear()
        return self
    
    def theme(self, theme: str) -> 'TextFormatter':
        """Apply preset themes: success, warning, error."""
        themes = {
            "success": (Rcolor.GREEN, Rstyle.BOLD),
            "warning": (Rcolor.YELLOW, Rstyle.ITALIC),
            "error": (Rcolor.RED, Rstyle.BOLD),
        }
        color, style = themes.get(theme, (Rcolor.RESET, Rstyle.RESET))
        return self.color(color).style(style)
    
    def gradient_text(self, text: str, start_color: tuple, end_color: tuple) -> str:
        """Apply a gradient effect over the text from start_color to end_color."""
        gradient_ratio = [i / (len(text) - 1) for i in range(len(text))]
        gradient = [blend_rgb(start_color, end_color, ratio) for ratio in gradient_ratio]
        return ''.join(f"{color}{char}" for color, char in zip(gradient, text)) + Rstyle.RESET

    def rainbow_text(self, text: str) -> str:
        """Apply a rainbow gradient effect over the text."""
        colors = [Rcolor.RED, Rcolor.YELLOW, Rcolor.GREEN, Rcolor.CYAN, Rcolor.BLUE, Rcolor.MAGENTA]
        return ''.join(f"{colors[i % len(colors)]}{char}" for i, char in enumerate(text)) + Rstyle.RESET


def progress_bar(progress, total, length=40, color=Rcolor.GREEN, eta=False, start_time=None):
    """Displays a progress bar in the terminal with optional color and ETA."""
    percent = progress / total
    filled_length = int(length * percent)
    bar = f"{color}{'█' * filled_length}{Rcolor.RESET}{'-' * (length - filled_length)}"
    eta_display = ""
    
    if eta and start_time:
        elapsed = time.time() - start_time
        remaining = (elapsed / (progress + 1)) * (total - progress)
        eta_display = f" | ETA: {int(remaining)}s" if progress < total else ""
    
    print(f'\rProgress: |{bar}| {int(percent * 100)}%{eta_display}', end='\r')
    if progress == total:
        print()


def rgb_color(r: int, g: int, b: int) -> str:
    """Returns a 24-bit RGB foreground color ANSI code."""
    return f"\033[38;2;{r};{g};{b}m"


def rgb_background(r: int, g: int, b: int) -> str:
    """Returns a 24-bit RGB background color ANSI code."""
    return f"\033[48;2;{r};{g};{b}m"


def blend_rgb(color1: tuple, color2: tuple, ratio: float) -> str:
    """Blends two RGB colors by a ratio and returns the ANSI color code."""
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return rgb_color(r, g, b)


def invert_color(color: tuple) -> str:
    """Return the inverted color of an RGB color."""
    r, g, b = 255 - color[0], 255 - color[1], 255 - color[2]
    return rgb_color(r, g, b)


def color_contrast(fg, bg):
    """Adjusts foreground color for readability against the background."""
    fg_luminance = 0.2126 * fg[0] + 0.7152 * fg[1] + 0.0722 * fg[2]
    bg_luminance = 0.2126 * bg[0] + 0.7152 * bg[1] + 0.0722 * bg[2]
    return fg if abs(fg_luminance - bg_luminance) > 50 else invert_color(fg)

"""
formatter = TextFormatter().color(Rcolor.BLUE).background(Rbackground.YELLOW).style(Rstyle.UNDERLINE)
print(formatter.apply("Rain, Colors!"))

print(TextFormatter().theme("success").apply("Rain successful installed!"))
print(TextFormatter().theme("warning").apply("Warning: Rain Storm."))
print(TextFormatter().theme("error").apply("Error: Rain failed to install!"))

print(TextFormatter().gradient_text("Gradient Text", (255, 0, 0), (0, 255, 0)))
print(TextFormatter().rainbow_text("Rainbow Text"))

import time
start_time = time.time()
for i in range(101):
    progress_bar(i, 100, color=Rcolor.CYAN, eta=True)
    time.sleep(0.05)
"""
