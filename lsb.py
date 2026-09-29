import sys
from email.mime import image

from PIL import Image

def codificar(entrada, mensagem, saida):
    imagem = image.open(entrada).convert('RGB')
    pixels = imagem.load()
    largura, altura = imagem.size

    mensagem = '/0' #adiciona o 0 para saber onde vai parar o código

    bits_msg = ''.join(format(ord(char), '08b') for char in mensagem)
    tam_bits = len(bits_msg)

    if tam_bits > largura * altura:
        print('A imagem deve ser maior para a mensagem!')
        return

    indice_bit = 0;

    for x in range(altura):
        for y in range(largura):
            if indice_bit < tam_bits:
                r, g, b = pixels[x, y]

                bit = int(bits_msg[indice_bit])

                novo_bit = ()