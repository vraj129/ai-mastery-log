import numpy as np


def grad(w):
    # Ripple mulitple by x
    pred = w * x + b

    # ripple multiplies by 1
    errors = pred - target

    # Formula average of 2 * x * errors
    return (2 * errors * x).mean()

def intercept_grad(b):
    pred = w * x + b

    errors = pred - target
    return (2 * errors).mean()


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    # w should be 2 to achieve the target
    target = 2 * x + 5

    w = 0
    b = 0
    learning_rate = 0.01

    assert abs(grad(w) - (-55)) < 0.01
    for _ in range(5000):
        w = w - learning_rate * grad(w)
        b = b - learning_rate * intercept_grad(b)
        print("-------------")
        print(f'Gradient: {grad(w)}')
        print(f'Intercept Gradient: {intercept_grad(b)}')
        print(f"w--> ${w}")
        print(f"b--> ${b}")

    assert abs(w - 2) < 0.01
    assert abs(b - 5) < 0.01
