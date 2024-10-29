# LestariClassifier

LESTARI (Layered Ensemble Stacking Technique with Adaptive Regression of Individual-errors) is an advanced ensemble classifier that intelligently combines multiple base models using a weighted ensemble approach. The weights are dynamically learned based on the prediction errors of individual instances across each base model.
LESTARI was developed as part of my Master of Computer Science thesis at BINUS University, and is lovingly dedicated to my beloved wife, whose surname Lestari inspired the name of this technique.

## Features

- Multiple base models support
- Automatic weight learning
- Scikit-learn compatible
- Probability estimates
- Internal cross-validation

## Install

```bash
pip install lestari-classifier
```

## Usage

```python
from lestari_classifier import LestariClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

estimators = [
    ('lgbm', LGBMClassifier()),
    ('cb', CatBoostClassifier(verbose=0))
]

clf = LestariClassifier(estimators=estimators)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
probabilities = clf.predict_proba(X_test)
```

## Changelog

### 0.1.1
- Enhanced predict_proba to return full probability matrix
- Improved probability estimation

### 0.1.0
- Initial release
