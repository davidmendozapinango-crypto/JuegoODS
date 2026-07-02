from pathlib import Path
from typing import Optional, Dict
import pygame

from config import IMAGES_DIR, FONTS_DIR


class AssetLoader:
    def __init__(self):
        self.images: Dict[int, Optional[pygame.Surface]] = {}
        self.fonts: Dict[str, pygame.font.Font] = {}

    def load_ods_image(self, theme_id: int) -> Optional[pygame.Surface]:
        if theme_id in self.images:
            return self.images[theme_id]

        path = IMAGES_DIR / f"ods_{theme_id:02d}.png"
        try:
            surface = pygame.image.load(str(path))
            self.images[theme_id] = surface
            return surface
        except Exception:
            self.images[theme_id] = None
            return None

    def load_font(self, name: str = "default", size: int = 24) -> pygame.font.Font:
        key = f"{name}:{size}"
        if key in self.fonts:
            return self.fonts[key]

        font_path = FONTS_DIR / f"{name}.ttf"
        try:
            font = pygame.font.Font(str(font_path), size)
        except Exception:
            font = pygame.font.SysFont("arial", size)
        self.fonts[key] = font
        return font
