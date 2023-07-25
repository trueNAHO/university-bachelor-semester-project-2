import pygame


class Settings:
    FPS: int = 24
    KEY_MOVE_DOWN: int = pygame.K_DOWN
    KEY_MOVE_LEFT: int = pygame.K_LEFT
    KEY_MOVE_RIGHT: int = pygame.K_RIGHT
    KEY_MOVE_UP: int = pygame.K_UP
    KEY_QUIT: int = pygame.K_ESCAPE
    KEY_UNDO: int = pygame.K_u
    PLAYER_SPAWN_X: float = 0
    PLAYER_SPAWN_Y: float = 0
    PLAYER_SPEED: float = 100
    SCREEN_HEIGHT: int = 500
    SCREEN_WIDTH: int = 500
    WINDOW_CAPTION: str = "Data Management and State Restoration in Gaming Software"
