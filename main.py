import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase


import webbrowser
from time import sleep
from plyer import vibrator
import os

os.popen("start_new_session=True")

from files import calculations, newfile


Builder.load_file("main.kv")

error_list = []

class MainScreen(Screen):
	
	return_value = None
	
	def shift_button_press(self, shift_var):
		if shift_var:
			return False
		else:
			return True
	
	def calculate_(self, equation):
		result = calculations.calculate(equation)
		try:
			int(result)
			return result
		except:
			vibrator.vibrate(0.3)
			return result

			

class Settings(Screen):
	pass

screen_manager = ScreenManager()
screen_manager.add_widget(MainScreen(name="main_screen"))
screen_manager.add_widget(Settings(name="settings_screen"))
vibrator.vibrate(0.1)

class MailApp(App):
	
	def build(self):
		return screen_manager

if __name__ == "__main__":
	MailApp().run()