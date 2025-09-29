# Meus Clientes

Aplicativo móvel (Kivy) para gerenciar clientes: cadastro completo, multi-ID TeamViewer/AnyDesk, export/import Excel e login local (admin/273010).

## Estrutura
- `app/` — código fonte
  - `main.py` — ponto de entrada
  - `database/db.py` — SQLite wrapper
  - `kv/main.kv` — layout
  - `screens/` — telas (login, lista, cadastro, import/export)
  - `utils/helpers.py` — abrir WhatsApp / TeamViewer / AnyDesk

## Funcionalidades
- Login único: `admin` / `273010`
- Cadastro de cliente com campos obrigatórios:
  - CNPJ, Razão Social, Nome Fantasia, CEP, Endereço, Cidade, UF, Telefone1, WhatsApp, Email, Inscrições, Complemento, Bairro
  - Tipo de contrato, Tipo de pagamento, Valor da mensalidade
  - TeamViewer: até 6 IDs + senhas (botão para abrir)
  - AnyDesk: até 6 IDs + senhas (botão para abrir)
- Exportar e importar clientes em `clientes_exportados.xlsx`
- Banco local SQLite (`clientes.db`) — permite uso offline para consultar dados já salvos

## Como rodar no desktop (testes)
1. Crie virtualenv:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

