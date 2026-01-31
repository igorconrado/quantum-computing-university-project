"""
Quantum Pong - Entry Point

Run this file to start the game:
    python main.py

Controls:
    H     - Apply Hadamard gate (creates superposition)
    X     - Apply X/NOT gate (flip qubit)
    Z     - Apply Z gate (phase flip)
    C     - Apply CNOT gate (entangle qubits)
    R     - Reset quantum state to |000⟩
    SPACE - Measure (collapse superposition to definite position)
    P     - Pause game
    ESC   - Quit

The quantum paddle starts in state |000⟩ (position 0).
Apply H to create superposition across all 8 positions.
Press SPACE to measure when the ball approaches!

Tip: The paddle can only block the ball when it's measured (collapsed).
     A paddle in superposition will let the ball pass through!
"""

from game import Game


def main():
    print("=" * 50)
    print("        QUANTUM PONG")
    print("=" * 50)
    print()
    print("Controls:")
    print("  H     - Hadamard gate (superposition)")
    print("  X     - NOT gate (flip)")
    print("  Z     - Phase gate")
    print("  C     - CNOT gate (entangle)")
    print("  R     - Reset to |000>")
    print("  SPACE - Measure position")
    print("  P     - Pause")
    print("  ESC   - Quit")
    print()
    print("Tip: Paddle in superposition can't block the ball!")
    print("     Measure (SPACE) before the ball arrives!")
    print()
    print("Starting game...")
    print()

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
