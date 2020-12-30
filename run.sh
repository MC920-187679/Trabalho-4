#!/bin/bash

# # monalisa com assinatura
# mkdir -p resultados/mona_assin
# echo Realizzato da Leonardo da Vinci™ | python3 codificar.py -o resultados/mona_assin/imagem.png imagens/monalisa.png
# python3 plano.py -o resultados/mona_assin/plano0.png  resultados/mona_assin/imagem.png
# python3 plano.py -o resultados/mona_assin/pl0chb.png -c b resultados/mona_assin/imagem.png
# python3 plano.py -o resultados/mona_assin/pl0chg.png -c g resultados/mona_assin/imagem.png
# python3 plano.py -o resultados/mona_assin/pl0chr.png -c r resultados/mona_assin/imagem.png

# # peppers com texto curto
# mkdir -p resultados/pep_peq
# python3 codificar.py -o resultados/pep_peq/imagem.png imagens/peppers.png textos/enunciado.md
# python3 plano.py -o resultados/pep_peq/plano0.png  resultados/pep_peq/imagem.png
# python3 plano.py -o resultados/pep_peq/pl0chb.png -c b resultados/pep_peq/imagem.png
# python3 plano.py -o resultados/pep_peq/pl0chg.png -c g resultados/pep_peq/imagem.png
# python3 plano.py -o resultados/pep_peq/pl0chr.png -c r resultados/pep_peq/imagem.png

# watch com texto longo
mkdir -p resultados/watch_gran
head -n 28700 textos/words.txt | python3 codificar.py -o resultados/watch_gran/imagem.png imagens/watch.png
python3 plano.py -o resultados/watch_gran/plano0.png  resultados/watch_gran/imagem.png
python3 plano.py -o resultados/watch_gran/pl0chb.png -c b resultados/watch_gran/imagem.png
python3 plano.py -o resultados/watch_gran/pl0chg.png -c g resultados/watch_gran/imagem.png
python3 plano.py -o resultados/watch_gran/pl0chr.png -c r resultados/watch_gran/imagem.png

# verficação
python3 decodificar.py resultados/mona_assin/imagem.png | diff -q - <(echo Realizzato da Leonardo da Vinci™)
python3 decodificar.py resultados/pep_peq/imagem.png | diff -q - textos/enunciado.md
python3 decodificar.py resultados/watch_gran/imagem.png | diff -q - <(head -n 28700 textos/words.txt)
