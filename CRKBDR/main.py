from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
# codeblock
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
import busio as io
import board

i2c = io.I2C(scl=board.SCL, sda=board.SDA)
trackball = Trackball(i2c, address=0x0A)
trackball.set_rgbw(255,0,0,0)
keyboard.modules.append(trackball)
# codeblock
# oled
oled_ext = Oled( OledData(image={0:OledReactionType.LAYER,1:["1.bmp","2.bmp","3.bmp","4.bmp","5.bmp","6.bmp","7.bmp","8.bmp"]}),toDisplay=OledDisplayMode.IMG,flip= True, i2c=i2c)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[0,0,242],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[0,0,242],[0,0,242],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[0,0,242],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[0,0,242],[0,0,242],[113,1,3],[0,0,242],[0,0,242],[113,1,3],[0,0,242],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0]],split=True,rightSide=True,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(use_pio=True)
keyboard.modules.append(split)

# keymap
keyboard.keymap = [ [KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.LALT,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.ENTER,KC.LCTRL,KC.MO(1),KC.SPACE,KC.SPACE,KC.MO(2),KC.LGUI,KC.RALT,KC.NO], 
[KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.KP_SLASH,KC.KP_7,KC.KP_8,KC.KP_9,KC.KP_MINUS,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.KP_ASTERISK,KC.KP_4,KC.KP_5,KC.KP_6,KC.KP_PLUS,KC.TRNS,KC.TRNS,KC.INSERT,KC.HOME,KC.END,KC.PGUP,KC.PGDOWN,KC.EQUAL,KC.KP_1,KC.KP_2,KC.KP_3,KC.DOT,KC.TRNS,KC.LALT,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.KP_0,KC.RALT,KC.NO], 
[KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.DELETE,KC.NO,KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.NO,KC.UNDERSCORE,KC.PLUS,KC.LEFT_CURLY_BRACE,KC.RIGHT_CURLY_BRACE,KC.PIPE,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINUS,KC.EQUAL,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.RALT,KC.NO], 
[KC.ESCAPE,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.TAB,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.ENTER,KC.LCTRL,KC.LALT,KC.SPACE,KC.SPACE,KC.TRNS,KC.LGUI,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO] ] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)