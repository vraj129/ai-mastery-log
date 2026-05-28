import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def dot(self, other):
        return float(self.x * other.x + self.y * other.y)

    def magnitude(self):
        return float(math.sqrt(self.x ** 2 + self.y ** 2))

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x},y={self.y})"

    def __len__(self):
        return 2


# vector1 = Vector(2, 3)
# vector2 = Vector(3, 3)
# print(vector1.add(vector2))
# print(vector1.dot(vector2))
# print(vector1.magnitude())
# print(vector1)
# print(len(vector1))

class Dataset:

    def __init__(self, samples, labels):
        self.samples = samples
        self.labels = labels

    def add(self, samples, labels):
        self.samples.append(samples)
        self.labels.append(labels)

    def split(self, ratio=0.8):
        cut = int(len(self.samples) * ratio)
        train = Dataset(self.samples[:cut], self.labels[cut:])
        test = Dataset(self.samples[cut:], self.labels[cut:])

        return train, test

    def __repr__(self):
        return f"{type(self).__name__}(samples={len(self.samples)},label={len(self.labels)})"

    def __len__(self):
        return len(self.samples)


data = Dataset(["image1", "image2", "image3"], ["cat", "dog", "cat"])

train, test = data.split(0.8)


# print(train)
# print(test)

class Layer:
    def __init__(self, name):
        self.name = name

    def forward(self, x):
        pass

    def __call__(self, x):
        return self.forward(x)

    def __repr__(self):
        return f"Layer(name={self.name})"


class LinearLayer(Layer):
    def __init__(self, name):
        super().__init__("linear")

    def forward(self, x):
        return x * 2


class ReluLayer(Layer):
    def __init__(self):
        super().__init__("relu")

    def forward(self, x):
        return max(0, x)

# TEST IT
linear = LinearLayer()
relu = ReluLayer()

print(linear(10))
print(relu(-5))
print(relu(3))
print(linear)