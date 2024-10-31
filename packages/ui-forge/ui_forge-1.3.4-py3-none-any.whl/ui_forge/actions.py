import curses
from curses.textpad import Textbox
from typing import Any, Callable, Tuple
from .common import IndexedDict
from .selector import dict_select


def run_function(item: dict):
    args = item.get("args")
    if not args:
        args = ()
    kwargs = item.get("kwargs")
    if not kwargs:
        kwargs = {}
    item["function"](*args, **kwargs)


def select(
    base_win: curses.window,
    options: dict,
    item_display: Callable[[Tuple[str, dict], bool], Tuple[str, int]],
    start_line: int = 0,
    start_pos: int = 0,
) -> Any:
    base_win.clear()
    base_win.refresh()
    selection = dict_select(base_win, IndexedDict(options), item_display, start_line, start_pos)[0]
    if selection[1].get("functionality") == "option":
        if (value := selection[1].get("value")) is not None:
            return value
    return selection[0]


def edit(base_win: curses.window, item: Tuple[str, dict]) -> str:
    base_win.clear()
    base_win.refresh()

    curses.curs_set(1)

    dimensions = base_win.getmaxyx()
    top_right = base_win.getbegyx()

    edit_win = curses.newwin(*dimensions, *top_right)
    header = f"Editing {item[0]}"
    if allowed_human_readable := item[1]["allowed_human_readable"]:
        header += f". {allowed_human_readable}"

    edit_win.addstr(0, 0, header)
    edit_win.addstr(2, 0, " > ")
    textpad_win = curses.newwin(
        1, dimensions[1] - 3, top_right[0] + 2, top_right[1] + 3
    )

    edit_win.refresh()
    textbox = Textbox(textpad_win, insert_mode=True)

    while True:
        textpad_win.clear()
        textpad_win.addstr(0, 0, item[1]["value"])
        textpad_win.refresh()

        value = textbox.edit().strip()
        validator = item[1].get("validator")
        if not validator:
            validator = lambda x: True  # noqa: E731

        if validator(value):
            curses.curs_set(0)
            return value
