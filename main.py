# main.py
from db_connection import criar_conexao  # Importando a função de conexão
from interface.gui import iniciar_interface  # Importando a função para iniciar a interface

def main():
    # Cria a conexão com o banco de dados
    conexao = criar_conexao()  # Chama a função de conexão

    if conexao:  # Verifica se a conexão foi bem-sucedida
        # Inicia a interface gráfica e passa a conexão
        iniciar_interface(conexao)  # Passa a conexão para a interface
        # A conexão será fechada quando a interface for finalizada

if __name__ == "__main__":
    main()
