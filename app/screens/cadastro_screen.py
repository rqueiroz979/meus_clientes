# app/screens/cadastro_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from app.database.db import Database

import json

db = Database()

MAX_IDS = 6

class CadastroScreen(BoxLayout):
    cliente_id = NumericProperty(0)

    def new_form(self):
        self.cliente_id = 0
        for field in self.ids:
            widget = self.ids[field]
            try:
                widget.text = ""
            except Exception:
                pass
        # reset lists
        self.ids.tv_ids_container.clear_widgets()
        self.ids.ad_ids_container.clear_widgets()
        self._ensure_tv_inputs(1)
        self._ensure_ad_inputs(1)

    def load_cliente(self, cliente_id):
        self.new_form()
        rec = db.get_cliente(cliente_id)
        if not rec:
            return
        self.cliente_id = cliente_id
        # map fields
        mapping = {
            "cnpj": "cnpj",
            "razao_social": "razao_social",
            "nome_fantasia": "nome_fantasia",
            "inscricao_estadual": "inscricao_estadual",
            "inscricao_municipal": "inscricao_municipal",
            "cep": "cep",
            "endereco": "endereco",
            "numero": "numero",
            "complemento": "complemento",
            "bairro": "bairro",
            "cidade": "cidade",
            "uf": "uf",
            "telefone1": "telefone1",
            "telefone2": "telefone2",
            "whatsapp": "whatsapp",
            "email": "email",
            "contrato": "contrato",
            "pagamento": "pagamento",
            "valor_mensalidade": "valor_mensalidade",
            "observacoes": "observacoes"
        }
        for key, fid in mapping.items():
            if fid in self.ids:
                self.ids[fid].text = rec.get(key) or ""

        # teamviewer and anydesk lists
        tv_ids = rec.get("teamviewer_ids") or []
        tv_passwords = rec.get("teamviewer_passwords") or []
        ad_ids = rec.get("anydesk_ids") or []
        ad_passwords = rec.get("anydesk_passwords") or []

        self.ids.tv_ids_container.clear_widgets()
        self.ids.ad_ids_container.clear_widgets()

        for i in range(max(1, len(tv_ids))):
            tvid = tv_ids[i] if i < len(tv_ids) else ""
            pwd = tv_passwords[i] if i < len(tv_passwords) else ""
            self._add_tv_input(tvid, pwd)

        for i in range(max(1, len(ad_ids))):
            adid = ad_ids[i] if i < len(ad_ids) else ""
            pwd = ad_passwords[i] if i < len(ad_passwords) else ""
            self._add_ad_input(adid, pwd)

    def _add_tv_input(self, tvid="", pwd=""):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        h = BoxLayout(size_hint_y=None, height=40)
        t = TextInput(text=tvid, hint_text="TV ID", multiline=False)
        p = TextInput(text=pwd, hint_text="Senha TV", multiline=False)
        b = Button(text="Abrir", size_hint_x=None, width=80)
        # bind open action
        b.bind(on_release=lambda *_: self.parent.app_abrir_teamviewer(t.text))
        h.add_widget(t); h.add_widget(p); h.add_widget(b)
        self.ids.tv_ids_container.add_widget(h)

    def _add_ad_input(self, adid="", pwd=""):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        h = BoxLayout(size_hint_y=None, height=40)
        t = TextInput(text=adid, hint_text="AnyDesk ID", multiline=False)
        p = TextInput(text=pwd, hint_text="Senha AD", multiline=False)
        b = Button(text="Abrir", size_hint_x=None, width=80)
        b.bind(on_release=lambda *_: self.parent.app_abrir_anydesk(t.text))
        h.add_widget(t); h.add_widget(p); h.add_widget(b)
        self.ids.ad_ids_container.add_widget(h)

    def _ensure_tv_inputs(self, n):
        for _ in range(n):
            self._add_tv_input()

    def _ensure_ad_inputs(self, n):
        for _ in range(n):
            self._add_ad_input()

    def adicionar_tv(self):
        if len(self.ids.tv_ids_container.children) >= MAX_IDS:
            return
        self._add_tv_input()

    def adicionar_ad(self):
        if len(self.ids.ad_ids_container.children) >= MAX_IDS:
            return
        self._add_ad_input()

    def salvar_cliente(self):
        # gather fields
        cliente = {}
        for key in ("cnpj","tipo_cliente","razao_social","nome_fantasia","inscricao_estadual","inscricao_municipal",
                    "cep","endereco","numero","complemento","bairro","cidade","uf",
                    "telefone1","telefone2","whatsapp","email","contrato","pagamento","valor_mensalidade","observacoes"):
            if key in self.ids:
                cliente[key] = self.ids[key].text.strip()

        # collect tv ids and pwds
        tv_ids = []
        tv_pw = []
        for box in reversed(self.ids.tv_ids_container.children):
            try:
                tid = box.children[2].text if len(box.children) >= 3 else ""
            except Exception:
                # different order: TextInput order
                tid = box.children[2].text if len(box.children) >= 3 else ""
            # children layout may vary; safer to find TextInput by type
            texts = [w.text for w in box.children if hasattr(w, "text")]
            if texts:
                tv_ids.append(texts[0])
                if len(texts) > 1:
                    tv_pw.append(texts[1])
                else:
                    tv_pw.append("")
        # anydesk
        ad_ids = []
        ad_pw = []
        for box in reversed(self.ids.ad_ids_container.children):
            texts = [w.text for w in box.children if hasattr(w, "text")]
            if texts:
                ad_ids.append(texts[0])
                if len(texts) > 1:
                    ad_pw.append(texts[1])
                else:
                    ad_pw.append("")

        cliente["teamviewer_ids"] = tv_ids
        cliente["teamviewer_passwords"] = tv_pw
        cliente["anydesk_ids"] = ad_ids
        cliente["anydesk_passwords"] = ad_pw

        if self.cliente_id and self.cliente_id > 0:
            db.update_cliente(self.cliente_id, cliente)
        else:
            db.insert_cliente(cliente)

        # voltar pra lista
        self.parent.current = "lista"
