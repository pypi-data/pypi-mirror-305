from .color import Rcolor, Rstyle, Rbackground, color_text

class Themes:
    ansi_enabled = True

    @staticmethod
    def template(text, color, style=None, background=None, *extra_styles):
        """
        Applies a theme to text with optional color, background, and styles.
        Multiple styles can be applied simultaneously.
        """
        if not Themes.ansi_enabled:
            return text

        styles = [style] + list(extra_styles) if style else [Rstyle.BOLD]
        style_code = ''.join([getattr(Rstyle, s.upper(), '') for s in styles if s])

        return color_text(text, color=color, background=background, style=style_code)

    success = lambda text: Themes.template(text, Rcolor.GREEN, Rstyle.BOLD)
    warning = lambda text: Themes.template(text, Rcolor.YELLOW, Rstyle.ITALIC)
    error = lambda text: Themes.template(text, Rcolor.RED, Rstyle.BOLD, Rstyle.UNDERLINE)
    info = lambda text: Themes.template(text, Rcolor.CYAN, Rstyle.DIM)

    @staticmethod
    def custom(text, color=None, background=None, *styles):
        """Apply custom theme with color, background, and multiple styles."""
        return Themes.template(text, color=color, background=background, *styles)

    @staticmethod
    def create_theme(name, color=None, background=None, *styles):
        """
        Dynamically creates a new theme function with the given name, color, background, and styles.
        Allows easy creation of themes for specific use cases.
        """
        setattr(Themes, name.lower(), lambda text: Themes.template(text, color, background=background, *styles))

"""
print(Themes.success("Operation successful!"))
print(Themes.warning("Proceed with caution."))
print(Themes.error("An error occurred."))
print(Themes.info("Informational message."))

print(Themes.custom("Custom theme example", Rcolor.ORANGE, Rbackground.BLACK, "BOLD", "ITALIC"))

Themes.create_theme("highlight", Rcolor.BRIGHT_PINK, Rbackground.LIGHT_BLUE, "BOLD", "UNDERLINE")
print(Themes.highlight("This is highlighted text!"))
"""