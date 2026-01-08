# Quick Start Guide

## For VS Code Users (Recommended)

### First Time Setup
```bash
cd hsl-data-presentation
mise install  # Installs Python + dependencies automatically
```

### Open and Run
1. Open project folder in VS Code
2. Open a notebook: `notebooks/01_data_extraction.ipynb`
3. Click kernel selector (top-right)
4. Choose: **"Python 3 (HSL Workshop)"** or **".venv (Python 3.14.2)"**
5. Run cells! 🚀

## For Terminal/Browser Users

### Activate Environment
```bash
source .venv/bin/activate
# or
source activate.sh
```

### Launch Jupyter
```bash
jupyter notebook
# or
jupyter lab
```

## Troubleshooting

### "Kernel not found"?
```bash
source .venv/bin/activate
python -m ipykernel install --user --name=hsl-workshop --display-name="Python 3 (HSL Workshop)"
```

### "Package not found"?
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### VS Code not using correct Python?
1. `Cmd + Shift + P`
2. Type: "Python: Select Interpreter"
3. Choose: `.venv/bin/python`

## What's Available

✅ Python 3.14.2
✅ All packages: pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter
✅ Pre-generated dataset: `data/raw/product_reviews.csv` (824 reviews)
✅ 5 interactive notebooks ready to run

## Workshop Order

1. `01_data_extraction.ipynb` - Load and explore data
2. `02_data_preparation.ipynb` - Clean and prepare data
3. `03_storage_theory.ipynb` - Learn about storage
4. `04_ml_analysis.ipynb` - Train ML model
5. `05_deployment_theory.ipynb` - Learn deployment

**Total time**: ~1 hour

---

📖 **Detailed guides:**
- [README.md](README.md) - Full workshop documentation
- [VSCODE_SETUP.md](VSCODE_SETUP.md) - VS Code specific setup

**Ready to start!** Open a notebook and begin coding. 🎉
