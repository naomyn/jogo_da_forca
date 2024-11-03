import random

palavras = [
    'Caminhao', 'Dracula', 'Morcego', 'Ornitorrinco', 
    'Caixao', 'Hamster', 'Cigarro', 'Abacate', 'Bola', 
    'Carro', 'Dado', 'Elefante', 'Flor', 'Gato', 
    'Hipopotamo', 'Iguana', 'Jacare', 'Kiwi', 'Leao', 
    'Mesa', 'Navio', 'Ocelote', 'Pato', 'Quadro', 
    'Rato', 'Sapo', 'Tigre', 'Urso', 'Vaca', 
    'Xaxim', 'Yeti', 'Zebra', 'Amor', 'Brisa', 
    'Casa', 'Danca', 'Escola', 'Futebol', 'Girassol', 
    'Harpa', 'Isla', 'Jardim', 'Laranja', 'Musica', 
    'Noite', 'Onda', 'Piano'
]
palavra_sorteada = palavras[random.randint(0, len(palavras) - 1)]

tentativas = 6

def underlines(string):
    tamanho_palavra = len(string)

    for letra in range(tamanho_palavra):
        print('_', end= ' ')

    print()

def iniciar_jogo():
    print('Olá! Bem vindo ao Jogo da Forca!!')
    print('')


print(palavra_sorteada)
underlines(palavra_sorteada)
