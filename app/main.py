# app/main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from pathlib import Path
import os

# import widgets / screens
from app.screens.login_screen import LoginScreen
from app.screens.lista_screen import ListaScreen
from app.screens.cadastro_screen import CadastroScreen
from app.screens.import_export import ImportExportScreen
from app.database.db import Database
from app.utils.helpers import abrir_whatsapp, abrir_app_teamviewer, abrir_app_anydesk

# force window size when running on PC for testing
if os.environ.get("KIVY_WINDOWED") or os.getenv("DISPLAY"):
    Window.size = (380, 760)

KV_PATH = Path(__file__).parent / "kv" / "main.kv"
Builder.load_file(str(KV_PATH))

class MeusClientesApp(App):
    def build(self):
        # ensure DB exists
        self.db = Database()
        self.sm = ScreenManager()
        # create screen instances using our kv screens
        self.sm.add_widget(Builder.template("LoginScreen") if False else LoginScreen(name="login"))
        # But since our kv defines classes as templates, easier to use existing ScreenManager in kv:
        root = Builder.load_file(str(KV_PATH))  # already loaded but ok
        # Instead of duplicating, return a ScreenManager defined in kv:
        # We defined <MainScreenManager@ScreenManager>: so instantiate it:
        # But simpler: load file and ask for root widget
        # Re-load file to get root
        root_widget = Builder.load_file(str(KV_PATH))
        # However loading multiple times can be messy - safer approach:
        # We'll construct ScreenManager manually
        sm = ScreenManager()
        # create screen Widgets that match kv names (they are BoxLayouts)
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(ListaScreen(name="lista"))
        sm.add_widget(CadastroScreen(name="cadastro"))
        sm.add_widget(ImportExportScreen(name="import_export"))
        self.sm = sm
        return sm

    # helper wrappers used by kv bindings
    def abrir_whatsapp(self, numero):
        abrir_whatsapp(numero)

    def app_abrir_teamviewer(self, tv_id):
        abrir_app_teamviewer(tv_id)

    def app_abrir_anydesk(self, ad_id):
        abrir_app_anydesk(ad_id)

    def adicionar_tv(self):
        screen = self.sm.get_screen("cadastro")
        screen.adicionar_tv()

    def adicionar_ad(self):
        screen = self.sm.get_screen("cadastro")
        screen.adicionar_ad()

if __name__ == "__main__":
    MeusClientesApp().run()
