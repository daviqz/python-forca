import random

def jogar():
    print("*********************************")
    print("*             Forca             *")
    print("*********************************")

    palavras = ["cocota", "carro", "fusca", "pessoa", "programa", "cha", "folha", "familia", "trem", "sapeca", "sua mae"]

    palavra_secreta = random.choice(palavras).lower()
    chutes_certos = []
    chutes_errados = []

    adivinhando_palavra = ["__" for letra in palavra_secreta]
    rodada = 0
    tentativas = 6

    enforcado = False
    vitoria = False

    print("Você possui {} tentativas.".format(tentativas))

    while(not enforcado and not vitoria):
        print(adivinhando_palavra)
        print("#########################")
        print("Rodada:", rodada)
        print("Acertos: ", chutes_certos)
        print("Erros: ", chutes_errados)
        print("#########################")
        chute = input("Digite uma letra: ").lower()

        letra_digitada = palavra_secreta.find(chute)
        acerto_letra = ''

        chute_valido = not chutes_errados.count(chute) and not chutes_certos.count(chute) and not chute == '' and len(chute) == 1

        if(chute_valido):
            if(letra_digitada == -1):
                chutes_errados.append(chute)
            else:
                chutes_certos.append(chute)
                acerto_letra = chute
        else:
            print("Você ja digitou essa letra, ou não é um caracter valido.")
            continue

        for idx, char in enumerate(palavra_secreta):
            if(acerto_letra == char):
                adivinhando_palavra[idx] = acerto_letra
       
        fim = [letra for letra in adivinhando_palavra if letra == "__"]
        vitoria = len(fim) == 0
        rodada = rodada + 1
        enforcado = len(chutes_errados) >= tentativas

    print("A palavra era:", palavra_secreta)

    if(vitoria):
        print("Vitória!")
    elif(enforcado):
        print("Você perdeu!")
    else:
        print("Outras condicoes se necessario")

if(__name__ == "__main__"):
    jogar()
