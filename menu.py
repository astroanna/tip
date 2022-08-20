#!/usr/bin/env python3

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import Frame, Layout, ListBox, Widget, Divider, Label
from asciimatics.effects import Background, Print
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import FigletText

import sys

class MenuView(Frame):
    def __init__(self, screen):
        super(MenuView, self).__init__(screen,
                                       screen.height * 9 // 10,
                                       screen.width * 9 // 10,
                                       reduce_cpu = True)
    
        layout = Layout([3, 3, 3], True)
        self.add_layout(layout)

        layout.add_widget(Label("T.I.P", align="^"), 1)

        layout.add_widget(Divider(height=10), 1)

        self._menu_view = ListBox(
            Widget.FILL_COLUMN,
            [("Start", 1), ("Continue", 2), ("Settings", 3)],
            add_scroll_bar=True)
        layout.add_widget(self._menu_view, 1)

        layout.add_widget(Divider(height=10), 1)

        self.fix()


def demo(screen, scene):
    screen.play([Scene([Background(screen), Print(screen, FigletText("Hit the arrow with the mouse!", "digital"),
              y=screen.height//3-3), MenuView(screen)], -1)], stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
