"""Pytest configuration and fixtures."""
import pytest
from pathlib import Path

@pytest.fixture
def sample_requirements(tmp_path):
    """Create a sample requirements file with known pure and non-pure packages."""
    requirements = tmp_path / "requirements.txt"
    content = """
# Pure Python packages
click==8.1.0
rich==13.0.0
requests>=2.31.0

# Non-pure packages (contain C extensions)
numpy>=1.20.0
pandas>=2.0.0
scipy>=1.11.0
psycopg2>=2.9.0
Pillow>=10.0.0  # Note: Pillow is case-sensitive

# Comments and empty lines for testing
# This is a comment
"""
    requirements.write_text(content.strip())
    return requirements

@pytest.fixture
def pure_only_requirements(tmp_path):
    """Create a requirements file with only pure Python packages."""
    requirements = tmp_path / "pure_requirements.txt"
    content = """
click==8.1.0
rich==13.0.0
requests>=2.31.0
PyYAML>=6.0.0
urllib3>=2.0.0
"""
    requirements.write_text(content.strip())
    return requirements

@pytest.fixture
def non_pure_only_requirements(tmp_path):
    """Create a requirements file with only non-pure packages."""
    requirements = tmp_path / "non_pure_requirements.txt"
    content = """
numpy>=1.20.0
pandas>=2.0.0
scipy>=1.11.0
psycopg2>=2.9.0
Pillow>=10.0.0
lxml>=4.9.0
"""
    requirements.write_text(content.strip())
    return requirements

@pytest.fixture
def complex_requirements(tmp_path):
    """Create a requirements file with complex formats."""
    requirements = tmp_path / "complex_requirements.txt"
    content = """
# Different version specifiers
requests==2.31.0
click>=1.0.0
rich~=13.0.0

# With extras
pandas[all]>=2.0.0
pytest[testing]>=7.0.0

# With comments
numpy>=1.20.0  # Latest stable
scipy>=1.11.0  # Required for scientific computing

# Case sensitivity
Pillow>=10.0.0
PyYAML>=6.0.0

# Empty lines and comments

# Invalid lines (should be ignored)
-e git+https://github.com/user/repo.git#egg=package
-r other-requirements.txt
"""
    requirements.write_text(content.strip())
    return requirements
