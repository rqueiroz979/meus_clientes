import sqlite3


def init_db():
    """Cria a tabela de clientes caso não exista."""
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
