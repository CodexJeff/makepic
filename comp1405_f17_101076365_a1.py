# ============================================================
#                                                             
# Student Name (as it appears on cuLearn): Jeff Jose
# Course Code (for this current semester): COMP1405B          
#                                                             
# ============================================================

#Imports Functions from the Pygame Library
import pygame

#Initializes Pygame
pygame.init()

#Creates a 48 X 56 Surface
drawing_window = pygame.display.set_mode((48, 56))

#Fills Surface White
drawing_window.fill((255, 255, 255))

#Draws Purple Polygon
pygame.draw.polygon(drawing_window, (131, 117, 175), ((7, 41),(15, 41),(15, 33),(21, 33),(21, 47),(7, 47)))

#Draws Green Polygon
pygame.draw.polygon(drawing_window, (82, 144, 60), ((15, 31),(21, 31),(21, 16),(20, 15),(19, 14),(18, 13),(17, 12),(16, 11),(15, 10)))

#Draws Gray Polygon
pygame.draw.polygon(drawing_window, (94, 102, 96), ((23, 2),(24, 3),(25, 4),(26, 5),(27, 6),(28, 7),(29, 8),(29, 22),(28, 21),(27, 20),(26, 19),(25, 18),(24, 17),(23, 16)))

#Draws Blue Polygon
pygame.draw.polygon(drawing_window, (68, 80, 140), ((32, 41),(45, 41),(45, 47),(38, 47),(37, 46),(36, 45),(35, 44),(34, 43),(33, 42)))

#Refreshes Display
pygame.display.update()

#Saves Output Display
pygame.image.save(drawing_window, '101076365.png')
