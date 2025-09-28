from kivy.uix.screenmanager import Screen
from kivy.app import App
from datetime import datetime
import sqlite3


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
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )

        cursor.execute("""
            INSERT INTO clientes 
            (cnpj, nome, fantasia, telefone, whatsapp, email, contrato, pagamento, valor,
             teamviewer, senha_tv, anydesk, senha_ad, obs, data_cadastro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)

        conn.commit()
        conn.close()

        # Limpa campos
        for campo in self.ids:
            if hasattr(self.ids[campo], "text"):
                self.ids[campo].text = ""

        App.get_running_app().root.current = "lista"

