__author__ = 'Jose Gonzalez'
import pygame


def main():
    text=open("Resources/sample.txt")
    for line in text:
        print(line)
    text.close()


if __name__ == '__main__':
    main()
