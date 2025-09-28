import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

# Ajuste da janela no PC (ignorado no celular)
Window.size = (380, 680)

# -------------------- BANCO DE DADOS --------------------
def init_db():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cnpj TEXT,
            nome TEXT,
            fantasia TEXT,
            telefone TEXT,
            whatsapp TEXT,
            email TEXT,
            contrato TEXT,
            pagamento TEXT,
            valor TEXT,
            teamviewer TEXT,
            senha_tv TEXT,
            anydesk TEXT,
            senha_ad TEXT,
            obs TEXT,
            data_cadastro TEXT
        )
    """)
    conn.commit()
    conn.close()

# -------------------- IMPORT DAS TELAS --------------------
from app.screens.login import LoginScreen
from app.screens.home import HomeScreen
from app.screens.cadastro import CadastroScreen
from app.screens.lista import ListaScreen
from app.screens.import_export import ImportExportScreen

# -------------------- APP --------------------
class MeusClientesApp(App):
    def build(self):
        init_db()
        Builder.load_file("app/ui/main.kv")

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CadastroScreen(name="cadastro"))
        sm.add_widget(ListaScreen(name="lista"))
        sm.add_widget(ImportExportScreen(name="import_export"))

        return sm


if __name__ == "__main__":
    MeusClientesApp().run()
