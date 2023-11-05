nome = str(input('Digite o nome do Herói: '))
xp = float(input('Digite XP do Herói: '))
if xp <1.000:
    print('O Herói de nome {} está no nivel de ferro.'.format(nome))
elif xp >= 1.000 and xp <2.000:
     print('O Herói de nome {} está no nivel de bronze.'.format(nome))
elif xp >=2.000 and xp <5.000:
     print('O Herói de nome {} está no nivel de prata ouro.'.format(nome))
elif xp >=5.000 and xp <8.000:
     print('O Herói de nome {} está no nivel de platina diamante.'.format(nome))
elif xp >=8.000 and xp <9.000:
     print('O Herói de nome {} está no nivel de ascendente.'.format(nome))
elif xp >=9.000 and xp <10.000:
     print('O Herói de nome {} está no nivel de imortal.'.format(nome))
elif xp >=10.000:
     print('O Herói de nome {} está no nivel de radiante.'.format(nome))