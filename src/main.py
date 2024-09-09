import pygame
import sys
from game import Game  # Importa la clase Game desde tu archivo principal del juego

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 0)
BLACK = (0, 0, 0)

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader - Aztec Game ")

# Definir fuentes
font_path = "assets/fonts/PressStart2P-Regular.ttf"  # Ruta a la fuente pixelada
font = pygame.font.Font(font_path, 60)
small_font = pygame.font.Font(None, 36)

# Cargar y reproducir la música de fondo
pygame.mixer.music.load("assets/music/menu.mp3")
pygame.mixer.music.play(-1)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        background_image = pygame.image.load("assets/images/background.jpg")
        background_image = pygame.transform.scale(background_image, (800, 600))
        screen.blit(background_image, (0, 0))
        
        draw_text("SPACE INVADER", font, WHITE, screen, 400, 200)
        draw_text("Presiona ENTER para iniciar el juego", small_font, WHITE, screen, 400, 400)
        draw_text("Presiona ESC para salir", small_font, WHITE, screen, 400, 450)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Iniciar el juego si se presiona ENTER
                    game = Game()
                    game.run()
                if event.key == pygame.K_ESCAPE:  # Salir del juego si se presiona ESC
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()