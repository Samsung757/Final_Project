"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py

Explanation video: http://youtu.be/5-SbFanyUkQ

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
import random
import pygame
import time
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)
BRONZE = (205, 127, 50)
moving_platform_speed = 1


deaths = 0
colours = [WHITE, BLUE, GREEN, RED, PURPLE, CYAN, YELLOW, SILVER, GOLD, BRONZE]


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class MovingWall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.y = y
        self.rect.x = x

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 500:
            self.speed = -self.speed
        if self.rect.y < 0:
            self.speed = -self.speed


class HorizontalMovingWall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.y = y
        self.rect.x = x

    def update(self):
        self.rect.x += self.speed

        if self.rect.x > 800:
            self.speed = -self.speed
        if self.rect.x < 0:
            self.speed = -self.speed





class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        
        for block in block_hit_list:
            # If we are moving right and we hit something, respawn us
            if self.change_x > 0:
                self.rect.x = 50
                self.rect.y = 50
                global deaths
                deaths += 1
                self.image.fill(random.choice(colours))


                time.sleep(1)




               # self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left and we  hit something, respawn us
                self.rect.x = 50
                self.rect.y = 50
                deaths += 1
                time.sleep(1)



        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            else:
                self.rect.top = block.rect.bottom



class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.movingwall_list = pygame.sprite.Group()
        self.horizontalwall_list = pygame.sprite.Group()







class Room1(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [490, 50, 20, 530, BLUE],
                 [290, 20, 20, 530, BLUE],
                 # [390, 250, 40, 100, BLUE],

                 ]


        # Loop through the list. Creathe wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


        moving_walls = [[390, 150, 40, 100, 10, BLUE],
                        [390, 350, 40, 100, -10, BLUE],
                        ]
        horizontal_moving_walls = [[390, 150, 40, 100, 10, BLUE],
                                   [390, 350, 40, 100, -10, BLUE]
                                   ]

        for item in moving_walls:
            moving_wall = MovingWall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.movingwall_list.add(moving_wall)
            self.wall_list.add(moving_wall)

        for item in horizontal_moving_walls:
            horizontal_moving_wall = HorizontalMovingWall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.horizontalwall_list.add(horizontal_moving_wall)
            self.wall_list.add(horizontal_moving_wall)




class Room2(Room):
    """This creates all the walls in room 2"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 525, GREEN],
                 [590, 25, 20, 525, GREEN],
                 [360, 25, 9, 525, GREEN],
                 [390, 50, 9, 525, GREEN],
                 [425, 25, 9, 525, GREEN],
                 [455, 50, 9, 525, GREEN]
                 ]
        moving_walls = [[290, 350, 20, 100, 10, GREEN],
                        [290, 150, 20, 100, -10, GREEN],
                        [290, 200, 20, 100, 10, GREEN],
                        [290, 300, 20, 100, -10, GREEN],
                        [290, 250, 20, 100, 5, GREEN],
                        [290, 250, 20, 100, -5, GREEN],
                        [515, 350, 20, 100, 10, GREEN],
                        [515, 150, 20, 100, -10, GREEN],
                        [515, 200, 20, 100, 10, GREEN],
                        [515, 300, 20, 100, -10, GREEN],
                        [515, 250, 20, 100, 5, GREEN],
                        [515, 250, 20, 100, -5, GREEN],
                        ]


        for item in moving_walls:
            moving_wall = MovingWall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.movingwall_list.add(moving_wall)
            self.wall_list.add(moving_wall)


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4],)
            self.wall_list.add(wall)



class Room3(Room):
    """This creates all the walls in room 3"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                 ]
        horizontal_moving_walls = [[400, 100, 40, 100, 5, WHITE],
                                   [400, 200, 40, 100, 5, WHITE],
                                   [400, 300, 40, 100, -5, WHITE],
                                   [400, 400, 40, 100, -5, WHITE]
                                   ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in horizontal_moving_walls:
            horizontal_moving_wall = HorizontalMovingWall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.horizontalwall_list.add(horizontal_moving_wall)
            self.wall_list.add(horizontal_moving_wall)

        for x in range(100, 800, 100):
           wall = Wall(x, 350, 20, 230, RED)
           self.wall_list.add(wall)

        for x in range(100, 800, 100):
            wall = Wall(x, 25, 20, 230, RED)
            self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
    font = pygame.font.SysFont("dejavusansmono", 25)
    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object
    player = Player(50, 50)

    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []
    # Create some variables to check deaths

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)




        # --- Game Logic ---

        current_room.wall_list.update()

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # --- Drawing ---
        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        screen.blit(
            font.render(f"Deaths: {deaths}", True, WHITE),
            (15, 15)
        )


        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()