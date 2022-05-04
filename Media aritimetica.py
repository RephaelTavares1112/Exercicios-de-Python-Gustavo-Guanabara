# Calculando a media do aluno
pnota = float(input('Primeira nota do aluno: '))
snota = float(input('Segunda nota do aluno: '))

media = (pnota + snota) / 2
print('A media entre {} e {} é igual a {:.1f}'.format(pnota, snota, media))