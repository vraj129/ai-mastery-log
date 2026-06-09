import numpy as np

if __name__ == "__main__":
    predictions = np.array([10,8,12,13])
    targets = np.array([5,6,7,8])

    errors = predictions - targets
    squared = errors ** 2
    mse = squared.mean()
    print(mse)