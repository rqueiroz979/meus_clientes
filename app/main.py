import sqlite3
import pandas as pd
from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang import Builder

# Ajuste tamanho da janela no PC (ignorado no celular)
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


# -------------------- TELAS --------------------
class LoginScreen(Screen):
    info = StringProperty("")

    def do_login(self):
        usuario = self.ids.email.text.strip()
        senha = self.ids.password.text.strip()
        if usuario == "admin" and senha == "273010":
            self.manager.current = "home"
            self.ids.email.text = ""
            self.ids.password.text = ""
            self.info = ""
        else:
            self.info = "Usuário ou senha incorretos!"


class HomeScreen(Screen):
    pass


class CadastroScreen(Screen):
    def salvar_cliente(self):
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()

        dados = (
            self.ids.cnpj.text,
            self.ids.nome.text,
            self.ids.fantasia.text,
            self.ids.telefone.text,
            self.ids.whatsapp.text,
            self.ids.email.text,
            self.ids.contrato.text,
            self.ids.pagamento.text,
            self.ids.valor.text,
            self.ids.teamviewer.text,
            self.ids.senha_tv.text,
            self.ids.anydesk.text,
            self.ids.senha_ad.text,
            self.ids.obs.text,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        cursor.execute("""
            INSERT INTO clientes 
            (cnpj, nome, fantasia, telefone, whatsapp, email, contrato, pagamento, valor,
             teamviewer, senha_tv, anydesk, senha_ad, obs, data_cadastro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)

        conn.commit()
        conn.close()

        # limpa campos
        for campo in self.ids:
            if hasattr(self.ids[campo], "text"):
                self.ids[campo].text = ""

        App.get_running_app().root.current = "lista"


class ListaScreen(Screen):
    def on_pre_enter(self):
        self.ids.lista_clientes.clear_widgets()

        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, telefone, whatsapp FROM clientes ORDER BY id DESC")
        clientes = cursor.fetchall()
        conn.close()

        from kivy.uix.button import Button
        for cliente in clientes:
            btn = Button(
                text=f"{cliente[1]} | Tel: {cliente[2]} | Whats: {cliente[3]}",
                size_hint_y=None,
                height=40,
                background_color=(0.2, 0.6, 0.8, 1)
            )
            self.ids.lista_clientes.add_widget(btn)


class ImportExportScreen(Screen):
    def exportar_excel(self):
        conn = sqlite3.connect("clientes.db")
        df = pd.read_sql_query("SELECT * FROM clientes", conn)
        df.to_excel("clientes_exportados.xlsx", index=False)
        conn.close()

        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        popup = Popup(title="Exportação concluída",
                      content=Label(text="Arquivo salvo como clientes_exportados.xlsx"),
                      size_hint=(0.8, 0.3))
        popup.open()

    def importar_excel(self):
        try:
            df = pd.read_excel("clientes_exportados.xlsx")
            conn = sqlite3.connect("clientes.db")
            df.to_sql("clientes", conn, if_exists="replace", index=False)
            conn.close()

            from kivy.uix.popup import Popup
            from kivy.uix.label import Label
            popup = Popup(title="Importação concluída",
                          content=Label(text="Clientes importados com sucesso!"),
                          size_hint=(0.8, 0.3))
            popup.open()
        except Exception as e:
            from kivy.uix.popup import Popup
            from kivy.uix.label import Label
            popup = Popup(title="Erro",
                          content=Label(text=str(e)),
                          size_hint=(0.8, 0.3))
            popup.open()


# -------------------- APP --------------------
class MeusClientesApp(App):
    def build(self):
        init_db()
        Builder.load_file("main.kv")
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CadastroScreen(name="cadastro"))
        sm.add_widget(ListaScreen(name="lista"))
        sm.add_widget(ImportExportScreen(name="import_export"))
        return sm


if __name__ == "__main__":
    MeusClientesApp().run()

