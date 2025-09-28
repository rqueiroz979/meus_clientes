from jnius import autoclass, cast

# Acesso ao Android
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')

def abrir_whatsapp(numero: str):
    """Abre o WhatsApp no número informado (+55DDDNÚMERO)."""
    try:
        activity = PythonActivity.mActivity
        uri = Uri.parse(f"smsto:{numero}")
        intent = Intent(Intent.ACTION_SENDTO, uri)
        intent.setPackage("com.whatsapp")
        activity.startActivity(intent)
    except Exception as e:
        print("Erro ao abrir WhatsApp:", e)

def abrir_teamviewer(tv_id: str):
    """Abre o TeamViewer no ID informado."""
    try:
        activity = PythonActivity.mActivity
        uri = Uri.parse(f"teamviewer8://{tv_id}")
        intent = Intent(Intent.ACTION_VIEW, uri)
        intent.setPackage("com.teamviewer.teamviewer.market.mobile")
        activity.startActivity(intent)
    except Exception as e:
        print("Erro ao abrir TeamViewer:", e)

def abrir_anydesk(ad_id: str):
    """Abre o AnyDesk no ID informado."""
    try:
        activity = PythonActivity.mActivity
        uri = Uri.parse(f"anydesk://{ad_id}")
        intent = Intent(Intent.ACTION_VIEW, uri)
        intent.setPackage("com.anydesk.anydeskandroid")
        activity.startActivity(intent)
    except Exception as e:
        print("Erro ao abrir AnyDesk:", e)
