import pygame
import sys
from game import Game  # Importa el Nivel 1 desde el archivo game.py
from game2 import Level2  # Importa el Nivel 2 desde el archivo game2.py

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
    selected_option = 0  # Controlar la selección (0 para Nivel 1, 1 para Nivel 2)
    options = ["Nivel Básico", "Nivel Avanzado"]  # Opciones del menú

    while True:
        background_image = pygame.image.load("assets/images/background.jpg")
        background_image = pygame.transform.scale(background_image, (800, 600))
        screen.blit(background_image, (0, 0))
        
        draw_text("SPACE INVADER", font, WHITE, screen, 400, 150)

        # Mostrar las opciones de niveles
        for i, option in enumerate(options):
            color = WHITE if i == selected_option else BLACK
            draw_text(option, small_font, color, screen, 400, 300 + i * 50)

        draw_text("Presiona ESC para salir", small_font, WHITE, screen, 400, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Mover hacia arriba en el menú
                    selected_option = (selected_option - 1) % len(options)
                if event.key == pygame.K_DOWN:  # Mover hacia abajo en el menú
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pygame.K_RETURN:  # Seleccionar una opción
                    if selected_option == 0:  # Iniciar el Nivel Básico (Nivel 1)
                        game = Game()
                        game.run()
                    elif selected_option == 1:  # Iniciar el Nivel Avanzado (Nivel 2)
                        game = Level2()  # Ejecuta la clase Level2 del archivo game2.py
                        game.run()
                if event.key == pygame.K_ESCAPE:  # Salir del juego si se presiona ESC
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()
