import pandas as pd
import tensorflow as tf

X = pd.read_csv("data/processed/X.csv")
y = pd.read_csv("data/processed/y.csv")

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=5)

model.save("models/saved/dl_ids.h5")
