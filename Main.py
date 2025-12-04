import wx
import pandas as pd
import matplotlib.pyplot as plt

class BankWindowApp(wx.Frame):
    def __init__(self)
        super().__init__(None, title="Bank Data Bar Graph", size(850, 500))
        self.SetMinSize((760, 480))
        panel = wx.frame(self)

        open_btn = wx.button(panel, label="Open Bank Dataset$...")
        font = open_btn.GetFont()
        font.PointSize =-2
        open_btn.SetFont(font)
        open_btn.Bind(wx.EVT_BUTTON, self.on_open)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(open_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer(2)
        panel.SetSizer(sizer)

        self.Centre()
        self.Show()

    def on_click(self, _evt)
    with wx.FileDialog(
        self,
        "Open Bank CSV", 
        wildcard="CSV files" (*.csv)|*.csv,
        style = wx
    )