# app/screens/lista_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from app.database.db import Database

db = Database()

class ListaScreen(BoxLayout):
    def on_pre_enter(self):
        self.ids.lista_clientes.clear_widgets()
        clientes = db.list_clientes()
        for c in clientes:
            btn = Button(
                text=f"{c.get('razao_social') or c.get('nome_fantasia')}  |  Tel: {c.get('telefone1') or ''}",
                size_hint_y=None, height=56
            )
            # attach cliente id to button and bind
            btn.cliente_id = c["id"]
            btn.bind(on_release=self.open_cliente)
            self.ids.lista_clientes.add_widget(btn)

    def open_cliente(self, instance):
        cid = getattr(instance, "cliente_id", None)
        if cid is not None:
            # muda para tela de cadastro com dados carregados (modo edição)
            cadastro = self.parent.get_screen("cadastro")
            cadastro.load_cliente(cid)
            self.parent.current = "cadastro"
