# db.py - sqlite local simples
import sqlite3
import json
import os

DB_NAME = "clientes.db"

class Database:
    def __init__(self, path=None):
        self.path = path or DB_NAME
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cnpj TEXT UNIQUE,
            tipo_cliente TEXT,
            nome TEXT,
            fantasia TEXT,
            inscricao_estadual TEXT,
            inscricao_municipal TEXT,
            cep TEXT,
            endereco TEXT,
            numero TEXT,
            complemento TEXT,
            bairro TEXT,
            cidade TEXT,
            uf TEXT,
            telefone1 TEXT,
            telefone2 TEXT,
            whatsapp TEXT,
            email TEXT,
            tipo_contrato TEXT,
            tipo_pagamento TEXT,
            valor_mensalidade TEXT,
            observacoes TEXT,
            data_cadastro TEXT,
            teamviewer TEXT,
            anydesk TEXT
        )
        """)
        self.conn.commit()

    def insert_cliente(self, data: dict):
        try:
            c = self.conn.cursor()
            c.execute("""
                INSERT INTO clientes (cnpj,tipo_cliente,nome,fantasia,inscricao_estadual,inscricao_municipal,
                  cep,endereco,numero,complemento,bairro,cidade,uf,telefone1,telefone2,whatsapp,email,
                  tipo_contrato,tipo_pagamento,valor_mensalidade,observacoes,data_cadastro,teamviewer,anydesk)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                data.get("cnpj"),
                data.get("tipo_cliente"),
                data.get("nome"),
                data.get("fantasia"),
                data.get("inscricao_estadual"),
                data.get("inscricao_municipal"),
                data.get("cep"),
                data.get("endereco"),
                data.get("numero"),
                data.get("complemento"),
                data.get("bairro"),
                data.get("cidade"),
                data.get("uf"),
                data.get("telefone1"),
                data.get("telefone2"),
                data.get("whatsapp"),
                data.get("email"),
                data.get("tipo_contrato"),
                data.get("tipo_pagamento"),
                data.get("valor_mensalidade"),
                data.get("observacoes"),
                data.get("data_cadastro"),
                json.dumps(data.get("teamviewer",[])),
                json.dumps(data.get("anydesk",[])),
            ))
            self.conn.commit()
            return True, "OK"
        except Exception as e:
            return False, str(e)

    def get_cliente_by_cnpj(self, cnpj):
        c = self.conn.cursor()
        c.execute("SELECT * FROM clientes WHERE cnpj = ?", (cnpj,))
        row = c.fetchone()
        if not row:
            return None
        return self._row_to_dict(row)

    def list_clientes(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM clientes ORDER BY nome")
        rows = c.fetchall()
        return [self._row_to_dict(r) for r in rows]

    def _row_to_dict(self, row):
        d = dict(row)
        try:
            d["teamviewer"] = json.loads(d.get("teamviewer") or "[]")
        except:
            d["teamviewer"] = []
        try:
            d["anydesk"] = json.loads(d.get("anydesk") or "[]")
        except:
            d["anydesk"] = []
        return d
