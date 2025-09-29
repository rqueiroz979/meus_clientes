import sqlite3
import csv
import os

DB_NAME = "clientes.db"

class Database:
    def __init__(self):
        self._init_db()

    def _connect(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""
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

    def export_csv(self, path="clientes_exportados.csv"):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes")
        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]
        conn.close()

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for row in rows:
                writer.writerow([row[h] for h in headers])

    def import_csv(self, path="clientes_exportados.csv"):
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} não encontrado")

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            clientes = list(reader)

        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM clientes")
        for c in clientes:
            cur.execute("""
                INSERT INTO clientes ({})
                VALUES ({})
            """.format(
                ",".join(c.keys()),
                ",".join(["?"] * len(c))
            ), list(c.values()))
        conn.commit()
        conn.close()


db = Database()
