<h1 align="center">Daenerys i.a</h1>


<p align="center">
  <img src="assets/preview.gif" alt="Preview" width="900" />
</p>
<br>
<br>

## Sumário

- [Descrição](#Descrição)
- [Instalação](#Instalação)
- [Controles](#Controles)
- [Bibliotecas](#Bibliotecas)
- [FAQ](#FAQ)
- [Contato](#Contato)

## Descrição

Este é o **Daenerys I.A.**, um jogo do tipo _endless runner_ onde o objetivo é acumular a maior quantidade de pontos possível. Aqui, a I.A. controla Daenerys enquanto ela desvia de obstáculos para se manter viva e avançar pelo caminho.

O diferencial do jogo é o uso de um algoritmo genético chamado **NEAT** para controlar os movimentos do personagem. Algoritmos genéticos são uma classe de algoritmos evolutivos que simulam o processo de seleção natural, inspirados na teoria de Darwin. Esses algoritmos utilizam conceitos como crossing over e mutação para "evoluir" cada geração de personagens.

No início do jogo, uma primeira geração de 100 indivíduos é criada para iniciar o processo de aprendizado, buscando desenvolver estratégias para superar os obstáculos com mais eficiência a cada nova geração





## Instalação

1. Clone o repositório.

2. No terminal, vá até o local onde o repositório foi clonado.

3. Para instalar as dependências, crie e ative um ambiente virtual:

    ```bash
    python -m venv venv  # Cria o ambiente virtual
    venv\Scripts\activate  # Ativa o ambiente
    pip install -r requirements.txt  # Instala os requerimentos
    ```

4. Rode o jogo com o comando a seguir:

    ```bash
    python main.py
    ```


## Controles
- Não precisa controlar o jogo, a IA faz isso por você :D

## Bibliotecas

- [pygame](https://www.pygame.org/news)
- [NEAT-Python](https://neat-python.readthedocs.io/en/latest/)

## FAQ
- [O que são algoritmos genéticos?](https://pt.wikipedia.org/wiki/Algoritmo_gen%C3%A9tico)

- [O que é NEAT?](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies)
- [Como aplicar NEAT aos jogos?](https://www.researchgate.net/publication/348007283_AVALIANDO_A_TECNICA_DE_APRENDIZADO_POR_REFORCO_NEAT_QUANDO_APLICADA_A_UMA_REDE_NEURAL_JOGANDO_UM_VIDEOGAME_DE_CONSOLE_DE_8_BITS)


## Contato

Fique à vontade para entrar em conato pelo [Linkedin](www.linkedin.com/in/ronaldo-amorim), se tiver alguma pergunta ou feedback! 
