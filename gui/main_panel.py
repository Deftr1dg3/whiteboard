import wx 

from gui.top_panel.top_panel import TopPanel
from gui.whiteboard_panel.whiteboard_panel import WhiteboardPanel

class MainPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.init_ui()

    
    def init_ui(self):
        # Create the sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)  # Arrange vertically (top to bottom)

        # Create your panels
        self.top_panel = TopPanel(self)
        self.whiteboard_panel = WhiteboardPanel(self)

        # Add panels to the sizer
        main_sizer.Add(self.top_panel, 0, wx.EXPAND)        # TopPanel with a little margin
        main_sizer.Add(self.whiteboard_panel, 1, wx.EXPAND) # WhiteboardPanel takes the rest space

        # Set the sizer to the MainPanel
        self.SetSizer(main_sizer)
