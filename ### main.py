### main.py - Professional Trading Terminal (Kivy)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.clock import Clock
import yfinance as yf
import threading
import pandas as pd
import io
import matplotlib.pyplot as plt
import mplfinance as mpf
from kivy.core.image import Image as CoreImage

# Config
FINNHUB_API_KEY = "d45rru9r01qieo4rm2t0d45rru9r01qieo4rm2tg"
REFRESH_INTERVAL = 5  # seconds
CHART_POINTS = 200

Window.clearcolor = (0.05, 0.05, 0.05, 1)  # dark theme

# KV UI
KV = """
ScreenManager:
    MenuScreen:
        name: 'menu'
    ChartScreen:
        name: 'chart'

<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 5
        spacing: 5
        Label:
            text: 'Professional Trading Terminal'
            font_size: 25
            color: 1,1,1,1
        TextInput:
            id: symbol_input
            hint_text: 'Enter Symbol'
            multiline: False
        BoxLayout:
            size_hint_y: None
            height: '48dp'
            spacing: 10
            Button:
                text: 'Start Live'
                on_press: root.start_live(symbol_input.text)
            Button:
                text: 'Quit'
                on_press: app.stop()

<ChartScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: '48dp'
            spacing: 10
            Button:
                text: '1m'
                on_press: root.set_timeframe('1m')
            Button:
                text: '5m'
                on_press: root.set_timeframe('5m')
            Button:
                text: '15m'
                on_press: root.set_timeframe('15m')    
            Button:
                text: '30m'
                on_press: root.set_timeframe('30m')    
            Button:
                text: '1h'
                on_press: root.set_timeframe('1h')
            Button:
                text: '4h'
                on_press: root.set_timeframe('4h')    
            Button:
                text: '1D'
                on_press: root.set_timeframe('1d')
            Button:
                text: 'Back'
                on_press: app.root.current = 'menu'
        Image:
            id: chart_img
        Label:
            id: status_label
            text: 'Status: Ready'
            size_hint_y: None
            height: '24dp'
            color: 1,1,1,1
"""

class MenuScreen(Screen):
    def start_live(self, symbol):
        self.manager.get_screen('chart').start_chart(symbol)
        self.manager.current = 'chart'

class ChartScreen(Screen):
    timeframe = StringProperty('1h')
    symbol = StringProperty('AAPL')

    def set_timeframe(self, tf):
        self.timeframe = tf
        self.start_chart(self.symbol)

    def start_chart(self, symbol):
        self.symbol = symbol
        self.ids.status_label.text = f'Loading {symbol} ({self.timeframe})...'
        threading.Thread(target=self._update_chart_thread, daemon=True).start()

    def _update_chart_thread(self):
        while True:
            try:
                df = yf.Ticker(self.symbol).history(period='2y', interval=self.timeframe)
                df = df.tail(CHART_POINTS)
                # Indicators
                df['SMA_20'] = df['Close'].rolling(20).mean()
                df['SMA_50'] = df['Close'].rolling(50).mean()
                # Generate chart
                buf = io.BytesIO()
                mc = mpf.make_marketcolors(up='green', down='red', inherit=True)
                s = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=mc)
                apds = [mpf.make_addplot(df['SMA_20']), mpf.make_addplot(df['SMA_50'])]
                mpf.plot(df, type='candle', style=s, addplot=apds, volume=True, savefig=dict(fname=buf, dpi=100, bbox_inches='tight'))
                buf.seek(0)
                self._update_image(buf)
                self.ids.status_label.text = f'{self.symbol} live ({self.timeframe})'
            except Exception as e:
                self.ids.status_label.text = f'Error: {e}'
            finally:
                import time; time.sleep(REFRESH_INTERVAL)

    def _update_image(self, buf):
        img = CoreImage(buf, ext='png')
        self.ids.chart_img.texture = img.texture

class ProMarketApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    ProMarketApp().run()
