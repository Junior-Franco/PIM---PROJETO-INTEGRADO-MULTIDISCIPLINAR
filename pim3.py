# Lista para guardar dados dos Usuários
nomes = []
senhas = []
notas = []

# Cadastro de 4 alunos
print("       Cadastro de Alunos       ")
i = 0
while i < 4:
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha: ")
    nomes.append(nome)
    senhas.append(senha)
    i = i + 1

# Registro e Login dos alunos
print("      Login e Notas       ")
i = 0
while i < 4:
    nome_login = input("Digite o nome para efetuar login: ")   
    senha_login = input("Digite a senha do aluno: ") 
    achou = 0
    j = 0
    while j < 4:
        if nome_login == nomes[j] and senha_login == senhas[j]:
            print("Login aprovado.")
            nota = float(input("Digite a nota do aluno (0 a 10): "))  
            notas.append(nota)
            achou = 1
            break
        j = j + 1
    if achou == 0:
        print("Login falhou. Nota registrada como 0.") 
        notas.append(0.0)  
    i = i + 1

# ESTATÍSTICAS: MÉDIA, MODA E MEDIANA

# Média
soma = 0
for nota in notas:
    soma += nota
media = soma / 4

# Moda
moda = notas[0]
cont_moda = 0
for i in range(4):
    cont = 0
    for j in range(4):
        if notas[i] == notas[j]:
            cont += 1
    if cont > cont_moda:
        cont_moda = cont
        moda = notas[i]

# Ordem para mediana
notas.sort()

# Mediana
mediana = (notas[1] + notas[2]) / 2

# Resultados
print("    Resultados     ")
print("Notas:", notas[0], notas[1], notas[2], notas[3])
print(f"Média: {media:.2f}")   # <- formatado com 2 casas decimais
print(f"Moda: {moda:.2f}")    
print(f"Mediana: {mediana:.2f}")  