import sqlite3

def execute_sql_commands(db_name='loja_eletronicos.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        sql_commands = [
            "DROP TABLE Produtos;",
            """CREATE TABLE Produtos(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                categoria TEXT,
                preco REAL,
                estoque INTEGER
            );""",
            """INSERT INTO Produtos (id, nome, categoria, preco, estoque) VALUES
                (1, 'Notebook', 'Informática', 3500.00, 10),
                (2, 'Fone de Ouvido', 'Acessório', 50.00, 50),
                (3, 'Placa de Vídeo', 'Hardware', 25999.99, 1),
                (4, 'Mouse', 'Acessório', 360.00, 7);""",
            "ALTER TABLE Produtos ADD COLUMN data_entrada DATE;",
            "UPDATE Produtos SET preco = 3300.00 WHERE nome = 'Notebook';",
            "UPDATE Produtos SET data_entrada = '2025-06-12' WHERE id = 1;",
        ]

        for command in sql_commands:
            cursor.execute(command)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Erro ao executar comandos SQL: {e}")


if __name__ == '__main__':
    execute_sql_commands()
