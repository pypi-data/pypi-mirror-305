from ctypes import *
from typing import Generic, Optional, TypeVar

import collections
import signal
import threading

from errno import ENODEV
from shaderbang.gl import *
from libevdev import EV_ABS, EV_KEY, EV_REL, EventsDroppedException
from lib import glsl
from threading import Thread

_pending_inputs = collections.deque()
_active_inputs = []


def _input_devices():
    for input in _active_inputs:
        if isinstance(input, MultiInput):
            for i in input.inputs:
                if isinstance(i, InputDevice):
                    yield i
        elif isinstance(input, InputDevice):
            yield input


def _evdev_event(input):
    try:
        while True:
            try:
                for ev in input.dev.events():
                    input.handler.event(ev, target=input)
            except EventsDroppedException:
                for ev in input.dev.sync():
                    input.handler.event(ev, target=input)
    except IOError as e:
        if e.errno == ENODEV:
            print(f'input device {input.dev.name} unplugged')
        else:
            print(f'error reading events from input device {input.dev.name}', e)
    except Exception as e:
        print(f'error reading events from input device {input.dev.name}', e)
    finally:
        ClosingDevice(input)


def _validate_input(input, width, height):
    # Remove the input if its device has closed
    if isinstance(input, ClosingDevice):
        if (isinstance(input.target, Mouse)
                and (multi := next(filter(lambda i: isinstance(i, MultiMouse), _active_inputs), None))):
            multi.remove(input.target)
            if len(multi.mice) == 1:
                mouse = multi.mice[0]
                multi.remove(mouse)
                _active_inputs.append(mouse)
                _active_inputs.remove(multi)
        else:
            _active_inputs.remove(input.target)
        return

    # Check if it's an input device that's already open
    if (isinstance(input, InputDevice)
            and next(filter(lambda i: i.dev.fd.name == input.dev.fd.name, _input_devices()), None)):
        return

    # Initialize the input
    try:
        input.init(width=width, height=height)
    except Exception as e:
        print(f"invalid {type(input).__name__} input '{input.name}': {e}")
        return

    _active_inputs.append(input)

    # Start processing events from the input device
    if isinstance(input, InputDevice):
        input.dev.grab()
        Thread(target=_evdev_event, args=[input], daemon=True).start()


def _drain(q: collections.deque):
    while True:
        try:
            yield q.pop()
        except IndexError:
            break


@CFUNCTYPE(None, c_uint, c_uint)
def _setup(width, height):
    # Drain all the inputs defined during initialisation
    for input in _drain(_pending_inputs):
        _validate_input(input, width, height)


@CFUNCTYPE(None, c_uint64, c_float)
def _update(frame, time):
    # Drain pending inputs (added at runtime)
    if len(_pending_inputs):
        viewport = (c_uint*4)()
        glsl.glGetIntegerv(GL_VIEWPORT, viewport)
        (width, height) = viewport[2:4]

        for input in _drain(_pending_inputs):
            _validate_input(input, width, height)

    # Render active inputs
    for input in _active_inputs:
        input.render(frame=frame, time=time)


glsl.onInit(_setup)
glsl.onRender(_update)


class NoActiveUniformVariable(Exception):
    name = None

    def __init__(self, name):
        super().__init__(f"no active uniform variable '{name}'")
        self.name = name


class Input:
    name = ''

    def __init__(self, name):
        self.name = name
        _pending_inputs.appendleft(self)

    def init(self, width, height):
        pass

    def render(self, frame, time):
        pass


class EventHandler:

    def event(self, ev, target, **__):
        raise NotImplementedError


class InputDevice(Input, EventHandler):
    dev = None
    handler = None

    def __init__(self, name, dev):
        super().__init__(name)
        self.dev = dev
        self.handler = self

    @property
    def device(self):
        return self.dev


class ClosingDevice(InputDevice):
    target: InputDevice = None

    def __init__(self, target):
        super().__init__(target.name, target.dev)
        self.target = target

    @property
    def device(self):
        return self.target.dev


keycodes = {
    EV_KEY.KEY_BACKSPACE: 8,
    EV_KEY.KEY_TAB: 9,
    EV_KEY.KEY_ENTER: 13,
    EV_KEY.KEY_LEFTSHIFT: 16,
    EV_KEY.KEY_RIGHTSHIFT: 16,
    EV_KEY.KEY_LEFTCTRL: 17,
    EV_KEY.KEY_RIGHTCTRL: 17,
    EV_KEY.KEY_LEFTALT: 18,
    EV_KEY.KEY_RIGHTALT: 18,
    EV_KEY.KEY_ESC: 27,
    EV_KEY.KEY_SPACE: 32,
    EV_KEY.KEY_LEFT: 37,
    EV_KEY.KEY_UP: 38,
    EV_KEY.KEY_RIGHT: 39,
    EV_KEY.KEY_DOWN: 40,
    EV_KEY.KEY_0: 48,
    EV_KEY.KEY_1: 49,
    EV_KEY.KEY_2: 50,
    EV_KEY.KEY_3: 51,
    EV_KEY.KEY_4: 52,
    EV_KEY.KEY_5: 53,
    EV_KEY.KEY_6: 54,
    EV_KEY.KEY_7: 55,
    EV_KEY.KEY_8: 56,
    EV_KEY.KEY_9: 57,
    EV_KEY.KEY_A: 65,
    EV_KEY.KEY_B: 66,
    EV_KEY.KEY_C: 67,
    EV_KEY.KEY_D: 68,
    EV_KEY.KEY_E: 69,
    EV_KEY.KEY_F: 70,
    EV_KEY.KEY_G: 71,
    EV_KEY.KEY_H: 72,
    EV_KEY.KEY_I: 73,
    EV_KEY.KEY_J: 74,
    EV_KEY.KEY_K: 75,
    EV_KEY.KEY_L: 76,
    EV_KEY.KEY_M: 77,
    EV_KEY.KEY_N: 78,
    EV_KEY.KEY_O: 79,
    EV_KEY.KEY_P: 80,
    EV_KEY.KEY_Q: 81,
    EV_KEY.KEY_R: 82,
    EV_KEY.KEY_S: 83,
    EV_KEY.KEY_T: 84,
    EV_KEY.KEY_U: 85,
    EV_KEY.KEY_V: 86,
    EV_KEY.KEY_W: 87,
    EV_KEY.KEY_X: 88,
    EV_KEY.KEY_Y: 89,
    EV_KEY.KEY_Z: 90,
    EV_KEY.KEY_LEFTMETA: 91,
    EV_KEY.KEY_RIGHTMETA: 92,
    EV_KEY.KEY_SLASH: 191,
}


class Mouse(InputDevice):
    drag = False
    resolution: (int, int) = None

    def init(self, width, height, **kwargs):
        super().init(width=width, height=height, **kwargs)

        self.resolution = (width, height)


# TODO: rely on implicit Generic class once Python 3.12+ becomes a requirement
T = TypeVar('T')


class MultiInput(Generic[T], Input):
    inputs: [T] = []


class MultiMouse(MultiInput[Mouse], EventHandler):
    active: Optional[Mouse] = None

    @property
    def mice(self):
        return self.inputs

    def init(self, **kwargs):
        super().init(**kwargs)

        for mouse in self.mice:
            mouse.init(**kwargs)

    def add(self, *mice: [Mouse]):
        for mouse in mice:
            mouse.handler = self
            self.mice.append(mouse)

    def remove(self, *mice: [Mouse]):
        for mouse in mice:
            self.mice.remove(mouse)
            mouse.handler = mouse

    def event(self, ev, target, **kwargs):
        target.event(ev, **kwargs)
        if self.active is None and target.drag:
            self.active = target

    def render(self, **kwargs):
        if self.active is not None:
            self.active.render(**kwargs)
            if not self.active.drag:
                self.active = None

