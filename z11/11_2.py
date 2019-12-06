#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import subprocess
import os
from matplotlib import pyplot as plt
import pygame
from pathlib import Path

'''
Program sortujący liczby z wykorzystaniem insertionSort generujący zdjęcia (biblioteka matplotlib) po każdym pojednynczym sortowaniu,
a następnie generujący animację z wykorzystaniem pygame
'''
ran = 0


# generuje zdjęcia w formacie png

def draw(tmp, arr):
    print("Generuje " + str(ran) + " zdjęcie")
    fig = plt.figure()
    plt.title("Sortowanie """ + str(ran))
    plt.xlabel("numer pozycji")
    plt.ylabel("liczba na pozycji")
    plt.plot(tmp, arr, 'ro')
    fig.savefig("zdjecia/sort" + str(ran) + ".png")

def save(arr, test = False):

    global ran
    tmp = []
    for i in range(0, len(arr)):
        tmp.append(i + 1)

    if test and ran % 4 == 0:
        draw(tmp, arr)

    if not test:
        draw(tmp, arr)

    ran += 1


def insertionSort(arr, test = False):
    for i in range(0, len(arr)):
        save(arr, test)

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    save(arr, test)


print("11_2")
alist = [9, 8, 7, 6, 5, 1, 2, 3, 4, 10, 20, 21, 29, 22, 28, 23, 24, 27, 26, 25, 40, 31, 32, 33, 39, 38, 37, 36, 35,
         11, 19, 18, 17, 16, 15, 14, 13, 12, 30, 34]

# create directory
path = "zdjecia"
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)


# gnerate animation with pygame
SIZE = WIDTH, HEIGHT = 600, 600  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
FPS = 10  # Frames per second


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        global ran
        for i in range(ran):
            if os.path.isfile('zdjecia/sort' + str(i) + '.png'):
                self.images.append(pygame.image.load('zdjecia/sort' + str(i) + '.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(5)


print("Sortowanie z generowaniem zdjęć - 1")
print("Sortowanie z generowaniem zdjęć i animacją - 2")
print("\nOgraniczenie generuje 3/4 mniej zdjęć")
print("Sortowanie z generowaniem zdjęć z ograniczeniem -3")
print("Sortowanie z generowaniem zdjęć i animacją z ograniczeniem - 4")
while(True):
    n = int(input(">"))
    if n == 1:
        insertionSort(alist)
        break
    elif n == 2:
        insertionSort(alist)

        if __name__ == '__main__':
            main()
        break
    elif n == 3:
        insertionSort(alist, True)
        break
    elif n == 4:
        insertionSort(alist, True)

        if __name__ == '__main__':
            main()
        break
    else:
        print("Bledna wartosc, wpisz jeszcze raz")

