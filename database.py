import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conta (
            id INTEGER PRIMARY KEY,
            saldo REAL
        )
    """)

    conn.commit()
    conn.close()


def obter_saldo():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT saldo FROM conta WHERE id = 1")
    resultado = cursor.fetchone()

    if resultado is None:
        cursor.execute("INSERT INTO conta (id, saldo) VALUES (1, 0)")
        conn.commit()
        saldo = 0
    else:
        saldo = resultado[0]

    conn.close()
    return saldo


def atualizar_saldo(novo_saldo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE conta SET saldo = ? WHERE id = 1",
        (novo_saldo,)
    )

    conn.commit()
    conn.close()
