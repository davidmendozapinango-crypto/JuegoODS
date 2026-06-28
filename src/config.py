import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
ASSETS_DIR = PROJECT_ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images" / "ods"
FONTS_DIR = ASSETS_DIR / "fonts"

PLAYERS_FILE = DATA_DIR / "JUGADORES.bin"
GAMES_FILE = DATA_DIR / "JUEGOS.bin"

MIN_DIMENSION = 5
MAX_DIMENSION = 15

SPECIAL_CHARS = {"*", "=", "%", "_"}
MIN_KEY_LENGTH = 6
MAX_KEY_LENGTH = 10

STATE_CODES = {
    "AMA",
    "ANC",
    "APU",
    "ARA",
    "BAR",
    "BOL",
    "CAR",
    "COJ",
    "DEL",
    "FAL",
    "GUA",
    "LAR",
    "MER",
    "MIR",
    "MON",
    "NVA",
    "POR",
    "SUC",
    "TAC",
    "TRU",
    "VARGAS",
    "YAR",
    "ZUL",
    "ZAM",
    "DF",
    "CCS",
}

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

DRAW_SPEEDS = {
    "manual": None,
    "1s": 1000,
    "2s": 2000,
}
