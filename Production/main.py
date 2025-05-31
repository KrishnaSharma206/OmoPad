import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.display_oled import DisplayOLED
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Matrix pinout
keyboard.row_pins = (board.IO4, board.IO0, board.IO1)
keyboard.col_pins = (board.IO26, board.IO27, board.IO28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Add media keys if needed
keyboard.extensions.append(MediaKeys())

# Rotary encoder module
encoder = EncoderHandler()
encoder.pins = ((board.IO29, board.IO2),)  # IO29 = A, IO2 = B
encoder.map = ((0, (keyboard.tap_key, 'volume_up'), (keyboard.tap_key, 'volume_down')),)
keyboard.modules.append(encoder)

# Rotary Encoder switch on IO3
extra_switch = digitalio.DigitalInOut(board.IO3)
extra_switch.switch_to_input(pull=digitalio.Pull.UP)

# OLED Display module (SSD1306)
display = DisplayOLED()
keyboard.modules.append(display)

# Keymap (example)
from kmk.keys import KC
keyboard.keymap = [
    [KC.A, KC.B, KC.C,
     KC.D, KC.E, KC.F,
     KC.G, KC.H, KC.I]
]

if __name__ == '__main__':
    keyboard.go()
