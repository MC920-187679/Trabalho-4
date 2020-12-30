#!/bin/bash

# monalisa com assinatura
mkdir -p resultados/mona_assin
echo Realizzato da Leonardo da Vinci™ | python3 codificar.py -o resultados/mona_assin/imagem.png imagens/monalisa.png
python3 plano.py -o resultados/mona_assin/plano0.png  resultados/mona_assin/imagem.png
python3 plano.py -o resultados/mona_assin/pl0chb.png -c b resultados/mona_assin/imagem.png
python3 plano.py -o resultados/mona_assin/pl0chg.png -c g resultados/mona_assin/imagem.png
python3 plano.py -o resultados/mona_assin/pl0chr.png -c r resultados/mona_assin/imagem.png

# monalisa com texto curto
mkdir -p resultados/mona_enunc
python3 codificar.py -o resultados/mona_enunc/imagem.png imagens/monalisa.png textos/enunciado.md
python3 plano.py -o resultados/mona_enunc/plano0.png  resultados/mona_enunc/imagem.png
python3 plano.py -o resultados/mona_enunc/pl0chb.png -c b resultados/mona_enunc/imagem.png
python3 plano.py -o resultados/mona_enunc/pl0chg.png -c g resultados/mona_enunc/imagem.png
python3 plano.py -o resultados/mona_enunc/pl0chr.png -c r resultados/mona_enunc/imagem.png

# watch com texto curto
mkdir -p resultados/watch_enunc
python3 codificar.py -o resultados/watch_enunc/imagem.png imagens/watch.png textos/enunciado.md
python3 plano.py -o resultados/watch_enunc/plano0.png  resultados/watch_enunc/imagem.png
python3 plano.py -o resultados/watch_enunc/pl0chb.png -c b resultados/watch_enunc/imagem.png
python3 plano.py -o resultados/watch_enunc/pl0chg.png -c g resultados/watch_enunc/imagem.png
python3 plano.py -o resultados/watch_enunc/pl0chr.png -c r resultados/watch_enunc/imagem.png

# verficação
python3 decodificar.py resultados/mona_assin/imagem.png | diff -q - <(echo Realizzato da Leonardo da Vinci™)
python3 decodificar.py resultados/mona_enunc/imagem.png | diff -q - textos/enunciado.md
python3 decodificar.py resultados/watch_enunc/imagem.png | diff -q - textos/enunciado.md
