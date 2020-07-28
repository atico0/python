import os

caminho = 'C:\\Users\core i3\Pictures\descartaveis'
for raiz, diretorios, arquivos in os.walk(caminho):
    print(arquivos,'\n',raiz,'\n',diretorios)
    for arquivo in  arquivos:
        caminho_completo = os.path.join(raiz,arquivo)
        tamanho = os.path.getsize(caminho_completo)
        print(caminho_completo,tamanho,sep='-->')