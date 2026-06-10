import numpy as np

def loss(w):
    pred = w * x
    errors = pred - target
    mse = (errors ** 2).mean()
    return mse

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    # w should be 2 to achieve the target
    target = np.array([2, 4, 6, 8])

    w = 0
    eps = 0.0001
    learning_rate = 0.01

    for _ in range(50):
        slope = (loss(w + eps) - loss(w)) / eps
        w = w - learning_rate * slope
        print("-------------")
        print(f'Slope: {slope}')
        print(w)

    assert abs(w - 2) < 0.01
