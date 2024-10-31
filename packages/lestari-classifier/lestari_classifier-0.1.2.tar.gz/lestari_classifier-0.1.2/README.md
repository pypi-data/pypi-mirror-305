# LestariClassifier

LESTARI (Layered Ensemble Stacking Technique with Adaptive Regression of Individual-errors) is an advanced ensemble classifier that intelligently combines multiple base models using a weighted ensemble approach. The weights are dynamically learned based on the prediction errors of individual instances across each base model.

LESTARI was developed as part of my Master of Computer Science thesis at BINUS University, and is lovingly dedicated to my beloved wife, whose surname Lestari inspired the name of this technique.

## Features
- Supports multiple base models
- Automatic weight learning based on feature space
- Default weight model: LGBMRegressor for robust weight prediction
- Default final model: GaussianNB for efficient probability calibration
- Internal cross-validation

## Changelog

### 0.1.2
- Changed default weight model to LGBMRegressor
- Changed default final model to GaussianNB
- Enhanced weight learning using feature space
- Improved probability calibration 

### 0.1.1
- Enhanced predict_proba to return full probability matrix

### 0.1.0
- Initial release
