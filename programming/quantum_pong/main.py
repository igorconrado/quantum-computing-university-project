"""
Quantum Pong - Entry Point

Run this file to start the game:
    python main.py

Controls:
    H     - Apply Hadamard gate (creates superposition)
    X     - Apply X/NOT gate (flip qubit)
    Z     - Apply Z gate (phase flip)
    SPACE - Measure (collapse superposition to definite position)
    P     - Pause game
    ESC   - Quit

The quantum paddle starts in state |000⟩ (bottom position).
Apply H to create superposition across all positions.
Press SPACE to measure when the ball approaches!
"""

from game import Game


def main():
    print("=" * 50)
    print("        QUANTUM PONG")
    print("=" * 50)
    print()
    print("Controls:")
    print("  H     - Hadamard gate (superposition)")
    print("  X     - NOT gate")
    print("  Z     - Phase gate")
    print("  SPACE - Measure position")
    print("  P     - Pause")
    print("  ESC   - Quit")
    print()
    print("Starting game...")
    print()

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
