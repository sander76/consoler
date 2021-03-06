import logging

from colorama import Fore, Style

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
SUCCESS_COLOR = Fore.GREEN
ATTENTION_COLOR = Fore.YELLOW + Style.BRIGHT

COLOR_ERROR=ERROR_COLOR
COLOR_SUCCESS=SUCCESS_COLOR
COLOR_ATTENTION=ATTENTION_COLOR
COLOR_LOW_FOCUS=Fore.BLACK + Style.BRIGHT

RIGHT_PAD = 10
BIG_RIGHT_PAD = 25
SMALL_RIGHT_PAD = 5
PAGE_WIDTH = 80