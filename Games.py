import sqlite3

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('C:\Users\Renato\Documents\New Live\Anotações\Projetos\Ainda não fiz - Games')
c = conn.cursor()

# Criar tabela no banco de dados
c.execute('''
CREATE TABLE games (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_date TEXT,
    team TEXT,
    rating REAL,
    times_listed TEXT,
    number_of_reviews TEXT,
    genres TEXT,
    summary TEXT,
    reviews TEXT,
    plays TEXT,
    playing TEXT,
    backlogs TEXT,
    wishlist TEXT
)
''')

# Inserir dados no banco de dados
games_df.to_sql('games', conn, if_exists='replace', index=False)

# Verificar se os dados foram inseridos corretamente
c.execute('SELECT * FROM games LIMIT 5')
rows = c.fetchall()

# Fechar a conexão com o banco de dados
conn.close()

rows

#Usar no SQL:
#Jogos com Maior Avaliação

#SELECT title, rating 
#FROM games 
#ORDER BY rating DESC 
#LIMIT 10;

#Quantidade de Jogos Lançados por Ano

#SELECT strftime('%Y', release_date) AS year, COUNT(*) AS count 
#FROM games 
#GROUP BY year 
#ORDER BY year;

#Gêneros Mais Comuns

#SELECT genres, COUNT(*) AS count 
#FROM games 
#GROUP BY genres 
#ORDER BY count DESC 
#LIMIT 10;

#Jogos com Mais Avaliações

#SELECT title, number_of_reviews 
#FROM games 
#ORDER BY number_of_reviews DESC 
#LIMIT 10;
