"""
Professional Snake Game with Modern Graphics and Effects

This is an enhanced version of the classic Snake game featuring modern visual effects,
smooth animations, and polished gameplay mechanics.

Features:
- Sleek neon visual style with dynamic lighting effects
- Smooth snake movement with incremental speed increase
- Modern color palette with pulsing effects
- Grid-based gameplay with collision detection
- Score tracking and game over screen
- Responsive controls with anti-reverse movement

Dependencies:
- Pygame: For game graphics and event handling
- Random: For food placement
- Math: For visual effect calculations
"""

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Modern Color Palette
COLORS = {
    "background": (18, 18, 18),  # Dark background for contrast
    "grid": (30, 30, 30),  # Subtle grid lines
    "snake_head": (102, 255, 102),  # Bright green head
    "snake_body": [(0, 153, 0), (25, 125, 25)],  # Alternating body segments
    "food": (255, 75, 75),  # Bright red food
    "text": (245, 245, 245),  # Light text
    "glow": (255, 100, 100, 50),  # Transparent glow effect
    "accent": (255, 180, 0),  # Golden accent color
    "overlay": (0, 0, 0, 150),  # Semi-transparent overlay
}

# Screen dimensions and layout settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 28
GRID_OFFSET = 2

# Game Settings


INITIAL_SPEED = 10  # Starting game speed
SPEED_INCREMENT = 0.4  # Speed increase per food eaten
MAX_SPEED = 24  # Maximum possible game speed

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class ProfessionalSnakeGame:
    """
    Main game class handling all game mechanics and rendering.

    This class manages the game state, renders graphics, handles input,
    and controls the game loop.
    """

    def __init__(self):
        """Initialize game window, clock, fonts, and game state."""
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Neon Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.big_font = pygame.font.Font(None, 64)
        self.reset_game()

    def reset_game(self):
        """Reset all game state variables to their initial values."""
        start_x = (WIDTH // 2) // CELL_SIZE * CELL_SIZE
        start_y = (HEIGHT // 2) // CELL_SIZE * CELL_SIZE
        self.snake = [(start_x, start_y)]
        self.direction = RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.current_speed = INITIAL_SPEED

    def generate_food(self):
        """
        Generate new food position.

        Returns:
            tuple: (x, y) coordinates for new food position
        """
        while True:
            x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
            y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
            food_pos = (x, y)
            if food_pos not in self.snake:
                return food_pos

    def move(self):
        """
        Update snake position and handle collisions.

        Handles:
        - Movement in current direction
        - Boundary collisions
        - Self collisions
        - Food collection and growth
        """
        if self.game_over:
            return

        head = self.snake[0]
        dx, dy = self.direction
        new_head = (head[0] + dx * CELL_SIZE, head[1] + dy * CELL_SIZE)

        # Boundary collision check
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):
            self.game_over = True
            return

        # Self-collision check
        if new_head in self.snake:
            self.game_over = True
            return

        head_rect = pygame.Rect(new_head[0], new_head[1], CELL_SIZE, CELL_SIZE)
        food_rect = pygame.Rect(self.food[0], self.food[1], CELL_SIZE, CELL_SIZE)

        self.snake.insert(0, new_head)

        if head_rect.colliderect(food_rect):
            self.score += 1
            self.current_speed = min(self.current_speed + SPEED_INCREMENT, MAX_SPEED)
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def draw_snake(self):
        """
        Render the snake with dynamic lighting effects.

        Features:
        - Different colors for head and body
        - Pulsing glow effect on head
        - Rounded segments for modern look
        """
        for i, segment in enumerate(self.snake):
            color = COLORS["snake_head"] if i == 0 else COLORS["snake_body"][i % 2]
            rect = pygame.Rect(
                segment[0] + GRID_OFFSET,
                segment[1] + GRID_OFFSET,
                CELL_SIZE - GRID_OFFSET * 2,
                CELL_SIZE - GRID_OFFSET * 2,
            )
            pygame.draw.rect(self.screen, color, rect, border_radius=7)

            if i == 0:
                glow_size = int(math.sin(pygame.time.get_ticks() * 0.005) * 5 + 10)
                glow_surface = pygame.Surface(
                    (CELL_SIZE * 2, CELL_SIZE * 2), pygame.SRCALPHA
                )
                pygame.draw.circle(
                    glow_surface,
                    (*COLORS["snake_head"], 50),
                    (glow_size, glow_size),
                    glow_size,
                )
                self.screen.blit(
                    glow_surface,
                    (segment[0] - CELL_SIZE // 2, segment[1] - CELL_SIZE // 2),
                )

    def draw_food(self):
        """
        Render food with pulsing effect and glow.

        Features:
        - Pulsing animation
        - Glowing aura
        - Elliptical shape
        """
        pulse = math.sin(pygame.time.get_ticks() * 0.005) * 3
        food_rect = pygame.Rect(
            self.food[0] + GRID_OFFSET + pulse,
            self.food[1] + GRID_OFFSET + pulse,
            CELL_SIZE - GRID_OFFSET * 2 - pulse * 2,
            CELL_SIZE - GRID_OFFSET * 2 - pulse * 2,
        )
        pygame.draw.ellipse(self.screen, COLORS["food"], food_rect)

        glow_surface = pygame.Surface((CELL_SIZE * 2, CELL_SIZE * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            glow_surface, (*COLORS["food"], 30), (CELL_SIZE, CELL_SIZE), CELL_SIZE // 2
        )
        self.screen.blit(
            glow_surface, (self.food[0] - CELL_SIZE // 2, self.food[1] - CELL_SIZE // 2)
        )

    def draw(self):
        """Render all game elements to the screen."""
        self.screen.fill(COLORS["background"])
        self.draw_grid()
        self.draw_snake()
        self.draw_food()
        self.draw_score()

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_grid(self):
        """Render the game grid."""
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, COLORS["grid"], (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, COLORS["grid"], (0, y), (WIDTH, y))

    def draw_score(self):
        """Render the current score."""
        score_text = self.font.render(f"Score: {self.score}", True, COLORS["text"])
        self.screen.blit(score_text, (10, 10))

    def draw_game_over(self):
        """
        Render game over screen with overlay and instructions.

        Features:
        - Semi-transparent dark overlay
        - Large game over text
        - Restart and quit instructions
        """
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill(COLORS["overlay"])
        self.screen.blit(overlay, (0, 0))

        game_over_text = self.big_font.render("GAME OVER", True, COLORS["accent"])
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.screen.blit(game_over_text, game_over_rect)

        restart_text = self.font.render(
            "Press SPACE to Restart  |  Q to Quit", True, COLORS["text"]
        )
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        self.screen.blit(restart_text, restart_rect)

    def run(self):
        """
        Main game loop handling events and updates.

        Controls:
        - Arrow keys: Move snake
        - Space: Restart game
        - Q: Quit game
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return
                    if event.key == pygame.K_SPACE:
                        if self.game_over:
                            self.reset_game()
                        else:
                            # Pause game if needed
                            pass
                    if not self.game_over:
                        if event.key == pygame.K_UP and self.direction != DOWN:
                            self.direction = UP
                        elif event.key == pygame.K_DOWN and self.direction != UP:
                            self.direction = DOWN
                        elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                            self.direction = LEFT
                        elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                            self.direction = RIGHT

            self.move()
            self.draw()
            self.clock.tick(int(self.current_speed))


if __name__ == "__main__":
    game = ProfessionalSnakeGame()
    game.run()
