print('Calculo aritmético\n')
num=0
quant=int(input('Quantos numeros deseja calcular a média? '))
for i in range(quant):
  num+=float(input(f'Digite o {i+1}° número: '))
media=num/quant
print(f'A média aritmética dos numeros é: {media}')