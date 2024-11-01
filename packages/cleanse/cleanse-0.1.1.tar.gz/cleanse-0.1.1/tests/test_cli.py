"""Tests for the CLI interface."""
from click.testing import CliRunner
from cleanse.cli import cli

def test_version():
    """Test version output."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output.lower()

def test_analyze(sample_requirements):
    """Test analyze command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", str(sample_requirements)])
    if result.exit_code != 0:
        print(f"Error output: {result.output}")
        print(f"Exception: {result.exception}")
    assert result.exit_code == 0
    assert "Package" in result.output  # Check for table header

def test_analyze_verbose(sample_requirements):
    """Test analyze command with verbose output."""
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--verbose", str(sample_requirements)])
    assert result.exit_code == 0
    assert "Package" in result.output
    assert "Indicators" in result.output

def test_analyze_json(sample_requirements):
    """Test analyze command with JSON output."""
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--json", str(sample_requirements)])
    assert result.exit_code == 0
    assert "{" in result.output  # Basic JSON check

def test_analyze_finds_pure_packages(pure_only_requirements):
    """Test that analyze correctly identifies pure packages."""
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--testing", str(pure_only_requirements)])
    assert result.exit_code == 0
    # All packages in this file should be marked as pure
    assert "✅" in result.output  # Pure indicator
    assert "❌" not in result.output  # Should not have any non-pure packages

def test_analyze_finds_non_pure_packages(non_pure_only_requirements):
    """Test that analyze correctly identifies non-pure packages."""
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--testing", str(non_pure_only_requirements)])
    assert result.exit_code == 0
    # All packages in this file should be marked as non-pure
    assert "❌" in result.output  # Non-pure indicator
    assert "✅" not in result.output  # Should not have any pure packages

def test_analyze_mixed_packages(sample_requirements):
    """Test that analyze correctly handles mixed pure and non-pure packages."""
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--testing", str(sample_requirements)])
    assert result.exit_code == 0
    # Should find both pure and non-pure packages
    assert "✅" in result.output  # Pure indicator
    assert "❌" in result.output  # Non-pure indicator
