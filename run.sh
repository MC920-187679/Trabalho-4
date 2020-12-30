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
# mkdir -p resultados/watch_gran
# head -n 28700 textos/words.txt | python3 codificar.py -o resultados/watch_gran/imagem.png imagens/watch.png
# python3 plano.py -o resultados/watch_gran/plano0.png  resultados/watch_gran/imagem.png
# python3 plano.py -o resultados/watch_gran/pl0chb.png -c b resultados/watch_gran/imagem.png
# python3 plano.py -o resultados/watch_gran/pl0chg.png -c g resultados/watch_gran/imagem.png
# python3 plano.py -o resultados/watch_gran/pl0chr.png -c r resultados/watch_gran/imagem.png

# # baboon com texto zipado
# mkdir -p resultados/bab_zip
# zip -9q resultados/bab.zip lib/*.py *.py textos/enunciado.md
# python3 codificar.py -o resultados/bab_zip/imagem.png imagens/baboon.png resultados/bab.zip
# python3 plano.py -o resultados/bab_zip/plano0.png  resultados/bab_zip/imagem.png
# python3 plano.py -o resultados/bab_zip/pl0chb.png -c b resultados/bab_zip/imagem.png
# python3 plano.py -o resultados/bab_zip/pl0chg.png -c g resultados/bab_zip/imagem.png
# python3 plano.py -o resultados/bab_zip/pl0chr.png -c r resultados/bab_zip/imagem.png

# # watch com monalisa
# mkdir -p resultados/watch_mona
# python3 codificar.py -o resultados/watch_mona/imagem.png imagens/watch.png imagens/monalisa.png
# python3 plano.py -o resultados/watch_mona/plano0.png  resultados/watch_mona/imagem.png
# python3 plano.py -o resultados/watch_mona/pl0chb.png -c b resultados/watch_mona/imagem.png
# python3 plano.py -o resultados/watch_mona/pl0chg.png -c g resultados/watch_mona/imagem.png
# python3 plano.py -o resultados/watch_mona/pl0chr.png -c r resultados/watch_mona/imagem.png

# # peppers com permutação
# mkdir -p resultados/pep_perm
# python3 codificar.py -o resultados/pep_perm/imagem.png -p imagens/peppers.png textos/enunciado.md
# python3 plano.py -o resultados/pep_perm/plano0.png  resultados/pep_perm/imagem.png
# python3 plano.py -o resultados/pep_perm/pl0chb.png -c b resultados/pep_perm/imagem.png
# python3 plano.py -o resultados/pep_perm/pl0chg.png -c g resultados/pep_perm/imagem.png
# python3 plano.py -o resultados/pep_perm/pl0chr.png -c r resultados/pep_perm/imagem.png

# # watch com permutação
# mkdir -p resultados/watch_perm
# python3 codificar.py -o resultados/watch_perm/imagem.png -p imagens/watch.png imagens/monalisa.png
# python3 plano.py -o resultados/watch_perm/plano0.png  resultados/watch_perm/imagem.png
# python3 plano.py -o resultados/watch_perm/pl0chb.png -c b resultados/watch_perm/imagem.png
# python3 plano.py -o resultados/watch_perm/pl0chg.png -c g resultados/watch_perm/imagem.png
# python3 plano.py -o resultados/watch_perm/pl0chr.png -c r resultados/watch_perm/imagem.png

# planos diferenciados
mkdir -p resultados/bits
python3 codificar.py -o resultados/bits/mona.png -b 3 imagens/monalisa.png textos/enunciado.md
head -n 5000 textos/words.txt | python3 codificar.py -o resultados/bits/pep.png -b 3 imagens/peppers.png

# verficação
python3 decodificar.py resultados/mona_assin/imagem.png | diff -q - <(echo Realizzato da Leonardo da Vinci™)
python3 decodificar.py resultados/pep_peq/imagem.png | diff -q - textos/enunciado.md
python3 decodificar.py resultados/watch_gran/imagem.png | diff -q - <(head -n 28700 textos/words.txt)
python3 decodificar.py resultados/bab_zip/imagem.png | diff -qb - resultados/bab.zip
python3 decodificar.py resultados/watch_mona/imagem.png | diff -qb - imagens/monalisa.png
python3 decodificar.py resultados/pep_perm/imagem.png | diff -q - textos/enunciado.md
python3 decodificar.py resultados/watch_perm/imagem.png | diff -qb - imagens/monalisa.png
python3 decodificar.py -b 3 resultados/bits/mona.png | diff -q - textos/enunciado.md
python3 decodificar.py -b 3 resultados/bits/pep.png | diff -q - <(head -n 5000 textos/words.txt)
