import pandas as pd

# Lista de alunos e suas notas
alunos = [
    ("Christian", 40),
    ("Paulo L", 31),
    ("Ellen", 37),
    ("Vitor Rodrigues", 38),
    ("Analynne", 52),
    ("Ju", 36),
    ("Davi Ferreira", 32),
    ("Lucas Pereira", 31),
    ("Marcos V", 50),
    ("Bianca C", 45),
    ("Mei", 41),
    ("Ana Paula Marinho", 38),
    ("Eloísa Negrão", 47),
    ("Wyran", 42),
    ("Mayze", 39),
    ("Gustavo Prestes", 46),
    ("Layze Cordeir", 39),
    ("Guimarães", 39),
    ("Éllen Gaia", 41),
    ("Marçal", 42),
    ("Liuan Silva", 42),
    ("Yuri", 51),
    ("Jefferson", 43),
    ("José", 37),
    ("Beckman", 38),
    ("Matheus", 45),
    ("Élber", 39),
    ("L.Mendes", 35),
    ("W.Rangel", 45),
    ("Leo", 41),
    ("Nay", 36),
    ("Ivanilda Rodrigues", 33),
    ("Heloisa", 38),
    ("Camila N", 42),
    ("Clarice", 32),
    ("Saymon", 47),
    ("Luciano", 40),
    ("Breno", 31),
    ("Yasmin", 46),
    ("Emily", 41),
    ("Ingrid", 38),
    ("Flavianny", 37),
    ("Edney", 33),
    ("Alice", 36),
    ("Weslley", 32),
    ("P.vinicius", 37),
    ("Vitor", 44),
    ("Adriele", 32),
    ("Robson Contente", 53),
    ("William", 39),
    ("Davi Willian", 37),
    ("Jadson", 42),
    ("Luis", 34),
    ("Vinicius Flexa", 34),
    ("Viviane", 30),
    ("Arthur", 38),
    ("Luan", 32),
    ("Bernardo", 33),
    ("Alexandre", 30),
    ("Marcos T", 47),
    ("Dara", 36),
    ("Julio Barbosa", 45),
    ("Gustavo Ferreira", 37),
    ("Sofia Yumi", 45),
    ("Maicon", 36),
    ("Nicole Rocha", 46),
    ("Breno Vitor", 54),
    ("A. Cris", 41),
    ("Davi", 36),
    ("João. P", 32),
    ("Walace", 54),
    ("Edjoan", 32),
    ("Adrian", 33),
    ("Anderson", 37),
    ("Guilherme William", 30),
    ("Adeilson Silva", 38),
    ("Roberto Raphael", 32),
    ("Vinicius Silva", 42),
    ("Deivison Gustavo", 47),
    ("Lucas Souza", 31),
    ("Maicon Lira", 41),
    ("Willy", 31),
    ("Erick Silva", 30),
    ("Ronaldo", 34),
    ("Joao V", 34),
    ("Adria luz", 30),
    ("Eduarda", 31)
]

# Remover nomes duplicados
alunos_sem_duplicatas = list(set(alunos))

# Organizar em ordem decrescente de notas
alunos_ordenados = sorted(alunos_sem_duplicatas, key=lambda x: x[1], reverse=True)

# Criar um DataFrame com os dados
df = pd.DataFrame(alunos_ordenados, columns=["Nome", "Idade"])

# Remover duplicatas pelo nome
df = df.drop_duplicates(subset='Nome', keep='first')

# Salvar o DataFrame em um arquivo CSV
df.to_csv("planilha_cebraspe_atualizada_ordenada_descendente_sem_duplicatas.csv", index=False)

print("Planilha atualizada, ordenada em ordem decrescente e sem duplicatas criada com sucesso.")

# https://is.gd/JeielMiranda
