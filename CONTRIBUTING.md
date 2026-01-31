# Contributing to Quantum Computing University Project

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/quantum-computing-university-project.git
   cd quantum-computing-university-project
   ```
3. Set up the development environment (see [Development Setup](#development-setup))
4. Create a new branch for your contribution

## How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker
- Describe the bug clearly with steps to reproduce
- Include your environment details (Python version, OS, etc.)
- If possible, include a minimal code example

### Suggesting Features

- Open an issue with the `enhancement` label
- Describe the feature and its use case
- Explain why this feature would be useful

### Submitting Code

1. Ensure your code follows our coding standards
2. Write or update tests as needed
3. Update documentation if necessary
4. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Run tests to verify setup
pytest
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=programming

# Run specific test file
pytest tests/test_quantum_paddle.py
```

### Linting

```bash
# Run ruff linter
ruff check .

# Run ruff formatter
ruff format .
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints for function signatures
- Write docstrings for all public functions and classes
- Maximum line length: 88 characters (Black default)

### Example

```python
def create_bell_state(variant: str = "phi_plus") -> QuantumCircuit:
    """
    Create a Bell state circuit.

    Args:
        variant: One of "phi_plus", "phi_minus", "psi_plus", "psi_minus"

    Returns:
        QuantumCircuit preparing the Bell state

    Raises:
        ValueError: If variant is not recognized
    """
    if variant not in ["phi_plus", "phi_minus", "psi_plus", "psi_minus"]:
        raise ValueError(f"Unknown variant: {variant}")

    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc
```

### Documentation

- Update README files when adding features
- Include docstrings with Args, Returns, and Raises sections
- Add inline comments for complex logic

## Commit Guidelines

We use [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```
<type>: <description>

[optional body]

[optional footer]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat: add quantum teleportation protocol

fix: correct phase calculation in Grover oracle

docs: update installation instructions

test: add unit tests for QUBO solver
```

## Pull Request Process

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes**:
   ```bash
   pytest
   ruff check .
   ```

4. **Commit your changes** with a descriptive message

5. **Push to your fork**:
   ```bash
   git push origin feat/your-feature-name
   ```

6. **Open a Pull Request** on GitHub:
   - Fill out the PR template
   - Link any related issues
   - Request review from maintainers

7. **Address review feedback** if any

8. **Merge** once approved

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages follow conventions

## Questions?

If you have questions, feel free to:

- Open an issue with the `question` label
- Contact the maintainers

Thank you for contributing! 🚀
