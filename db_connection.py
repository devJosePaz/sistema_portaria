# db_connection.py
import mysql.connector
from mysql.connector import Error

def criar_conexao():
    """Cria a conexão com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',        # Substitua por seu usuário do MySQL
            password='kagijo10',  # Substitua por sua senha do MySQL
            database='portaria'  # Substitua pelo nome do seu banco de dados
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida com o MySQL")
            return conexao
    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
