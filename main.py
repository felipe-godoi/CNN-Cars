from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.layers import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator

classificador = Sequential()
classificador.add(
    Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
classificador.add(BatchNormalization())
classificador.add(MaxPooling2D(pool_size=(2, 2)))

classificador.add(
    Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
classificador.add(BatchNormalization())
classificador.add(MaxPooling2D(pool_size=(2, 2)))

classificador.add(Flatten())

classificador.add(Dense(units=100, activation='relu'))
classificador.add(Dense(units=100, activation='relu'))
classificador.add(Dense(units=9, activation='softmax'))

classificador.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

dados_treinamento = ImageDataGenerator(rescale=1./255)
dados_teste = ImageDataGenerator(rescale=1./255)

amostras_treinamento = dados_treinamento.flow_from_directory(
    './training', target_size=(64, 64), batch_size=32, class_mode='categorical')

amostras_teste = dados_teste.flow_from_directory(
    './test', target_size=(64, 64), batch_size=32, class_mode='categorical')

classificador.fit(amostras_treinamento, steps_per_epoch=140,
                            epochs=10, validation_data=amostras_teste, validation_steps=576)

classificador.save('classificador.h5')

dados_previsao = dados_treinamento.flow_from_directory(
    './previsao', target_size=(64, 64), batch_size=1, class_mode='categorical')

previsao = classificador.predict(dados_previsao)
print(previsao)