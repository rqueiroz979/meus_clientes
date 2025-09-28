[app]
title = Meus Clientes
package.name = meus_clientes
package.domain = org.rqueiroz979

# código-fonte
source.dir = app
source.main = main.py
source.include_exts = py,png,jpg,kv,txt,xml

# versão
version = 0.1

# dependências
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,openpyxl,pyjnius,setuptools,wheel

# orientação
orientation = portrait
fullscreen = 0

# APIs suportadas
android.api = 33
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a

# Permissões necessárias
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CALL_PHONE

# Atalhos para abrir apps externos (WhatsApp, TeamViewer, AnyDesk)
# Vamos usar intents, então precisa destas permissões extras:
android.permissions += QUERY_ALL_PACKAGES

# Suporte a salvar e importar planilhas Excel
android.permissions += MANAGE_EXTERNAL_STORAGE

# Ícone e outras configs opcionais
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

