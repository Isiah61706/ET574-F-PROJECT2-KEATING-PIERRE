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
        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dlg:
            if dlg.ShowModal() != wx.ID_OK:
                return
            path = dlg.GetPath()

        try:
            df = pd.read_csv(path)
            want = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

             # Normalize headers if present
            df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
            if df.shape[1] == 5 and not set(want).issubset(df.columns):
                # assume no headers; assign expected names
                df.columns = want

            # Basic checks
            for c in ["sepal_length", "petal_length", "species"]:
            #for c in ["sepal_width", "petal_width", "species"]:
                if c not in df.columns:
                    raise ValueError("CSV must contain 4 features + 'species'.")

            plt.figure(figsize=(7.5, 5.0))
            for sp, sub in df.groupby("species"):
                plt.bar(sub[FEATURE_X]. sub[FEATURE_Y])