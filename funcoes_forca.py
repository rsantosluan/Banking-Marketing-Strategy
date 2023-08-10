### Importações
import random
 



### Classe referentes a mensagens
class mensagens:
    
    def abertura():
        print("*********************************")
        print("** Bem vindo ao jogo da Forca! **")
        print("*********************************")
        
    def vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")    
        
    def  perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")  
    
    def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")
        
        if(erros == 0):
            print(" |            ")
            print(" |            ")
            print(" |            ")
        if(erros == 1):
            print(" |     (*-*)   ")
            print(" |             ")
            print(" |             ")
            print(" |             ")

        if(erros == 2):
            print(" |     (*-*)   ")
            print(" |      \      ")
            print(" |             ")
            print(" |             ")

        if(erros == 3):
            print(" |     (*-*)   ")
            print(" |      \|     ")
            print(" |             ")
            print(" |             ")

        if(erros == 4):
            print(" |     (*-*)   ")
            print(" |      \|/    ")
            print(" |             ")
            print(" |             ")

        if(erros == 5):
            print(" |     (*-*)   ")
            print(" |      \|/    ")
            print(" |       |     ")
            print(" |             ")

        if(erros == 6):
            print(" |     (*-*)   ")
            print(" |      \|/    ")
            print(" |       |     ")
            print(" |      /      ")

        if (erros == 7):
            print(" |     (*-*)   ")
            print(" |      \|/    ")
            print(" |       |     ")
            print(" |      / \    ")

        print(" |            ")
        print("_|___         ")
        print()     
        
    def mostra_letras_acertadas( letras_acertadas, palavra_secreta, letras_faltando ):
        print( 'Palavra secreta: ' )
        print( '| ' , end='')
        if '-' in palavra_secreta:
            for i in range(len(letras_acertadas)):
                print( f'{letras_acertadas[i]}', end=' ' )
            print( f' | contendo {len(palavra_secreta)-1} e faltam {letras_faltando} letras' )    
        else:    
            for i in range(len(letras_acertadas)):
                print( f'{letras_acertadas[i]}', end=' ' )
        print( f' | contendo {len(palavra_secreta)} e faltam {letras_faltando} letras' )


### Carrega e define a palavra secreta
class palavra():
    @staticmethod
    def define_palavra(tema):
        palavras = []
        ## Se o tema escolhido for
        # 1
        if tema == 1:
            ## Faz a leitura de todo o arquivo e coloca cada palavra em uma posição da lista
            with open( "./data/palavras.txt", 'r', encoding = 'utf-8' ) as arquvivo:
                for linha in arquvivo:
                    linha = linha.strip()
                    palavras.append( linha )

            ## Seleciona uma palavra aleatoriamente
            palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
        elif tema == 2:
            ## Faz a leitura de todo o arquivo e coloca cada palavra em uma posição da lista
            with open( "./data/educacao.txt", 'r', encoding = 'utf-8' ) as arquvivo:
                for linha in arquvivo:
                    linha = linha.strip()
                    palavras.append( linha )
                    ## Seleciona uma palavra aleatoriamente
                    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
        elif tema == 3:
            ## Faz a leitura de todo o arquivo e coloca cada palavra em uma posição da lista
            with open( "./data/senac.txt", 'r', encoding = 'utf-8' ) as arquvivo:
                for linha in arquvivo:
                    linha = linha.strip()
                    palavras.append( linha )
                    ## Seleciona uma palavra aleatoriamente
                    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
        elif tema == 4:
            ## Faz a leitura de todo o arquivo e coloca cada palavra em uma posição da lista
            with open( "./data/servidor.txt", 'r', encoding = 'utf-8' ) as arquvivo:
                for linha in arquvivo:
                    linha = linha.strip()
                    palavras.append( linha )
                    ## Seleciona uma palavra aleatoriamente
                    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
        else:
            ## Faz a leitura de todo o arquivo e coloca cada palavra em uma posição da lista
            with open( "./data/video_games.txt", 'r', encoding = 'utf-8' ) as arquvivo:
                for linha in arquvivo:
                    linha = linha.strip()
                    palavras.append( linha )
                    ## Seleciona uma palavra aleatoriamente
                    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
            
            ## Seleciona uma palavra aleatoriamente
            palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()    
            ## Seleciona uma palavra aleatoriamente
            palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()    
            ## Seleciona uma palavra aleatoriamente
            palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()    
            ## Seleciona uma palavra aleatoriamente
            palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()    
        return palavra_secreta 
    
### Ações do jogo
class acoes_de_jogo():
    ## Inicializa letras acertadas
    @staticmethod
    def inicializa_letras_acertadas(palavra_secreta):
        letras_acertadas = []
        for letra in palavra_secreta:
            if letra == '-':
                letras_acertadas.append( '-' )
            else:
                letras_acertadas.append( '_' )
                    
        return letras_acertadas
    ## Pede chute ao usuário
    @staticmethod
    def pedir_cute():
        chute = input( 'Digite uma letra: ' )
        chute = chute.strip().upper()
        return chute  
    
    ## Define o chute do usuário como correto
    @staticmethod
    def chute_certo(chute, letras_certas, palavra_secreta):
        i = 0
        for  letra in palavra_secreta:
            if ( chute == letra ):
                letras_certas[i] = letra
            i += 1    
        return letras_certas    

class iniciar_jogo():
    def jogar():
        ## Imprime mensagem de abertura
        mensagens.abertura()


        tema = 0
        lista_temas = ['Aleatório', 'Educação', 'Senac', 'Windows Server', 'Videogames']
        while tema not in [1,2,3,4,5]:
            ## Define o tema das palavras
            print( 'Escolha o tema digitando: ' )
            print(  '1 para Aleatório' )
            print(  '2 para Educação' )
            print(  '3 para Senac' )
            print(  '4 para Windows Server' )
            print(  '5 para Videogames' )
            tema = int(input('Digite o número referente ao tema: '))
            if tema not in [1,2,3,4,5]:
                print( '----------------------------------------------------------------------2' )
                print( 'Informe o número corretamente!' )
            else:
                print (f'Tema escolhido: {lista_temas[tema - 1]}')    

        ## Carrega palavra secreta
        palavra_secreta = palavra.define_palavra(tema)

        ## Inicializa letras acertadas
        letras_acertadas = acoes_de_jogo.inicializa_letras_acertadas( palavra_secreta )
        
        ## Inicia as variáveis para verificar andamento do jogo
        enforcou = False
        acertou = False
        erros = 0
        if '-' in palavra_secreta:
            letras_faltando = len( palavra_secreta ) - 1
        else:
            letras_faltando = len( palavra_secreta )
        chutes = []

        ## Mostrando desenho da forca
        mensagens.desenha_forca( erros )

        ## Mostrando na tela as letras acertadas para que o usuário saiba quantas letras tem a palavra
        mensagens.mostra_letras_acertadas( letras_acertadas, palavra_secreta, letras_faltando )

        ## Iniciando o jogo
        while (not acertou and not enforcou):

            ## Define se o chute já foi dado anteriormente
            ok = False
            while not ok:
                chute = acoes_de_jogo.pedir_cute()
                if chute not in chutes:
                    chutes.append( chute )
                    ok = True
                else:
                    print( '------------------------------------------------------------------------------------------------------------' )
                    print('Você já tentou esta letra. Por favor digite outra: ')    

                    mensagens.mostra_letras_acertadas( letras_acertadas, palavra_secreta, letras_faltando )                


            # conferindo se chute está contido na palavra
            if ( chute in palavra_secreta ):
                # Define o chute como certo
                letras_acertadas = acoes_de_jogo.chute_certo( chute, letras_acertadas, palavra_secreta )

                # Define quantidade de letras faltando
                letras_faltando =  letras_acertadas.count('_') 

                #Retorna mensagem com letras faltantes
                mensagens.mostra_letras_acertadas( letras_acertadas, palavra_secreta, letras_faltando )
                if (letras_faltando == 0):
                    # Define jogo como ganho
                    acertou = True
            else:
                # Adiciona 1 erro
                erros += 1    
                mensagens.desenha_forca( erros )
                mensagens.mostra_letras_acertadas( letras_acertadas, palavra_secreta, letras_faltando )

                # Confere se o usuário perdeu
                if erros == 7:
                    enforcou = True

            # Mostra tentativas
            print( f'Letras já chutadas: {chutes}' )         

        if ( acertou ):
            mensagens.vencedor()
        else:
            mensagens.perdedor( palavra_secreta )        