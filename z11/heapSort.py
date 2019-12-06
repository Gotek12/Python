#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import os
from matplotlib import pyplot as plt
import pygame
ran = 0


def save(arr):
    global ran
    tmp = []
    for i in range(0, len(arr)):
        tmp.append(i+1)

    fig = plt.figure()
    plt.title("Sortowanie """ + str(ran))
    plt.xlabel("numer pozycji")
    plt.ylabel("liczba na pozycji")
    plt.plot(tmp, arr, 'ro')
    fig.savefig("zdjecia/sort" + str(ran) + ".png")

    ran += 1


def heapify(arr, n, i):
    save(arr)

    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


arr = [9, 8, 7, 6, 5, 1, 2, 3, 4, 10, 20, 21, 29, 22, 28, 23, 24, 27, 26, 25, 40, 31, 32, 33, 39, 38, 37, 36, 35, 11,
         19, 18, 17, 16, 15, 14, 13, 12, 30, 34]

# create directory
path = "zdjecia"
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

heapSort(arr)
# n = len(arr)
# print ("Sorted array is")
# for i in range(n):
#     print ("%d" %arr[i]),

SIZE = WIDTH, HEIGHT = 600, 600  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
FPS = 10  # Frames per second


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        global ran
        for i in range(ran):
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
        clock.tick(10)


if __name__ == '__main__':
    main()