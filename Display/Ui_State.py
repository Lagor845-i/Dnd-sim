class UiState:
    def __init__(self) -> None:
        self._current_screen = ""
        self._widgets_layers = []
        self._currently_focused_widget = None
        self.fps_counter = True
        self.current_fps = 0
    
    def change_screen(self,screen_name:str) -> None:
        self._current_screen = screen_name

    def get_current_screen(self) -> str:
        return self._current_screen

    def focus_widget(self,widget_index):
        self._currently_focused_widget = widget_index
        
    def get_focused_widget(self):
        return self._currently_focused_widget