import sys
import sqlite3
import banco as inventario
from banco import iniciar_banco, inserir_roupa, listar_roupas, atualizar_quantidade, deletar_roupa

def mostrar_menu():
    print("\n--- Loja de Roupas ---")
    print("1. Inserir Roupa")
    print("2. Listar Roupas")
    print("3. Atualizar Quantidade")
    print("4. Deletar Roupa")
    print("0. Sair")

def main():
    iniciar_banco()
    while True:
        mostrar_menu()
        opcao = input("Escolha sua opção: ").strip()
        match opcao:
            case "1":
                nome = input("Nome do produto: ").strip()
                tamanho = input("Tamanho: ").strip()
                try:
                    quantidade = int(input("Quantidade: "))
                    valor = float(input("Valor: R$ "))
                except ValueError:
                    print("Quantidade e valor devem ser números válidos.")
                    continue
                inventario.inserir_roupa(nome, tamanho, quantidade, valor)
            case "2":
                inventario.listar_roupas()
            case "3":
                nome = input("Nome do produto para atualizar quantidade: ").strip()
                try:
                    nova_quantidade = int(input("Nova quantidade: "))
                except ValueError:
                    print("Quantidade deve ser um número inteiro.")
                    continue
                inventario.atualizar_quantidade(nome, nova_quantidade)
            case "4":
                nome = input("Nome do produto para deletar: ").strip()
                inventario.deletar_roupa(nome)
            case "0":
                print("Saindo...")
                sys.exit(0)
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
