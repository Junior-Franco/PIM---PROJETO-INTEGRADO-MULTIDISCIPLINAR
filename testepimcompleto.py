import os
import json
import hashlib
from collections import Counter

CAMINHO_ARQUIVO = "dados/dados_alunos.json"

# Cria pasta se não existir
os.makedirs("dados", exist_ok=True)

# Função para criptografar senhas
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para calcular estatísticas
def calcular_estatisticas(notas):
    media = sum(notas) / len(notas)
    notas_ordenadas = sorted(notas)
    mediana = (notas_ordenadas[1] + notas_ordenadas[2]) / 2

    contagem = Counter(notas)
    mais_comum = contagem.most_common()
    freq = mais_comum[0][1]
    modas = [nota for nota, f in mais_comum if f == freq]
    moda = modas if freq > 1 else "Nenhuma"

    return media, mediana, moda

# Tenta carregar dados existentes
if os.path.exists(CAMINHO_ARQUIVO):
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    print("\nArquivo carregado. Dados existentes encontrados.")
else:
    dados = {"alunos": []}
    print("\nNenhum dado encontrado. Iniciando novo cadastro.")

# Cadastra ou atualiza alunos (com nome real)
while len(dados["alunos"]) < 4:
    print(f"\nCadastro do aluno {len(dados['alunos']) + 1}")
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha do aluno: ")
    senha_hash = criptografar_senha(senha)
    aluno = {
        "nome": nome,
        "senha_hash": senha_hash,
        "nota": None
    }
    dados["alunos"].append(aluno)

# Registro de notas via login
print("\nLogin dos alunos para registrar notas:")
for aluno in dados["alunos"]:
    print(f"\nLogin de {aluno['nome']}")
    senha = input("Digite a senha: ")
    if criptografar_senha(senha) == aluno["senha_hash"]:
        nota = float(input("Login aprovado. Digite a nota (0 a 10): "))
        aluno["nota"] = nota
    else:
        print("Senha incorreta. Nota registrada como 0.")
        aluno["nota"] = 0.0

# Estatísticas
notas = [aluno["nota"] for aluno in dados["alunos"]]
media, mediana, moda = calcular_estatisticas(notas)

# Relatório
print("\n===== RELATÓRIO FINAL =====")
for aluno in dados["alunos"]:
    print(f"{aluno['nome']}: Nota = {aluno['nota']}")

print(f"\nMédia: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print("Moda:", moda if moda != "Nenhuma" else "nenhuma (todas diferentes)")

# Atualiza estatísticas no arquivo
dados["estatisticas"] = {
    "media": round(media, 2),
    "mediana": round(mediana, 2),
    "moda": moda if isinstance(moda, str) else [round(m, 2) for m in moda]
}

# Salva dados no JSON
with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("\nDados salvos com sucesso no arquivo JSON.")