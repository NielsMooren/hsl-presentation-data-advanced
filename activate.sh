#!/bin/bash
# Quick activation script for the workshop environment

# Activate the virtual environment
source .venv/bin/activate

echo "✓ HSL Workshop environment activated!"
echo ""
echo "Python: $(python --version)"
echo "Location: $(which python)"
echo ""
echo "Available commands:"
echo "  jupyter notebook    - Launch Jupyter in browser"
echo "  jupyter lab         - Launch JupyterLab"
echo "  python              - Run Python scripts"
echo ""
echo "To deactivate: deactivate"
