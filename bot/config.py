import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "1978134322:AAHnsT661fYL1YgQARfYmnw3wRprNv-qt4s")
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH', "b08691f7d75645093f690010f58bafec")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', 6759688))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
