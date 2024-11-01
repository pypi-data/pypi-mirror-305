"""Command line interface for cleanse."""
import click
from rich.console import Console
from rich.table import Table
from pathlib import Path
from . import __version__
from .core import DependencyAnalyzer
from .utils import parse_requirements

console = Console()

@click.group()
@click.version_option(version=__version__)
def cli():
    """Analyze Python package dependencies for purity."""
    pass

@cli.command()
@click.argument('requirements_file', type=click.Path(exists=True), required=False)
@click.option('--json', is_flag=True, help="Output results as JSON")
@click.option('--verbose', '-v', is_flag=True, help="Show detailed output")
@click.option('--testing', is_flag=True, hidden=True, help="Enable testing mode", default=False)
def analyze(requirements_file: str, json: bool = False, verbose: bool = False, testing: bool = False):
    """Analyze dependencies for non-pure packages."""
    analyzer = DependencyAnalyzer(testing_mode=testing)
    
    with console.status("Analyzing dependencies..."):
        if requirements_file:
            packages = parse_requirements(Path(requirements_file))
            results = {name: analyzer.analyze_package(name) for name in packages}
        else:
            results = analyzer.get_all_dependencies()
    
    if json:
        # Convert results to JSON-serializable format
        json_results = {
            name: {
                "name": pkg.name,
                "version": pkg.version,
                "is_pure": pkg.is_pure,
                "dependencies": list(pkg.dependencies),
                "indicators": list(pkg.indicators)
            }
            for name, pkg in results.items()
        }
        click.echo(json_results)
        return
        
    # Create a rich table for output
    table = Table(title="Dependency Analysis Results")
    table.add_column("Package")
    table.add_column("Version")
    table.add_column("Pure?")
    
    if verbose:
        table.add_column("Indicators")
    
    for pkg in results.values():
        row = [
            pkg.name,
            pkg.version,
            "✅" if pkg.is_pure else "❌"
        ]
        if verbose:
            row.append("\n".join(pkg.indicators))
        table.add_row(*row)
    
    console.print(table)
