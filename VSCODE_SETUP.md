# VS Code + Mise Setup Guide

## What's Been Configured

✅ mise with Python 3.14.2 and automatic virtual environment (`.venv`)
✅ All Python dependencies installed in the virtual environment
✅ Jupyter kernel registered: "Python 3 (HSL Workshop)"
✅ VS Code settings configured to use the mise environment

## How to Use in VS Code

### 1. Open a Notebook

1. Open any notebook file (e.g., `notebooks/01_data_extraction.ipynb`)
2. VS Code will automatically open it in the Notebook editor

### 2. Select the Kernel

When you open a notebook for the first time:

1. Click on the kernel selector in the top-right corner (it might say "Select Kernel" or show the current kernel)
2. Choose **"Python 3 (HSL Workshop)"** from the list
   - Alternatively, you can select **"Python Environments..."** and choose `.venv (Python 3.14.2)`

### 3. Run Cells

- Click the play button (▶) next to any cell to run it
- Or use keyboard shortcuts:
  - `Shift + Enter`: Run cell and move to next
  - `Ctrl + Enter`: Run cell and stay on current cell

## Verifying the Setup

Open a notebook and run this cell to verify everything is working:

```python
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

print("✓ All packages imported successfully!")
print(f"Python: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
```

## Troubleshooting

### Kernel not showing up?

1. Reload VS Code: `Cmd + Shift + P` → "Reload Window"
2. Check the kernel list: Click kernel selector → "Select Another Kernel"
3. Look for "Python 3 (HSL Workshop)" or `.venv`

### Wrong Python interpreter?

1. Open Command Palette: `Cmd + Shift + P`
2. Type "Python: Select Interpreter"
3. Choose `.venv` (should show path: `.venv/bin/python`)

### Packages not found?

Make sure you're using the correct kernel:
```bash
# In terminal, verify packages are installed
source .venv/bin/activate
python -c "import pandas; print('OK')"
```

## Using mise in Terminal

If you want to use the terminal within VS Code:

1. Open a new terminal: `Cmd + J` or Terminal → New Terminal
2. The mise environment should auto-activate
3. Verify with: `which python` (should show `.venv/bin/python`)

Or manually activate:
```bash
source .venv/bin/activate
```

## Running All Notebooks

To run all notebooks sequentially:

1. Open `notebooks/01_data_extraction.ipynb`
2. Select kernel: "Python 3 (HSL Workshop)"
3. Run all cells: Click "Run All" button or `Cmd + Shift + Enter`
4. Move to the next notebook and repeat

## Alternative: Using Jupyter in Browser

If you prefer the classic Jupyter interface:

```bash
source .venv/bin/activate
jupyter notebook
```

This will open Jupyter in your browser, and the "Python 3 (HSL Workshop)" kernel will be available.

## Configuration Files

The following files configure the setup:

- **`mise.toml`**: Defines Python version and virtual environment
- **`.vscode/settings.json`**: VS Code Python and Jupyter settings
- **`requirements.txt`**: Python package dependencies

## Notes

- The virtual environment (`.venv`) is created automatically by mise
- All dependencies are isolated in this environment
- VS Code is configured to use this environment by default
- The Jupyter kernel is registered system-wide but points to this project's venv

---

**Ready to go!** Open a notebook and start coding. 🚀
