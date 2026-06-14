"""Obsługa konfiguracji gry i pliku opcji."""

import os
import yaml
from constants import DEFAULT_SCREEN_SIZE

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.yaml")

class Config:
    """Przechowuje ustawienia gry oraz rekord."""

    def __init__(self, file_path=SETTINGS_FILE):
        """Tworzy konfigurację i wczytuje dane z pliku."""
        self.file_path = file_path
        self.screen_size = DEFAULT_SCREEN_SIZE
        self.fps = 60
        self.high_score = 0
        self.load()

    def load(self):
        """Wczytuje ustawienia z pliku YAML lub tworzy plik domyślny."""
        if not os.path.exists(self.file_path):
            self.save()
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        self.screen_size = data.get("screen_size", self.screen_size)
        self.fps = data.get("fps", self.fps)
        self.high_score = data.get("high_score", self.high_score)

    def save(self):
        """Zapisuje bieżące ustawienia do pliku YAML."""
        data = {
            "screen_size": self.screen_size,
            "fps": self.fps,
            "high_score": self.high_score,
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, sort_keys=False)
