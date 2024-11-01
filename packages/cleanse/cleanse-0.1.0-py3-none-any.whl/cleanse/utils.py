"""Utility functions for cleanse."""
import re
from pathlib import Path
from typing import Set

def parse_requirements(requirements_file: Path) -> Set[str]:
    """Parse a requirements file and return package names."""
    packages = set()
    with requirements_file.open() as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Handle various requirement formats
                # Examples:
                # package==1.0.0
                # package>=1.0.0
                # package~=1.0.0
                # package[extra]>=1.0.0
                # -e git+https://...
                # package  # comment
                
                # Skip lines starting with -e (editable installs) or -r (requirements files)
                if line.startswith(('-e', '-r')):
                    continue
                
                # Remove inline comments
                line = line.split('#')[0].strip()
                
                # Extract package name
                if line:
                    # Remove any extras
                    line = re.sub(r'\[.*\]', '', line)
                    # Get the package name (everything before any version specifier)
                    match = re.match(r'^([a-zA-Z0-9\-._]+).*', line)
                    if match:
                        packages.add(match.group(1))
    
    return packages

def is_valid_package_name(name: str) -> bool:
    """Check if a string is a valid Python package name."""
    return bool(re.match(r'^[a-zA-Z0-9\-._]+$', name))
