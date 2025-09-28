## 📱 Meus Clientes

Aplicativo **offline** para gestão de clientes, desenvolvido em **Python + Kivy/KivyMD**, com armazenamento local em **SQLite** e suporte a importação/exportação de dados em **Excel**.

Projeto de uso **pessoal**, para rodar direto no celular Android via APK, sem necessidade de servidor web.

---

## 🚀 Funcionalidades

- 🔑 **Login fixo**: usuário `admin` e senha `273010`.
- 👤 **Cadastro de clientes** com os seguintes campos:
  - **CNPJ**
  - **Tipo de cliente**: física, jurídica, exterior
  - **Razão social / Nome**
  - **Nome fantasia**
  - **Inscrição estadual**
  - **Inscrição municipal**
  - **Endereço completo**
  - **Telefone**
  - **WhatsApp** (com botão para abrir o app direto)
  - **E-mail**
  - **Tipo de contrato**: mensal, anual, sem contrato
  - **Tipo de pagamento**: boleto, pix, transferência
  - **Valor da mensalidade**
  - **Acesso remoto**
    - Até 6 IDs/senhas do **TeamViewer**
    - Até 6 IDs/senhas do **AnyDesk**
  - **Observações gerais**
  - **Data de cadastro** (gerada automaticamente)
- 📋 **Listagem de clientes**
  - Visualizar clientes cadastrados
  - Botões para abrir WhatsApp, TeamViewer ou AnyDesk
- 📤 **Exportar para Excel**
- 📥 **Importar de Excel**
- 📂 Banco de dados **local no celular** (SQLite)
- 📱 Funciona **sem internet** (exceto ao buscar dados externos por CNPJ)

---

## 🛠 Tecnologias utilizadas

- **Python 3.12+**
- **Kivy 2.2.1**
- **KivyMD 1.1.1**
- **SQLite3**
- **Pandas + Openpyxl** (para Excel)
- **Buildozer** (para gerar APK Android)

---

## 📂 Estrutura inicial do projeto

```bash
meus_clientes/
│── app/
│   ├── screens/         # Telas (login, cadastro, lista, etc.)
│   ├── database/        # SQLite e inicialização do banco
│   ├── utils/           # Funções auxiliares (Excel, integração)
│── main.py              # Arquivo principal do app
│── main.kv              # Layout em linguagem KV
│── buildozer.spec       # Configuração para gerar APK
│── requirements.txt     # Dependências do projeto

▶️ Rodando no PC (modo dev)
Crie o ambiente virtual:
python3 -m venv .venv
source .venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Rode o app:
python main.py

📦 Gerando o APK (Android)
Instale o Buildozer e dependências (já configurado no Ubuntu).
Na pasta do projeto, rode:
buildozer -v android debug

O APK será gerado em:
bin/meus_clientes-0.1-debug.apk

Transfira o APK para o celular e instale manualmente.

📱 Telas planejadas
Login
Menu inicial
Cadastro de cliente
Lista de clientes
Detalhes do cliente
Exportar/Importar Excel
Configurações

📖 Histórico de decisões
Inicialmente o projeto seria web + backend em Flask, mas foi migrado para app mobile standalone para simplificar.
O banco de dados é local (SQLite) no celular.
O login será fixo (admin / 273010) pois o app é de uso pessoal.
O app deve permitir acesso offline, mas precisa de internet para buscar informações externas de CNPJ.
Definido o nome em inglês para o repositório: meus_clientes.
Gerenciamento de dependências via requirements.txt.
Buildozer escolhido para empacotar em APK Android.

✍️ Autor: Ramon Queiroz
---
👉 Agora é só criar o arquivo:

```bash
cd ~/Documentos/meus_clientes
nano README.md

Cole o conteúdo acima, salve (CTRL+O + ENTER) e saia (CTRL+X).

Depois suba pro GitHub:

git add README.md
git commit -m "Adiciona documentação inicial do projeto"
git push origin main
