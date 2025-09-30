import sqlite3

conexao = sqlite3.connect("Inventario.db")
cursor = conexao.cursor()

def iniciar_banco():
    conexao = sqlite3.connect("Inventario.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roupas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        tamanho TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

def inserir_roupa(nome, tamanho, quantidade, valor):
    try:
        conexao = sqlite3.connect("Inventario.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO roupas (nome, tamanho, quantidade, valor) VALUES (?, ?, ?, ?)",
            (nome, tamanho, quantidade, valor)
        )
        conexao.commit()
        print(f"Roupa '{nome}' inserida com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Roupa já existente com esse nome.")
    finally:
        conexao.close()

def listar_roupas():
    conexao = sqlite3.connect("Inventario.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, tamanho, quantidade, valor FROM roupas")
    roupas = cursor.fetchall()
    if roupas:
        print("\nLista de Roupas:")
        for roupa in roupas:
            print(f"ID: {roupa[0]} | Nome: {roupa[1]} | Tamanho: {roupa[2]} | Quantidade: {roupa[3]} | Valor: R$ {roupa[4]:.2f}")
    else:
        print("Nenhuma roupa cadastrada.")
    conexao.close()

def atualizar_quantidade(nome, nova_quantidade):
    conexao = sqlite3.connect("Inventario.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE roupas SET quantidade = ? WHERE nome = ?", (nova_quantidade, nome))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Quantidade da roupa '{nome}' atualizada para {nova_quantidade}.")
    else:
        print("Roupa não encontrada.")
    conexao.close()

def deletar_roupa(nome):
    conexao = sqlite3.connect("Inventario.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM roupas WHERE nome = ?", (nome,))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Roupa '{nome}' deletada com sucesso.")
    else:
        print("Roupa não encontrada.")
    conexao.close()

# Função para fechar a conexão com o banco, salvando qualquer alteração pendente
def fechar_banco():
    conexao.commit()
    conexao.close()