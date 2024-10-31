import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.naive_bayes import GaussianNB
from lightgbm import LGBMRegressor
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import clone

class LestariClassifier(BaseEstimator, ClassifierMixin):
    """
    Lestari Ensemble Classifier.

    This classifier supports an arbitrary number of base models. It combines their predictions
    using a weighted ensemble approach, where the weights are learned based on the prediction
    errors of each base model.

    Parameters:
    - estimators: List of (name, model) tuples for base models.
                  Example:
                  estimators=[
                      ('cb', CatBoostClassifier(iterations=100, verbose=0, random_state=42)),
                      ('lgbm', LGBMClassifier(n_estimators=100, random_state=42)),
                  ]
    - final_model: Final model to combine predictions. Default is GaussianNB.
    - weight_model: Model to predict weights for each base model. Default is LGBMRegressor.
    """
    def __init__(self,
                 estimators,
                 final_model=None,
                 weight_model=None):
        self.estimators = estimators
        self.final_model = final_model if final_model is not None else GaussianNB()
        self.weight_model = weight_model if weight_model is not None else LGBMRegressor(n_estimators=100, random_state=42)
        self.weight_models = [clone(self.weight_model) for _ in self.estimators]
        self.cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        self.scaler = MinMaxScaler()

    def fit(self, X, y):
        """
        Fit the Lestari ensemble classifier.

        Parameters:
        - X: Training features.
        - y: Training labels.
        """
        # Ensure y is a NumPy array and 1D
        y = np.asarray(y).ravel()

        # Identify unique classes
        self.classes_ = np.unique(y)

        # Collect cross-validated predictions from each base estimator
        base_preds_cv = []
        for name, model in self.estimators:
            # Obtain probability estimates for the positive class
            pred = cross_val_predict(model, X, y, cv=self.cv, method='predict_proba')[:, 1]
            base_preds_cv.append(pred)

        # Combine predictions into a 2D array: shape (n_samples, n_estimators)
        base_preds_cv = np.column_stack(base_preds_cv)

        # Compute prediction errors for each base estimator
        error_train = np.abs(y[:, np.newaxis] - base_preds_cv)

        # Sum of errors across all estimators for each sample
        total_error_train = np.sum(error_train, axis=1)
        total_error_train[total_error_train == 0] = 1e-10  # Avoid division by zero

        # Calculate weights for each base estimator based on their errors
        # Weight for estimator i: (total_error - error_i) / total_error
        weights_train = (total_error_train[:, np.newaxis] - error_train) / total_error_train[:, np.newaxis]

        # Normalize weights so that they sum to 1 for each sample
        weights_sum = np.sum(weights_train, axis=1, keepdims=True)
        weights_sum[weights_sum == 0] = 1e-10  # Prevent division by zero
        weights_train = weights_train / weights_sum

        # Train each weight model to predict the weights for its corresponding base estimator
        for i, (name, model) in enumerate(self.estimators):
            self.weight_models[i].fit(X, weights_train[:, i])

        # Fit each base estimator on the entire training data
        for name, model in self.estimators:
            model.fit(X, y)

        # Create meta-features for the final model
        weighted_preds_train = []
        for i in range(len(self.estimators)):
            pred = base_preds_cv[:, i]
            weight = weights_train[:, i]
            weighted_preds_train.extend([pred, 0.5 + (pred - 0.5) * (2 * weight)])

        # Combine all meta-features: shape (n_samples, 2 * n_estimators)
        X_logit_train_weighted = np.column_stack(weighted_preds_train)

        # Fit the final model on the meta-features
        self.final_model.fit(X_logit_train_weighted, y)

        return self

    def predict_proba(self, X):
        """
        Predict class probabilities.

        Parameters:
        - X: Input features.

        Returns:
        - Probability estimates for both classes.
        """
        # Obtain predictions from each base estimator
        base_preds = []
        for name, model in self.estimators:
            pred = model.predict_proba(X)[:, 1]
            base_preds.append(pred)

        # Combine predictions into a 2D array: shape (n_samples, n_estimators)
        base_preds = np.column_stack(base_preds)

        # Predict weights for each base estimator using their respective weight models
        weights = []
        for i in range(len(self.estimators)):
            weight = self.weight_models[i].predict(X)
            weights.append(weight)

        # Convert list of weights to a 2D array: shape (n_samples, n_estimators)
        weights = np.column_stack(weights)

        # Normalize weights so that they sum to 1 for each sample
        weights_sum = np.sum(weights, axis=1, keepdims=True)
        weights_sum[weights_sum == 0] = 1e-10  # Prevent division by zero
        weights = weights / weights_sum

        # Create meta-features for the final model
        weighted_preds = []
        for i in range(len(self.estimators)):
            pred = base_preds[:, i]
            weight = weights[:, i]
            weighted_preds.extend([pred, 0.5 + (pred - 0.5) * (2 * weight)])

        # Combine all meta-features: shape (n_samples, 2 * n_estimators)
        X_logit = np.column_stack(weighted_preds)

        # Predict probabilities using the final model
        return self.final_model.predict_proba(X_logit)

    def predict(self, X):
        """
        Predict class labels.

        Parameters:
        - X: Input features.

        Returns:
        - Predicted class labels.
        """
        y_prob = self.predict_proba(X)
        return np.argmax(y_prob, axis=1)
