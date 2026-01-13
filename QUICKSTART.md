# Quick Start Guide

Get started with the MLE Lifecycle Workshop in 5 minutes! ⚡

## 🚀 For VS Code Users (Recommended)

### First Time Setup
```bash
cd hsl-presentation-data-advanced
mise install  # Installs Python 3.14.2 + all dependencies
```

### Open and Run
1. Open project folder in VS Code
2. Open first notebook: `notebooks/01_business_analysis.ipynb`
3. Click kernel selector (top-right)
4. Choose: **"Python 3 (HSL Workshop)"** or **".venv (Python 3.14.2)"**
5. Run cells! 🎉

---

## 💻 For Terminal/Browser Users

### Activate Environment
```bash
source .venv/bin/activate
# or use helper script
source activate.sh
```

### Launch Jupyter
```bash
jupyter notebook
# or
jupyter lab
```

Then navigate to `notebooks/` and open notebooks in order.

---

## 📚 Workshop Order (Follow This!)

| # | Notebook | Duration | What You'll Learn |
|---|----------|----------|-------------------|
| 1 | `01_business_analysis.ipynb` | 10-12 min | Explore data & assess feasibility |
| 2 | `02_etl_data_preparation.ipynb` | 15-18 min | Build ETL pipeline (Bronze→Silver→Gold) |
| 3 | `03_ml_model_training.ipynb` | 18-20 min | Train ML model + smart discounts + MLOps |
| 4 | `04_deployment_practice.ipynb` | 12-15 min | Build API + monitoring dashboard |

**Total**: ~60 minutes

---

## ✅ What's Pre-configured

✅ Python 3.14.2
✅ All packages: pandas, numpy, scikit-learn, matplotlib, FastAPI
✅ Pre-generated dataset: `data/raw/product_reviews.csv` (800 reviews)
✅ Jupyter kernel: "Python 3 (HSL Workshop)"

---

## 🔧 Quick Troubleshooting

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

### "Dataset not found"?
```bash
python generate_realistic_data.py
```

### VS Code not using correct Python?
1. `Cmd/Ctrl + Shift + P`
2. Type: "Python: Select Interpreter"
3. Choose: `.venv/bin/python`

---

## 🎯 What You'll Build

By the end, you'll have:
- ✅ Complete ETL pipeline (Bronze/Silver/Gold data layers)
- ✅ Trained sentiment analysis model (87%+ accuracy)
- ✅ Smart discount system (ML + inventory + sales)
- ✅ Working REST API with FastAPI
- ✅ Live monitoring dashboard
- ✅ Model versioning & validation (MLOps basics)

---

## 📖 Need More Help?

- **Full documentation**: [README.md](README.md)
- **VS Code setup guide**: [VSCODE_SETUP.md](VSCODE_SETUP.md)
- **Interactive discussions**: Built into notebooks!

---

**Ready to start!** Open `notebooks/01_business_analysis.ipynb` and begin your MLE journey! 🚀
