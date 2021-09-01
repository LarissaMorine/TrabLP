import pygame
from time import sleep

def comeco_do_jogo():

    #imagem
    pygame.init()
    janela = pygame.display.set_mode((500, 418))
    bemvindo = pygame.image.load('benvindo.png')
    pygame.display.set_caption("Bem-vindo ao Vai dar Namoro")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(bemvindo, (0, 0))
    pygame.quit()
    janela = pygame.display.set_mode((500, 418))
    bemvindo2 = pygame.image.load('benvindo2.png')
    pygame.display.set_caption("Bem-vindo ao Vai dar Namoro")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(bemvindo2, (0, 0))
    pygame.quit()

    #resposta
    print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m:")
    resposta = input(' R: ').lower().strip()
    while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
        print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
        resposta = input(' R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if 's' in resposta:
        introducao()
    else:
        #imagem de saída
        janela = pygame.display.set_mode((500, 418))
        gameover1 = pygame.image.load('1°gameover.png')
        pygame.display.set_caption("Que pena :P")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover1, (0, 0))
        pygame.quit()
        agradecimento()

def introducao():

    print("Imagine que você é \033[1;31mapaixonado por Mônica\033[m desde os 8 anos de idade, quando ela se mudou para o mesmo bairro que você: "
          "\nPodemos dizer que foi \033[4mamor à primeira vista\033[m.")
    sleep(4)
    print("\nPorém, vocês nunca conseguiram criar nenhum tipo de relação, já que Mônica começou a namorar bem nova.")
    sleep(3)
    print("\n\033[1;30;107mMas agora chegou sua vez...\033[m")
    sleep(2)
    print("\nDepois de terminar um longo relacionamento, ela pode viver um novo romance"
          "\nE, quem sabe, você possa ser sortudo e \033[4mconquistar o coração de seu amor de infância!\033[m")
    sleep(5)
    print("\n\033[1;32mVAMOS NESSA!\033[m")
    sleep(1)

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    sleep(1)
    print("\033[1;33mHoje é uma sexta-feira e você está de folga da faculdade, então resolve fazer algo para relaxar...\033[m")
    print("\nO que você escolhe:")
    print(" \033[1;32m1)\033[m Ir andar pelo parque/bairro")
    print(" \033[1;32m2)\033[m Maratonar aquela série que você está há tempos planejando assistir")

    #resposta
    resposta = input('  R: ').lower().strip()
    while resposta != '1' and resposta != '2':
        print("\n\033[1mMas você já vai estragar tudo?\033[m Responda com \033[1;32m1\033[m ou \033[1;32m2\033[m! \033[4mTente novamente\033[m:")
        resposta = input('  R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == '1':
        #imagens
        janela = pygame.display.set_mode((500, 418))
        benvindo = pygame.image.load('encontramonica.png')
        pygame.display.set_caption("Encontrando a Mônica")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(benvindo, (0, 0))
        pygame.quit()
        janela = pygame.display.set_mode((500, 418))
        benvindo = pygame.image.load('coisascomuns.png')
        pygame.display.set_caption("Coisas em comum")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(benvindo, (0, 0))
        pygame.quit()
        item_1()

    else:
        #GAME OVER + PLAY AGAIN (1/6)
        #imagem
        janela = pygame.display.set_mode((500, 418))
        gameover = pygame.image.load('gameover.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover, (0, 0))
        pygame.quit()

        #tentar novamente
        print('\033[4mVocê deseja tentar essa fase novamente?\033[m')
        resposta = input('  R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()

        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 's' in resposta:
            introducao()
        else:
            agradecimento()

def item_1():

    #definição dos pontos
    pontos_de_proximidade = 0
    pontos_de_coragem = 0

    #imagem
    janela = pygame.display.set_mode((500, 418))
    celular = pygame.image.load('itemcelular.png')
    pygame.display.set_caption("Item Celular")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(celular, (0, 0))
    pygame.quit()

    #resposta
    print("\033[1;30;107mVocê deseja coletar esse item?\033[m")
    resposta = input(' R: ').lower().strip()
    while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
        print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
        resposta = input(' R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if 's' in resposta:

        #PONTO DE CORAGEM (1/4)
        #imagem
        janela = pygame.display.set_mode((500, 418))
        coragem = pygame.image.load('pontocoragem.png')
        pygame.display.set_caption("Ponto de Coragem")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(coragem, (0, 0))
        pygame.quit()

        #somatório
        pontos_de_coragem += 1
        print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto de coragem e', pontos_de_proximidade, 'pontos de proximidade')
        sleep(2)
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        por_onde_chamar(pontos_de_coragem, pontos_de_proximidade)

    else:
        print("\033[1;33mNa manhã seguinte, Mônica posta stories falando sobre o livro que ela acabou de ler!\033[m")
        sleep(3)
        print('\nPor sorte, você também havia terminado de ler esse livro algum tempo atrás')
        sleep(3)
        print('\nComo você não pediu o número dela no dia anterior, sua única opção é responder os stories...')
        sleep(3)
        print('\nVocês começaram a conversar bastante sobre diversos assuntos'
              '\nResolveram, então, marcar de se encontrar no parque.')
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        sleep(3)

        #PONTO DE PROXIMIDADE (1a/3)
        #imagem
        janela = pygame.display.set_mode((500, 418))
        proximidade = pygame.image.load('pontoproximidade.png')
        pygame.display.set_caption("Ponto de Proximidade")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(proximidade, (0, 0))
        pygame.quit()

        #somatório
        pontos_de_proximidade += 1
        print('\n\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'pontos de coragem e', pontos_de_proximidade, 'ponto de proximidade')
        sleep(2)
        parque(pontos_de_coragem, pontos_de_proximidade)

def por_onde_chamar(pontos_de_coragem, pontos_de_proximidade):

    print("\033[1;33mNa manhã seguinte, Mônica posta stories falando sobre o livro que ela acabou de ler!\033[m")
    sleep(3)
    print('Por sorte, você também havia terminado de ler esse livro algum tempo atrás')
    sleep(3)
    print("\nComo você coletou o item 'número de celular', você pode escolher entre 2 opções:")
    print(" \033[1;32m1)\033[m Responder os stories falando sobre o livro")
    print(" \033[1;32m2)\033[m Chamar no whats falando sobre o livro")

    #resposta
    resposta = input('  R: ').lower().strip()
    while resposta != '1' and resposta != '2':
        print("\n\033[m Responda com \033[1;32m1\033[m ou \033[1;32m2\033[m! \033[4mTente novamente\033[m:")
        resposta = input('  R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == '1':
        print('\033[1;33mVocês começaram a conversar bastante sobre diversos assuntos\033[m'
              '\nResolveram, então, marcar de se encontrar no parque.')
        sleep(4)

        #imagem
        janela = pygame.display.set_mode((500, 418))
        proximidade = pygame.image.load('pontoproximidade.png')
        pygame.display.set_caption("Ponto de Proximidade")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(proximidade, (0, 0))
        pygame.quit()

        #PONTO DE PROXIMIDADE (1b/3)
        #somatório
        pontos_de_proximidade += 1
        print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
        sleep(2)
        parque(pontos_de_coragem, pontos_de_proximidade)
    else:
        depois_wpp(pontos_de_coragem, pontos_de_proximidade)

def depois_wpp(pontos_de_coragem, pontos_de_proximidade):

    print('\033[1;33mWOW, vocês ficaram a noite toda conversando e estão ainda mais próximos!\033[m')
    sleep(3)

    #imagem
    janela = pygame.display.set_mode((500, 418))
    proximidade = pygame.image.load('pontoproximidade.png')
    pygame.display.set_caption("Ponto de Proximidade")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(proximidade, (0, 0))
    pygame.quit()

    #PONTO DE PROXIMIDADE (1c/3)
    #somatório
    pontos_de_proximidade += 1
    print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
    sleep(2)

    print("\nVocê decide dar um passo adiante e resolve \033[1;33mconvidá-la para sair.\033[m")
    sleep(3)
    print("\nEai, qual vai ser: \033[1;32mparque\033[m ou \033[1;32mcinema\033[m?")

    #resposta
    resposta = input(' R: ').lower().strip()
    while resposta != 'parque' and resposta != 'cinema':
        print("\nResponda com '\033[1;32mparque\033[m' ou '\033[1;32mcinema\033[m'! Tente novamente:")
        resposta = input(' R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'parque':
        parque(pontos_de_coragem, pontos_de_proximidade)
    else:
        cinema(pontos_de_coragem, pontos_de_proximidade)

def cinema(pontos_de_coragem, pontos_de_proximidade):

    print('\033[1;33mUUUUH, ela topou!\033[m Só falta escolher o gênero, vamos de \033[1;32mterror\033[m ou \033[1;32mromance?\033[m')

    #resposta
    resposta = input(' R: ').lower().strip()
    while resposta != 'terror' and resposta != 'romance':
        print("\nResponda com '\033[1;32mterror\033[m' ou '\033[1;32mromance\033[m'! Tente novamente:")
        resposta = input(' R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'romance':
        print('Iih...o filme que vocês assistem \033[1;31mlembra o ex namorado dela\033[m'
              '\nEla acha que isso pode ser um sinal e acaba indo embora pensando em voltar com ele :(')
        sleep(4)

        #GAME OVER + PLAY AGAIN (2/6)
        #imagem
        pygame.init()
        janela = pygame.display.set_mode((500, 418))
        gameover_geral = pygame.image.load('gameover_geral.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover_geral, (0, 0))
        pygame.quit()

        #tentar novamente
        print('\033[4mVocê deseja tentar essa fase novamente?\033[m')
        resposta = input('  R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()

        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 's' in resposta:
            cinema(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('\033[1;33mO filme de terror deu super certo e vocês ficaram agarradinhos a noite toda.\033[m')
        sleep(3)

        #imagem
        janela = pygame.display.set_mode((500, 418))
        proximidade = pygame.image.load('pontoproximidade.png')
        pygame.display.set_caption("Ponto de Proximidade")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(proximidade, (0, 0))
        pygame.quit()

        #PONTO DE PROXIMIDADE (2/3)
        #somatório
        pontos_de_proximidade += 1
        print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
        sleep(2)

        print("\nAntes de ir embora, \033[4mela te chama para jantar\033[m e, obviamente, você aceita.")
        sleep(3)
        print("\nFicou combinado de ambos se encontrarem amanhã às 20h00 no Olive Garden.")
        sleep(3)
        encontro_1(pontos_de_coragem, pontos_de_proximidade)

def parque(pontos_de_coragem, pontos_de_proximidade):

    print('\033[1;33mVocês se encontraram no ponto de ônibus e foram caminhando até o parque...\033[m')
    sleep(3)
    print('\nVishh, começou a chover, pensaram em voltar para casa mas acabaram se divertindo na chuva.')
    sleep(3)
    print('\nApós esse momento super especial, vocês decidem sair para jantar no próximo dia '
          '\nE combinam de se encontrarem às 20h00 no Oliver Garden.')
    sleep(4)
    encontro_1(pontos_de_coragem, pontos_de_proximidade)

def encontro_1(pontos_de_coragem, pontos_de_proximidade):
    print("\n\033[1;30;107mNO OUTRO DIA...\033[m")
    sleep(2)

    print('\nTá quase na hora do encontro hein, você vai ir de \033[1;32mcarro\033[m ou \033[1;32muber\033[m?')

    #resposta
    resposta = input(' R: ').lower().strip()
    while resposta != 'carro' and resposta != 'uber':
        print("\nResponda com '\033[1;32mcarro\033[m' ou '\033[1;32muber\033[m'! \033[4mTente novamente\033[m:")
        resposta = input(' R: ').lower().strip()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'carro':
        print('Caraca, o carro estava ZERADO de gasolina e você teve de parar no posto para abastecer.')
        sleep(3)
        print("Infelizmente acabou demorando muito porque a bomba travou bem na sua vez :(")
        sleep(3)
        print("Quando chegou ao restaurante já estava meia hora atrasado, \033[1;31me ela tinha ido embora achando que você não viria…\033[m")
        sleep(3)

        #GAME OVER + PLAY AGAIN (3/6)
        #imagem
        pygame.init()
        janela = pygame.display.set_mode((500, 418))
        gameover_geral = pygame.image.load('gameover_geral.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover_geral, (0, 0))
        pygame.quit()

        #tentar novamente
        print('\033[4mVocê deseja tentar essa fase novamente?\033[m')
        resposta = input('  R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()

        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 's' in resposta:
            encontro_1(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('\033[1;33mVocê chegou e logo pediu ao garçom a melhor mesa!\033[m'
              '\nMônica chega depois de um tempo e você só consegue pensar em como ela está linda!')
        sleep(4)
        print('\n\033[1;33mQue noite INCRÍVEL!\033[m Você percebe que Mônica realmente é a pessoa certa para você!')
        sleep(3)
        acompanhar(pontos_de_coragem, pontos_de_proximidade)

def acompanhar(pontos_de_coragem, pontos_de_proximidade):
    print("\nEla pergunta se você pode acompanha-lá até sua casa.")
    sleep(2)
    print("\nEai, \033[1;32msim\033[m ou \033[1;31mnão?\033[m")

    #resposta
    resposta = input(' R: ').lower().strip()
    while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
        print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
        resposta = input(' R: ').lower().strip()

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if 's' in resposta:

        #PONTO DE PROXIMIDADE (3/3)
        #imagem
        janela = pygame.display.set_mode((500, 418))
        proximidade = pygame.image.load('pontoproximidade.png')
        pygame.display.set_caption("Ponto de Proximidade")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(proximidade, (0, 0))
        pygame.quit()

        #somatório
        pontos_de_proximidade += 1
        print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
        sleep(3)
        janela = pygame.display.set_mode((500, 418))
        beijo = pygame.image.load('itembeijo.png')
        pygame.display.set_caption("Primeiro Beijo")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(beijo, (0, 0))
        pygame.quit()
        print("\n\033[1;30;107mAinda está muito cedo para coletar esse item?\033[m")

        #resposta
        resposta = input(' R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 'n' in resposta:

            #PONTO DE CORAGEM (2/4)
            #imagem
            janela = pygame.display.set_mode((500, 418))
            coragem = pygame.image.load('pontocoragem.png')
            pygame.display.set_caption("Ponto de Coragem")
            janela_aberta = True
            while janela_aberta:
                pygame.time.delay(50)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        janela_aberta = False
                pygame.display.update()
                janela.blit(coragem, (0, 0))
            pygame.quit()

            #somatório
            pontos_de_coragem += 1
            print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
            sleep(2)

            print('\n\033[1;33mCARACA, que beijão de cinema!\033[m Você volta saltitando de felicidade para casa.')
            sleep(3)
            mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)
        else:
            print("\033[1;33mVocês se despedem com um breve abraço e vão embora.\033[m")
            sleep(3)
            mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)
    else:
        print('\033[1;33mVocê diz que não pode, pois irá para a casa de sua tia.\033[m')
        sleep(2)
        print("Mônica fica um pouco chateada mas compreende.")
        sleep(2)
        print("Vocês se despedem com um breve abraço e vão embora.")
        sleep(2)
        mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)

def mandar_mensagem(pontos_de_coragem, pontos_de_proximidade):
    print("\nE agora vem a dúvida... \033[1;32mmandar mensagem\033[m ou \033[1;32mesperar que ela mande\033[m?")

    #resposta
    resposta = input(' R: ').lower().strip()
    while resposta != 'mandar mensagem' and resposta != 'mandar' and resposta != 'esperar' and resposta != 'esperar que ela mande':
        print("\nResponda com '\033[1;32mmandar (mensagem)\033[m' ou '\033[1;32mesperar (que ela mande)\033[m'! Tente novamente:")
        resposta = input(' R: ').lower().strip()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'esperar' or resposta == 'esperar que ela mande':
        print('\033[1;31mPuts!\033[m Esperava um pouco mais de atitude! Vacilou ein!')
        sleep(2)

        #GAME OVER + PLAY AGAIN (4/6)
        #imagem
        pygame.init()
        janela = pygame.display.set_mode((500, 418))
        gameover_geral = pygame.image.load('gameover_geral.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover_geral, (0, 0))
        pygame.quit()

        #tentar novamente
        print('\033[4mVocê deseja tentar essa fase novamente?\033[m')
        resposta = input('  R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()

        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 's' in resposta:
            mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('\033[1;33mIsso aí! Perfeito!\033[m Você está no caminho certo, atitude é fundamental!')
        sleep(2)

        #PONTO DE CORAGEM (3/4)
        #imagem
        janela = pygame.display.set_mode((500, 418))
        coragem = pygame.image.load('pontocoragem.png')
        pygame.display.set_caption("Ponto de Coragem")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(coragem, (0, 0))
        pygame.quit()

        #somatório
        pontos_de_coragem += 1
        print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade, 'ponto(s) de proximidade')
        sleep(3)
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        apos_encontro(pontos_de_coragem, pontos_de_proximidade)

def apos_encontro(pontos_de_coragem, pontos_de_proximidade):
    print("Já faz um tempo que vocês estão nessa, vários rolês, vários encontros, vários momentos! "
          "\n\033[1;30;107mAcredito que já esteja na hora de dar um passo a mais...\033[m")
    sleep(4)
    print("\nO que você acha de chamar ela para vocês conversarem, analisar se os sentimentos estão batendo ou não?")
    sleep(3)
    print("\nVamos lá... \033[1;32mse declarar\033[m ou \033[1;32mdeixar rolar\033[m?")

    #resposta
    resposta = input(' R: ').lower().strip()
    while resposta != 'se declarar' and resposta != 'deixar rolar' and resposta != 'deixar' and resposta != 'declarar':
        print("\nResponda com '\033[1;32mse declarar\033[m' ou '\033[1;32mdeixar (rolar)\033[m'! \033[4mTente novamente\033[m:")
        resposta = input(' R: ').lower().strip()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'deixar rolar' or resposta == 'deixar':
        print('\033[1;31mPoxa! Estava indo tão bem...\033[m Era só deixar a insegurança de lado e se jogar no lance!')
        sleep(3)

        #GAME OVER + PLAY AGAIN (5/6)
        #imagem
        pygame.init()
        janela = pygame.display.set_mode((500, 418))
        gameover_geral = pygame.image.load('gameover_geral.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover_geral, (0, 0))
        pygame.quit()

        #tentar novamente
        print('\033[4mVocê deseja tentar essa fase novamente?\033[m')
        resposta = input('  R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()

        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 's' in resposta:
            apos_encontro(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('\033[1;33m O tiro foi certeiro!\033[m Ela também está na sua, agora é só se empenhar pra não vacilar!')
        sleep(3)

        #PONTO DE CORAGEM (4/4)
        #imagem
        janela = pygame.display.set_mode((500, 418))
        coragem = pygame.image.load('pontocoragem.png')
        pygame.display.set_caption("Ponto de Coragem")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(coragem, (0, 0))
        pygame.quit()

        #somatório
        pontos_de_coragem += 1
        print('\033[1;97;44mEstoque atual:\033[m', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade, 'ponto(s) de proximidade')
        sleep(2)
        pedido_namoro(pontos_de_coragem, pontos_de_proximidade)

def pedido_namoro(pontos_de_coragem, pontos_de_proximidade):
    print("\nDepois desse momento muito fofo, você decide que está na hora de pedi-lá em namoro...")
    sleep(3)
    print("\n\033[1;33mChegou o dia! Está tudo perfeito!\033[m"
          "\nVocê compra um buquê de flores para ela, prepara um jantar M-A-R-A e a chama para sua casa!")
    sleep(4)
    print("\nNo momento certo, você ajoelha e faz o pedido...")
    sleep(2)
    print("\nEai, ela aceitou ou não?")
    continuar = input("\033[1;30;107mDê um enter para descobrir!\033[m")

    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if pontos_de_coragem == 4 and pontos_de_proximidade == 3:

        #imagem
        janela = pygame.display.set_mode((500, 418))
        aceitou = pygame.image.load('aceitou.png')
        pygame.display.set_caption("Parabéns!")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(aceitou, (0, 0))
        pygame.quit()

        print('\n\033[1;97;42mParabéns! Você conseguiu acumular 4 pontos de coragem e 3 pontos de proximidade ao longo do jogo!\033[m'
              '\nAssim, você cumpriu o seu objetivo!')
        sleep(5)
        print('\nÓtimas escolhas! No quesito conquistar corações, você é PhD!')
        sleep(3)
        print('\nSó não vale tentar seguir esses passos na vida real, ein?')
        sleep(2)
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        agradecimento()
    else:
        #imagem
        janela = pygame.display.set_mode((500, 418))
        perdeu = pygame.image.load('perdeu.png')
        pygame.display.set_caption("Não foi dessa vez :P")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(perdeu, (0, 0))
        pygame.quit()

        print("\033[1;97;41mVocê não acumulou todos os 4 pontos de coragem e 3 de proximidade, escondidos entre as possibilidades do jogo..\033[m"
              "\nEles eram necessários para conquistá-la!")
        sleep(4)
        print('\nEntão, Mônica acabou negando seu pedido... Sinto muito! :(')
        sleep(3)

        #GAME OVER + PLAY AGAIN (6/6)
        #imagem
        pygame.init()
        janela = pygame.display.set_mode((500, 418))
        gameover_geral = pygame.image.load('gameover_geral.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(gameover_geral, (0, 0))
        pygame.quit()

        #tentar novamente
        print('\n\033[4mVocê deseja começar do início e tentar encontrar todos os pontos?\033[m')
        resposta = input('  R: ').lower().strip()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao' and resposta != 'n' and resposta != 's':
            print("\nResponda com\033[1;32m 'sim'\033[m ou\033[1;31m 'não'\033[m! \033[4mTente novamente\033[m:")
            resposta = input(' R: ').lower().strip()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if 's' in resposta:
            comeco_do_jogo()
        else:
            agradecimento()

def agradecimento():
    #imagem agradecimento
    janela = pygame.display.set_mode((500, 418))
    gracias = pygame.image.load('agradecimento.png')
    pygame.display.set_caption("Agradecimento")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(gracias, (0, 0))
    pygame.quit()

comeco_do_jogo()