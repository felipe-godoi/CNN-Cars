from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

classificador = load_model('classificador.h5')

dados_treinamento = ImageDataGenerator(rescale=1./255)

dados_previsao = dados_treinamento.flow_from_directory(
    './previsao', target_size=(64, 64), batch_size=1, class_mode='categorical')

previsao = classificador.predict(dados_previsao)
print(previsao)