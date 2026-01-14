# Data Advanced Workshop: Complete MLE Lifecycle
## ETL → ML → MLOps → Deployment

A hands-on workshop teaching the **complete Machine Learning Engineering lifecycle** through a real-world sentiment analysis project for Albert Heijn fresh product reviews.

## Overview

This workshop guides students through a realistic ML project lifecycle: from business analysis and ETL pipelines, through model training and validation, to API deployment and monitoring. Students experience the full data engineering and MLOps workflow used in production systems.

**Duration**: 1 hour
**Level**: Data Advanced 1 students
**Tools**: Python, Jupyter Notebooks, scikit-learn, FastAPI

## Workshop Scenario

🥬 **The Challenge**: Supermarket wants to reduce food waste and optimize discounts for fresh products using customer sentiment analysis.

**Business Goal**: Build an ML system that:
- Analyzes customer reviews of fresh products (lettuce, tomatoes, spinach, etc.)
- Predicts sentiment (positive/neutral/negative)
- Recommends **smart discounts** at the product level
- Deploys as a REST API for real-time predictions

**Key Innovation**: Smart discounts combine THREE data sources:
1. **Customer sentiment** (from ML model predictions)
2. **Inventory pressure** (stock levels vs. sales velocity)
3. **Model confidence** (high confidence = more aggressive discount)

**Example**: Lettuce with 80% negative reviews + 95 units in stock + only 2 sales/day = **90% discount** to clear inventory before spoilage!

## Learning Objectives

By the end of this workshop, students will understand and apply:

### 🎯 **MLE Lifecycle Components**

1. **Business Analysis** - Validate project feasibility BEFORE coding
   - Explore raw data to assess quality and volume
   - Identify key insights and feasibility blockers
   - Make data-driven go/no-go decisions

2. **ETL & Data Engineering** - Build production-ready data pipelines
   - Implement **medallion architecture** (Bronze → Silver → Gold)
   - Clean datasets separately (reviews, inventory, sales)
   - Merge and enrich data for ML consumption
   - Handle missing values, duplicates, and data quality issues

3. **ML Model Training** - Train and validate production models
   - Build sentiment classifier (TF-IDF + Logistic Regression)
   - Achieve 87%+ accuracy on test set
   - Aggregate predictions at product level
   - Create smart discount system using ML + business data

4. **MLOps & Model Registry** - Professional model management
   - Version models with metadata (accuracy, timestamp, params)
   - Validate models before deployment (quality gates)
   - Save artifacts (model + vectorizer) for serving

5. **API Deployment** - Build and deploy ML services
   - Create REST API with FastAPI
   - Implement prediction endpoint with error handling
   - Test locally with interactive examples


### 🔑 **Key Skills Developed**

✅ End-to-end ML project workflow (business → deployment)
✅ Production ETL patterns (medallion architecture)
✅ Combining ML predictions with business logic
✅ Model versioning and validation (MLOps basics)
✅ REST API development for ML serving

## Setup Instructions

### Prerequisites

- **Python 3.10+** (3.14.2 recommended)
- **VS Code** with Jupyter extension (recommended) OR Jupyter Notebook/Lab
- **mise** (for Python environment management) - [Install mise](https://mise.jdx.dev/)

### Quick Installation

```bash
# 1. Clone or download this repository
cd hsl-presentation-data-advanced

# 2. Install Python + dependencies with mise
mise install

# This automatically:
#   ✅ Installs Python 3.14.2
#   ✅ Creates virtual environment at .venv
#   ✅ Installs all packages from requirements.txt
```

### VS Code Setup (Recommended)

**Already configured!** Just:

1. Open project folder in VS Code
2. Open any notebook: `notebooks/01_business_analysis.ipynb`
3. Click kernel selector (top-right corner)
4. Choose: **"Python 3 (HSL Workshop)"** or **".venv (Python 3.14.2)"**
5. Run cells! 🚀

📖 Detailed VS Code guide: [VSCODE_SETUP.md](VSCODE_SETUP.md)

### Jupyter in Browser

```bash
# Activate environment
source .venv/bin/activate
# or use helper script
source activate.sh

# Launch Jupyter
jupyter notebook
# or
jupyter lab
```

### Generate Fresh Data (Optional)

The dataset is pre-generated, but you can create a new one:

```bash
source .venv/bin/activate
python generate_realistic_data.py
```

This creates `data/raw/product_reviews.csv` with ~800 reviews.

## Project Structure

```
hsl-presentation-data-advanced/
├── README.md                          # This file
├── QUICKSTART.md                      # Quick reference guide
├── VSCODE_SETUP.md                    # VS Code setup guide
├── requirements.txt                   # Python dependencies
├── mise.toml                          # mise configuration
├── activate.sh                        # Environment activation script
│
├── notebooks/                         # Interactive workshop notebooks
│   ├── 01_business_analysis.ipynb     # Data exploration & feasibility
│   ├── 02_etl_data_preparation.ipynb  # ETL pipeline (Bronze→Silver→Gold)
│   ├── 03_ml_model_training.ipynb     # ML training + MLOps + smart discounts
│   ├── 04_deployment_practice.ipynb   # FastAPI + monitoring dashboard
│
├── data/                              # Data storage (medallion architecture)
│   ├── raw/                           # 🥉 Bronze: Raw, unprocessed data
│   │   └── product_reviews.csv        # Generated synthetic reviews
│   ├── bronze/                        # 🥉 Bronze layer (raw snapshots)
│   ├── silver/                        # 🥈 Silver: Cleaned datasets
│   │   ├── reviews_clean.csv
│   │   ├── inventory_clean.csv
│   │   └── sales_clean.csv
│   └── gold/                          # 🥇 Gold: ML-ready enriched data
│       └── final_dataset.csv
│
├── models/                            # ML model artifacts (versioned)
│   ├── sentiment_model_v1.pkl         # Trained classifier
│   ├── tfidf_vectorizer_v1.pkl        # Text vectorizer
│   └── model_registry.json            # Model metadata & versions
│
├── monitoring/                        # Monitoring artifacts
│   └── dashboard_*.png                # Saved dashboard snapshots
│
└── generate_realistic_data.py         # Data generation script
```

## Dataset

The dataset is **synthetically generated** to ensure relevance and appropriate size for a 1-hour workshop.

### Features

| Column | Description | Example |
|--------|-------------|---------|
| `product_id` | Unique product identifier | `P001` |
| `product_name` | Fresh product name | `Lettuce`, `Tomatoes` |
| `review_text` | Customer review | "Fresh and crispy!" |
| `rating` | Star rating (1-5) | `4` |
| `date` | Review date | `2025-01-15` |
| `avg_stock_level` | Average inventory units | `45` |
| `avg_daily_sales` | Average daily sales velocity | `12.5` |

## Troubleshooting

### Environment Issues

**"Module not found" error**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**"Kernel not found" in Jupyter**
```bash
source .venv/bin/activate
python -m ipykernel install --user --name=hsl-workshop --display-name="Python 3 (HSL Workshop)"
```

**mise not working**
```bash
# Install mise first
curl https://mise.run | sh
# Then
mise install
```

### Data Issues

**"File not found" for dataset**
```bash
# Generate new dataset
source .venv/bin/activate
python generate_realistic_data.py
```

**"data/silver/ directory not found"**
- This is normal! Silver/Gold directories are created automatically when running Notebook 2
- Run notebooks in order: 01 → 02 → 03 → 04

### Model Issues

**"Model file not found"**
- Run Notebook 3 first to train and save the model
- Check `models/` directory for `sentiment_model_v1.pkl`

**"Vectorizer not found"**
- Models and vectorizers are saved together in Notebook 3
- Both files must exist for API to work

### API Issues

**"Port 8000 already in use"**
```python
# In notebook, change port:
uvicorn.run(app, host="0.0.0.0", port=8001)
```

**"Address already in use"**
- Stop existing FastAPI server
- Restart Jupyter kernel
- Run API cell again

### VS Code Issues

**Wrong Python interpreter**
1. Press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows)
2. Type: "Python: Select Interpreter"
3. Choose: `.venv/bin/python`

**Kernel keeps crashing**
- Restart VS Code
- Clear all outputs: Cell → All Output → Clear
- Restart kernel: Kernel → Restart

## Extensions and Next Steps

After completing the workshop, students can explore:

### 🚀 Extend the Workshop

1. **Improve the ML Model**
   - Try different algorithms (Random Forest, SVM, Naive Bayes)
   - Use pre-trained transformers (DistilBERT, RoBERTa)
   - Add aspect-based sentiment (price, freshness, taste)
   - Implement multilingual support (Dutch + English)

2. **Enhance the Discount System**
   - Add seasonality factors (summer vs winter products)
   - Include product price tiers
   - Factor in competitor pricing
   - Add promotion effectiveness tracking

3. **Build Production Features**
   - Add authentication to API (API keys, OAuth)
   - Implement rate limiting
   - Add request logging
   - Create admin dashboard for model retraining

4. **Deploy to Cloud**
   - Deploy API to Azure App Service
   - Use Azure ML for model training
   - Set up Azure Monitor for observability
   - Implement CI/CD with GitHub Actions

5. **Advanced MLOps**
   - Set up A/B testing for model versions
   - Implement automated retraining pipeline
   - Add data drift detection
   - Create model explainability dashboard



## Authors

- Agata Sowa (Strategy & Analytics @ Albert Heijn)
- Niels Mooren (Platform Engineer @ Albert Heijn)

