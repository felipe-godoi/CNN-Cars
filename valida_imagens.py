import os
from PIL import Image

def verifica_imagens_corrompidas(diretorio):
    imagens_corrompidas = []
    
    for nome_pasta in os.listdir(diretorio):
        print(f"Verificando a pasta {nome_pasta}")
        for nome_arquivo in os.listdir(f'{diretorio}/{nome_pasta}'):
            if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                try:
                    with Image.open(os.path.join(f'{diretorio}/{nome_pasta}', nome_arquivo)) as img:
                        img.verify()
                except (IOError, SyntaxError) as e:
                    imagens_corrompidas.append(nome_arquivo)
    
    if len(imagens_corrompidas) > 0:
        print("Imagens corrompidas encontradas:")
        for imagem in imagens_corrompidas:
            print(imagem)
    else:
        print("Nenhuma imagem corrompida foi encontrada.")

if __name__ == "__main__":
    diretorio = "training"
    verifica_imagens_corrompidas(diretorio)
