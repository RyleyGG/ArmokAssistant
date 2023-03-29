from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import glob
from os import getcwd

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        definitionStr = ""
        for file in glob.glob(f'{getcwd()}/views/*.kv'):
            file = file.replace('\\', '/')
            reader = open(file, 'r')

            for line in reader:
                definitionStr += line
            definitionStr += '\n'

        Builder.load_string(definitionStr)
        sm = ScreenManager()
        # Note: By default, first widget added to the ScreenManager will be the one shown on app execution
        sm.add_widget(HomeScreen(name='Home'))
        # sm.add_widget(MenuScreen(name='menu'))
        # sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    TestApp().run()