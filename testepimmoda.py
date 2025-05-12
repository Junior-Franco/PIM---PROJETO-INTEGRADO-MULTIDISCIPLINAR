from collections import Counter

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
print("\n      Login e Notas       ")
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

# Moda (versão melhorada com Counter)
contagem = Counter(notas)               # Conta quantas vezes cada nota aparece
mais_comum = contagem.most_common()    # Pega todas as mais comuns

# Verifica se há empate ou se todas as notas são únicas
maior_frequencia = mais_comum[0][1]
modas = [nota for nota, freq in mais_comum if freq == maior_frequencia]

if maior_frequencia == 1:
    moda_resultado = None
else:
    moda_resultado = modas

# Ordem para mediana
notas.sort()

# Mediana (como são 4 alunos, usamos média dos dois valores centrais)
mediana = (notas[1] + notas[2]) / 2

# Resultados
print("\n    Resultados     ")
print("Notas:", notas[0], notas[1], notas[2], notas[3])
print(f"Média: {media:.2f}")

if moda_resultado is None:
    print("Moda: nenhuma (todas as notas são diferentes)")
elif len(moda_resultado) == 1:
    print(f"Moda: {moda_resultado[0]:.2f}")
else:
    print(f"Moda (empate):", ', '.join(f"{m:.2f}" for m in moda_resultado))

print(f"Mediana: {mediana:.2f}")