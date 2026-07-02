import datetime
from typing import Any, Optional

import pygame

from auth.login import login
from auth.player import Player
from auth.profile import delete_profile, get_profile, update_profile
from auth.registration import register
from auth.validator import validate_key
from common.errors import (
    DuplicateCedulaError,
    PlayerNotFoundError,
    ValidationError,
)
from config import DRAW_SPEEDS, MAX_DIMENSION, MIN_DIMENSION, STATE_CODES
from core.card import Card
from core.game import Game
from core.points import card_sum
from ods.data import get_ods_themes
from persistence.games import save_game
from reports.export import export_report
from ui.messages import get
from ui.renderer import draw_button, draw_card, draw_text, draw_text_input


class BaseScreen:
    def __init__(self, app, state):
        self.app = app
        self.state = state
        self.font = app.assets.load_font("default", 24)
        self.small_font = app.assets.load_font("default", 18)
        self.error_message = ""
        self.info_message = ""

    def handle_event(self, event):
        return None

    def update(self, delta_time):
        pass

    def draw(self, surface):
        surface.fill((30, 30, 30))
        if self.error_message:
            draw_text(
                surface, self.error_message, self.small_font, (255, 100, 100), 20, 20
            )
        if self.info_message:
            draw_text(
                surface, self.info_message, self.small_font, (100, 255, 100), 20, 45
            )

    def _center_x(self, text_width):
        return 512 - text_width // 2


class WelcomeScreen(BaseScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.buttons = [
            {"label": get("register"), "y": 300, "action": "register"},
            {"label": get("login"), "y": 360, "action": "login"},
            {"label": get("exit"), "y": 420, "action": "quit"},
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in self.buttons:
                if 400 <= x <= 624 and button["y"] <= y <= button["y"] + 40:
                    return button["action"]
        return None

    def draw(self, surface):
        super().draw(surface)
        draw_text(
            surface,
            get("welcome"),
            self.app.assets.load_font("default", 48),
            (255, 255, 255),
            330,
            200,
        )
        for button in self.buttons:
            draw_button(surface, button["label"], self.font, 400, button["y"], 224, 40)


class TextInputScreen(BaseScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.fields = []
        self.active_field = 0
        self.values = {}

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.active_field = (self.active_field + 1) % len(self.fields)
            elif event.key == pygame.K_RETURN:
                return self._submit()
            elif event.key == pygame.K_BACKSPACE:
                key = self.fields[self.active_field]["key"]
                self.values[key] = self.values.get(key, "")[:-1]
            elif event.key == pygame.K_ESCAPE:
                return "welcome"
            elif event.unicode.isprintable():
                key = self.fields[self.active_field]["key"]
                self.values[key] = self.values.get(key, "") + event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for idx, field in enumerate(self.fields):
                if 350 <= x <= 674 and field["y"] <= y <= field["y"] + 35:
                    self.active_field = idx
        return None

    def _submit(self):
        return None


class RegisterScreen(TextInputScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.fields = [
            {"key": "cedula", "label": get("cedula"), "y": 180},
            {"key": "full_name", "label": get("full_name"), "y": 230},
            {"key": "sex", "label": get("sex") + " (m/f)", "y": 280},
            {"key": "birthdate", "label": get("birthdate") + " (YYYY-MM-DD)", "y": 330},
            {"key": "state_code", "label": get("state"), "y": 380},
            {"key": "access_key", "label": get("access_key"), "y": 430},
        ]
        self.values = {field["key"]: "" for field in self.fields}

    def _submit(self):
        try:
            player = register(
                self.values["cedula"],
                self.values["full_name"],
                self.values["sex"],
                self.values["birthdate"],
                self.values["state_code"],
                self.values["access_key"],
            )
            self.state.current_player = player
            self.error_message = ""
            return "menu"
        except (ValidationError, DuplicateCedulaError) as exc:
            self.error_message = str(exc)
        return None

    def draw(self, surface):
        super().draw(surface)
        draw_text(
            surface,
            get("register"),
            self.app.assets.load_font("default", 36),
            (255, 255, 255),
            440,
            120,
        )
        for idx, field in enumerate(self.fields):
            color = (255, 255, 0) if idx == self.active_field else (255, 255, 255)
            draw_text(surface, field["label"], self.font, color, 50, field["y"])
            draw_text_input(
                surface,
                self.values[field["key"]],
                self.font,
                350,
                field["y"],
                324,
                35,
                idx == self.active_field,
            )
        draw_button(surface, get("submit"), self.font, 400, 500, 224, 40)
        draw_text(
            surface, get("back") + " (Esc)", self.small_font, (200, 200, 200), 20, 700
        )


class LoginScreen(TextInputScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.fields = [
            {"key": "cedula", "label": get("cedula"), "y": 250},
            {"key": "access_key", "label": get("access_key"), "y": 300},
        ]
        self.values = {field["key"]: "" for field in self.fields}

    def _submit(self):
        try:
            player = login(self.values["cedula"], self.values["access_key"])
            self.state.current_player = player
            self.error_message = ""
            return "menu"
        except ValidationError as exc:
            self.error_message = str(exc)
        return None

    def draw(self, surface):
        super().draw(surface)
        draw_text(
            surface,
            get("login"),
            self.app.assets.load_font("default", 36),
            (255, 255, 255),
            430,
            180,
        )
        for idx, field in enumerate(self.fields):
            color = (255, 255, 0) if idx == self.active_field else (255, 255, 255)
            draw_text(surface, field["label"], self.font, color, 50, field["y"])
            draw_text_input(
                surface,
                self.values[field["key"]],
                self.font,
                350,
                field["y"],
                324,
                35,
                idx == self.active_field,
            )
        draw_button(surface, get("submit"), self.font, 400, 380, 224, 40)
        draw_text(
            surface, get("back") + " (Esc)", self.small_font, (200, 200, 200), 20, 700
        )


class MenuScreen(BaseScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.buttons = [
            {"label": get("play"), "y": 280, "action": "card_creation"},
            {"label": get("profile"), "y": 340, "action": "profile"},
            {"label": get("reports"), "y": 400, "action": "reports"},
            {"label": get("logout"), "y": 460, "action": "welcome"},
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in self.buttons:
                if 400 <= x <= 624 and button["y"] <= y <= button["y"] + 40:
                    if button["action"] == "welcome":
                        self.state.current_player = None
                    return button["action"]
        return None

    def draw(self, surface):
        super().draw(surface)
        name = self.state.current_player.full_name if self.state.current_player else ""
        draw_text(
            surface,
            f"Hola, {name}",
            self.app.assets.load_font("default", 36),
            (255, 255, 255),
            50,
            120,
        )
        for button in self.buttons:
            draw_button(surface, button["label"], self.font, 400, button["y"], 224, 40)


class ProfileScreen(TextInputScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.fields = [
            {"key": "full_name", "label": get("full_name"), "y": 200},
            {"key": "state_code", "label": get("state"), "y": 250},
            {"key": "access_key", "label": get("access_key"), "y": 300},
        ]
        self.values = {field["key"]: "" for field in self.fields}

    def update(self, delta_time):
        if self.state.current_player and not self.values["full_name"]:
            self.values["full_name"] = self.state.current_player.full_name
            self.values["state_code"] = self.state.current_player.state_code
            self.values["access_key"] = self.state.current_player.access_key

    def _submit(self):
        if not self.state.current_player:
            return "welcome"
        try:
            updated = update_profile(
                self.state.current_player.cedula,
                {
                    "full_name": self.values["full_name"],
                    "state_code": self.values["state_code"],
                    "access_key": self.values["access_key"],
                },
            )
            self.state.current_player = updated
            self.info_message = get("profile_updated")
            self.error_message = ""
        except (ValidationError, DuplicateCedulaError) as exc:
            self.error_message = str(exc)
            self.info_message = ""
        return None

    def handle_event(self, event):
        result = super().handle_event(event)
        if result:
            return result
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            try:
                delete_profile(self.state.current_player.cedula)
                self.state.current_player = None
                return "welcome"
            except PlayerNotFoundError as exc:
                self.error_message = str(exc)
        return None

    def draw(self, surface):
        super().draw(surface)
        draw_text(
            surface,
            get("profile"),
            self.app.assets.load_font("default", 36),
            (255, 255, 255),
            450,
            120,
        )
        for idx, field in enumerate(self.fields):
            color = (255, 255, 0) if idx == self.active_field else (255, 255, 255)
            draw_text(surface, field["label"], self.font, color, 50, field["y"])
            draw_text_input(
                surface,
                self.values[field["key"]],
                self.font,
                350,
                field["y"],
                324,
                35,
                idx == self.active_field,
            )
        draw_button(surface, get("submit"), self.font, 400, 380, 224, 40)
        draw_text(
            surface,
            "Eliminar perfil (Supr)",
            self.small_font,
            (255, 100, 100),
            400,
            440,
        )
        draw_text(
            surface, get("back") + " (Esc)", self.small_font, (200, 200, 200), 20, 700
        )


class CardCreationScreen(TextInputScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.themes = get_ods_themes()
        self.fields = [
            {"key": "dimension", "label": "Dimensión (impar 5-15)", "y": 200},
        ]
        self.values = {"dimension": "5"}
        self.selected_theme = 1

    def handle_event(self, event):
        result = super().handle_event(event)
        if result:
            return result
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.selected_theme = max(1, self.selected_theme - 1)
            elif event.key == pygame.K_RIGHT:
                self.selected_theme = min(17, self.selected_theme + 1)
            elif event.key == pygame.K_SPACE:
                return self._submit()
        return None

    def _submit(self):
        if not self.state.current_player:
            self.error_message = "Debe iniciar sesión"
            return None
        try:
            dimension = int(self.values["dimension"])
            if (
                dimension < MIN_DIMENSION
                or dimension > MAX_DIMENSION
                or dimension % 2 == 0
            ):
                raise ValueError
            main, complement = Card.create_pair(dimension, self.selected_theme)
            self.state.cards = (main, complement)
            self.error_message = ""
            return "game"
        except ValueError:
            self.error_message = get("invalid_dimension")
        return None

    def draw(self, surface):
        super().draw(surface)
        draw_text(
            surface,
            "Crear cartones",
            self.app.assets.load_font("default", 36),
            (255, 255, 255),
            400,
            120,
        )
        draw_text(
            surface,
            self.fields[0]["label"],
            self.font,
            (255, 255, 255),
            50,
            self.fields[0]["y"],
        )
        draw_text_input(
            surface,
            self.values["dimension"],
            self.font,
            350,
            self.fields[0]["y"],
            324,
            35,
            True,
        )
        theme = self.themes[self.selected_theme - 1]
        draw_text(
            surface,
            f"ODS {theme['number']}: {theme['name']}",
            self.font,
            theme["color"],
            50,
            300,
        )
        draw_text(surface, theme["slogan"], self.small_font, (200, 200, 200), 50, 340)
        draw_text(
            surface,
            "← → para cambiar ODS | Espacio para continuar",
            self.small_font,
            (200, 200, 200),
            50,
            400,
        )
        draw_text(
            surface, get("back") + " (Esc)", self.small_font, (200, 200, 200), 20, 700
        )


class GameScreen(BaseScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.draw_timer = 0
        self.speed_ms = None
        self.pending_draws = []
        self.current_number = None
        self.game_over = False
        self.last_draw_time = 0

    def update(self, delta_time):
        if self.game_over or not self.state.current_game:
            return
        if self.speed_ms is None:
            return
        self.draw_timer += delta_time
        if self.draw_timer >= self.speed_ms:
            self.draw_timer = 0
            self._draw_next_number()

    def _draw_next_number(self):
        if not self.pending_draws or self.game_over:
            return
        number = self.pending_draws.pop(0)
        self.current_number = number
        main, complement = self.state.cards
        main.mark_number(number)
        complement.mark_number(number)

        main_wins = main.is_winner()
        complement_wins = complement.is_winner()
        if main_wins and complement_wins:
            self.state.current_game.winner_card = "both"
        elif main_wins:
            self.state.current_game.winner_card = "main"
        elif complement_wins:
            self.state.current_game.winner_card = "complement"
        else:
            return

        self.game_over = True
        self.state.current_game.drawn_numbers = self._all_drawn_numbers()
        save_game(self.state.current_game)

    def _all_drawn_numbers(self):
        n = self.state.cards[0].dimension
        all_numbers = list(range(1, n * n + 1))
        return [num for num in all_numbers if num not in self.pending_draws]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"
            if (
                event.key == pygame.K_SPACE
                and self.speed_ms is None
                and not self.game_over
            ):
                self._draw_next_number()
            if event.key == pygame.K_1:
                self.speed_ms = DRAW_SPEEDS["1s"]
            elif event.key == pygame.K_2:
                self.speed_ms = DRAW_SPEEDS["2s"]
            elif event.key == pygame.K_m:
                self.speed_ms = DRAW_SPEEDS["manual"]
            elif event.key == pygame.K_RETURN and self.game_over:
                return "results"
        return None

    def on_enter(self):
        if not self.state.cards:
            return
        main, complement = self.state.cards
        self.state.current_game = Game.new(
            self.state.current_player.cedula,
            main.dimension,
            main.theme_id,
            main.cells,
            complement.cells,
        )
        self.pending_draws = list(range(1, main.dimension * main.dimension + 1))
        import random

        random.shuffle(self.pending_draws)
        self.game_over = False
        self.current_number = None
        self.draw_timer = 0
        self.speed_ms = None

    def draw(self, surface):
        super().draw(surface)
        if not self.state.cards:
            draw_text(surface, get("no_cards"), self.font, (255, 100, 100), 350, 300)
            return
        main, complement = self.state.cards
        draw_card(
            surface,
            main,
            50,
            100,
            300,
            self.app.assets.load_font("default", 16),
            "Principal",
        )
        draw_card(
            surface,
            complement,
            600,
            100,
            300,
            self.app.assets.load_font("default", 16),
            "Complementario",
        )
        if self.current_number:
            draw_text(
                surface,
                f"Último número: {self.current_number}",
                self.font,
                (255, 255, 0),
                400,
                50,
            )
        draw_text(
            surface,
            "Velocidad: M=Manual 1=1s 2=2s",
            self.small_font,
            (200, 200, 200),
            50,
            650,
        )
        if self.game_over:
            draw_text(
                surface,
                get("game_over") + " - Enter para resultados",
                self.font,
                (100, 255, 100),
                300,
                700,
            )


class ResultsScreen(BaseScreen):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"
        return None

    def draw(self, surface):
        super().draw(surface)
        if not self.state.current_game:
            draw_text(surface, "Sin resultados", self.font, (255, 255, 255), 400, 300)
            return
        game = self.state.current_game
        draw_text(
            surface,
            get("winner") if game.winner_card != "none" else get("draw"),
            self.app.assets.load_font("default", 48),
            (255, 255, 0),
            400,
            150,
        )
        draw_text(
            surface,
            f"Ganador: {game.winner_card}",
            self.font,
            (255, 255, 255),
            400,
            250,
        )
        draw_text(
            surface,
            f"{get('card_sum')} principal: {game.main_card_sum}",
            self.font,
            (255, 255, 255),
            400,
            300,
        )
        draw_text(
            surface,
            f"{get('card_sum')} complementario: {game.complement_card_sum}",
            self.font,
            (255, 255, 255),
            400,
            340,
        )
        draw_text(
            surface, get("back") + " (Esc)", self.small_font, (200, 200, 200), 20, 700
        )


class ReportsScreen(TextInputScreen):
    def __init__(self, app, state):
        super().__init__(app, state)
        self.fields = [
            {"key": "date_from", "label": "Desde (YYYY-MM-DD)", "y": 200},
            {"key": "date_to", "label": "Hasta (YYYY-MM-DD)", "y": 250},
        ]
        self.values = {"date_from": "", "date_to": ""}
        self.report_types = ["player_summary", "gantt", "logs", "top5"]
        self.selected_report = 0

    def handle_event(self, event):
        result = super().handle_event(event)
        if result:
            return result
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.selected_report = (self.selected_report - 1) % len(
                    self.report_types
                )
            elif event.key == pygame.K_RIGHT:
                self.selected_report = (self.selected_report + 1) % len(
                    self.report_types
                )
            elif event.key == pygame.K_SPACE:
                return self._submit()
        return None

    def _submit(self):
        try:
            date_from = self.values["date_from"] or None
            date_to = self.values["date_to"] or None
            if date_from and date_to and date_to < date_from:
                raise ValidationError(get("invalid_date_range"))
            report_type = self.report_types[self.selected_report]
            path = f"reports/{report_type}.txt"
            export_report(report_type, path, date_from=date_from, date_to=date_to)
            self.info_message = f"Reporte guardado en {path}"
            self.error_message = ""
        except ValidationError as exc:
            self.error_message = str(exc)
            self.info_message = ""
        return None

    def draw(self, surface):
        super().draw(surface)
        draw_text(
            surface,
            get("reports"),
            self.app.assets.load_font("default", 36),
            (255, 255, 255),
            450,
            120,
        )
        for idx, field in enumerate(self.fields):
            color = (255, 255, 0) if idx == self.active_field else (255, 255, 255)
            draw_text(surface, field["label"], self.font, color, 50, field["y"])
            draw_text_input(
                surface,
                self.values[field["key"]],
                self.font,
                350,
                field["y"],
                324,
                35,
                idx == self.active_field,
            )
        draw_text(
            surface,
            f"Tipo: {self.report_types[self.selected_report]}",
            self.font,
            (255, 255, 255),
            50,
            320,
        )
        draw_text(
            surface,
            "← → para cambiar tipo | Espacio para generar",
            self.small_font,
            (200, 200, 200),
            50,
            360,
        )
        draw_text(
            surface, get("back") + " (Esc)", self.small_font, (200, 200, 200), 20, 700
        )
