import wx 

class TopPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent, size=(-1, 40))

        self.SetBackgroundColour("#252525")

        self.init_ui()

    
    def init_ui(self):
        self.panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # ...............Options.................................................

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        
        self.background_color = wx.Button(self, label='Background Color')
        hbox.Add(self.background_color, 0, wx.LEFT | wx.TOP, 10)


        self.SetSizer(hbox)

        self.bind_events()

    
    def bind_events(self):

        self.background_color.Bind(wx.EVT_BUTTON, self.on_background_color)

    
    # ---------- Handle Events -----------

    def on_background_color(self, event: wx.Event):

        color_data = wx.ColourData()
        
        # Step 2: Set the default color (for example, a nice green)
        color_data.SetColour(wx.Colour(29, 28, 28))

        # Step 3: Create ColourDialog **with** the ColourData
        color_dialog = wx.ColourDialog(self, data=color_data)

        color_dialog.GetColourData().SetColour(color_data.GetColour())

        if color_dialog.ShowModal() == wx.ID_OK:
            # Get the chosen color
            color_data = color_dialog.GetColourData()
            color = color_data.GetColour()

            # Print RGB
            rgb = (color.Red(), color.Green(), color.Blue())
            print("RGB:", rgb)

            # Print HEX
            # hex_color = color.GetAsString(wx.C2S_HTML_SYNTAX)  # "#FF6464" style
            # print("HEX:", hex_color)

            # Set the panel background to the chosen color
            self.GetParent().whiteboard_panel.SetBackgroundColour(color)
            # self.SetBackgroundColour(color)
            self.Refresh()  # Important! Refresh to apply color immediately

        color_dialog.Destroy()




