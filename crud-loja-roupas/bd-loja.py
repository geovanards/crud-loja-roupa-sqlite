import sqlite3

# Cria conexão com o banco de dados "Inventario.db" (arquivo local)
conexao = sqlite3.connect("Estoque.db")
# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

def iniciar_banco():
    # Abre conexão e cursor novamente (pode ser redundante, mas funciona)
    conexao = sqlite3.connect("Estoque.db")
    cursor = conexao.cursor()

    # Cria tabela 'roupas' com colunas:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roupas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT UNIQUE NOT NULL,
        tamanho TEXT NOT NULL,
        quantidade INT NOT NULL,
        valor REAL
        )
        """)
    
# Função para inserir um novo item no banco
def inserir_roupa(nome_produto, tamanho, quantidade, valor):
    try:
        # Insere os dados passados na tabela 'roupas'
        cursor.execute("INSERT INTO roupas (nome_produto, tamanho, quantidade, valor) VALUES(?,?,?,?)", 
        (nome_produto, tamanho, quantidade, valor))
        # Confirma a operação para salvar no banco    
        conexao.commit()
        print("Item inserido com sucesso")
    except sqlite3.IntegrityError:
        # Caso o nome da roupa já exista (único), dá erro e imprime mensagem
        print("Erro: Item já existente")

# Função para listar todos os itens da tabela
def listar_roupas():
    # Busca todos os registros da tabela 'itens'
    cursor.execute("SELECT * FROM itens")
    roupas = cursor.fetchall()  # pega todos os resultados
    # Imprime cada item encontrado
    for r in roupas:
        print(r)