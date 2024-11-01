from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from . import App


class Binder:
    """Class for binding events to keys"""

    def __init__(self, base: App) -> None:
        self.base = base

        self.bindings = self.base.settings.bindings
        self.events = self.base.commands

        self.bind_all()

    def bind_all(self) -> None:
        """Bind all bindings from config"""

        self.bind(self.bindings.new_file, self.events.new_file)
        self.bind(self.bindings.new_window, self.events.new_window)
        self.bind(self.bindings.open_file, self.events.open_file)
        self.bind(self.bindings.open_dir, self.events.open_directory)
        self.bind(self.bindings.save, self.events.save_file)
        self.bind(self.bindings.save_as, self.events.save_file_as)
        self.bind(self.bindings.close_file, self.events.close_editor)
        self.bind(self.bindings.quit, self.events.quit_biscuit)
        self.bind(self.bindings.undo, self.events.undo)
        self.bind(self.bindings.redo, self.events.redo)
        self.bind(
            self.bindings.restore_closed_tab, self.events.restore_last_closed_editor
        )

    def late_bind_all(self) -> None:
        """Bindings that require full initialization"""

        self.bind(self.bindings.commandpalette, self.events.show_command_palette)
        self.bind(self.bindings.filesearch, self.events.search_files)
        self.bind(self.bindings.symbolpalette, self.events.show_symbol_palette)
        self.bind(self.bindings.panel, self.base.contentpane.toggle_panel)

    def bind(self, this, to_this) -> None:
        self.base.bind(this, to_this)
