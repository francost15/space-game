import pygame

def game_over_screen(screen, restart_game, score):
    # Inicializar el mezclador de sonido
    pygame.mixer.init()

    # Cargar el sonido de perder
    lose_sound = pygame.mixer.Sound("assets/music/perder.wav")
    lose_sound.play()

    # Cargar la fuente pixelada
    font_path = "assets/fonts/PressStart2P-Regular.ttf"  # Ruta a la fuente pixelada
    font = pygame.font.Font(font_path, 74)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(400, 300))
    
    retry_font = pygame.font.Font(font_path, 36)
    retry_text = retry_font.render("Press R to Retry", True, (255, 255, 255))
    retry_rect = retry_text.get_rect(center=(400, 400))

    score_font = pygame.font.Font(font_path, 36)
    score_text = score_font.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(400, 350))

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(retry_text, retry_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    restart_game()  # Reinicia el juego