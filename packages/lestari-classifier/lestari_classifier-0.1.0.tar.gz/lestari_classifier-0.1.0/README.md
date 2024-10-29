# LestariClassifier

LESTARI (Layered Ensemble Stacking Technique with Adaptive Regression of Individual-errors) is an advanced ensemble classifier that intelligently combines multiple base models using a weighted ensemble approach. The weights are dynamically learned based on the prediction errors of individual instances across each base model.
LESTARI was developed as part of my Master of Computer Science thesis at BINUS University, and is lovingly dedicated to my beloved wife, whose surname Lestari inspired the name of this technique.

## Installation

```bash
pip install lestari-classifier
```

## Quick Start

```python
from lestari_classifier import LestariClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier

# Define base models
estimators = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('lgbm', LGBMClassifier(n_estimators=100, random_state=42)),
    ('cb', CatBoostClassifier(iterations=100, verbose=0, random_state=42))
]

# Initialize and use LestariClassifier
clf = LestariClassifier(estimators=estimators)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
probabilities = clf.predict_proba(X_test)
```

## Features

- Supports multiple base models
- Automatic weight learning
- Compatible with scikit-learn API
- Probability estimates support
- Internal cross-validation
