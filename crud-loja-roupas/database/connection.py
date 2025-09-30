import sqlite3

# Cria conexão com o banco de dados "Inventario.db" (arquivo local)
conexao = sqlite3.connect("Estoque.db")
conexao.row_factory