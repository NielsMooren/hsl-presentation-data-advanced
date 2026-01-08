# Data Advanced Workshop: ETL & ML Sentiment Analysis

## Overview

This workshop teaches students about the complete data lifecycle through a practical sentiment analysis project for Albert Heijn fresh product reviews. Students will learn ETL processes, data preparation, storage concepts, machine learning, and deployment theory.

**Duration**: 1 hour
**Level**: Data Advanced 1 students
**Tools**: Python, Jupyter Notebooks, scikit-learn

## Workshop Scenario

Albert Heijn wants to analyze customer reviews of fresh products (potatoes, carrots, spinach, etc.) to determine which products need discounts based on customer sentiment. The goal is to reduce food waste by identifying products with negative reviews and recommending appropriate discounts.

**Example**: A review saying "worst spinach ever" should trigger a 90% discount recommendation.

## Learning Objectives

By the end of this workshop, students will be able to:

1. Extract and explore data (ETL concepts)
2. Clean and prepare data for machine learning
3. Understand data storage options and lifecycle management
4. Train a sentiment analysis model using scikit-learn
5. Make predictions and create a discount recommendation system
6. Understand ML deployment strategies (theoretical)

## Workshop Structure

### Part 1: Data Extraction (ETL) - 10 minutes
- Load product review dataset
- Explore data structure and quality
- Identify missing values, duplicates, and inconsistencies

**Notebook**: [01_data_extraction.ipynb](notebooks/01_data_extraction.ipynb)

### Part 2: Data Preparation - 15 minutes
- Handle missing values and duplicates
- Clean and normalize text data
- Create sentiment labels from ratings
- Save cleaned data for analysis

**Notebook**: [02_data_preparation.ipynb](notebooks/02_data_preparation.ipynb)

### Part 3: Storage Theory - 10 minutes
- Data lifecycle stages (Bronze/Silver/Gold)
- Storage options (Local, Cloud, Databases, Data Lakes)
- Azure Blob Storage and lifecycle management
- Real-world example: AH Dynamic Markdown architecture

**Notebook**: [03_storage_theory.ipynb](notebooks/03_storage_theory.ipynb)

### Part 4: ML Analysis - 15 minutes
- Train sentiment classification model (TF-IDF + Logistic Regression)
- Evaluate model performance
- Make predictions on new reviews
- Create discount recommendation system
- Analyze product-level sentiment

**Notebook**: [04_ml_analysis.ipynb](notebooks/04_ml_analysis.ipynb)

### Part 5: Deployment Theory - 5 minutes
- Batch vs. real-time deployment
- Model serialization and versioning
- Monitoring and retraining strategies
- MLOps best practices
- Real-world deployment examples

**Notebook**: [05_deployment_theory.ipynb](notebooks/05_deployment_theory.ipynb)

### Part 6: Q&A - 5 minutes

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- VS Code with Jupyter extension (recommended) OR Jupyter Notebook/JupyterLab
- mise (for Python environment management)

### Installation

1. **Clone or download this repository**

2. **Set up Python environment with mise**
   ```bash
   cd hsl-data-presentation
   mise install
   ```

   This will automatically:
   - Install Python 3.14.2
   - Create a virtual environment at `.venv`
   - Install all dependencies from `requirements.txt`

3. **Register the Jupyter kernel** (already done if you see "hsl-workshop")
   ```bash
   source .venv/bin/activate
   python -m ipykernel install --user --name=hsl-workshop --display-name="Python 3 (HSL Workshop)"
   ```

### Using with VS Code (Recommended)

**Everything is already configured!** Just:

1. Open the project folder in VS Code
2. Open any notebook (e.g., `notebooks/01_data_extraction.ipynb`)
3. Click the kernel selector (top-right) and choose **"Python 3 (HSL Workshop)"**
4. Start running cells!

📖 See [VSCODE_SETUP.md](VSCODE_SETUP.md) for detailed VS Code setup and troubleshooting.

### Using with Jupyter in Browser

If you prefer the classic Jupyter interface:

```bash
source .venv/bin/activate
jupyter notebook
```

The kernel "Python 3 (HSL Workshop)" will be available in the kernel list.

### Quick Start

```bash
# Option 1: Use the activation script
source activate.sh

# Option 2: Activate manually
source .venv/bin/activate

# Then launch Jupyter
jupyter notebook
```

### Workflow

1. Start with `notebooks/01_data_extraction.ipynb`
2. Work through notebooks 01 → 05 sequentially
3. The dataset is already generated in `data/raw/product_reviews.csv`

## Project Structure

```
hsl-data-presentation/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── mise.toml                      # mise configuration
├── notebooks/
│   ├── 01_data_extraction.ipynb   # ETL and data exploration
│   ├── 02_data_preparation.ipynb  # Data cleaning and preprocessing
│   ├── 03_storage_theory.ipynb    # Storage concepts (theoretical)
│   ├── 04_ml_analysis.ipynb       # ML model training and analysis
│   └── 05_deployment_theory.ipynb # Deployment concepts (theoretical)
├── data/
│   ├── raw/
│   │   └── product_reviews.csv    # Original dataset (generated)
│   └── cleaned/
│       └── cleaned_reviews.csv    # Cleaned dataset (created in notebook 02)
├── scripts/
│   └── generate_dataset.py        # Generate synthetic review data
├── models/
│   ├── sentiment_model.pkl        # Trained ML model (created in notebook 04)
│   └── tfidf_vectorizer.pkl       # TF-IDF vectorizer (created in notebook 04)
└── utils/
    └── discount_predictor.py      # Reusable prediction functions
```

## Dataset

The dataset is **synthetically generated** to ensure relevance to Albert Heijn and appropriate size for the workshop.

**Features**:
- **product_id**: Unique identifier for each product
- **product_name**: Name of fresh product (Potatoes, Carrots, Spinach, Tomatoes, Lettuce, Broccoli)
- **review_text**: Customer review text
- **rating**: Star rating (1-5)
- **date**: Review date
- **sales_volume**: Units sold in last 30 days
- **stock_level**: Current inventory level

**Statistics**:
- ~800 reviews total
- 6 fresh products
- Sentiment distribution: 60% positive, 25% neutral, 15% negative
- Includes data quality issues (5% missing values, 3% duplicates)

## Key Concepts Covered

### ETL (Extract, Transform, Load)
- Data extraction from files
- Data quality assessment
- Identifying issues early in the pipeline

### Data Preparation
- Handling missing values (drop vs. impute)
- Removing duplicates
- Text preprocessing and normalization
- Feature engineering

### Data Storage
- Data lifecycle stages
- Cloud storage (Azure Blob Storage)
- Retention policies and cleanup
- Real-world architecture examples

### Machine Learning
- Text vectorization (TF-IDF)
- Classification with Logistic Regression
- Model evaluation (accuracy, confusion matrix)
- Model interpretability

### Deployment
- Batch vs. real-time predictions
- Model serialization
- Monitoring and retraining
- MLOps best practices

## Connection to Data Advanced 1

This workshop aligns with Data Advanced 1 curriculum:

- **ETL Pipelines**: Similar to YouTube data warehouse project
- **Data Preparation**: Essential for any data project
- **Storage Concepts**: Cloud storage and data lifecycle
- **ML Basics**: Extension of clustering/classification concepts
- **Real-World Application**: AH Dynamic Markdown as case study

## Real-World Connection: AH Dynamic Markdown

Throughout the workshop, we relate concepts to Albert Heijn's actual Dynamic Markdown system:

- **Data Storage**: Azure Blob Storage for raw sales and inventory data
- **Processing**: Databricks for ETL and ML model training
- **Serving**: Azure SQL Database for real-time access
- **Analytics**: PowerBI dashboards for store managers
- **Impact**: Reduced food waste, optimized discounts, data-driven decisions

## Example Outputs

### Discount Predictions

| Product | Review | Sentiment | Confidence | Discount |
|---------|--------|-----------|------------|----------|
| Spinach | "worst spinach ever" | Negative | 94% | 90% |
| Potatoes | "best potatoes in my life" | Positive | 89% | 5% |
| Carrots | "carrot was a bit stale" | Negative | 72% | 70% |

### Product Recommendations

| Product | Negative % | Avg Rating | Recommendation |
|---------|-----------|------------|----------------|
| Broccoli | 18.2% | 3.4 | Moderate discount (30-50%) |
| Spinach | 16.5% | 3.5 | Moderate discount (30-50%) |
| Potatoes | 14.1% | 3.7 | Good sentiment (0-20%) |

## Troubleshooting

### "Module not found" error
- Make sure you installed dependencies: `mise exec -- pip install -r requirements.txt`
- Ensure you're using mise: `mise exec -- jupyter notebook`

### "File not found" error for dataset
- Run the dataset generation script: `cd scripts && mise exec -- python generate_dataset.py`

### "Model not found" error
- Run notebooks in order (01 → 05)
- The model is created in notebook 04

### Jupyter kernel issues
- Restart the kernel: Kernel → Restart
- Clear output: Cell → All Output → Clear

## Extensions and Next Steps

After completing the workshop, students can:

1. **Experiment with different ML models**
   - Try Random Forest, SVM, or Naive Bayes
   - Compare performance with Logistic Regression

2. **Add more features**
   - Product price
   - Seasonality (time of year)
   - Store location

3. **Build a simple API**
   - Create a Flask or FastAPI service
   - Deploy locally and test with Postman

4. **Explore cloud deployment**
   - Try Azure ML or Databricks Community Edition
   - Deploy model to Azure App Service

5. **Improve the model**
   - Use pre-trained transformers (DistilBERT)
   - Handle multilingual reviews
   - Add aspect-based sentiment analysis

## Resources

### Course Materials
- Skills learned in the Data Advanced 1 course
- YouTube data warehouse project

### Bonus Learning
Microsoft has good free [learning paths](https://learn.microsoft.com/en-us/training/browse/?roles=data-scientist) that everyone can use.

### External Resources
- [scikit-learn documentation](https://scikit-learn.org/stable/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Azure ML documentation](https://docs.microsoft.com/en-us/azure/machine-learning/)
- [TF-IDF explained](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

## Authors

- Agata Sowa (Strategy & Analytics @ Albert Heijn)
- Niels Mooren (Platform Engineer @ Albert Heijn)

## License

This workshop is for educational purposes only.

## Feedback

For questions or feedback about this workshop, please contact your instructor.

---

**Good luck with the workshop! Remember: The goal is to learn the complete data lifecycle, from raw data to deployment.**
