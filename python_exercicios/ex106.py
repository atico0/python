while True:
    print('\033[31;46mSISTEMA DE AJUDA PYHELP')
    ajuda = input('\033[04;30;44mFunção ou biblioteca (Digite Fim para encerrar):\033[01;32;40m').strip()
    if ajuda == 'Fim':
        break
    help(ajuda)
print('\033[07;37;40mATÉ logo')