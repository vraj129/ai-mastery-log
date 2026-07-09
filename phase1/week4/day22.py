import numpy as np


def grad(w):
    # Ripple mulitple by x
    pred = w * x

    # ripple multiplies by 1
    errors = pred - target

    # Formula average of 2 * x * errors
    return (2 * x * errors).mean()


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    # w should be 2 to achieve the target
    target = np.array([2, 4, 6, 8])

    w = 0
    learning_rate = 0.01

    assert abs(grad(w) - (-30)) < 0.01
    for _ in range(50):
        w = w - learning_rate * grad(w)
        print("-------------")
        print(f'Gradient: {grad(w)}')
        print(w)

    assert abs(w - 2) < 0.01
