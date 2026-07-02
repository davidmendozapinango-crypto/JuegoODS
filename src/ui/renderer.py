import pygame


def draw_text(surface, text, font, color, x, y):
    rendered = font.render(str(text), True, color)
    surface.blit(rendered, (x, y))


def draw_button(
    surface,
    text,
    font,
    x,
    y,
    width,
    height,
    color=(80, 80, 80),
    text_color=(255, 255, 255),
):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, (200, 200, 200), rect, 2)
    rendered = font.render(text, True, text_color)
    text_x = x + (width - rendered.get_width()) // 2
    text_y = y + (height - rendered.get_height()) // 2
    surface.blit(rendered, (text_x, text_y))


def draw_text_input(surface, text, font, x, y, width, height, active):
    rect = pygame.Rect(x, y, width, height)
    color = (60, 60, 60) if not active else (80, 80, 120)
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, (255, 255, 255) if active else (150, 150, 150), rect, 2)
    rendered = font.render(text + ("|" if active else ""), True, (255, 255, 255))
    surface.blit(rendered, (x + 5, y + 5))


def draw_card(surface, card, x, y, width, font, label=""):
    n = card.dimension
    cell_size = min(width // n, 40)
    total_width = cell_size * n
    total_height = cell_size * n

    draw_text(surface, label, font, (255, 255, 255), x, y - 30)

    for i in range(n):
        for j in range(n):
            cell_x = x + j * cell_size
            cell_y = y + i * cell_size
            rect = pygame.Rect(cell_x, cell_y, cell_size, cell_size)
            if card.marked[i][j]:
                pygame.draw.rect(surface, (100, 200, 100), rect)
            else:
                pygame.draw.rect(surface, (50, 50, 50), rect)
            pygame.draw.rect(surface, (200, 200, 200), rect, 1)
            text = str(card.cells[i][j])
            rendered = font.render(text, True, (255, 255, 255))
            text_x = cell_x + (cell_size - rendered.get_width()) // 2
            text_y = cell_y + (cell_size - rendered.get_height()) // 2
            surface.blit(rendered, (text_x, text_y))
