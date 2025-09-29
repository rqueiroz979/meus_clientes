[app]
title = Meus Clientes
package.name = meus_clientes
package.domain = org.rqueiroz979
source.dir = app
source.main = main.py
source.include_exts = py,png,jpg,kv,txt,csv
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,pyjnius
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
android.api = 33
android.minapi = 21
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1

