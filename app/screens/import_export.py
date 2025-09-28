from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sqlite3
import pandas as pd


class ImportExportScreen(Screen):
    def exportar_excel(self):
        conn = sqlite3.connect("clientes.db")
        df = pd.read_sql_query("SELECT * FROM clientes", conn)
        df.to_excel("clientes_exportados.xlsx", index=False)
        conn.close()

        popup = Popup(
            title="Exportação concluída",
            content=Label(text="Arquivo salvo como clientes_exportados.xlsx"),
            size_hint=(0.8, 0.3)
        )
        popup.open()

    def importar_excel(self):
        try:
            df = pd.read_excel("clientes_exportados.xlsx")
            conn = sqlite3.connect("clientes.db")
            df.to_sql("clientes", conn, if_exists="replace", index=False)
            conn.close()

            popup = Popup(
                title="Importação concluída",
                content=Label(text="Clientes importados com sucesso!"),
                size_hint=(0.8, 0.3)
            )
            popup.open()
        except Exception as e:
            popup = Popup(
                title="Erro",
                content=Label(text=str(e)),
                size_hint=(0.8, 0.3)
            )
            popup.open()

