        #Lista para guardar dados dos usuários
nomes = []
senhas = []
notas = []

#Cadastro de aluno
print("       Cadastro de Alunos       ")
nome = input("Digite o nome do aluno: ")
senha = input("Digite a senha: ")
nomes.append(nome)
senhas.append(senha)

#Registro e Login do aluno
print("\n      Login e Notas       ")

nome_login = input("Digite o nome para efetuar login: ")
senha_login = input("Digite a senha do aluno: ") 

achou = 0

#Verifica se o login está correto
if nome_login in nomes:
    indice = nomes.index(nome_login)
    if senha_login == senhas[indice]:
        print("Login aprovado.")
        achou = 1

        # Solicita notas e calcula média
        qn = int(input("Quantas notas deseja inserir? "))
        if qn > 0:
            soma = 0
            for i in range(qn):
                nota = float(input(f"Digite a nota {i+1}: "))
                soma += nota
                notas.append(nota)
            media = soma / qn
            print(f"A média das notas é: {media:.2f}")
        else:
            print("Número de notas inválido.")
    else:
        print("Senha incorreta.")
else:
    print("Nome de usuário não encontrado.")

if achou == 0:
    print("Login falhou. Nota registrada como 0.")
    notas.append(0.0)
if nota > 6:
    print("Aluno aprovado")
else:
    nota < 6
    print("Aluno reprovado")