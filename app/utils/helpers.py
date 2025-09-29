# app/utils/helpers.py
import webbrowser
import sys

def abrir_whatsapp(numero: str):
    """
    Abre o WhatsApp para enviar mensagem. Número em formato com DDI+DDD+numero (ex: 55DDDNNNNNNNN).
    """
    if not numero:
        return False
    link = f"https://wa.me/{numero}"
    try:
        webbrowser.open(link)
        return True
    except Exception:
        return False

def abrir_app_teamviewer(tv_id: str):
    """
    Tenta abrir URI do TeamViewer (no Android, se app instalado a intent abre).
    Fallback: abre site de teamviewer quicksupport.
    """
    if not tv_id:
        return False
    # teamviewer uri (android intent) - will only work on android if configured
    uri = f"teamviewer15://remotecontrol?connect={tv_id}"
    try:
        webbrowser.open(uri)
        return True
    except Exception:
        # fallback
        webbrowser.open("https://login.teamviewer.com")
        return False

def abrir_app_anydesk(ad_id: str):
    if not ad_id:
        return False
    uri = f"anydesk://{ad_id}"
    try:
        webbrowser.open(uri)
        return True
    except Exception:
        # fallback
        webbrowser.open("https://anydesk.com")
        return False
