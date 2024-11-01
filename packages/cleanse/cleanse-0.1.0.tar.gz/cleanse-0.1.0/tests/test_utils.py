"""Tests for utility functions."""
from pathlib import Path
from cleanse.utils import parse_requirements, is_valid_package_name

def test_parse_simple_requirements(sample_requirements):
    """Test parsing simple requirements."""
    packages = parse_requirements(sample_requirements)
    assert "click" in packages
    assert "numpy" in packages
    assert "requests" in packages

def test_parse_complex_requirements(complex_requirements):
    """Test parsing complex requirements formats."""
    packages = parse_requirements(complex_requirements)
    assert "pandas" in packages
    assert "Pillow" in packages
    assert "PyYAML" in packages
    # Should not include git or -r requirements
    assert not any(pkg.startswith('git+') for pkg in packages)
    assert not any(pkg.startswith('-r') for pkg in packages)

def test_valid_package_names():
    """Test package name validation."""
    assert is_valid_package_name("requests")
    assert is_valid_package_name("python-dateutil")
    assert is_valid_package_name("PyYAML")
    assert not is_valid_package_name("invalid/name")
    assert not is_valid_package_name("invalid space")
