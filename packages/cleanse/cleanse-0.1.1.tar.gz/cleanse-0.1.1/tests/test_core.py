"""Tests for core functionality."""
from cleanse.core import DependencyAnalyzer, PackageInfo

def test_analyzer_creation():
    """Test analyzer instantiation."""
    analyzer = DependencyAnalyzer()
    assert analyzer is not None

def test_package_analysis():
    """Test package analysis."""
    analyzer = DependencyAnalyzer()
    info = analyzer.analyze_package("click")
    assert isinstance(info, PackageInfo)
    assert info.name == "click"
