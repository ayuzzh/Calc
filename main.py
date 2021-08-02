import kivy
from plyer import vibrator
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase

Builder.load_file("main.kv")

class MainScreen(Screen):
	
	def calculate(self, equation):
		if str(equation) == "":
			return ""
		try:
			return str(eval(equation))
		except ZeroDivisionError:
			vibrator.vibrate(0.4)
			return "Zero Division Error"
		except SyntaxError:
			vibrator.vibrate(0.4)
			return "Error"
		except NameError:
			vibrator.vibrate(0.4)
			return "Press \"AC\" after any errors"
			
	def save_debug_report(report):
		pass

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