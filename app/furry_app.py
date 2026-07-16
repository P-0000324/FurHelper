from app.furry_base import FurryBase
from app.furry_i18n import FurryI18N
from app.furry_persistence import FurryPersistence
from app.furry_auth import FurryAuth
from app.furry_oobe import FurryOOBE
from app.furry_commands import FurryCommands
from app.furry_gui import FurryGUI

class Furry(FurryBase, FurryI18N, FurryPersistence, FurryAuth, FurryOOBE, FurryCommands, FurryGUI):
    pass
