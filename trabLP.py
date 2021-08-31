import pygame
pygame.init()
janela = pygame.display.set_mode((500, 418))
benvindo = pygame.image.load('benvindo.png')
pygame.display.set_caption("Bem-vindo ao vai dar namoro")
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    pygame.display.update()
    janela.blit(benvindo, (0, 0))
pygame.quit()

def comeco_do_jogo():
    print()
    janela = pygame.display.set_mode((500, 418))
    benvindo = pygame.image.load('benvindo2.png')
    pygame.display.set_caption("Bem-vindo ao vai dar namoro")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(benvindo, (0, 0))
    pygame.quit()
    resposta = input(' R: ').lower()
    while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
        print("\nResponda com 'sim' ou 'não'! Tente novamente:")
        resposta = input(' R: ').lower()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if 's' in resposta:
        introducao()
    else:
        janela = pygame.display.set_mode((500, 418))
        benvindo = pygame.image.load('1°gameover.png')
        pygame.display.set_caption("Que pena :p")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(benvindo, (0, 0))
        pygame.quit()

def introducao():
    print("Imagine que você é apaixonado por Mônica desde os 8 anos de idade, quando ela se mudou para o mesmo bairro que você: podemos dizer que foi amor à primeira vista.")
    print("Porém, vocês nunca conseguiram criar nenhum tipo de relação, já que Mônica começou a namorar bem nova. Mas agora chegou a sua vez... ")
    print("Depois de terminar um longo relacionamento, ela pode viver um novo romance e, quem sabe, você possa ser sortudo e conquistar o coração de seu amor de infância!")
    print("Vamos nessa!")
    print("\nHoje é uma sexta-feira e você está off da faculdade, então resolve fazer algo para relaxar...")
    print("O que você escolhe:")
    print(" 1) Ir andar pelo parque/bairro")
    print(" 2) Maratonar aquela série que você está há tempos planejando assistir")
    resposta = input('  R: ')
    while resposta != '1' and resposta != '2':
        print("\nMas você já vai estragar tudo? Responda com 1 ou 2! Tente novamente:")
        resposta = input('  R: ')
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == '1':
        janela = pygame.display.set_mode((500, 418))
        benvindo = pygame.image.load('encontramonica.png')
        pygame.display.set_caption("Encontrando a Mõnica")
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
        janela = pygame.display.set_mode((500, 418))
        benvindo = pygame.image.load('gameover.png')
        pygame.display.set_caption("Game Over")
        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            pygame.display.update()
            janela.blit(benvindo, (0, 0))
        pygame.quit()
        # GAME OVER + PLAY AGAIN (1/6)
        print('Você deseja tentar essa fase novamente?')
        resposta = input('  R: ')
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if resposta == 'sim':
            introducao()
        else:
            agradecimento()
def item_1():
    pontos_de_proximidade = 0
    pontos_de_coragem = 0
    janela = pygame.display.set_mode((500, 418))
    benvindo = pygame.image.load('itemcelular.png')
    pygame.display.set_caption("itemcelular")
    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        pygame.display.update()
        janela.blit(benvindo, (0, 0))
    pygame.quit()
    print("Você deseja coletar esse item?")
    resposta = input(' R: ').lower()
    while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
        print("\nResponda com 'sim' ou 'não'! Tente novamente:")
        resposta = input(' R: ').lower()
    print(
        '\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'sim':
        print('**VOCÊ DESBLOQUEOU: 1 PONTO DE CORAGEM!!')  # PONTO DE CORAGEM (1/4)
        pontos_de_coragem += 1
        print('Estoque atual:', pontos_de_coragem, 'ponto de coragem e', pontos_de_proximidade, 'pontos de proximidade')
        por_onde_chamar(pontos_de_coragem, pontos_de_proximidade)
    else:
        print('Na manhã seguinte, Mônica posta stories falando sobre o livro que ela acabou de ler!')
        print('Por sorte, você também havia terminado de ler esse livro algum tempo atrás')
        print('Como você não pediu o número dela no dia anterior, sua única opção é responder os stories...')
        print('Vocês começaram a conversar bastante sobre diversos assuntos e resolveram, então, marcar de se encontrar no parque.')
        print('\n**VOCÊ DESBLOQUEOU: 1 PONTO DE PROXIMIDADE!!')  # PONTO DE PROXIMIDADE (1a/3)
        pontos_de_proximidade += 1
        print('Estoque atual:', pontos_de_coragem, 'pontos de coragem e', pontos_de_proximidade, 'ponto de proximidade')
        parque(pontos_de_coragem, pontos_de_proximidade)

def por_onde_chamar(pontos_de_coragem, pontos_de_proximidade):
    print('\nNa manhã seguinte, Mônica posta stories falando sobre o livro que ela acabou de ler!')
    print('Por sorte, você também havia terminado de ler esse livro algum tempo atrás')
    print("Como você coletou o item 'número de celular', você pode escolher entre 2 opções:")
    print(" 1) Responder os stories falando sobre o livro")
    print(" 2) Chamar no whats falando sobre o livro")
    resposta = input('  R: ')
    while resposta != '1' and resposta != '2':
        print("\nResponda com 1 ou 2! Tente novamente:")
        resposta = input('  R: ')
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == '1':
        print('Vocês começaram a conversar bastante sobre diversos assuntos e resolveram, então, marcar de se encontrar no parque.')
        print('\n**VOCÊ DESBLOQUEOU: 1 PONTO DE PROXIMIDADE!!')
        pontos_de_proximidade += 1  # PONTO DE PROXIMIDADE (1b/3)
        print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
        parque(pontos_de_coragem, pontos_de_proximidade)
    else:
        depois_wpp(pontos_de_coragem, pontos_de_proximidade)

def depois_wpp(pontos_de_coragem, pontos_de_proximidade):
    print('WOW, vocês ficaram a noite toda conversando e estão ainda mais próximos!')
    print('\n**VOCÊ DESBLOQUEOU: 1 PONTO DE PROXIMIDADE!!')
    pontos_de_proximidade += 1  # PONTO DE PROXIMIDADE (1c/3)
    print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
    print("\nVocê decide dar um passo adiante e resolve convidá-la para sair.")
    print("Eai, qual vai ser: Parque ou Cinema?")
    resposta = input(' R: ').lower()
    while resposta != 'parque' and resposta != 'cinema':
        print("Responda com 'Parque' ou 'Cinema'! Tente novamente:")
        resposta = input(' R: ').lower()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'parque':
        parque(pontos_de_coragem, pontos_de_proximidade)
    else:
        cinema(pontos_de_coragem, pontos_de_proximidade)

def cinema(pontos_de_coragem, pontos_de_proximidade):
    print('UUUUH, ela topou! Só falta escolher o gênero, vamos de terror ou romance?')
    resposta = input(' R: ').lower()
    while resposta != 'terror' and resposta != 'romance':
        print("Responda com 'Terror' ou 'Romance'! Tente novamente:")
        resposta = input(' R: ').lower()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'romance':
        print('Iih...o filme que vocês assistem lembra o ex namorado dela, ela acha que isso pode ser um sinal e acaba indo embora pensando em voltar com ele :(')
        print('\nGAME OVER')  # GAME OVER + PLAY AGAIN (2/6)
        print('Você deseja tentar essa fase novamente?')
        resposta = input('  R: ')
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if resposta == 'sim':
            cinema(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('O filme de terror deu super certo e vocês ficaram agarradinhos a noite toda.')
        print('\n**VOCÊ DESBLOQUEOU: 1 PONTO DE PROXIMIDADE!!')
        pontos_de_proximidade += 1  # PONTO DE PROXIMIDADE (2/3)
        print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
        print("\nAntes de ir embora, ela te chama para jantar e, obviamente, você aceita. Ficou combinado de ambos se encontrarem amanhã às 20h00 no Olive Garden.")
        encontro_1(pontos_de_coragem, pontos_de_proximidade)

def parque(pontos_de_coragem, pontos_de_proximidade):
    print('Vocês se encontraram no ponto de ônibus e foram caminhando até o parque...')
    print('\nVishh, começou a chover, pensaram em voltar para casa mas acabaram se divertindo na chuva.')
    print('Após esse momento super especial, vocês decidem sair para jantar no próximo dia e combinam de se encontrarem às 20h00 no Oliver Garden.')
    encontro_1(pontos_de_coragem, pontos_de_proximidade)

def encontro_1(pontos_de_coragem, pontos_de_proximidade):
    print('\nTá quase na hora do encontro hein, você vai ir de carro ou uber?')
    resposta = input(' R: ').lower()
    while resposta != 'carro' and resposta != 'uber':
        print("\nResponda com 'carro' ou 'uber'! Tente novamente:")
        resposta = input(' R: ').lower()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'carro':
        print('Caraca, o carro estava ZERADO de gasolina e você teve de parar no posto para abastecer')
        print("Infelizmente acabou demorando muito porque a bomba travou bem na sua vez :(")
        print(
            "Quando chegou ao restaurante já estava meia hora atrasado, e ela tinha ido embora achando que você não viria…")
        print('\nGAME OVER')  # GAME OVER + PLAY AGAIN (3/6)
        print('Você deseja tentar essa fase novamente?')
        resposta = input('  R: ').lower()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if resposta == 'sim':
            encontro_1(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('Você chegou e logo pediu ao garçom a melhor mesa! Mônica chega depois de um tempo e você só consegue pensar em como ela está linda!')
        print('\nQue noite INCRÍVEL! Você percebe que Mônica realmente é a pessoa certa para você!')
        acompanhar(pontos_de_coragem, pontos_de_proximidade)

def acompanhar(pontos_de_coragem, pontos_de_proximidade):
    print("Ela pergunta se você pode acompanha-lá até sua casa.")
    print("Eai, sim ou não?")
    resposta = input(' R: ').lower()
    while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
        print("\nResponda com 'sim' ou 'não'! Tente novamente:")
        resposta = input(' R: ').lower()
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'sim':
        print('**VOCÊ DESBLOQUEOU: +1 PONTO DE PROXIMIDADE!!')  # PONTO DE PROXIMIDADE (3/3)
        pontos_de_proximidade += 1
        print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
        print('\n**ITEM DISPONÍVEL: primeiro beijo.')  # ITEM BEIJO
        print("Ainda está muito cedo para coletar esse item?")
        resposta = input(' R: ').lower()
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if resposta == 'não' or resposta == 'nao':
            print('**VOCÊ DESBLOQUEOU: +1 PONTO DE CORAGEM!!')  # PONTO DE CORAGEM (2/4)
            pontos_de_coragem += 1
            print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade,'ponto(s) de proximidade')
            print('\nCARACA, que beijão de cinema! Você volta saltitando de felicidade para casa.')
            mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)
        else:
            print("Vocês se despedem com um breve abraço e vão embora.")
            mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)
    else:
        print('Você diz que não pode, pois irá para a casa de sua tia.')
        print("Mônica fica um pouco chateada mas compreende.")
        print("Vocês se despedem com um breve abraço e vão embora.")
        mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)

def mandar_mensagem(pontos_de_coragem, pontos_de_proximidade):
    print("\nE agora vem a dúvida... mandar mensagem ou esperar que ela mande?")
    resposta = input(' R: ').lower()
    while resposta != 'mandar mensagem' and resposta != 'esperar':
        print("\nResponda com 'mandar mensagem' ou 'esperar'! Tente novamente:")
        resposta = input(' R: ').lower()
    print(
        '\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'esperar':
        print('Puts! Esperava um pouco mais de atitude! Vacilou ein!.')
        print('\nGAME OVER')  # GAME OVER + PLAY AGAIN (4/6)
        print('Você deseja tentar essa fase novamente?')
        resposta = input('  R: ')
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if resposta == 'sim':
            mandar_mensagem(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('Isso aí! Perfeito! Você está no caminho certo, atitude é fundamental!')
        print('\n**VOCÊ DESBLOQUEOU: +1 PONTO DE CORAGEM!')  # PONTO DE CORAGEM (3/4)
        pontos_de_coragem += 1
        print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade, 'ponto(s) de proximidade')
        apos_encontro(pontos_de_coragem, pontos_de_proximidade)

def apos_encontro(pontos_de_coragem, pontos_de_proximidade):
    print("\nJá faz um tempo que vocês estão nessa, vários rolês, vários encontros, vários momentos! O que você acha de dar um passo a mais?")
    print("O que você acha de chamar ela para vocês conversarem, analisar se os sentimentos estão batendo ou não?")
    print("Vamos lá... se declarar ou deixar rolar?")
    resposta = input(' R: ').lower()
    while resposta != 'se declarar' and resposta != 'deixar rolar':
        print("\nResponda com 'se declarar' ou 'deixa rolar'! Tente novamente:")
        resposta = input(' R: ').lower()
    print(
        '\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta == 'deixar rolar':
        print('Poxa! Estava indo tão bem... era só deixar a insegurança de lado e se jogar no lance!')
        print('\nGAME OVER')  # GAME OVER + PLAY AGAIN (5/6)
        print('Você deseja tentar essa fase novamente?')
        resposta = input('  R: ')
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if resposta == 'sim':
            apos_encontro(pontos_de_coragem, pontos_de_proximidade)
        else:
            agradecimento()
    else:
        print('O tiro foi certeiro! Ela também está na sua, agora é só se empenhar pra não vacilar! ')
        print('\n**VOCÊ DESBLOQUEOU: +1 PONTO DE CORAGEM!')  # PONTO DE CORAGEM (4/4)
        pontos_de_coragem += 1
        print('Estoque atual:', pontos_de_coragem, 'ponto(s) de coragem e', pontos_de_proximidade, 'ponto(s) de proximidade')
        pedido_namoro(pontos_de_coragem, pontos_de_proximidade)

def pedido_namoro(pontos_de_coragem, pontos_de_proximidade):
    print("\nDepois desse momento muito fofo, você decide que está na hora de pedi-la em namoro...")
    print("Chegou o dia! Está tudo perfeito! Você compra um buquê de flores para ela, prepara um jantar M-A-R-A e a chama para sua casa!")
    print("No momento certo, você ajoelha e pede ela em namoro...")
    print("\nEai, ela aceitou ou não?")
    continuar = input("Dê um enter para descobrir!")
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if pontos_de_coragem == 4 and pontos_de_proximidade == 3:
        print("ACEITOUUU!!!!")
        print('\nParabéns! Você conseguiu acumular 4 pontos de coragem e 3 pontos de proximidade ao longo do jogo e assim cumpriu o objetivo!')
        print('Ótimas escolhas! No quesito conquistar corações, você é PhD!')
        print('Só não vale tentar seguir esses passos na vida real, ein?')
        agradecimento()
    else:
        print("Puts! Não foi dessa vez! Você não acumulou todos os 4 pontos de coragem e 3 de proximidade, escondidos entre as possibilidades do jogo, necessários para conquistá-la!")
        print('Então, Mônica acabou negando seu pedido... Sinto muito! :(')
        print("\nGAME OVER")  # GAME OVER + PLAY AGAIN (6/6)
        print('\nVocê deseja começar do início e tentar encontrar todos os pontos?')
        resposta = input('  R: ')
        while resposta != 'sim' and resposta != 'não' and resposta != 'nao':
            print("\nResponda com 'sim' ou 'não'! Tente novamente:")
            resposta = input(' R: ').lower()
        if resposta == 'sim':
            comeco_do_jogo()
        else:
            agradecimento()


def agradecimento():
    print('\nAgradecemos por jogar"Vai dar Namoro"')
    print('Por: Giovanna Ishida, Larissa Morine e Nathalia Andeloce :)))')

comeco_do_jogo()