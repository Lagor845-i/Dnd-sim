class UiState:
    def __init__(self) -> None:
        self._current_loc = ""
        self._widgets_layers = []
        self._currently_focused_widget = None

    def focus_widget(self,widget_index):
        self._currently_focused_widget = widget_index
        
    def get_focused_widget(self):
        return self._currently_focused_widget