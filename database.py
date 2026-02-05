import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conta (
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conta_id INTEGER,
            tipo TEXT,
            valor REAL,
            data TEXT,
            FOREIGN KEY (conta_id) REFERENCES conta(id)
        )
    """)

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

    from datetime import datetime

def registrar_transacao(conta_id, tipo, valor):
    conn = conectar()
    cursor = conn.cursor()

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO transacao (conta_id, tipo, valor, data) VALUES (?, ?, ?, ?)",
        (conta_id, tipo, valor, data)
    )

    conn.commit()
    conn.close()


def listar_transacoes(conta_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT tipo, valor, data FROM transacao WHERE conta_id = ? ORDER BY id",
        (conta_id,)
    )

    rows = cursor.fetchall()
    conn.close()
    return rows

