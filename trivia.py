import random

# Lista de listas no formato [pergunta, primeira alternativa, segunda alternativa, terceira alternativa, quarta alternativa, resposta]
trivia = [
    ["Qual é o maior planeta do sistema solar?", "Marte", "Júpiter", "Vênus", "Saturno", "b"],
    ["Quem escreveu a peça de teatro 'Romeu e Julieta'?", "William Shakespeare", "Charles Dickens", "Jane Austen", "F. Scott Fitzgerald", "a"],
    ["Qual é o metal líquido à temperatura ambiente?", "Ferro", "Ouro", "Mercúrio", "Prata", "c"],
    ["Qual é o rio mais longo do mundo?", "Rio Amazonas", "Rio Nilo", "Rio Mississippi", "Rio Yangtzé", "b"],
    ["Quem pintou a Mona Lisa?", "Michelangelo", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "b"],
    ["Qual é o maior oceano do mundo?", "Oceano Pacífico", "Oceano Índico", "Oceano Atlântico", "Oceano Ártico", "a"],
    ["Qual é a capital do Brasil?", "Brasília", "Rio de Janeiro", "São Paulo", "Salvador", "a"],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams", "a"],
    ["Qual é o elemento químico com símbolo 'H'?", "Hidrogênio", "Hélio", "Háfnio", "Hidrônio", "a"],
    ["Quem escreveu 'O Pequeno Príncipe'?", "J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "Antoine de Saint-Exupéry", "d"],
    ["Qual é o maior deserto do mundo?", "Deserto do Saara", "Deserto de Atacama", "Deserto da Arábia", "Deserto do Kalahari", "a"],
    ["Qual é a montanha mais alta do mundo?", "Monte Everest", "Monte Kilimanjaro", "Monte Fuji", "Monte McKinley (Denali)", "a"],
    ["Quem escreveu 'Harry Potter e a Pedra Filosofal'?", "J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin", "c"],
    ["Qual é a capital da França?", "Paris", "Londres", "Berlim", "Roma", "a"],
    ["Qual é o maior animal terrestre do mundo?", "Elefante Africano", "Girafa", "Rinoceronte Branco", "Urso Polar", "a"]
]

# Função principal que inicializa o Trivia
def iniciarTrivia(number_of_questions):
    score = 0
    if len(trivia) == 0: # Verifica se não há mais perguntas disponíveis para serem sorteadas na lista 'trivia'.
        print('Você zerou o jogo!')
        return
    sorted_questions = random.sample(trivia, number_of_questions) # Sorteia as perguntas da rodada
    for i in sorted_questions:
        print("Pergunta:", i[0])
        print("A:", i[1])
        print("B:", i[2])
        print("C:", i[3])
        print("D:", i[4])
        answer = input('Qual é a sua resposta?').lower()
        while answer not in ['a', 'b', 'c', 'd']:
            print('Insira uma opção válida.')
            answer = input('Qual é a sua resposta?').lower()
        if answer == i[-1]:
            score += 1 # Adiciona 1 à pontuação, caso acerte
            print('Acertou!')
        else:
            print('Errou!')
            if len(trivia) < 15: # Verifica se não é a primeira rodada de perguntas
                print('Game Over!')
                return
    print('Fim de jogo!')
    if score == number_of_questions:
        print(r'Parabéns, você acertou 100% das perguntas!')
        for i in sorted_questions:
            trivia.remove(i)
        iniciarTrivia(number_of_questions)
    else:
        print(f'Você acertou {(score/number_of_questions)*100:,.2f}%')


# Iniciar o jogo
iniciarTrivia(5)
