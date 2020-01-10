"""Package with helper functions to get some unity output on my console apps."""

import logging
import asyncio
from colorama import Fore, Style

__version__ = "0.1"
_LOGGER = logging.getLogger(__name__)

bouncing_bar = {
    "interval": 80,
    "frames": [
        "[    ]",
        "[   =]",
        "[  ==]",
        "[ ===]",
        "[====]",
        "[=== ]",
        "[==  ]",
        "[=   ]",
        "[    ]",
        "[=   ]",
        "[==  ]",
        "[=== ]",
        "[====]",
        "[ ===]",
        "[  ==]",
        "[   =]",
    ],
}

ERROR_COLOR = Fore.RED + Style.BRIGHT
SUCCESS = Fore.GREEN

RIGHT_PAD = 10
BIG_RIGHT_PAD = 25
SMALL_RIGHT_PAD = 5
PAGE_WIDTH = 80


def _out(text, color=None, end="\n"):
    if color:
        print(color + text, end=end)
    else:
        print(Style.RESET_ALL + text, end=end)


async def print_waiting_countdown(delay: int):
    """Print a waiting message including a countdown timer

    Args:
        delay The amount of seconds to countdown.

    Returns:

    """
    for i in range(delay, 0, -1):
        print(f"waiting for {i} seconds\r", end="", flush=True)
        await asyncio.sleep(1)
    print("\n", end="")


def print_key_value(key, value, spacing=RIGHT_PAD, color=None):
    """Print a key-value with the value indented from the left border with a certain
        spacing

    Args:
        key: The key to print out
        value: The value to print out
        spacing: Print the value with an indentation relative to the left border
        color: A colorama color

    """
    _str = str(key).ljust(spacing) + str(value)
    _out(_str, color=color)
