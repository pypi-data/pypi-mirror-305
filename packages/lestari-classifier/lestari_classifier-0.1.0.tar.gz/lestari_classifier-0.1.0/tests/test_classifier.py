import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

from lestari_classifier import LestariClassifier

def test_lestari_classifier():
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=20, 
                             n_informative=15, n_redundant=5,
                             random_state=42)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Define base models
    estimators = [
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('lgbm', LGBMClassifier(n_estimators=100, random_state=42)),
        ('cb', CatBoostClassifier(iterations=100, verbose=0, random_state=42))
    ]
    
    # Test classifier
    clf = LestariClassifier(estimators=estimators)
    clf.fit(X_train, y_train)
    
    # Make predictions
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)
    
    # Basic checks
    accuracy = accuracy_score(y_test, y_pred)
    assert accuracy > 0.7, f"Model accuracy {accuracy} is below threshold"
    assert y_prob.shape == (X_test.shape[0],)
    assert np.all((y_prob >= 0) & (y_prob <= 1))

if __name__ == '__main__':
    test_lestari_classifier()
