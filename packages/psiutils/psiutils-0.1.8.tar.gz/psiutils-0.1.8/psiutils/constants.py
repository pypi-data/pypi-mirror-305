"""Constants for the tkinter psiutils."""
from .utilities import invert

DIALOG_STATUS: dict = {
    'yes': True,
    'no': False,
    'cancel': None,
    'null': 0,
    'exit': 1,
    'ok': 2,
    'updated': 3,
    'error': 4,
}
DIALOG_STATUS = invert(DIALOG_STATUS)

MODES: dict[int, str] | dict[str, int] = {
    0: 'view',
    1: 'new',
    2: 'edit',
    3: 'delete'
}
MODES = invert(MODES)

# GUI
PAD = 5
PADR = (0, PAD)
PADT = (PAD, 0)
PADB = (0, PAD)
LARGE_FONT = ('Arial', 16)
BOLD_FONT = ('Arial', 12, 'bold')
