import wx 

from gui.main_panel import MainPanel

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None)
        
        self.SetSize((1200, 750))
        # self.SetMinSize(min_size)
        self.SetPosition((200, 70))
        self.SetTitle("Whiteboard")
        
        self.init_ui()

    def init_ui(self):
        self.main_panel = MainPanel(self)