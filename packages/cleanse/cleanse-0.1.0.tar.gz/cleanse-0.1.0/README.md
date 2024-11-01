# cleanse

A tool to analyze Python package dependencies for purity.

## Installation

```bash
pip install cleanse
```

## Usage

```bash
# Analyze requirements file
cleanse analyze requirements.txt

# Show verbose output
cleanse analyze -v requirements.txt

# Output as JSON
cleanse analyze --json requirements.txt

# Show help
cleanse --help
```

## Development

This project uses PDM for dependency management.

```bash
# Install dependencies
pdm install

# Run tests
pdm run test

# Run linting
pdm run lint
```

## License

MIT License
