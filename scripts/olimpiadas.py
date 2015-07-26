#!/usr/bin/python
# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib
import os
import hashlib


def limpa_lixos():
    os.system('find ' + diretorio + ' -name .DS_Store -delete')
    os.system('find ' + diretorio + ' -name ._* -delete')
    os.system('find ' + diretorio + ' -name __MACOSX -delete')


# Seção (Barra) / Categoria (Parque Olímpico) / Videos 
# secão: id/titSecao
# categoria: titCategoria/descCategoria
# video: idVideo/titVideo/descVideo/credVideo/dataVideo


lista = {}
htmls =  u'/Users/lflrocha/Repositorios/ebc.olimpiadas2016/'

naoesportivas = [ 'Não esportivas',[
['Vila Olímpica', 'Descrição',   [
    ['2015-06_0021','Vila Olímpica','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-03_0025','Vila Olímpica','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['IBC/MPC e Hotel de Mídia', 'Descrição',   [
    ['2015-05_0008','IBC/MPC','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0012','IBC/MPC','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],

    ['2015-03_0039','IBC/MPC','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['Infraestrutura viária', 'Descrição',   [
    ['2015-03_0024','Transolímpica','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0042','Transcarioca','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
]]


barra = [ 'Região Barra',[
['Parque Olímpico do Rio', 'Descrição', [  
    ['2015-06_0009','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],

    ['2015-05_0010','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0028','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0029','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0030','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0040','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Arena Olímpica do Rio',  'Descrição', [
    ['2015-03_0032','Arena Olímpica do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Parque Aquático Maria Lenk', 'Descrição',  [
    ['2015-03_0031','Parque Aquático Maria Lenk','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Centro Olímpico de Tênis', 'Descrição',  [
    ['2015-06_0011','Centro Olímpico de Tênis','Quadras secundárias. Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0011','Centro Olímpico de Tênis','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0034','Centro Olímpico de Tênis','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0035','Centro Olímpico de Tênis','Quadras secundárias. Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],


]],

['Estádio Olímpico de Esportes Aquáticos', 'Descrição',  [
    ['2015-06_0012','Estádio Olímpico de Esportes Aquáticos','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],


    ['2015-05_0009','Estádio Olímpico de Esportes Aquáticos','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0038','Estádio Olímpico de Esportes Aquáticos','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],

]],

['Arenas Cariocas', 'Descrição',  [
    ['2015-03_0036','Arenas Cariocas','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],

#['Hall Olímpico', 'Descrição',  [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],

['Arena do Futuro', 'Descrição', [ 
    ['2015-03_0037','Arena do Futuro','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Velódromo Olímpico', 'Descrição',  [
    ['2015-06_0010','Velódromo Olímpico','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],

    ['2015-03_0033','Velódromo Olímpico','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Riocentro', 'Descrição',  [
    ['2015-03_0027','Riocentro','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Campo Olímpico de golfe', 'Descrição',  [
    ['2015-06_0017','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0018','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],


    ['2015-03_0041','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0042','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],

#['Pontal', 'Descrição',  [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],
]]

deodoro = [ 'Região Deodoro',[
['Arena de Rúgbi e Pentatlo Moderno', 'Descrição',   [
    ['2015-06_0005','Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0007','Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-03_0009','Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0010','Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0011','Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['Arena da Juventude', 'Descrição',   [
    ['2015-06_0005','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0007','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0008','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0003','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0005','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0009','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0010','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0011','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0012','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0013','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0016','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['Centro Nacional de Hipismo', 'Descrição',   [
    ['2015-06_0003','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0004','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0007','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0017','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0018','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0019','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0021','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0023','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['Centro Olímpico de Tiro', 'Descrição',   [
    ['2015-06_0016','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0002','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0005','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0006','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0007','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0008','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],

]],
['Centro Aquático do Pentatlo Moderno', 'Descrição',   [
    ['2015-06_0002','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0005','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0007','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0003','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0004','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0006','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0014','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0016','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['Centro Nacional de Hóquei Sobre Grama', 'Descrição',   [
    ['2015-06_0001','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0005','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0007','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0003','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0004','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0005','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0015','Centro Nacional de Hóquei Sobre Grama','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0016','Centro Nacional de Hóquei Sobre Grama','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
['Parque Radical do Rio', 'Descrição',   [
    ['2015-06_0013','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0014','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0015','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0019','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0020','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-05_0001','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-03_0001','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0002','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0003','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0004','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],
]]

copacabana = [ 'Região Copacabana',[
#['Estádio de Copacabana', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],

#['Forte de Copacabana', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],

#['Lagoa Rodrigo de Freitas', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],

#['Marina da Glória', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],
]]

maracana = [ 'Região Maracanã',[
#['Estádio Olímpico João Havelange – Engenhão', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],
#['Estádio Maracanã', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],

#['Ginásio do Maracanãzinho', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],
#['Sambódromo', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],
#['Parque Aquático Julio de Lamare', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#
#]],
]]



sedesfutebol = [ 'Sedes do futebol',[
['Belo Horizonte', 'Descrição',   [
    ['FUT-BH_0001','Estádio Mineirão','Interna / Cam Tilt e Pan no final do take / Aberta / Foco / teto da cobertura do estádio e torcedores vibrando','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-BH_0002','Estádio Mineirão','Interna / Cam Pan ida e volta / Aberta / Foco / Teto da cobertura do estádio e torcedores vibrando','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-BH_0003','Estádio Mineirão','Interna / Cam Pan / Aberta / Foco / Grande plano aberto mostra telão, gramado e arquibancadas com torcedores','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-BH_0004','Estádio Mineirão','Interna / Cam Fixa e sutil Pan no final do take / Aberta / Foco / Teto da cobertura do estádio e torcedores','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-BH_0005','Estádio Mineirão','Interna / Cam Pan / Aberta / Foco / Fogos de artifícios na abertura do teto do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-BH_0006','Estádio Mineirão','Interna / Cam Fixa / Aberta / Foco / Fogos de artifícios na abertura do teto do estádio, parte da cobertura e telão ao fundo','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-BH_0007','Estádio Mineirão','Externa / Cam Pan e rápido zoom de aproximação no final/ Aberta / Foco / estrutura superior do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],
['Brasília', 'Descrição',   [
    ['FUT-BSB_0001','Estádio Nacional Mané Garrincha','Interna / Cam Fixa com zoom / Fechado e Aberta / Foco / Colunas, cobertura e parte das arquibancadas','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0002','Estádio Nacional Mané Garrincha','Interna / Cam Pan / Aberta / Foco / Pequena parte do gramado, arquibancadas e cobertura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0003','Estádio Nacional Mané Garrincha','Interna / Cam Pan ida e volta / Aberta / Foco / Arquibancadas vazias e teto da cobertura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0004','Estádio Nacional Mané Garrincha','Interna / Cam Pan ida e volta / Aberta / Foco / Arquibancadas vazias, teto da cobertura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0005','Estádio Nacional Mané Garrincha','Externa / Cam Pan ida e volta / Aberta / Foco / Estrutura completa do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0006','Estádio Nacional Mané Garrincha','Externa / Cam Pan ida e volta / Aberta / Foco / Parte das arquibancadas, das colunas e vidraças do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0007','Estádio Nacional Mané Garrincha','Externa / Cam Pan com suave inclinação circular / Aberta / Foco / Colunas do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0008','Estádio Nacional Mané Garrincha','Interna / Cam Pan discreto / Aberta / Foco / Pequena parte do gramado, arquibancadas e cobertura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0009','Estádio Nacional Mané Garrincha','Interna / Cam com zoom de distanciamento e aproximação / Aberta / Foco / estrutura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-BSB_0010','Estádio Nacional Mané Garrincha','Interna / Cam com zoom de distanciamento e leve Tilt no final / Aberta / Foco / estrutura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
]],
['Manaus', 'Descrição',   [
    ['FUT-MAN_0001','Arena da Amazônia','Interna / Cam Fixa com efeito de aceleração / Aberta / Foco / Gramado, arquibancadas e teto da cobertura do estádio na parte mais superior do enquadramento inclusive o céu, enquanto trabalhadores movimentam-se rapidamente','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0002','Arena da Amazônia','Interna / Cam Tilt / Aberta / Foco / Arquibancadas e teto da cobertura do estádio na parte mais superior do enquadramento inclusive o céu','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0003','Arena da Amazônia','Interna / Cam Fixa com zoom de distanciamento e aproximação / Aberta / Foco / Teto do estádio com holofotes abre até mostrar toda a estrutura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0004','Arena da Amazônia','Externa / Cam Pan ida e volta / Aberta / Foco / Parte da cidade até mostrar a estrutura arredondada do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0005','Arena da Amazônia','Interna / Cam Pan ida e volta / Aberta / Foco / Parte das arquibancadas com as cadeiras e o teto/cobertura, depois com o movimento mostra o resto do estádio com o gramado e o céu aparecendo','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0006','Arena da Amazônia','Interna / Cam Tilt várias vezes / Aberta / Foco / Céu, depois arquibancadas, teto da cobertura e o restante da estrutura do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0007','Arena da Amazônia','Interna / Cam Pan ida e volta / Semi-aberta / Foco / Teto-cobertura e parte das arquibancadas superiores, ao passar mostra telão e com leve inclinação aparece holofotes e o céu ','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0008','Arena da Amazônia','Interna / Cam Tilt várias vezes / Aberta / Foco / Holofotes e estrutura do teto, depois arquibancadas do estádio até ficar nítido as cadeiras','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0009','Arena da Amazônia','Externa / Cam Pan ida e volta / Aberta / Foco / Ênfase na estrutura arredondada do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['FUT-MAN_0010','Arena da Amazônia','Externa / Cam Fixa / Semi-aberta / Foco e desfocada no início / Ênfase nos gomos da estrutura arredondada do estádio','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],
#['Salvador', 'Descrição',   [
#    ['2015-03_0000','Título','Descrição','Ministério do Esporte do Brasil'],
#]],
['São Paulo', 'Descrição',   [
    ['FUT-SAO_0001','Arena Corinthians','Interna / Cam Fixa / Aberta / Foco / Gramado e arquibancadas dividem a tela meio-a-meio','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-SAO_0002','Arena Corinthians','Interna / Cam Fixa / Aberta / Foco / Gramado, arquibancadas e teto-cobertura, com partes do céu nublado aparecendo nas bordas do enquadramento tendo o telão em uma delas','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-SAO_0003','Arena Corinthians','Interna / Cam Tilt / Aberta / Foco / Céu nublado, depois toda a estrutura do estádio com teto, arquibancadas e gramado ','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-SAO_0004','Arena Corinthians','Interna / Cam Pan / Aberta / Foco / Cadeiras das arquibancadas, gramado, teto-cobertura e no final do movimento o telão','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
    ['FUT-SAO_0005','Arena Corinthians','Interna / Cam Pan / Aberta / Foco / Gramado e arquibancadas, no final do movimento o telão','Ministério do Esporte do Brasil/EBC Serviços','Maio/2014'],
]],
]]


rio = [ 'Rio de Janeiro',[

['Aéreas', 'Descrição',   [
    ['RIO_0046','Rio de Janeiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2014'],
    ['RIO_0047','Rio de Janeiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2014'],
]],


['Praias', 'Descrição',   [
    ['RIO_0068','Rio de Janeiro - Praias','Plano geral. Mar.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0069','Rio de Janeiro - Praias','Plano geral. Mar. Prédios.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0070','Rio de Janeiro - Praias','Plano geral. Calçadão. Vendedor ambulante.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0071','Rio de Janeiro - Praias','Plano geral. Ciclovia. Pessoas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0072','Rio de Janeiro - Praias','Plano geral. Ciclovia. Pessoas caminhando.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0073','Rio de Janeiro - Praias','Contra-plongée. Ciclovia. Ciclistas','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0074','Rio de Janeiro - Praias','Traveling lateral. Praia. Ciclistas. Surfistas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0075','Rio de Janeiro - Praias','Plano aberto. Praia. Futvolei. ','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0076','Rio de Janeiro - Praias','Traveling lateral. Praia. Futvolei.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0077','Rio de Janeiro - Praias','Contra-plongée. Futvolei.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0079','Rio de Janeiro - Praias','Plano geral. Praia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0080','Rio de Janeiro - Praias','Plano geral. Ciclovia. Calçadão.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0081','Rio de Janeiro - Praias','Plano médio. Praia. Futebol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0082','Rio de Janeiro - Praias','Plano médio. Praia. Futebol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0083','Rio de Janeiro - Praias','Plano aberto. Praia. Futebol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0084','Rio de Janeiro - Praias','Plano aberto. Praia. Futebol. Por do sol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0085','Rio de Janeiro - Praias','Plano aberto. Praia. Futebol. Por do sol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],

['Aeroporto', 'Descrição',   [
    ['RIO_0001','Rio de Janeiro - Aeroporto','Plano aberto. Guiches. Aeroporto.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0002','Rio de Janeiro - Aeroporto','Pan. Aeroporto. Noite.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0003','Rio de Janeiro - Aeroporto','Desfoque. Aeroporto. Noite.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0004','Rio de Janeiro - Aeroporto','Desfoque. Aeroporto. Check-in.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0006','Rio de Janeiro - Aeroporto','Pan. Aeroporto. Check-in.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0008','Rio de Janeiro - Aeroporto','Carrinho elétrico. Aeroporto.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0010','Rio de Janeiro - Aeroporto','Traveling. Transporte. Aeroporto','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0011','Rio de Janeiro - Aeroporto','Traveling. Esteira rolante. Aeroporto','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],

['Centro', 'Descrição',   [
    ['RIO_0018','Rio de Janeiro - Centro','Timelapse. Theatro Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0019','Rio de Janeiro - Centro','Timelapse. Câmara Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0020','Rio de Janeiro - Centro','Plano aberto. Fachada. Theatro Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0021','Rio de Janeiro - Centro','Contra-plongée. Traveling. Fachada. Theatro Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0022','Rio de Janeiro - Centro','Plano geral. Fachada. Biblioteca Nacional.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0024','Rio de Janeiro - Centro','Plano geral. Fachada. Câmara Municipal','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],

]],

['Jardim Botânico', 'Descrição',   [
    ['RIO_0052','Rio de Janeiro - Jardim Botânico','Plano geral. Lagoa. Vitória régia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0053','Rio de Janeiro - Jardim Botânico','Plano geral. Lagoa. Vitória régia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0054','Rio de Janeiro - Jardim Botânico','Close. Flor. Vitória régia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0055','Rio de Janeiro - Jardim Botânico','Pan-Tilt. Vitória régia','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0056','Rio de Janeiro - Jardim Botânico','Plano aberto. Casal. Escadaria.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0057','Rio de Janeiro - Jardim Botânico','Tilt down em diagonal. Chafariz. Natureza.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0058','Rio de Janeiro - Jardim Botânico','Tilt. Palmeiras.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0059','Rio de Janeiro - Jardim Botânico','Tilt. Caminho. ','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0060','Rio de Janeiro - Jardim Botânico','Pan. Natureza.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],

['Feira de São Cristóvão', 'Descrição',   [
    ['RIO_0032','Rio de Janeiro - Feira de São Cristóvão','Time-lapse. Pessoas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0033','Rio de Janeiro - Feira de São Cristóvão','Plano aberto. Repentistas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0034','Rio de Janeiro - Feira de São Cristóvão','Plano aberto. Show.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0036','Rio de Janeiro - Feira de São Cristóvão','Tilt. Pessoas','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0037','Rio de Janeiro - Feira de São Cristóvão','Portait. Vendedor de cordel.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0044','Rio de Janeiro - Feira de São Cristóvão','Close. Boneco.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0045','Rio de Janeiro - Feira de São Cristóvão','Pan. Lembranças do Rio de Janeiro.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],
['Escadaria da Lapa', 'Descrição',   [
    ['RIO_0026','Rio de Janeiro - Escadaria da Lapa','Time lapse. Pessoas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0027','Rio de Janeiro - Escadaria da Lapa','Close. Degrau.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0028','Rio de Janeiro - Escadaria da Lapa','Close. Degrau.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0029','Rio de Janeiro - Escadaria da Lapa','Portrait. Casal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0030','Rio de Janeiro - Escadaria da Lapa','Portrait. Mulher.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0031','Rio de Janeiro - Escadaria da Lapa','Portrait. Mulher.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],

]]


data = [ 'Por data',[

['Junho de 2015', 'Descrição',   [
    ['2015-06_0001','Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0002','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0003','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0004','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0005','Arena da Juventude, Centro Nacional de Hóquei Sobre Grama e Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0007','Arena da Juventude, Centro Nacional de Hóquei Sobre Grama e Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0008','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0009','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0010','Velódromo Olímpico','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0011','Centro Olímpico de Tênis','Quadras secundárias. Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0012','Estádio Olímpico de Esportes Aquáticos','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0013','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0014','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0015','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0016','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0017','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0018','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0019','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0020','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Junho/2015'],
    ['2015-06_0021','Vila Olímpica','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Junho/2015'],
]],

['Maio de 2015', 'Descrição',   [
    ['2015-05_0001','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0002','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0003','Arena da Juventude, Centro Nacional de Hóquei Sobre Grama e Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0004','Centro Nacional de Hóquei Sobre Grama e Centro Aquático do Pentatlo Moderno','Imagem aérea','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0005','Arena da Juventude e Centro Nacional de Hóquei Sobre Grama','Imagem aérea','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0006','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0007','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0008','Hotel de Mídia e IBC/MPC','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0009','Estádio Olímpico de Esportes Aquáticos','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0010','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0011','Centro Olímpico de Tênis','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
    ['2015-05_0012','IBC/MPC','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Maio/2015'],
]],


['Abril de 2015', 'Descrição',   [
    ['2015-03_0001','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0002','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0003','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0004','Parque Radical do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0005','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0006','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0007','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0008','Centro Olímpico de Tiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0009','Arena da Juventude e Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0010','Arena da Juventude e Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0011','Arena da Juventude e Arena de Rúgbi e Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0012','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0013','Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0014','Centro Aquático do Pentatlo Moderno','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0015','Centro Nacional de Hóquei Sobre Grama','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0016','Centro Nacional de Hóquei Sobre Grama, Centro Aquático do Pentatlo Moderno e Arena da Juventude','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0017','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0018','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0019','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0021','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0023','Centro Nacional de Hipismo','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0024','Transolímpica','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0025','Vila Olímpica','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0027','Riocentro','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0028','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0029','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0030','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0031','Parque Aquático Maria Lenk','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0032','Arena Olímpica do Rio','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0033','Velódromo Olímpico','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0034','Estádio Olímpico de Esportes Aquáticos','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0035','Centro Olímpico de Tênis','Quadras secundárias. Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0036','Arenas Cariocas','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0037','Arena do Futuro','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0038','Estádio Olímpico de Esportes Aquáticos','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0039','IBC/MPC','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0040','Parque Olímpico do Rio','Imagem aérea. Obras.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0041','Campo Olímpico de golfe','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
    ['2015-03_0042','Campo Olímpico de golfe e via Transcarioca','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2015'],
]],

['Abril de 2014', 'Descrição',   [
    ['RIO_0046','Rio de Janeiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2014'],
    ['RIO_0047','Rio de Janeiro','Imagem aérea.','Ministério do Esporte do Brasil','Abril/2014'],
    ['RIO_0068','Rio de Janeiro - Praias','Plano geral. Mar.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0069','Rio de Janeiro - Praias','Plano geral. Mar. Prédios.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0070','Rio de Janeiro - Praias','Plano geral. Calçadão. Vendedor ambulante.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0071','Rio de Janeiro - Praias','Plano geral. Ciclovia. Pessoas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0072','Rio de Janeiro - Praias','Plano geral. Ciclovia. Pessoas caminhando.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0073','Rio de Janeiro - Praias','Contra-plongée. Ciclovia. Ciclistas','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0074','Rio de Janeiro - Praias','Traveling lateral. Praia. Ciclistas. Surfistas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0075','Rio de Janeiro - Praias','Plano aberto. Praia. Futvolei. ','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0076','Rio de Janeiro - Praias','Traveling lateral. Praia. Futvolei.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0077','Rio de Janeiro - Praias','Contra-plongée. Futvolei.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0079','Rio de Janeiro - Praias','Plano geral. Praia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0080','Rio de Janeiro - Praias','Plano geral. Ciclovia. Calçadão.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0081','Rio de Janeiro - Praias','Plano médio. Praia. Futebol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0082','Rio de Janeiro - Praias','Plano médio. Praia. Futebol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0083','Rio de Janeiro - Praias','Plano aberto. Praia. Futebol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0084','Rio de Janeiro - Praias','Plano aberto. Praia. Futebol. Por do sol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0085','Rio de Janeiro - Praias','Plano aberto. Praia. Futebol. Por do sol.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0001','Rio de Janeiro - Aeroporto','Plano aberto. Guiches. Aeroporto.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0002','Rio de Janeiro - Aeroporto','Pan. Aeroporto. Noite.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0003','Rio de Janeiro - Aeroporto','Desfoque. Aeroporto. Noite.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0004','Rio de Janeiro - Aeroporto','Desfoque. Aeroporto. Check-in.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0006','Rio de Janeiro - Aeroporto','Pan. Aeroporto. Check-in.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0008','Rio de Janeiro - Aeroporto','Carrinho elétrico. Aeroporto.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0010','Rio de Janeiro - Aeroporto','Traveling. Transporte. Aeroporto','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0011','Rio de Janeiro - Aeroporto','Traveling. Esteira rolante. Aeroporto','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0018','Rio de Janeiro - Centro','Timelapse. Theatro Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0019','Rio de Janeiro - Centro','Timelapse. Câmara Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0020','Rio de Janeiro - Centro','Plano aberto. Fachada. Theatro Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0021','Rio de Janeiro - Centro','Contra-plongée. Traveling. Fachada. Theatro Municipal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0022','Rio de Janeiro - Centro','Plano geral. Fachada. Biblioteca Nacional.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0024','Rio de Janeiro - Centro','Plano geral. Fachada. Câmara Municipal','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0052','Rio de Janeiro - Jardim Botânico','Plano geral. Lagoa. Vitória régia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0053','Rio de Janeiro - Jardim Botânico','Plano geral. Lagoa. Vitória régia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0054','Rio de Janeiro - Jardim Botânico','Close. Flor. Vitória régia.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0055','Rio de Janeiro - Jardim Botânico','Pan-Tilt. Vitória régia','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0056','Rio de Janeiro - Jardim Botânico','Plano aberto. Casal. Escadaria.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0057','Rio de Janeiro - Jardim Botânico','Tilt down em diagonal. Chafariz. Natureza.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0058','Rio de Janeiro - Jardim Botânico','Tilt. Palmeiras.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0059','Rio de Janeiro - Jardim Botânico','Tilt. Caminho. ','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0060','Rio de Janeiro - Jardim Botânico','Pan. Natureza.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0032','Rio de Janeiro - Feira de São Cristóvão','Time-lapse. Pessoas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0033','Rio de Janeiro - Feira de São Cristóvão','Plano aberto. Repentistas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0034','Rio de Janeiro - Feira de São Cristóvão','Plano aberto. Show.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0036','Rio de Janeiro - Feira de São Cristóvão','Tilt. Pessoas','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0037','Rio de Janeiro - Feira de São Cristóvão','Portait. Vendedor de cordel.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0044','Rio de Janeiro - Feira de São Cristóvão','Close. Boneco.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0045','Rio de Janeiro - Feira de São Cristóvão','Pan. Lembranças do Rio de Janeiro.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0026','Rio de Janeiro - Escadaria da Lapa','Time lapse. Pessoas.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0027','Rio de Janeiro - Escadaria da Lapa','Close. Degrau.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0028','Rio de Janeiro - Escadaria da Lapa','Close. Degrau.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0029','Rio de Janeiro - Escadaria da Lapa','Portrait. Casal.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0030','Rio de Janeiro - Escadaria da Lapa','Portrait. Mulher.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
    ['RIO_0031','Rio de Janeiro - Escadaria da Lapa','Portrait. Mulher.','Ministério do Esporte do Brasil/EBC Serviços','Abril/2014'],
]],
]]

lista = { 'inst_naoesportivas': naoesportivas,
          'inst_barra': barra,
          'inst_deodoro': deodoro,
#          'inst_copacabana': copacabana,
#          'inst_maracana': maracana,
          'inst_sedesfutebol': sedesfutebol,
          'rio': rio,
          'data': data,          
}


def geraPagina(secao):
            
#    f = open(htmls+secao+'.html', 'r+')

    aux = lista[secao]

    idSecao = secao
    titSecao = aux[0]
    categorias = aux[1]

    linMeio = []
    
    linMeio.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
    linMeio.append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
    linMeio.append('<head>\n')
    linMeio.append('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n')
    linMeio.append('<title>Brasil 2016 - BANCO DE IMAGENS</title>\n')
    linMeio.append('<meta name="description" content="Brasil 2016 - BANCO DE IMAGENS">\n')
    linMeio.append('<link rel="shortcut icon" href="_images/fav_icon.ico" type="image/png" />\n')
    linMeio.append('<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Lato:400,700,900,400italic,700italic,900italic" type="text/css">\n')
    linMeio.append('<link rel="stylesheet" href="css/estilo.css">\n')
    linMeio.append('<link rel="stylesheet" href="css/jquery.remodal.css">\n')
    linMeio.append('<link rel="stylesheet" href="css/smoothness/jquery-ui-1.10.4.custom.css">\n')
    linMeio.append('<link rel="stylesheet" href="build/mediaelementplayer.min.css" />\n')
    linMeio.append('<script src="js/jquery-1.10.2.js"></script>\n')
    linMeio.append('<script src="js/jquery-ui-1.10.4.custom.min.js"></script>\n')
    linMeio.append('<script src="js/jPages.min.js" type="text/javascript"></script>\n')
    linMeio.append('<script src="build/mediaelement-and-player.min.js"></script>\n')
    linMeio.append('<script>document.getElementById("#menu").style.zIndex = "1000000";</script>\n')
    linMeio.append('<script>\n')
    linMeio.append('$(document).ready(function () {\n')

    for num in range(len(categorias)):
        linMeio.append('$("div#holder' + str(num) + '").jPages({\n')
        linMeio.append('containerID: "itemContainer' +  str(num) + '",\n')
        linMeio.append('perPage: 8,\n')
        linMeio.append('keyBrowse: true,\n')
        linMeio.append('scrollBrowse: false\n')
        linMeio.append('});\n')

    linMeio.append('$(".loading").hide();')
    linMeio.append('});\n')
    linMeio.append('</script>\n')
    linMeio.append('<script>\n')
    linMeio.append('$(function() {\n')
    linMeio.append('$( "#accordion" ).accordion({heightStyle: "content"});\n')
    linMeio.append('$( "#dialog-link, #icons li" ).hover(\n')
    linMeio.append('function() {\n')
    linMeio.append('$( this ).addClass( "ui-state-hover" );\n')
    linMeio.append('},\n')
    linMeio.append('function() {\n')
    linMeio.append('$( this ).removeClass( "ui-state-hover" );\n')
    linMeio.append('}\n')
    linMeio.append(');\n')
    linMeio.append('$("#accordion").css({"visibility":"visible"});\n')      
    linMeio.append('});\n')
    linMeio.append('</script>\n')
    linMeio.append('</head>\n')
    linMeio.append('<body>\n')
    linMeio.append('<div id="barra-brasil" style="background:#7F7F7F; height: 20px; padding:0 0 0 10px;display:block;">\n')
    linMeio.append('<ul id="menu-barra-temp" style="list-style:none;">\n')
    linMeio.append('<li style="display:inline; float:left;padding-right:10px; margin-right:10px; border-right:1px solid #EDEDED"><a href="http://brasil.gov.br" style="font-family:sans,sans-serif; text-decoration:none; color:white;">Portal do Governo Brasileiro</a></li>\n')
    linMeio.append('<li><a style="font-family:sans,sans-serif; text-decoration:none; color:white;" href="http://epwg.governoeletronico.gov.br/barra/atualize.html">Atualize sua Barra de Governo</a></li>\n')
    linMeio.append('</ul>\n')
    linMeio.append('</div>\n')
    linMeio.append('<div id="wrapper" class="remodal-bg">\n')
    linMeio.append('<div id="topo">\n')
    linMeio.append('<a href="http://brasil2016.gov.br" target="_blank"><img id="logo" src="_images/brasil2016-logo.png" alt="Brasil 2014 - A Copa das Copas"/></a>\n')
    linMeio.append('<div id="topoIcones">\n')
    linMeio.append('<ul>\n')
    linMeio.append('<li><a href="https://www.facebook.com/brasilgov2016" target="_blank"><img src="_images/icone-facebook.png" alt="Facebook" /></a></li>\n')
    linMeio.append('<li><a href="https://twitter.com/brasil2016" target="_blank"><img src="_images/icone-twitter.png" alt="Twitter" /></a></li>\n')
    linMeio.append('<li><a href="http://instagram.com/2016brasil" target="_blank"><img src="_images/icone-instagram.png" alt="Instagram" /></a></li>\n')
    linMeio.append('<li><a href="http://www.youtube.com/brasil2016" target="_blank"><img src="_images/icone-youtube.png" alt="Youtube" /></a></li>\n')
    linMeio.append('<li><a href="https://plus.google.com/+Brasil2016/posts" target="_blank"><img src="_images/icone-google.png"/></a></li>\n')
    linMeio.append('<li><a href="http://www.flickr.com/photos/ministeriodoesporte" target="_blank"><img src="_images/icone-flickr.png" alt="Flickr" /></a></li>\n')
    linMeio.append('</ul>\n')
    linMeio.append('<ul id="idioma">\n')
    linMeio.append('<li><a class="portugues verde" href="">PT</a></li>\n')
    linMeio.append('<li><a class="ingles verde" href="">EN</a></li>\n')
    linMeio.append('</ul>\n')
    linMeio.append('</div>\n')
    linMeio.append('<a href="index.html"><img id="bancoDeImagens" src="_images/banco-de-imagens.png" alt="Banco de Imagens"/></a>\n')
    linMeio.append('<div id="datasJogos">\n')
    linMeio.append('5 a 21 de Agosto 2016<br><span class="verde">Jogos Olímpicos</span><br><br>\n')
    linMeio.append('7 a 18 de Setembro 2016<br><span class="amarelo">Jogos Paralímpicos</span>\n')
    linMeio.append('</div>\n')
    linMeio.append('</div>\n')
    linMeio.append('<ul id="menu">\n')
    linMeio.append('<li class="btPrincipal selected"><a  href="#">INSTALAÇÕES</a>\n')
    linMeio.append('<div class="dropdown_2columns">\n')
    linMeio.append('<ol class="col_1">\n')
    linMeio.append('<li>Competição\n')
    linMeio.append('<ol>\n')
    linMeio.append('<li><a href="inst_barra.html">Região Barra</a></li>\n')
    linMeio.append('<li><a href="inst_deodoro.html">Região Deodoro</a></li>\n')
#    linMeio.append('<li><a href="#"class="desativado">Região Copacabana<br>(em breve)</a></li>\n')
#    linMeio.append('<li><a href="#"class="desativado">Região Maracanã<br>(em breve)</a></li>\n')
    linMeio.append('<li><a href="inst_sedesfutebol.html">Sedes do futebol</a></li>\n')
    linMeio.append('</ol>\n')
    linMeio.append('</li>\n')
    linMeio.append('</ol>\n')
    linMeio.append('<ol class="col_1">\n')
    linMeio.append('<li class="col_1"><a href="inst_naoesportivas.html">Não esportivas</a></li>\n')
    linMeio.append('</ol>\n')
    linMeio.append('</div>\n')
    linMeio.append('</li>\n')
    linMeio.append('<li class="btPrincipal riodejaneiro"><a href="rio.html">RIO DE JANEIRO</a></li>\n')
    linMeio.append('<li class="btPrincipal pordata"><a href="data.html">POR DATA</a></li>\n')
    linMeio.append('</ul>\n')



    linMeio.append('<div class="internabgAzul">\n')
    linMeio.append('<p class="tituloInterna">' + titSecao + '</p>\n')
    linMeio.append('<div class="loading"><img src="_images/ajax-loader.gif"/><br>Carregando</div>\n')
    linMeio.append('<div id="accordion"  class="paginacao">\n')

    contador = 0
    for categoria in categorias:

        titCategoria  = categoria[0]
        descCategoria = categoria[1]
        videos = categoria[2]

        linMeio.append('<h3>'+ categoria[0] +'</h3>\n')
        linMeio.append('<div>\n')
        linMeio.append('<ul id="itemContainer'+str(contador)+'">\n')

        subCont = 0

        for video in videos:

            idVideo = video[0]
            titVideo = video[1]
            descVideo = video[2]
            credVideo = video[3]
            dataVideo = video[4]

            linMeio.append('<li>\n')
            linMeio.append('<a href="#modal-'+secao+'_'+str(contador)+'_'+str(subCont)+'"><img src="_thumb/' + idVideo + '.png"/>\n')
#           linMeio.append('<p><span>Abril/2015<br></span>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.</p></a>')
            linMeio.append('<p><span>' + dataVideo + '</span></p></a>\n')
            linMeio.append('<a href="http://videosolimpiadas2016.planalto.gov.br/'+  video[0] +'.mp4" download')
            linMeio.append(''' onClick="ga('send', 'event', \''''+ secao +'''\', 'click', \''''+ idVideo +'''\')" ''')
            linMeio.append('><img src="_images/botaodownload.png" alt="Download"/></a>\n')
            linMeio.append('</li>\n')
            subCont = subCont + 1

        linMeio.append('</ul>\n')
        linMeio.append('<div class="holder" id="holder'+str(contador)+'"> </div>\n')
        linMeio.append('</div>\n')
        contador = contador + 1

    linMeio.append('</div>\n')
    linMeio.append('</div>\n')
    linMeio.append('</div>\n')

    linMeio.append('<div id="rodape">')
    linMeio.append('<div id="acesseTambem">')
    linMeio.append('<h2>Acesse também</h2>')
    linMeio.append('<ul>')
    linMeio.append('<li><a href="http://www.esporte.gov.br/" title="Ministério do Esporte" target="_blank"><img src="_images/logo-min-esporte.png" alt="" width="65" height="auto"></a></li>')
    linMeio.append('<li><a href="http://www.apo.gov.br" title="Autoridade Pública Olímpica " target="_blank"><img src="_images/logo-apo.png" alt="" width="65" height="65"></a></li>')
    linMeio.append('<li><a href="http://www.cob.org.br/" title="COB " target="_blank"><img src="_images/logo-cob.png" alt="" width="65" height="auto"></a></li>')
    linMeio.append('<li><a href="http://www.cpb.org.br/" title="CPB " target="_blank"><img src="_images/logo-cpb.png" alt="" width="65" height="auto"></a></li>')
    linMeio.append('<li><a href="http://www.rio2016.com/" title="Rio 2016 " target="_blank"><img  src="_images/logo-rio2016.png" alt="" width="65" height="65"></a></li>')
    linMeio.append('<li><a href="http://www.olympic.org/ioc" title="COI " target="_blank"><img  src="_images/logo-coi.png" alt="" width="65" height="auto"></a></li>')
    linMeio.append('<li><a href="http://www.paralympic.org/" title="IPC " target="_blank"><img  src="_images/logo-paralympic.png" alt="" width="65" height="auto"></a></li>')
    linMeio.append('<li><a href="http://www.cidadeolimpica.com.br/" title="Cidade Olímpica " target="_blank"><img  src="_images/logo-cidade-olimpica.png" alt="" width="65" height="65"></a></li>')
    linMeio.append('<li><a href="http://www.copa2014.gov.br" title="Portal da Copa " target="_blank"><img src="_images/logo-portal-da-copa.png" alt="" width="65" height="65"></a></li>')
    linMeio.append('<li><a href="http://www.portaldatransparencia.gov.br" title="Portal da Transparência " target="_blank"><img src="_images/logo-portal-transparencia.png" alt="" width="65" height="65"></a></li>')
    linMeio.append('</ul>')
    linMeio.append('</div>')
    linMeio.append('<div id="copywrite">&#169; 2015 - Todos os direitos reservados.</div>')
    linMeio.append('</div>\n')


                  


    contador = 0
    
    for categoria in categorias:

        titCategoria  = categoria[0]
        descCategoria = categoria[1]
        videos = categoria[2]


        subCont = 0
        
        for video in videos:

            idVideo = video[0]
            titVideo = video[1]
            descVideo = video[2]
            credVideo = video[3]
            dataVideo = video[4]


            linMeio.append('<div class="remodal" data-remodal-id="modal-'+secao+'_'+str(contador)+'_'+str(subCont)+'">\n')
            linMeio.append('<div id="wrapperFancybox">\n')
#            linMeio.append('<p class="tituloFancybox">' + titVideo + '</p>\n')
            linMeio.append('<p class="tituloFancybox">'+ titVideo + '</p>\n')
            linMeio.append('<div class="video-container">\n')
            linMeio.append('<video src="_preview/'  + idVideo + '.mp4" preload="none"  id="' + idVideo + '"></video>\n')
            linMeio.append('<script>$("#' + idVideo + '").mediaelementplayer({defaultVideoWidth: 640, defaultVideoHeight: 360,});</script>\n')
            linMeio.append('</div>\n')
            linMeio.append('<p class="pFancybox">'+ descVideo +'</p>\n')
            linMeio.append('<a href="http://videosolimpiadas2016.planalto.gov.br/'+ idVideo +'.mp4" download><img src="_images/botaodownload.png" alt="Download"/></a>\n')
            linMeio.append('<p class="creditos">'+ credVideo + ' - ' + dataVideo +'</p>\n')
            linMeio.append('</div>\n')
            linMeio.append('</div>\n')
            subCont = subCont + 1

        contador = contador + 1
        


    linMeio.append('<script src="js/jquery.remodal.js"></script>\n')
    linMeio.append('<script>\n')
    linMeio.append('$(document).on("close", ".remodal", function () {\n')
    linMeio.append('$("video").each(function() {\n')
    linMeio.append('$(this)[0].pause();\n')
    linMeio.append('});\n')
    linMeio.append('});\n')
    linMeio.append('</script>\n')
    linMeio.append('<script>\n')
    linMeio.append("(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n")
    linMeio.append('(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n')
    linMeio.append('m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n')
    linMeio.append("})(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n")
    linMeio.append("ga('create', 'UA-7778114-7', 'ebc.com.br');\n")
    linMeio.append("ga('send', 'pageview');\n")
    linMeio.append('</script>\n')
    linMeio.append('<script defer="defer" src="http://barra.brasil.gov.br/barra.js" type="text/javascript"></script>\n')
    linMeio.append('</body>\n')
    linMeio.append('</html>\n')

    f = open(htmls+secao+'.html', 'w')

    for aux in linMeio:
        f.write(aux)
    f.close()

def main():    

    for secao in lista.keys():
#        print a, lista[a]

        geraPagina(secao)

if  __name__ =='__main__':main()
    