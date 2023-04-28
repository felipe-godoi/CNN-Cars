import os
from PIL import Image

def verifica_imagens_corrompidas(diretorio):
    imagens_corrompidas = []
    
    for nome_arquivo in os.listdir(diretorio):
        print(f"Verificando a imagem {nome_arquivo}")
        if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            try:
                with Image.open(os.path.join(diretorio, nome_arquivo)) as img:
                    img.verify()
            except (IOError, SyntaxError) as e:
                print(f"A imagem {nome_arquivo} está corrompida.")
                imagens_corrompidas.append(nome_arquivo)
    
    if len(imagens_corrompidas) > 0:
        print("Imagens corrompidas encontradas:")
        for imagem in imagens_corrompidas:
            print(imagem)
    else:
        print("Nenhuma imagem corrompida foi encontrada.")

if __name__ == "__main__":
    diretorio = "test/yaris"
    verifica_imagens_corrompidas(diretorio)
