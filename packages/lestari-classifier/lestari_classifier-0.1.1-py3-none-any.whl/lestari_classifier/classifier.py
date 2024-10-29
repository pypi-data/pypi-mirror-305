import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import clone

class LestariClassifier(BaseEstimator, ClassifierMixin):
    """
    Lestari Ensemble Classifier.
    """
    def __init__(self,
                 estimators,
                 final_model=None,
                 weight_model=None):
        self.estimators = estimators
        self.final_model = final_model if final_model is not None else LogisticRegression(max_iter=1000, random_state=42)
        self.weight_model = weight_model if weight_model is not None else LinearRegression()
        self.weight_models = [clone(self.weight_model) for _ in self.estimators]
        self.cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        self.scaler = MinMaxScaler()

    def fit(self, X, y):
        y = np.asarray(y).ravel()
        self.classes_ = np.unique(y)
        
        # Get cross-validated predictions
        base_preds_cv = []
        for name, model in self.estimators:
            pred = cross_val_predict(model, X, y, cv=self.cv, method='predict_proba')[:, 1]
            base_preds_cv.append(pred)
        base_preds_cv = np.column_stack(base_preds_cv)
        
        # Calculate errors and weights
        error_train = np.abs(y[:, np.newaxis] - base_preds_cv)
        total_error_train = np.sum(error_train, axis=1)
        total_error_train[total_error_train == 0] = 1e-10
        
        weights_train = (total_error_train[:, np.newaxis] - error_train) / total_error_train[:, np.newaxis]
        weights_sum = np.sum(weights_train, axis=1, keepdims=True)
        weights_sum[weights_sum == 0] = 1e-10
        weights_train = weights_train / weights_sum
        
        # Train weight models
        for i, (name, model) in enumerate(self.estimators):
            self.weight_models[i].fit(base_preds_cv[:, [i]], weights_train[:, i])
            model.fit(X, y)
        
        # Prepare meta-features and train final model
        weighted_preds_train = []
        for i in range(len(self.estimators)):
            pred = base_preds_cv[:, i]
            weight = weights_train[:, i]
            weighted_preds_train.extend([pred, weight * pred])
        
        X_meta = np.column_stack(weighted_preds_train)
        self.final_model.fit(X_meta, y)
        
        return self

    def predict_proba(self, X):
        # Get predictions
        base_preds = []
        for name, model in self.estimators:
            pred = model.predict_proba(X)[:, 1]
            base_preds.append(pred)
        base_preds = np.column_stack(base_preds)
        
        # Calculate weights
        weights = []
        for i in range(len(self.estimators)):
            weight = self.weight_models[i].predict(base_preds[:, [i]])
            weights.append(weight)
        weights = np.column_stack(weights)
        
        # Normalize weights
        weights_sum = np.sum(weights, axis=1, keepdims=True)
        weights_sum[weights_sum == 0] = 1e-10
        weights = weights / weights_sum
        
        # Create meta-features
        weighted_preds = []
        for i in range(len(self.estimators)):
            pred = base_preds[:, i]
            weight = weights[:, i]
            weighted_preds.extend([pred, weight * pred])
        
        # Final prediction
        X_meta = np.column_stack(weighted_preds)
        return self.final_model.predict_proba(X_meta)

    def predict(self, X):
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)
