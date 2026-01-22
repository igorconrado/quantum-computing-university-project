"""
Quantum Pong - Main game loop using Pygame.

TODO: Implement the game logic.
"""

import pygame
import sys

# TODO: Import QuantumPaddle when implemented
# from quantum_paddle import QuantumPaddle


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
QUANTUM_BLUE = (0, 150, 255)
QUANTUM_PURPLE = (150, 0, 255)


class Ball:
    """The pong ball."""

    def __init__(self, x: int, y: int, radius: int = 10):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = 5  # velocity x
        self.dy = 3  # velocity y

    def move(self):
        """Update ball position."""
        # TODO: Implement movement
        pass

    def bounce_vertical(self):
        """Bounce off top/bottom walls."""
        # TODO: Implement
        pass

    def bounce_horizontal(self):
        """Bounce off paddle."""
        # TODO: Implement
        pass

    def draw(self, screen):
        """Draw the ball."""
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)


class ClassicalPaddle:
    """A normal paddle (for the opponent)."""

    def __init__(self, x: int, y: int, width: int = 10, height: int = 80):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5

    def move_up(self):
        """Move paddle up."""
        # TODO: Implement
        pass

    def move_down(self, screen_height: int):
        """Move paddle down."""
        # TODO: Implement
        pass

    def draw(self, screen):
        """Draw the paddle."""
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))


class QuantumPaddleVisual:
    """
    Visual representation of the quantum paddle.
    Shows probability distribution as gradient.
    """

    def __init__(self, x: int, screen_height: int, width: int = 10, n_positions: int = 8):
        self.x = x
        self.screen_height = screen_height
        self.width = width
        self.n_positions = n_positions
        self.segment_height = screen_height // n_positions

        # TODO: Initialize QuantumPaddle
        # self.quantum = QuantumPaddle(n_qubits=3)
        self.current_position = 0
        self.probabilities = [1/n_positions] * n_positions

    def apply_gate(self, gate: str):
        """
        Apply a quantum gate.

        Args:
            gate: 'H', 'X', 'Z', etc.
        """
        # TODO: Apply gate to quantum paddle
        # TODO: Update probabilities
        pass

    def measure(self) -> int:
        """Measure and collapse to definite position."""
        # TODO: Measure quantum paddle
        # TODO: Update current_position
        pass

    def draw_probabilities(self, screen):
        """Draw probability distribution as colored segments."""
        for i, prob in enumerate(self.probabilities):
            y = i * self.segment_height
            # Color intensity based on probability
            intensity = int(255 * prob * self.n_positions)
            color = (0, min(intensity, 255), min(intensity, 255))
            pygame.draw.rect(screen, color, (self.x, y, self.width, self.segment_height))

    def draw_collapsed(self, screen):
        """Draw paddle at measured position."""
        y = self.current_position * self.segment_height
        pygame.draw.rect(screen, QUANTUM_BLUE, (self.x, y, self.width, self.segment_height))


class Game:
    """Main game class."""

    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Quantum Pong")
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Game objects
        self.ball = Ball(width // 2, height // 2)
        self.player = QuantumPaddleVisual(20, height)
        self.opponent = ClassicalPaddle(width - 30, height // 2 - 40)

        # Score
        self.player_score = 0
        self.opponent_score = 0

        # Game state
        self.running = True
        self.paused = False

    def handle_events(self):
        """Handle keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Quantum controls
                if event.key == pygame.K_h:
                    self.player.apply_gate('H')
                elif event.key == pygame.K_x:
                    self.player.apply_gate('X')
                elif event.key == pygame.K_z:
                    self.player.apply_gate('Z')
                elif event.key == pygame.K_SPACE:
                    self.player.measure()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

    def update(self):
        """Update game state."""
        if self.paused:
            return

        # TODO: Move ball
        # TODO: Check collisions
        # TODO: Update scores
        # TODO: AI for opponent
        pass

    def draw(self):
        """Draw everything."""
        self.screen.fill(BLACK)

        # Draw center line
        for y in range(0, self.height, 20):
            pygame.draw.rect(self.screen, WHITE, (self.width // 2 - 2, y, 4, 10))

        # Draw game objects
        self.ball.draw(self.screen)
        self.player.draw_probabilities(self.screen)
        self.opponent.draw(self.screen)

        # Draw scores
        font = pygame.font.Font(None, 74)
        player_text = font.render(str(self.player_score), True, WHITE)
        opponent_text = font.render(str(self.opponent_score), True, WHITE)
        self.screen.blit(player_text, (self.width // 4, 20))
        self.screen.blit(opponent_text, (3 * self.width // 4, 20))

        # Draw controls help
        font_small = pygame.font.Font(None, 24)
        controls = [
            "H: Hadamard (superposition)",
            "X: NOT gate",
            "Z: Phase flip",
            "SPACE: Measure",
            "P: Pause"
        ]
        for i, text in enumerate(controls):
            surface = font_small.render(text, True, QUANTUM_PURPLE)
            self.screen.blit(surface, (10, self.height - 120 + i * 20))

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
