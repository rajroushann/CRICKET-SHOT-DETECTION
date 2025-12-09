# Contributing Guide

## Welcome! 👋

Thank you for your interest in contributing to the Cricket Shot Detection project. This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive criticism
- Welcome diverse perspectives
- Report inappropriate behavior to maintainers

## Getting Started

### 1. Fork the Repository
```bash
git clone https://github.com/yourusername/cricket-shot-detection.git
cd cricket-shot-detection
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Set Up Development Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Development Workflow

### Code Style
- Follow **PEP 8** guidelines
- Use **Black** for code formatting
- Use **Flake8** for linting

```bash
# Format code
black src/

# Check code quality
flake8 src/
mypy src/
```

### Writing Tests
- Write unit tests for new features
- Aim for >80% code coverage
- Use pytest framework

```bash
# Run tests
pytest tests/ -v

# Check coverage
pytest --cov=src tests/
```

### Commit Messages
Use conventional commits format:
```
type(scope): description

feat(model): add attention mechanism to LSTM
fix(api): handle empty video uploads
docs(readme): update installation instructions
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Pull Request Process
1. Update documentation and CHANGELOG
2. Add tests for new features
3. Ensure all tests pass
4. Submit PR with clear description
5. Respond to review feedback

## Reporting Issues

### Bug Reports
Include:
- Python version and OS
- Minimal reproduction steps
- Expected vs actual behavior
- Error logs/traceback

### Feature Requests
Include:
- Use case description
- Proposed solution
- Alternative approaches considered

## Documentation

### Update Files
- `README.md` - High-level overview
- `docs/` - Detailed documentation
- Inline code comments for complex logic
- Docstrings for all functions (Google style)

Example docstring:
```python
def predict_shot(video_path: str, model_type: str = 'cnn-lstm') -> dict:
    """
    Predict cricket shots from video.
    
    Args:
        video_path: Path to cricket video file
        model_type: Type of model to use
    
    Returns:
        Dictionary containing predictions and metadata
        
    Raises:
        FileNotFoundError: If video file not found
        ValueError: If unsupported video format
    """
```

## Release Process

1. Update version in `__init__.py`
2. Update CHANGELOG with changes
3. Create release branch
4. Tag release: `git tag v1.0.0`
5. Push to GitHub

## Questions?

- Open an issue for discussions
- Check existing issues first
- Use GitHub Discussions for questions

Thank you for contributing! 🙏
