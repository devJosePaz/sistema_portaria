def registrar_funcionario(conexao, nome, cargo, entrada, saida):
    """Registra um novo funcionário no banco de dados."""
    if conexao:  # Verifica se a conexão foi estabelecida
        cursor = conexao.cursor()  # Cria um cursor para executar comandos
        inserir_funcionario = """
        INSERT INTO funcionarios (nome, cargo, entrada, saida) 
        VALUES (%s, %s, %s, %s)
        """
        dados = (nome, cargo, entrada, saida)  # Dados a serem inseridos
        cursor.execute(inserir_funcionario, dados)  # Executa a inserção
        conexao.commit()  # Salva as alterações no banco de dados
        cursor.close()  # Fecha o cursor
        print(f"Funcionário {nome} registrado com sucesso.")

def registrar_visitante(conexao, nome, documento, empresa, entrada, saida, visitado, contato):
    """Registra um novo visitante no banco de dados."""
    if conexao:  # Verifica se a conexão foi estabelecida
        cursor = conexao.cursor()  # Cria um cursor para executar comandos
        inserir_visitante = """
        INSERT INTO visitantes(nome, documento, empresa, entrada, saida, visitado, contato)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        dados = (nome, documento, empresa, entrada, saida, visitado, contato)  # Dados a serem inseridos
        cursor.execute(inserir_visitante, dados)  # Executa a inserção
        conexao.commit()  # Salva as alterações no banco de dados
        cursor.close()  # Fecha o cursor
        print(f"Visitante {nome} registrado com sucesso.")
