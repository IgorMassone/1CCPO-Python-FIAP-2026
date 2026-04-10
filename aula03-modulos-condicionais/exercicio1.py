import pygame
import time

def iniciar():
    pygame.init()
    pygame.mixer.init()

def tocar(arquivo):
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

def parar():
    pygame.mixer.music.stop()

def esta_tocando():
    return pygame.mixer.music.get_busy()

def main():
    iniciar()
    tocar("ost.mp3")

    while esta_tocando():
        time.sleep(1)

    print("Música terminou!")

if __name__ == '__main__':
    main()