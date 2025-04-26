import wx 

from gui.main_frame import MainFrame


class MainApp(wx.App):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.main_frame = MainFrame()
        self.main_frame.Show()