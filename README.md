# Trabalho 4

## Especificação do Problema

O objetivo deste trabalho é aplicar operadores morfológicos para segmentar regiões compreendendo *texto* e *não texto* em uma imagem de entrada.

Os seguintes passos devem ser realizados:

1. dilatação da imagem original com um elemento estruturante de 1 pixel de altura e 100 pixels de largura;
1. erosão da imagem resultante com o mesmo elemento estruturante do passo (1);
1. dilatação da imagem original com um elemento estruturante de 200 pixels de altura e 1 pixel de largura;
1. erosão da imagem resultante com o mesmo elemento estruturante do passo (3);
1. aplicação da intersecção (AND) dos resultados dos passos (2) e (4);
1. fechamento do resultado obtido no passo (5) com um elemento estruturante de 1 pixel de altura e 30 pixels de largura;
1. aplicação de algoritmo para identificação de componentes conexos sobre o resultado do passo (6);
1. para cada retângulo envolvendo um objeto, calcule:
    - razão entre o número de pixels pretos e o número total de pixels (altura x largura);
    - razão entre o número de transições verticais e horizontais *branco para preto* e o número total de pixels pretos;
1. criação de uma regra para classificar cada componente conexo, de acordo com as medidas obtidas no passo (8), como *texto* e *não texto*.
1. aplicação de operadores morfológicos apropriados para segmentar cada linha do texto em blocos de palavras. Coloque um retângulo envolvendo cada palavra na imagem original. Calcule o número total de linhas de texto e de blocos de palavras na imagem.

## Entrada de Dados

As imagens de entrada estão no formato PBM (*Portable Bitmap*).  Um exemplo de imagem pode ser encontrada em [http://www.ic.unicamp.br/~helio/imagens_binarias/](http://www.ic.unicamp.br/~helio/imagens_binarias/).

## Saída de Dados

As imagens de saída, após a aplicação das operações, devem estar no formato PBM (*PortableBitMap*).

## Especificação da Entrega

- A entrega do trabalho deve conter os seguintes itens:
    - código fonte: o arquivo final deve estar no formato *zip* ou no formato *tgz*, contendo todos os programas ou dados necessários para sua execução.
    - relatório: deve conter uma descrição dos algoritmos e das estruturas de dados, considerações adotadas na solução do problema, testes executados, eventuais limitações ou situações especiais não tratadas pelo programa.
- O trabalho deve ser submetido por meio da plataforma *Google Classroom*.

## Observações Gerais

- Os programas ser ão executados em ambiente Linux. Os formatos de entrada e saída dos dados devem ser rigorosamente respeitados pelo programa, conforme definidos anteriormente.

- Os seguintes aspectos serão considerados na avaliação: funcionamento da implementação, clareza do código, qualidade do relatório técnico.
