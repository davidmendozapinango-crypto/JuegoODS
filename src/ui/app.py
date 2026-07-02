import sys
from typing import Any, Dict, Optional

import pygame

from auth.player import Player
from config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from ui.assets import AssetLoader
from ui.messages import get
from ui.screens import (
    CardCreationScreen,
    GameScreen,
    LoginScreen,
    MenuScreen,
    ProfileScreen,
    RegisterScreen,
    ReportsScreen,
    ResultsScreen,
    WelcomeScreen,
)


class AppState:
    def __init__(self):
        self.current_player: Optional[Player] = None
        self.cards: Optional[tuple] = None
        self.selected_speed: Optional[str] = None
        self.current_game: Optional[Any] = None
        self.message_catalog = get


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(get("app_title"))
        self.clock = pygame.time.Clock()
        self.assets = AssetLoader()
        self.state = AppState()
        self.screens = {
            "welcome": WelcomeScreen(self, self.state),
            "register": RegisterScreen(self, self.state),
            "login": LoginScreen(self, self.state),
            "profile": ProfileScreen(self, self.state),
            "menu": MenuScreen(self, self.state),
            "card_creation": CardCreationScreen(self, self.state),
            "game": GameScreen(self, self.state),
            "results": ResultsScreen(self, self.state),
            "reports": ReportsScreen(self, self.state),
        }
        self.active_screen = "welcome"
        self.running = True

    def run(self):
        while self.running:
            delta_time = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    next_screen = self.screens[self.active_screen].handle_event(event)
                    if next_screen == "quit":
                        self.running = False
                    elif next_screen:
                        self.active_screen = next_screen
                        if hasattr(self.screens[self.active_screen], "on_enter"):
                            self.screens[self.active_screen].on_enter()

            self.screens[self.active_screen].update(delta_time)
            self.screens[self.active_screen].draw(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
