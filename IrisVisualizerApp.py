# IrisVisualizerApp.py  — one-button, clean layout
# Requires: wxPython, pandas, matplotlib

import wx
import pandas as pd
import matplotlib.pyplot as plt

FEATURE_X = "sepal_length"
FEATURE_Y = "petal_length"

class IrisVisualizerApp(wx.Frame):
    def __init__(self, parent=None, title="Iris Dataset Visualizer"):
        super().__init__(parent, title=title, size=(820, 520))
        self.SetMinSize((760, 480))
        panel = wx.Panel(self)

        # Centered big button
        open_btn = wx.Button(panel, label="Open Iris Dataset…")
        font = open_btn.GetFont()
        font.PointSize += 2
        open_btn.SetFont(font)
        open_btn.Bind(wx.EVT_BUTTON, self.on_open)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(open_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer(2)  # more whitespace below
        panel.SetSizer(sizer)

        self.Centre()
        self.Show()

    def on_open(self, _evt):
        with wx.FileDialog(
            self,
            "Open Iris CSV",
            wildcard="CSV files (*.csv)|*.csv",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dlg:
            if dlg.ShowModal() != wx.ID_OK:
                return
            path = dlg.GetPath()

        try:
            df = pd.read_csv(path)
            # Handle common header names or headerless CSVs.
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

            # Plot — simple, readable scatter
            plt.figure(figsize=(7.5, 5.0))
            for sp, sub in df.groupby("species"):
                plt.scatter(sub[FEATURE_X], sub[FEATURE_Y], s=40, alpha=0.85, label=str(sp))
            plt.title(f"Iris: {FEATURE_X.replace('_',' ').title()} vs {FEATURE_Y.replace('_',' ').title()}")
            plt.xlabel(FEATURE_X.replace('_',' ').title())
            plt.ylabel(FEATURE_Y.replace('_',' ').title())
            plt.grid(True, linestyle="--", alpha=0.3)
            plt.legend(title="Species", frameon=True)
            plt.tight_layout()
            plt.show()


        except Exception as e:
            wx.MessageBox(f"Could not load/plot file:\n{e}", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    IrisVisualizerApp()
    app.MainLoop()
