import pygame
import sys
from abc import ABC, abstractmethod

# Soup class represents the final product, which is a type of soup.
class Soup:
    def __init__(self):
        self.ingredients = []  # List to hold the ingredients.

    def add_ingredient(self, ingredient):
        # Method to add an ingredient to the soup.
        self.ingredients.append(ingredient)

    def display(self):
        # Print out all ingredients in the soup to the console.
        print("Soup with the following ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

# Abstract builder class for building soups.
class SoupBuilder(ABC):
    def __init__(self):
        self.soup = None

    def create_new_soup(self):
        # Initializes a new Soup object.
        self.soup = Soup()

    @abstractmethod
    def add_water(self):
        # Abstract method to add water to the soup.
        pass

    @abstractmethod
    def add_vegetable(self):
        # Abstract method to add vegetables to the soup.
        pass

    def get_result(self):
        # Returns the final product (soup).
        return self.soup

# Concrete builder for making tomato soup.
class TomatoSoupBuilder(SoupBuilder):
    def add_water(self):
        # Adds water specifically for tomato soup.
        self.soup.add_ingredient("Water")

    def add_vegetable(self):
        # Adds vegetables specifically used in tomato soup.
        self.soup.add_ingredient("Onion")
        self.soup.add_ingredient("Tomato")
        self.soup.add_ingredient("Carrot")

# Concrete builder for making vegetable minestrone.
class VegetableMinestroneBuilder(SoupBuilder):
    def add_water(self):
        # Adds water specifically for minestrone.
        self.soup.add_ingredient("Water")

    def add_vegetable(self):
        # Adds vegetables specifically used in minestrone.
        self.soup.add_ingredient("Celery")
        self.soup.add_ingredient("Asparagus")
        self.soup.add_ingredient("Garlic")

# Director class to manage the soup building process.
class SoupDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_soup(self):
        # Directs the builder to create a soup, step by step.
        self.builder.create_new_soup()
        self.builder.add_water()
        self.builder.add_vegetable()
        return self.builder.get_result()

# Helper function to draw text on Pygame screen.
def draw_text(screen, text, x, y, font, color):
    # Creates a surface with text and draws it on the given coordinates.
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Soup Builder')
font = pygame.font.Font(pygame.font.get_default_font(), 18)

# Client code to use the builders and director
tomatosoup_builder = TomatoSoupBuilder()
director = SoupDirector(tomatosoup_builder)
tomato_soup = director.build_soup()

minestronesoup_builder = VegetableMinestroneBuilder()
director.builder = minestronesoup_builder
minestrone_soup = director.build_soup()

# Main loop to keep the Pygame window running and display soup ingredients
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white before drawing
    screen.fill((255, 255, 255))

    # Display the ingredients of Tomato Soup on the left
    draw_text(screen, "Tomato Soup:", 10, 10, font, (0, 0, 0))
    for index, ingredient in enumerate(tomato_soup.ingredients):
        draw_text(screen, f"- {ingredient}", 10, 40 + index * 30, font, (0, 0, 0))

    # Display the ingredients of Veggie Minestrone Soup on the right
    draw_text(screen, "Veggie Minestrone Soup:", 300, 10, font, (0, 0, 0))
    for index, ingredient in enumerate(minestrone_soup.ingredients):
        draw_text(screen, f"- {ingredient}", 300, 40 + index * 30, font, (0, 0, 0))


    pygame.display.flip()
    pygame.time.delay(100)
