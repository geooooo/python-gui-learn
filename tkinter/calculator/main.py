'''
    Простейший калькулятор
'''


import pygubu
import tkinter as tk


class Application:

    _ICON_PATH = 'icon.gif'

    def __init__(self):
        self._init_ui()
        self._run()

    def _init_ui(self):
        self._load_ui_from_file()
        self._init_ui_components()
        self._load_icon()

    def _load_icon(self):
        icon = tk.Image('photo', file=self._ICON_PATH)
        self._components['toplevel_main'].call(
            'wm',
            'iconphoto',
            self._components['toplevel_main']._w,
            icon
        )

    def _load_ui_from_file(self):
        self._builder = pygubu.Builder()
        self._builder.add_from_file('main.ui')

    def _init_ui_components(self):
        self._get_ui_components()
        self._events_bind()

    def _run(self):
        self._components['toplevel_main'].mainloop()

    def _get_ui_components(self):
        self._components = {
            'toplevel_main': self._builder.get_object('Toplevel_main'),
            'entry_result': self._builder.get_object('Entry_result'),
            'button_dig0': self._builder.get_object('Button_dig0'),
            'button_dig1': self._builder.get_object('Button_dig1'),
            'button_dig2': self._builder.get_object('Button_dig2'),
            'button_dig3': self._builder.get_object('Button_dig3'),
            'button_dig4': self._builder.get_object('Button_dig4'),
            'button_dig5': self._builder.get_object('Button_dig5'),
            'button_dig6': self._builder.get_object('Button_dig6'),
            'button_dig7': self._builder.get_object('Button_dig7'),
            'button_dig8': self._builder.get_object('Button_dig8'),
            'button_dig9': self._builder.get_object('Button_dig9'),
            'button_add': self._builder.get_object('Button_add'),
            'button_sub': self._builder.get_object('Button_sub'),
            'button_mul': self._builder.get_object('Button_mul'),
            'button_div': self._builder.get_object('Button_div'),
            'button_clear': self._builder.get_object('Button_clear'),
            'button_dot': self._builder.get_object('Button_dot'),
        }

    def _events_bind(self):
        pass


Application()
