"""
Quantum Pong - Main game loop using Pygame.

Based on the 'Programming on Quantum Computers' YouTube series.
"""

import pygame
import sys
import random

from quantum_paddle import QuantumPaddle


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
QUANTUM_BLUE = (0, 150, 255)
QUANTUM_PURPLE = (150, 0, 255)
SUPERPOSITION_COLOR = (0, 200, 200)


class Ball:
    """The pong ball."""

    def __init__(self, x: int, y: int, radius: int = 10):
        self.start_x = x
        self.start_y = y
        self.x = float(x)
        self.y = float(y)
        self.radius = radius
        self.base_speed = 5
        self.dx = self.base_speed
        self.dy = random.uniform(-3, 3)

    def reset(self, direction: int = 1):
        """Reset ball to center with given direction."""
        self.x = float(self.start_x)
        self.y = float(self.start_y)
        self.dx = self.base_speed * direction
        self.dy = random.uniform(-3, 3)

    def move(self):
        """Update ball position."""
        self.x += self.dx
        self.y += self.dy

    def bounce_vertical(self, screen_height: int):
        """Bounce off top/bottom walls."""
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy = -self.dy
        elif self.y + self.radius >= screen_height:
            self.y = screen_height - self.radius
            self.dy = -self.dy

    def bounce_horizontal(self):
        """Bounce off paddle (reverse x direction)."""
        self.dx = -self.dx
        # Add some randomness to make game interesting
        self.dy += random.uniform(-1, 1)
        # Limit vertical speed
        self.dy = max(-8, min(8, self.dy))

    def draw(self, screen):
        """Draw the ball."""
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)


class ClassicalPaddle:
    """A normal paddle (for the opponent)."""

    def __init__(self, x: int, y: int, width: int = 10, height: int = 80):
        self.x = x
        self.y = float(y)
        self.width = width
        self.height = height
        self.speed = 4

    def move_up(self, min_y: int = 0):
        """Move paddle up."""
        self.y = max(min_y, self.y - self.speed)

    def move_down(self, screen_height: int):
        """Move paddle down."""
        self.y = min(screen_height - self.height, self.y + self.speed)

    def ai_move(self, ball: Ball, screen_height: int):
        """Simple AI: follow the ball."""
        paddle_center = self.y + self.height / 2
        if ball.x > self.x / 2:  # Only move when ball is on AI's side
            if ball.y < paddle_center - 10:
                self.move_up()
            elif ball.y > paddle_center + 10:
                self.move_down(screen_height)

    def collides_with(self, ball: Ball) -> bool:
        """Check if ball collides with paddle."""
        return (
            ball.x + ball.radius >= self.x
            and ball.x - ball.radius <= self.x + self.width
            and ball.y + ball.radius >= self.y
            and ball.y - ball.radius <= self.y + self.height
        )

    def draw(self, screen):
        """Draw the paddle."""
        pygame.draw.rect(screen, WHITE, (self.x, int(self.y), self.width, self.height))


class QuantumPaddleVisual:
    """
    Visual representation of the quantum paddle.
    Shows probability distribution as gradient.
    """

    def __init__(self, x: int, screen_height: int, width: int = 15, n_qubits: int = 3):
        self.x = x
        self.screen_height = screen_height
        self.width = width
        self.n_qubits = n_qubits
        self.n_positions = 2 ** n_qubits
        self.segment_height = screen_height // self.n_positions
        self.paddle_height = self.segment_height  # Paddle covers one segment

        # Initialize quantum paddle
        self.quantum = QuantumPaddle(n_qubits=n_qubits)
        self.current_position = 0
        self.probabilities = self.quantum.get_probabilities()
        self.is_measured = True  # Starts in definite state |000⟩

    def apply_gate(self, gate: str):
        """
        Apply a quantum gate.

        Args:
            gate: 'H', 'X', 'Z', etc.
        """
        if gate == 'H':
            self.quantum.apply_hadamard()
            self.is_measured = False
        elif gate == 'X':
            # Apply X to first qubit (most significant effect)
            self.quantum.apply_x(0)
        elif gate == 'Z':
            self.quantum.apply_z(0)
        elif gate == 'CNOT':
            if self.n_qubits >= 2:
                self.quantum.apply_cnot(0, 1)

        # Update probabilities display
        self.probabilities = self.quantum.get_probabilities()

    def measure(self) -> int:
        """Measure and collapse to definite position."""
        self.current_position = self.quantum.measure()
        self.probabilities = self.quantum.get_probabilities()
        self.is_measured = True
        return self.current_position

    def get_paddle_rect(self) -> tuple:
        """Get the rectangle of the collapsed paddle for collision detection."""
        y = self.current_position * self.segment_height
        return (self.x, y, self.width, self.paddle_height)

    def collides_with(self, ball: Ball) -> bool:
        """Check if ball collides with measured paddle position."""
        if not self.is_measured:
            return False  # Can't collide with superposition!

        rect = self.get_paddle_rect()
        x, y, w, h = rect
        return (
            ball.x - ball.radius <= x + w
            and ball.x + ball.radius >= x
            and ball.y + ball.radius >= y
            and ball.y - ball.radius <= y + h
        )

    def draw_probabilities(self, screen):
        """Draw probability distribution as colored segments."""
        for i, prob in enumerate(self.probabilities):
            y = i * self.segment_height
            # Color intensity based on probability
            intensity = int(255 * prob * self.n_positions)
            intensity = min(255, intensity)
            color = (0, intensity, intensity)
            pygame.draw.rect(
                screen, color, (self.x, y, self.width, self.segment_height)
            )
            # Draw segment border
            pygame.draw.rect(
                screen,
                QUANTUM_PURPLE,
                (self.x, y, self.width, self.segment_height),
                1,
            )

    def draw_collapsed(self, screen):
        """Draw paddle at measured position."""
        y = self.current_position * self.segment_height
        pygame.draw.rect(
            screen, QUANTUM_BLUE, (self.x, y, self.width, self.segment_height)
        )

    def draw(self, screen):
        """Draw the quantum paddle (superposition or collapsed)."""
        self.draw_probabilities(screen)
        if self.is_measured:
            self.draw_collapsed(screen)


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
        self.player = QuantumPaddleVisual(20, height, n_qubits=3)
        self.opponent = ClassicalPaddle(width - 30, height // 2 - 40)

        # Score
        self.player_score = 0
        self.opponent_score = 0
        self.max_score = 5

        # Game state
        self.running = True
        self.paused = False
        self.game_over = False
        self.winner = None
        self.show_instructions = True  # Show tutorial at start

        # Fonts
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_title = pygame.font.Font(None, 56)

    def reset_game(self):
        """Reset game to initial state."""
        self.ball.reset(direction=1)
        self.player = QuantumPaddleVisual(20, self.height, n_qubits=3)
        self.opponent = ClassicalPaddle(self.width - 30, self.height // 2 - 40)
        self.player_score = 0
        self.opponent_score = 0
        self.game_over = False
        self.winner = None
        self.paused = False

    def handle_events(self):
        """Handle keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if self.show_instructions:
                    # Any key starts the game
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    else:
                        self.show_instructions = False
                elif self.game_over:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                else:
                    # Quantum controls
                    if event.key == pygame.K_h:
                        self.player.apply_gate('H')
                    elif event.key == pygame.K_x:
                        self.player.apply_gate('X')
                    elif event.key == pygame.K_z:
                        self.player.apply_gate('Z')
                    elif event.key == pygame.K_c:
                        self.player.apply_gate('CNOT')
                    elif event.key == pygame.K_SPACE:
                        self.player.measure()
                    elif event.key == pygame.K_r:
                        self.player.quantum.reset()
                        self.player.probabilities = self.player.quantum.get_probabilities()
                        self.player.is_measured = True
                        self.player.current_position = 0
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused

    def update(self):
        """Update game state."""
        if self.show_instructions or self.paused or self.game_over:
            return

        # Move ball
        self.ball.move()

        # Bounce off top/bottom
        self.ball.bounce_vertical(self.height)

        # AI opponent
        self.opponent.ai_move(self.ball, self.height)

        # Check collision with player paddle (quantum)
        if self.ball.dx < 0 and self.player.collides_with(self.ball):
            self.ball.bounce_horizontal()
            # Move ball out of paddle to avoid multiple collisions
            self.ball.x = self.player.x + self.player.width + self.ball.radius

        # Check collision with opponent paddle (classical)
        if self.ball.dx > 0 and self.opponent.collides_with(self.ball):
            self.ball.bounce_horizontal()
            self.ball.x = self.opponent.x - self.ball.radius

        # Check scoring
        if self.ball.x < 0:
            # Opponent scores
            self.opponent_score += 1
            if self.opponent_score >= self.max_score:
                self.game_over = True
                self.winner = "Classical"
            else:
                self.ball.reset(direction=1)
                # Reset quantum paddle
                self.player.quantum.reset()
                self.player.probabilities = self.player.quantum.get_probabilities()
                self.player.is_measured = True
                self.player.current_position = 0

        elif self.ball.x > self.width:
            # Player scores
            self.player_score += 1
            if self.player_score >= self.max_score:
                self.game_over = True
                self.winner = "Quantum"
            else:
                self.ball.reset(direction=-1)

    def draw(self):
        """Draw everything."""
        self.screen.fill(BLACK)

        # Show instructions screen at start
        if self.show_instructions:
            self._draw_instructions()
            pygame.display.flip()
            return

        # Draw center line
        for y in range(0, self.height, 20):
            pygame.draw.rect(self.screen, WHITE, (self.width // 2 - 2, y, 4, 10))

        # Draw game objects
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        self.opponent.draw(self.screen)

        # Draw scores
        player_text = self.font_large.render(str(self.player_score), True, QUANTUM_BLUE)
        opponent_text = self.font_large.render(str(self.opponent_score), True, WHITE)
        self.screen.blit(player_text, (self.width // 4, 20))
        self.screen.blit(opponent_text, (3 * self.width // 4, 20))

        # Draw quantum state indicator (bottom center)
        state_text = "SUPERPOSICAO" if not self.player.is_measured else f"POSICAO: {self.player.current_position}"
        state_color = SUPERPOSITION_COLOR if not self.player.is_measured else QUANTUM_BLUE
        state_surface = self.font_small.render(state_text, True, state_color)
        self.screen.blit(state_surface, state_surface.get_rect(center=(self.width // 2, self.height - 20)))

        # Draw controls help (bottom, subtle)
        controls = "H: Super  |  SPACE: Medir  |  R: Reset"
        ctrl_surface = self.font_small.render(controls, True, (60, 60, 60))
        self.screen.blit(ctrl_surface, ctrl_surface.get_rect(center=(self.width // 2, self.height - 45)))

        # Draw game over screen
        if self.game_over:
            self._draw_game_over()

        # Draw pause overlay
        if self.paused and not self.game_over:
            pause_surface = self.font_large.render("PAUSED", True, WHITE)
            rect = pause_surface.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(pause_surface, rect)

        pygame.display.flip()

    def _draw_instructions(self):
        """Draw the instructions/tutorial screen."""
        cx = self.width // 2

        # Title
        title = self.font_large.render("QUANTUM PONG", True, QUANTUM_BLUE)
        self.screen.blit(title, title.get_rect(center=(cx, 60)))

        # Main concept - centered and simple
        lines = [
            ("Sua raquete e QUANTICA!", WHITE),
            ("", WHITE),
            ("H  -  Superposicao (8 posicoes)", SUPERPOSITION_COLOR),
            ("SPACE  -  Medir (colapsar)", QUANTUM_BLUE),
            ("", WHITE),
            ("Raquete em superposicao NAO bloqueia!", (255, 100, 100)),
            ("Meca antes da bola chegar!", (255, 100, 100)),
        ]

        y = 150
        for text, color in lines:
            if text:
                surface = self.font_medium.render(text, True, color)
                self.screen.blit(surface, surface.get_rect(center=(cx, y)))
            y += 38

        # Controls (bottom, above start prompt)
        controls = "R: Reset  |  P: Pause  |  ESC: Sair"
        ctrl_surface = self.font_small.render(controls, True, (100, 100, 100))
        self.screen.blit(ctrl_surface, ctrl_surface.get_rect(center=(cx, self.height - 100)))

        # Start prompt
        start_text = self.font_medium.render("Pressione qualquer tecla", True, WHITE)
        self.screen.blit(start_text, start_text.get_rect(center=(cx, self.height - 60)))

    def _draw_game_over(self):
        """Draw game over screen."""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.fill(BLACK)
        overlay.set_alpha(180)
        self.screen.blit(overlay, (0, 0))

        # Winner text
        color = QUANTUM_BLUE if self.winner == "Quantum" else WHITE
        winner_text = self.font_large.render(f"{self.winner} Wins!", True, color)
        rect = winner_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(winner_text, rect)

        # Score
        score_text = self.font_medium.render(
            f"Final: {self.player_score} - {self.opponent_score}", True, WHITE
        )
        rect = score_text.get_rect(center=(self.width // 2, self.height // 2 + 20))
        self.screen.blit(score_text, rect)

        # Instructions
        restart_text = self.font_small.render("Press ENTER to play again or ESC to quit", True, WHITE)
        rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 80))
        self.screen.blit(restart_text, rect)

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
