"""OH MY GOD package built upon rich console interface"""

__version__ = "0.1.0"


from .main import OhMyGod
from .scripture import Scripture
from .format import Color

__all__ = ["OhMyGod", "Scripture", "Color"]
