try:
    import imblearn
    print("imbalanced-learn is installed.")
    print("imbalanced-learn version:", imblearn.__version__)
except ImportError:
    print("imbalanced-learn is not installed.")