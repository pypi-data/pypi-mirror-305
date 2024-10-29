import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import clone

class LestariClassifier(BaseEstimator, ClassifierMixin):
    """
    Lestari Ensemble Classifier.

    This classifier combines multiple base models using a weighted ensemble approach,
    where the weights are learned based on the prediction errors of each base model.

    Parameters:
    -----------
    estimators : list of (string, estimator) tuples
        List of base models to be used in the ensemble.
        Example:
        [
            ('rf', RandomForestClassifier()),
            ('lgbm', LGBMClassifier()),
            ('cb', CatBoostClassifier())
        ]
    
    final_model : estimator, optional (default=LogisticRegression)
        Model used to combine the predictions of base models.
        
    weight_model : estimator, optional (default=LinearRegression)
        Model used to predict weights for each base model.
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
        """
        Fit the ensemble classifier.

        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            Training data
            
        y : array-like of shape (n_samples,)
            Target values

        Returns:
        --------
        self : object
            Returns self.
        """
        # Ensure y is a NumPy array and 1D
        y = np.asarray(y).ravel()

        # Identify unique classes
        self.classes_ = np.unique(y)

        # Get cross-validated predictions from base models
        base_preds_cv = []
        for name, model in self.estimators:
            pred = cross_val_predict(model, X, y, cv=self.cv, method='predict_proba')[:, 1]
            base_preds_cv.append(pred)
        base_preds_cv = np.column_stack(base_preds_cv)

        # Calculate prediction errors
        error_train = np.abs(y[:, np.newaxis] - base_preds_cv)
        total_error_train = np.sum(error_train, axis=1)
        total_error_train[total_error_train == 0] = 1e-10

        # Calculate and normalize weights
        weights_train = (total_error_train[:, np.newaxis] - error_train) / total_error_train[:, np.newaxis]
        weights_sum = np.sum(weights_train, axis=1, keepdims=True)
        weights_sum[weights_sum == 0] = 1e-10
        weights_train = weights_train / weights_sum

        # Train weight models
        for i, (name, model) in enumerate(self.estimators):
            self.weight_models[i].fit(base_preds_cv[:, [i]], weights_train[:, i])

        # Fit base models
        for name, model in self.estimators:
            model.fit(X, y)

        # Prepare meta-features
        weighted_preds_train = []
        for i in range(len(self.estimators)):
            pred = base_preds_cv[:, i]
            weight = weights_train[:, i]
            weighted_preds_train.extend([pred, weight * pred])

        # Train final model
        X_meta = np.column_stack(weighted_preds_train)
        self.final_model.fit(X_meta, y)

        return self

    def predict_proba(self, X):
        """
        Predict class probabilities.

        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            The input samples.

        Returns:
        --------
        array of shape (n_samples,)
            The probability estimates.
        """
        # Get base predictions
        base_preds = []
        for name, model in self.estimators:
            pred = model.predict_proba(X)[:, 1]
            base_preds.append(pred)
        base_preds = np.column_stack(base_preds)

        # Predict weights
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
        return self.final_model.predict_proba(X_meta)[:, 1]

    def predict(self, X):
        """
        Predict class labels.

        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            The input samples.

        Returns:
        --------
        array of shape (n_samples,)
            The predicted class labels.
        """
        return (self.predict_proba(X) >= 0.5).astype(int)
