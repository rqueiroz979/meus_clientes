from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import sqlite3


class ListaScreen(Screen):
    def on_pre_enter(self):
        self.ids.lista_clientes.clear_widgets()

        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, telefone, whatsapp FROM clientes ORDER BY id DESC")
        clientes = cursor.fetchall()
        conn.close()

        for cliente in clientes:
            btn = Button(
                text=f"{cliente[1]} | Tel: {cliente[2]} | Whats: {cliente[3]}",
                size_hint_y=None,
                height=40,
                background_color=(0.2, 0.6, 0.8, 1)
            )
            self.ids.lista_clientes.add_widget(btn)

