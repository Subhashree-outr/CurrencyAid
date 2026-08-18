import tensorflow as tf
from tensorflow.keras import layers, models

# Create a simple model that matches the expected input shape (224, 224, 3)
model = models.Sequential([
    layers.Input(shape=(224, 224, 3)),
    layers.Flatten(),
    layers.Dense(8, activation='softmax') # 8 classes based on labels.txt
])

model.save("keras_model.h5")
print("Placeholder model saved as keras_model.h5")
