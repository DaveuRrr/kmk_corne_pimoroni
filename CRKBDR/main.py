import busio as io
import board
import supervisor
from kb import KMKKeyboard
from kmk.extensions.peg_oled_display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.handlers.sequences import send_string
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.combos import Chord, Combos
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
from storage import getmount

# supervisor.runtime.autoreload = False
keyboard = KMKKeyboard()
modtap = ModTap()
combos = Combos()
oneshot = OneShot()
layers = Layers()
mousekeys = MouseKeys()
oneshot.tap_time = 450

# OS_LCTL = KC.OS(KC.LCTL)
# OS_LSFT = KC.OS(KC.LSFT)
# OS_LALT = KC.OS(KC.LALT)
keyboard.modules.append(oneshot)
keyboard.modules.append(layers)
keyboard.modules.append(modtap)
keyboard.modules.append(combos)
keyboard.modules.append(mousekeys)

combos.combos = [
    Chord((22, 46), KC.TG(3), match_coord=True)
]

i2c = io.I2C(scl=board.SCL, sda=board.SDA)
name = str(getmount('/').label)
if name.endswith('L'):
    trackball = Trackball(i2c, address=0x0A)
    trackball.set_rgbw(255,0,0,0)
    keyboard.modules.append(trackball)

oled = Oled(OledData(image={0:OledReactionType.LAYER,1:["1.bmp","2.bmp","3.bmp","4.bmp","5.bmp","6.bmp","7.bmp","8.bmp"]}),toDisplay=OledDisplayMode.IMG,flip= True, i2c=i2c)

keyboard.extensions.append(oled)

rgb = Rgb_matrix(ledDisplay=[[0,0,242],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[0,0,242],[0,0,242],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[0,0,242],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[71,1,138],[0,0,242],[0,0,242],[113,1,3],[0,0,242],[0,0,242],[113,1,3],[0,0,242],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0],[3,0,0]],split=True,rightSide=True,disable_auto_write=True)

keyboard.extensions.append(rgb)
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(use_pio=True)
keyboard.modules.append(split)

# Cleaner key names
________ = KC.TRNS
XXXXXXXX = KC.NO
TB_Handl = KC.TB_NEXT_HANDLER
MB_LMB   = KC.MB_LMB
MB_RMB   = KC.MB_RMB

# keymap
keyboard.keymap = [ 
    # 0 QWERTY
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |   Q  |   W  |   E  |   R  |   T  |                    |   Y  |   U  |   I  |   O  |   P  | BKSP |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LALT |   A  |   S  |   D  |   F  |   G  |                    |   H  |   J  |   K  |   L  |  ;:  |  '"  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Shft |   Z  |   X  |   C  |   V  |   B  |-------.    ,-------|   N  |   M  |  ,<  |  .>  |  /?  |  ENT |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          | LCTL | LT1  | / Space /       \ Space\  |  LT2 | LGUI |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                         KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,  \
        KC.LALT,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                         KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOTE, \
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                         KC.N,     KC.M,     KC.COMMA, KC.DOT,   KC.SLASH, KC.ENTER, \
                                                KC.LCTL,  KC.MO(1), KC.SPACE, KC.SPACE, KC.MO(2), KC.LGUI,
    ], 
    # 1 Functions and Numpad
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |                    |   /  |   7  |   8  |   9  |   -  | BKSP |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |  F7  |  F8  |  F9  | F10  | F11  | F12  |                    |   *  |   4  |   5  |   6  |   +  |  '"  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Shft |  INS |  HME | END  | PGUP | PGDN |-------.    ,-------|   =  |   1  |   2  |   3  |   .  |  ENT |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          | LALT | LT1  | / Space /       \ Space\  |  LT2 |   0  |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,                        KC.PSLS,  KC.KP_7,  KC.KP_8,  KC.KP_9,  KC.MINS,  ________, \
        KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,                       KC.PAST,  KC.KP_4,  KC.KP_5,  KC.KP_6,  KC.PPLS,  ________, \
        ________, KC.INS,   KC.HOME,  KC.END,   KC.PGUP,  KC.PGDN,                      KC.EQUAL, KC.KP_1,  KC.KP_2,  KC.KP_3,  KC.DOT,   ________, \
                                                KC.LALT,  ________, ________, ________, ________, KC.KP_0,
    ], 
    # 2 Direction and Modifiers
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # |  `   |  1   |  2   |  3   |  4   |  5   |                    |   6  |   7  |   8  |   9  |   0  | DEL  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      |  <   |  \/  |  /\  |  >   |      |                    |   _  |   +  |   {  |   }  |   |  |  '"  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Shft |      |      |      |      |      |-------.    ,-------|   -  |   =  |   [  |   ]  |   \  |  ENT |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          | LALT | LT1  | / Space /       \ Space\  |  LT2 | LGUI |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        KC.GRAVE, KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                        KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.DEL,   \
        XXXXXXXX, KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT, XXXXXXXX,                     KC.UNDS,  KC.PLUS,  KC.LCBR,  KC.RCBR,  KC.PIPE,  ________, \
        ________, XXXXXXXX, XXXXXXXX, MB_LMB,   MB_RMB,   TB_Handl,                     KC.MINUS, KC.EQUAL, KC.LABK,  KC.RABK,  KC.BSLS,  ________, \
                                                ________, ________, ________, ________, ________, ________,
    ], 
    # 3 Gaming
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |   Q  |   W  |   E  |   R  |   T  |                    |   Y  |   U  |   I  |   O  |   P  | BKSP |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LALT |   A  |   S  |   D  |   F  |   G  |                    |   H  |   J  |   K  |   L  |  ;:  |  '"  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Shft |   Z  |   X  |   C  |   V  |   B  |-------.    ,-------|   N  |   M  |  ,<  |  .>  |  /?  |  ENT |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          | LCTL | LT1  | / Space /       \ Space\  |  LT2 | LGUI |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        KC.ESC,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                         KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,  \
        KC.TAB,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                         KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOTE, \
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                         KC.N,     KC.M,     KC.COMMA, KC.DOT,   KC.SLASH, KC.ENTER, \
                                                KC.LCTL,  KC.LALT,  KC.SPACE, KC.SPACE, ________, KC.LGUI,
    ], 
    # 4 Dummy
    [
        ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, \
        ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, \
        ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, ________, \
                                                ________, ________, ________, ________, ________, ________,
    ],
    # 5 Dummy
    [
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
                                                XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX,
    ],
    # 6 Dummy
    [
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
                                                XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX,
    ],
    # 7 Dummy
    [
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
        XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, \
                                                XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX, XXXXXXXX,
    ]
] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)