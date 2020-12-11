# Trabalho 4

## Especificação do Problema

O objetivo deste trabalho é implementar um algoritmo de esteganografia em imagens digitais.

### Esteganografia

A técnica de esteganografia consiste em ocultar uma mensagem dentro de uma imagem. A mensagem pode ser um texto ou mesmo uma outra imagem.

A esteganografia possui várias aplicações interessantes, tais como a divulgação de mensagens sem o conhecimento de um possível interceptador, a inclusão de marcas para verificação de direitos autorais, entre outras.

Uma técnica comum é a modificação de um ou mais bits que compõem cada pixel da imagem, de modo que a mensagem a ser oculta seja armazenada nesses bits modificados. O bit menos significativo de cada pixel, ou seja, aquele se encontra mais à direita da palavra binária, é conveniente para ser modificado, pois produz alterações na imagem que não são normalmente perceptíveis à visão humana.

Neste trabalho, a esteganografia deve alterar os bits da mensagem a ser oculta nos bits menos significativos de cada um dos três canais de cor da imagem. Dessa forma, cada pixel da imagem pode armazenar 3 bits de informação, tal que a imagem pode comportar três vezes o número de pixels que ela possui.

O diagrama ilustrado na Figura 1 apresenta as principais etapas da esteganografia, em que a mensagem "MC" é oculta em uma imagem colorida por meio da alteração dos bits menos significativos dos pixels da imagem pertencentes a cada canal de cor.

![Ilustração da esteganografia em imagens coloridas.](papers/exemplo.svg "Figura 1")

Implemente a técnica de esteganografia em imagens coloridas por meio da alteração de seus bits menos significativos. O programa deve codificar e decodificar uma mensagem de texto levando-se em conta os bits em qualquer um dos três planos de bits menos significativos.

O processo de codificação deve converter cada caractere da mensagem para sua palavra binária correspondente (código ASCII) e alterar os bits menos significativos da imagem com os bits da mensagem. O processo de decodificação deve recuperar a informaao binária da imagem e gerar a mensagem de texto.

Uma sugestão para execução do programa para o módulo de codificação e decodificação é dada a seguir:

```bash
python codificar.py imagem_entrada.png texto_entrada.txt plano_bits imagem_saida.png
python decodificar.py imagem_saida.png plano_bits texto_saida.txt
```

em que os parâmetros são:

- `codificar.py`: programa que oculta mensagem de texto na imagem.
- `decodificar.py`: programa que recupera mensagem de texto da imagem.
- `imagem_entrada.png`: imagem no formato PNG em que será embutida a mensagem.
- `imagem_saida.png`: imagem no formato PNG com mensagem embutida.
- `texto_entrada.txt`: arquivo-texto contendo mensagem a ser oculta.
- `texto_saida.txt`: arquivo-texto contendo mensagem recuperada.
- `plano_bits`: três planos de bits menos significativos representados pelos valores 0, 1 ou 2.

Para ajudar a determinar se uma imagem contém uma mensagem oculta em seus pixels, mostre os planos de bits (separadamente) 7, 0, 1 e 2 de cada canal de cor (vermelho, verde e azul) da imagem após o processo de esteganografia.

## Entrada de Dados

As imagens de entrada estão no formato PNG (*Portable Network Graphics*). Alguns exemplos encontram-se disponíveis no diretório: [http://www.ic.unicamp.br/~helio/imagens_coloridas/](http://www.ic.unicamp.br/~helio/imagens_coloridas/).

## Saída de Dados

As imagens de saída devem estar no formato PNG (*Portable Network Graphics*). Resultados intermediários podem ser também exibidos na tela.

## Especificação da Entrega

- A entrega do trabalho deve conter os seguintes itens:
    - código fonte: o arquivo final deve estar no formato *zip* ou no formato *tgz*, contendo todos os programas ou dados necessários para sua execução.
    - relatório: deve conter uma descrição dos algoritmos e das estruturas de dados, considerações adotadas na solução do problema, testes executados, eventuais limitações ou situações especiais não tratadas pelo programa.
- O trabalho deve ser submetido por meio da plataforma *Google Classroom*.

## Observações Gerais

- Os programas ser ão executados em ambiente Linux. Os formatos de entrada e saída dos dados devem ser rigorosamente respeitados pelo programa, conforme definidos anteriormente. Não serão aceitos trabalhos após a data de entrega.

- Os seguintes aspectos serão considerados na avaliação: funcionamento da implementação, clareza do código, qualidade do relatório técnico.
