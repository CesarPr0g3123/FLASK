import sqlite3

def get_connection():
    return sqlite3.connect('produtos.db')

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL CHECK (preco >= 0),
            estoque INTEGER NOT NULL DEFAULT 0 CHECK (estoque >= 0)
        )
    """)
    conn.commit()
    conn.close()

def inserir_produto(nome, preco, estoque):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO produto (nome, preco, estoque)
        VALUES (?, ?, ?)
    """, (nome, preco, estoque))
    conn.commit()
    conn.close()
    print(f'Produto "{nome}" inserido com sucesso.')

def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()
    conn.close()
    if produtos:
        print("\nProdutos cadastrados:")
        for p in produtos:
            print(f"ID: {p[0]}, Nome: {p[1]}, Preço: R${p[2]:.2f}, Estoque: {p[3]}")
    else:
        print("\nNenhum produto cadastrado.")

def atualizar_preco(id_produto, novo_preco):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE produto
        SET preco = ?
        WHERE id = ?
    """, (novo_preco, id_produto))
    conn.commit()
    conn.close()
    print(f'Preço do produto ID {id_produto} atualizado para R${novo_preco:.2f}.')

def excluir_produto(id_produto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM produto
        WHERE id = ?
    """, (id_produto,))
    conn.commit()
    conn.close()
    print(f'Produto ID {id_produto} excluído com sucesso.')

def menu():
    criar_tabela()
    while True:
        print("\n--- Menu ---")
        print("1. Inserir produto")
        print("2. Listar produtos")
        print("3. Atualizar preço")
        print("4. Excluir produto")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: R$"))
            estoque = int(input("Quantidade em estoque: "))
            inserir_produto(nome, preco, estoque)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            id_produto = int(input("ID do produto a ser atualizado: "))
            novo_preco = float(input("Novo preço: R$"))
            atualizar_preco(id_produto, novo_preco)
        elif opcao == "4":
            id_produto = int(input("ID do produto a ser excluído: "))
            excluir_produto(id_produto)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()