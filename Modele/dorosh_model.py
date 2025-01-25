# -*- coding: utf-8 -*-
"""Dorosh_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q-9lSzjjuGf3sU6TmmWI3p-UWT-y6LKF
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

"""Pobieram zestaw danych MNIST, który składa się z 60000 obrazów treningowych i 10000 obrazów testowych 28x28."""

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("x_train:", x_train.shape)
print("y_train:", y_train.shape)
print("x_test:", x_test.shape)
print("Przykładowa etykieta:", y_train[0])

import matplotlib.pyplot as plt
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i])
plt.show()

plt.imshow(x_train[600])
plt.show()
print("Label:", y_train[600])

"""Normalizacja wartości pikseli. Wartości pikseli w MNIST mieszczą się w zakresie [0, 255]. Seci konwolucyjne lepiej działają, gdy wartości są skalowane do zakresu [0, 1]."""

#normalizacja wartości pikseli
x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32')/255.0

"""Zmieniamy wymiary danych z 3D na 4D."""

x_train = x_train.reshape(-1, 28, 28, 1)  # (liczba próbek, wysokość, szerokość, liczba kanałów 1(odćienia szarości))
x_test = x_test.reshape(-1, 28, 28, 1)

"""One-Hot encoding. Przestawia kolumnę kategorialną, tworząc n kolumn, gdzie n jest równe liczbie unikatowych wartości w kolumnie. Liczba 1 jest przypisywana do odpowiedniej kolumny dla każdego wiersza, a 0 do pozostałych kolumn, które zostały wygenerowane dla kategorii."""

#One-Hot encoding. Przypisuje 1 do odp kolumny i 0 do pozostałych
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

"""Dzielę zbiór danych treningowych na zbiór danych treningowych i walidacyjnych."""

from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

print(x_train.shape)
print(y_train.shape)
print(x_val.shape)
print(y_val.shape)

"""Sieć konwolucyjna. Składa się z warstw konwolucyjnych(Conv2D), warstw spoolingujących(MaxPooling2D), warstw genstych(Dense). Tworzę model: 1 warstwa konwolucyjna z 32 filtrami o rozmiarze 3x3, aktywacja relu usuwa wartości ujemne, input_shape =(28, 28, 1) rozmiar zdjenć w zbiorze, warstwa MaxPooling2D((2, 2)) zmniejszająca wymiary obrazów przez wybieranie najwieńkszej wartości w oknie 2x2; 2 warstwa konwolucyjna z 64 filtrami; 3 warstwa konwolucyjna z 128 filtrami; Flatten() spłaszcza dane wejściowe do postaci jednowymiarowej tablicy, co jest wymagane dla warstw Dense; warstwa gęsta Dense połączona z 128 neuronami, Dropout(0.5) wyłącz 50% neuronów podczas treningu, co zapobega przeuczeniu; ostatnia warstwa klasyfikacyjna Dense(10, activation='softmax') z 10 wyjsciami po 1 dla każdej klasy MNIST."""

# Model CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1))) # rozmiar filtru
model.add(MaxPooling2D((2, 2))) # rozmiar padu
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

"""Dla kompilacji modelu zdefiniowane optymizator 'adam', funkcja straty i metryki."""

# Kompilacja modelu
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Trenowanie modelu
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=40, batch_size=32, callbacks=[tf.keras.callbacks.EarlyStopping(patience=15, restore_best_weights=True)])

plt.subplot(1, 2, 1)
plt.plot(history.history["loss"], label="loss")
plt.plot(history.history["val_loss"], label="val_loss")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history["accuracy"], label="accuracy")
plt.plot(history.history["val_accuracy"], label="val_accuracy")
plt.legend()
plt.show()

"""Dokładność na zbiorze testowym wyniosła 0.9868999719619751."""

# Oceniamy model na zbiorze testowym
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test loss: {test_loss}")
print(f"Test accuracy: {test_accuracy}")

model.save('Dorosh.h5')