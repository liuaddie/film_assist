import webview
from flask import Flask, render_template
from markupsafe import Markup, escape
import time
from AppKit import NSScreen

screenW = NSScreen.mainScreen().frame().size.width
screenH = NSScreen.mainScreen().frame().size.height
appScreenRatio = 0.5
msg = ""
msg += Markup("This is a message<br>")
msg += Markup("This is a message<br>")

app = Flask(__name__, static_folder='assets')

@app.route('/')
def main():
     return render_template('index.html', Message=msg)

class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def quit(self):
        self._window.destroy()

    def minimize(self):
        self._window.minimize()

    def enlarge(self):
        self._window.move(0, 0)
        self._window.resize(screenW, screenH)

    def import_srt(self):
        file_types = ('SRT Files (*.srt)', 'All files (*.*)')
        result = self._window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        print(result)

    def import_excel(self):
        file_types = ('Excel Files (*.xlsx, *.xls)', 'All files (*.*)')
        result = self._window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        print(result)

def start_app():
    api = Api()
    window = webview.create_window(
        title='Film Assist',
        url=app,
        js_api=api,
        width=screenW*appScreenRatio, height=screenH*appScreenRatio, min_size=(320, 480),
        x=None, y=None, hidden=False,
        fullscreen=False, resizable=True,
        frameless=True, easy_drag=False, text_select=False,
        minimized=False, on_top=False,
        confirm_close=True, background_color='#2E2E2E'
    )
    api.set_window(window)

    webview.start()


if __name__ == '__main__':
    start_app()
