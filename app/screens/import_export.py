from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from app.database.db import db
import os

class ImportExportScreen(BoxLayout):
    def exportar(self):
        path = "clientes_exportados.csv"
        try:
            db.export_csv(path)
            Popup(
                title="Exportado",
                content=Label(text=f"Arquivo salvo: {path}"),
                size_hint=(0.8,0.3)
            ).open()
        except Exception as e:
            Popup(title="Erro", content=Label(text=str(e)), size_hint=(0.8,0.3)).open()

    def importar(self):
        path = "clientes_exportados.csv"
        if not os.path.exists(path):
            Popup(title="Erro", content=Label(text=f"{path} não encontrado"), size_hint=(0.8,0.3)).open()
            return
        try:
            db.import_csv(path)
            Popup(title="Importado", content=Label(text="Importação concluída"), size_hint=(0.8,0.3)).open()
        except Exception as e:
            Popup(title="Erro", content=Label(text=str(e)), size_hint=(0.8,0.3)).open()
