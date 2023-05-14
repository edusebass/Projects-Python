import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Generador de arte generativo")

# Bucle principal del programa
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generación de colores aleatorios
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Generación de formas y patrones aleatorios
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(10, 100)
    pygame.draw.circle(window, (r, g, b), (x, y), size)

    # Actualizar la ventana
    pygame.display.flip()

# Salir del programa
pygame.quit()