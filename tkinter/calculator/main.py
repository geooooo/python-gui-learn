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
        self._operation = None
        self._components['button_clear'].bind('<Button-1>', self._button_clear_onclick)
        self._components['button_dig0'].bind('<Button-1>', self._button_dig0_onclick)
        self._components['button_dig1'].bind('<Button-1>', self._button_dig1_onclick)
        self._components['button_dig2'].bind('<Button-1>', self._button_dig2_onclick)
        self._components['button_dig3'].bind('<Button-1>', self._button_dig3_onclick)
        self._components['button_dig4'].bind('<Button-1>', self._button_dig4_onclick)
        self._components['button_dig5'].bind('<Button-1>', self._button_dig5_onclick)
        self._components['button_dig6'].bind('<Button-1>', self._button_dig6_onclick)
        self._components['button_dig7'].bind('<Button-1>', self._button_dig7_onclick)
        self._components['button_dig8'].bind('<Button-1>', self._button_dig8_onclick)
        self._components['button_dig9'].bind('<Button-1>', self._button_dig9_onclick)
        self._components['button_add'].bind('<Button-1>', self._button_add_onclick)
        self._components['button_sub'].bind('<Button-1>', self._button_sub_onclick)
        self._components['button_mul'].bind('<Button-1>', self._button_mul_onclick)
        self._components['button_div'].bind('<Button-1>', self._button_div_onclick)
        self._components['button_dot'].bind('<Button-1>', self._button_dot_onclick)

    def _get_entry_result_pos(self):
        text_len = len(self._components['entry_result'].get())
        return self._components['entry_result'].index(text_len + 1)

    def _entry_result_append_str(self, sval):
        cursor_pos = self._get_entry_result_pos()
        if sval in {'+', '-', '/', '*'}:
            self._operation = sval
            self._components['entry_result'].insert(cursor_pos, sval)
        elif self._operation:
            val1 = float(self._components['entry_result'].get()[:-1])
            val2 = float(sval)
            if self._operation == '+':
                sval = val1 + val2
            elif self._operation == '-':
                sval = val1 - val2
            elif self._operation == '*':
                sval = val1 * val2
            elif self._operation == '/':
                sval = val1 / val2
            self._operation = None
            self._button_clear_onclick(None)
            self._components['entry_result'].insert(0, str(sval))
        else:
            self._operation = None
            self._components['entry_result'].insert(cursor_pos, sval)

    def _button_clear_onclick(self, event):
        self._operation = None
        cursor_pos = self._get_entry_result_pos()
        self._components['entry_result'].delete(0, cursor_pos)

    def _button_dig0_onclick(self, event):
        self._entry_result_append_str('0')

    def _button_dig1_onclick(self, event):
        self._entry_result_append_str('1')

    def _button_dig2_onclick(self, event):
        self._entry_result_append_str('2')

    def _button_dig3_onclick(self, event):
        self._entry_result_append_str('3')

    def _button_dig4_onclick(self, event):
        self._entry_result_append_str('4')

    def _button_dig5_onclick(self, event):
        self._entry_result_append_str('5')

    def _button_dig6_onclick(self, event):
        self._entry_result_append_str('6')

    def _button_dig7_onclick(self, event):
        self._entry_result_append_str('7')

    def _button_dig8_onclick(self, event):
        self._entry_result_append_str('8')

    def _button_dig9_onclick(self, event):
        self._entry_result_append_str('9')

    def _button_add_onclick(self, event):
        self._entry_result_append_str('+')

    def _button_sub_onclick(self, event):
        self._entry_result_append_str('-')

    def _button_mul_onclick(self, event):
        self._entry_result_append_str('*')

    def _button_div_onclick(self, event):
        self._entry_result_append_str('/')

    def _button_dot_onclick(self, event):
        self._entry_result_append_str('.')




Application()
