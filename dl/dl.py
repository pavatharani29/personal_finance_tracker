import numpy as np
import matplotlib.pyplot as plt
from keras import layers, models
from keras.datasets import mnist

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize and reshape
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train[..., None]
x_test = x_test[..., None]

# Build CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Prediction example
idx = np.random.randint(0, len(x_test))
img = x_test[idx]
label = y_test[idx]

plt.imshow(img.squeeze(), cmap='gray')
plt.title(f"True Label: {label}")
plt.show()

pred = model.predict(img.reshape(1,28,28,1))
print("Predicted digit:", np.argmax(pred))
