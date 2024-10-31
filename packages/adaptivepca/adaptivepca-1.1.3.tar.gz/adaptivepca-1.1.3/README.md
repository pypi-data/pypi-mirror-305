# ASPIRE (Adaptive Scaler and PCA with Intelligent REduction)
*Previously known as AdaptivePCA*

ASPIRE is an advanced implementation of Principal Component Analysis (PCA) that provides intelligent feature scaling, comprehensive preprocessing, and built-in validation capabilities. It automatically adapts to your data's characteristics to deliver optimal dimensionality reduction results.

## Core Functionality

AdaptivePCA employs a comprehensive preprocessing and analysis approach:

1. **Intelligent Preprocessing**
   - Comprehensive data cleaning and preprocessing
   - Handles outliers using IQR method
   - Manages infinity values and missing data
   - Feature-wise normality testing using Shapiro-Wilk test
   - Automatic selection between StandardScaler and MinMaxScaler
   - Class imbalance detection and handling via SMOTE

2. **Dynamic Dimensionality Reduction**
   - Determines optimal number of PCA components based on variance threshold
   - Considers eigenvalue thresholds for component selection
   - Adapts to dataset characteristics
   - Built-in validation framework


The algorithm's key innovation lies in its adaptive nature, particularly in:

- Automatic selection between StandardScaler and MinMaxScaler based on feature distributions
- Dynamic component selection based on cumulative variance threshold
- Integrated preprocessing pipeline with outlier handling and missing value imputation
- Automatic class imbalance detection and correction
- Comprehensive validation framework with efficiency metrics

This implementation provides an end-to-end solution for dimensionality reduction while handling common data challenges automatically.

## Overall Design Pattern
```bash
Data → Preprocessing → Scaler Selection → PCA Optimization → Validation → Prediction
```

## Dependencies
- numpy>=1.19.0
- pandas>=1.2.0
- scikit-learn>=0.24.0
- lightgbm>=3.0.0
- imbalanced-learn>=0.8.0
- scipy>=1.6.0

## Installation

Install dependencies:
```bash
pip install scikit-learn numpy pandas lightgbm scipy imbalanced-learn
```

Instal from Pypi repository:
```bash
pip install adaptivepca
```

Clone this repository and install the package using `pip`:
```bash
git clone https://github.com/nqmn/adaptivepca.git
cd adaptivepca
pip install .
```

## Usage

### Basic Usage

```python
# Load your data
data = pd.read_csv("your_dataset.csv")
X = data.drop(['Label'])
y = data['Label']

# Initialize AdaptivePCA
adaptive_pca = AdaptivePCA()
X_preprocessed, y_preprocessed, smote_applied = adaptive_pca.preprocess_data(X, y)
adaptive_pca.fit(X_preprocessed, y_preprocessed, smote_applied)
adaptive_pca.validate_with_classifier(X_preprocessed, y_preprocessed)
adaptive_pca.predict_with_classifier(X_preprocessed, y_preprocessed)
adaptive_pca.export_model('your_model_name.joblib')
```

### Advanced Usage

```python
import pandas as pd
from adaptivepca import AdaptivePCA
from sklearn.tree import DecisionTreeClassifier

# Load your data
data = pd.read_csv("your_dataset.csv")
X = data.drop(columns=['Label'])  # Features
y = data['Label']  # Target variable

# Initialize AdaptivePCA
adaptive_pca = AdaptivePCA(
    variance_threshold=0.95,
    max_components=50,
    min_eigenvalue_threshold=1e-4,
    normality_ratio=0.05,
    verbose=1
)
# Run Preprocessing
X_preprocessed, y_preprocessed, smote_applied = adaptive_pca.preprocess_data(X, y)

# Fit AdaptivePCA
adaptive_pca.fit(X_preprocessed, y_preprocessed, smote_applied)


# Optional - Validate with a classifier with full and reduced dataset performance
adaptive_pca.validate_with_classifier(X, y, classifier=DecisionTreeClassifier(), test_size=0.2, cv=5)

# Optional - Run prediction with classifier, show output of confusion matrix, classification report,
#  inference time, fpr, far, specificity, auc-roc, mcc
adaptive_pca.predict_with_classifier(X, y)

# Optional - Export the model in joblib format
adaptive_pca.export_model("your_model_name.joblib")

```

# Key Components

## Initialization Parameters
- `variance_threshold`: Minimum cumulative explained variance (default: 0.95)
- `max_components`: Maximum PCA components to consider (default: 50)
- `min_eigenvalue_threshold`: Minimum eigenvalue cutoff (default: 1e-4)
- `normality_ratio`: P-value threshold for Shapiro-Wilk test (default: 0.05)
- `verbose`: Logging detail level (default: 0)

## Preprocessing Pipeline
### Data Cleaning
- Selection of numeric columns only
- Handles outliers using `IQR methods` (clips values outside 1.5\*IQR)
- Replaces infinitiy values with finite extremes
- Imputes missing values using `mean` strategy

### Feature Scaling Selection
- Perform `Shapiro-Wilk test` on each feature
- Counts features better suited for StandardScaler and MinMaxScaler
- Applies majority voting to select final scaler

### Class Balance Handling
- Perform chi-squared test for class imbalance
- Applies SMOTE if significant imbalance detected `(p<0.05)`

## PCA Optimization Algorithm
- Find optimal components meeting variance threshold: `max variance_threshold` and `min_eigenvalue_threshold`

## Validation Framework
- Classification validation on full and reduced dataset
- Performance metrics: Accuracy comparison, time efficiency, ROC-AUC score, detailed classification report

## Key Mathematical Components
### Feature normality testing
- Shapiro-Wilk test for normality

### Class imbalance detection
- Chi-squared test for class balance

## Methods
- `fit(X)`: Fits the AdaptivePCA model to the data `X`.
- `preprocess_data(X)`: Run preprocessing pipeline.
- `validate_with_classifier(X, y, classifier=None, cv=5, test_size=0.2)`: Tests model performance.
- `predict_with_classifier(X, y)`: Makes predictions using trained classifier.
- `export_model(model_name, classifier)`: Saves model to file.

## Use Cases
ASPIRE is particularly valuable for:
- Machine learning pipelines requiring automated preprocessing
- High-dimensional data analysis
- Feature engineering optimization
- Model performance enhancement
- Exploratory data analysis

## Technical Foundation
The system integrates:
- Statistical testing for data distribution analysis
- Adaptive scaling techniques
- Principal Component Analysis
- Machine learning validation frameworks
- Performance optimization methods

## Performance Comparison: AdaptivePCA vs. Traditional PCA Optimization (GridSearch)

### Speed

AdaptivePCA adaptively selects the optimal configuration based on data-driven rules, which is less computationally intense than the exhaustive search performed by grid search. In our tests, AdaptivePCA achieved up to a 90% reduction in processing time compared to the traditional PCA method. This is especially useful when working with high-dimensional data, where traditional methods may take significantly longer due to sequential grid search.

### Explained Variance

Both AdaptivePCA and traditional PCA achieve similar levels of explained variance, with AdaptivePCA dynamically selecting the number of components based on a defined variance threshold. Traditional PCA, on the other hand, requires manual parameter tuning, which can be time-consuming.

## Performance on Different Dataset (Full & Reduced Dataset)

Most datasets maintain high accuracy, with reduced datasets achieving similar scores to full datasets in nearly all cases. Additionally, the reduced datasets significantly decrease processing time, with time reductions ranging from 1.85% to 58.03%. This indicates that reduced datasets can offer substantial efficiency benefits, especially for larger datasets.

| Dataset | Score (Acc) | Time (s) | Gain (%) |
|---------|-------------|----------|----------|
|insdn_ddos_binary_01.ds (full)| 1.000000 | 1.5492 | - |
|insdn_ddos_binary_01.ds (reduced)| 1.000000 | 0.6502 | 58.03 |
|hldddosdn_hlddos_combine_binary.ds (full)| 1.000000 | 30.3948 | - |
|hldddosdn_hlddos_combine_binary.ds (reduced)| 1.000000 | 14.4875 | 52.34 |
|cicddos2019_tcpudp_combine_d1_binary_rus.ds (full) | 1.000000 | 1.6453 | - |
|cicddos2019_tcpudp_combine_d1_binary_rus.ds (reduced) | 1.000000 | 0.7371 | 55.20 |
|mendeley_ddos_sdn_binary_19.ds (full) | 1.000000 | 0.9839 | - |
|mendeley_ddos_sdn_binary_19.ds (reduced) | 0.942738 | 0.9355 | 4.93 |
|Wednesday-workingHours.pcap_ISCX.csv (full) | 0.921126 | 39.7610 | - |
|Wednesday-workingHours.pcap_ISCX.csv (reduced) | 0.970010 | 28.8390 | 27.47 |
|LR-HR DDoS 2024 Dataset for SDN-Based Networks.csv (full) | 0.999982 | 0.7314 | - |
|LR-HR DDoS 2024 Dataset for SDN-Based Networks.csv (reduced) | 0.999982 | 0.5131 | 29.84 |
|dataset_sdn.csv (full) | 1.000000 | 1.0547 | - |
|dataset_sdn.csv (reduced) | 0.932359 | 1.0352 | 1.85 |

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to discuss your changes.

## Acknowledgments
This project makes use of the `scikit-learn`, `numpy`, and `pandas` libraries for data processing and machine learning.

## Version Update Log
- `1.0.3` - Added flexibility in scaling, fix error handling when max_components exceeding the available number of features or samples.
- `1.0.6` - Added Parameter verbose as an argument to __init__, with a default value of 0.
- `1.1.0` - Added validation, prediction with classifier, clean up the code.
- `1.1.3` - Revamped the code. Refer to description above.
