import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def registrar_funcionario(conexao, nome, cargo, entrada, saida):
    """Registra um novo funcionário no banco de dados."""
    if conexao:
        cursor = conexao.cursor()
        inserir_funcionario = """
        INSERT INTO funcionarios (nome, cargo, entrada, saida) 
        VALUES (%s, %s, %s, %s)
        """
        dados = (nome, cargo, entrada, saida)
        cursor.execute(inserir_funcionario, dados)
        conexao.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", f"Funcionário {nome} registrado com sucesso.")

def registrar_visitante(conexao, nome, documento, empresa, entrada, saida, visitado, contato):
    """Registra um novo visitante no banco de dados."""
    if conexao:
        cursor = conexao.cursor()
        inserir_visitante = """
        INSERT INTO visitantes(nome, documento, empresa, entrada, saida, visitado, contato)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        dados = (nome, documento, empresa, entrada, saida, visitado, contato)
        cursor.execute(inserir_visitante, dados)
        conexao.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", f"Visitante {nome} registrado com sucesso.")

def registrar_visitante_interface(conexao):
    """Função para registrar visitante a partir da interface."""
    nome = entry_nome_visitante.get()
    documento = entry_documento_visitante.get()
    empresa = entry_empresa_visitante.get()
    entrada = entry_entrada_visitante.get()
    saida = entry_saida_visitante.get()
    visitado = entry_visitado.get()
    contato = entry_contato.get()

    registrar_visitante(conexao, nome, documento, empresa, entrada, saida, visitado, contato)

def registrar_funcionario_interface(conexao):
    """Função para registrar funcionário a partir da interface."""
    nome = entry_nome_funcionario.get()
    cargo = entry_cargo.get()
    entrada = entry_entrada.get()
    saida = entry_saida.get()

    registrar_funcionario(conexao, nome, cargo, entrada, saida)

def iniciar_interface(conexao):
    """Inicia a interface gráfica."""
    janela = tk.Tk()
    janela.title("Sistema de Portaria")
    janela.geometry("600x400")

    # Cria as abas
    abas = ttk.Notebook(janela)
    aba_funcionario = ttk.Frame(abas)
    aba_visitante = ttk.Frame(abas)

    abas.add(aba_funcionario, text="Cadastrar Funcionário")
    abas.add(aba_visitante, text="Cadastrar Visitante")
    abas.pack(expand=1, fill="both")

    # Estilo para a aba
    frame_funcionario = tk.Frame(aba_funcionario, padx=20, pady=20)
    frame_funcionario.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando a frame de funcionário

    frame_visitante = tk.Frame(aba_visitante, padx=20, pady=20)
    frame_visitante.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando a frame de visitante

    # Aba Funcionário
    tk.Label(frame_funcionario, text="Nome:").grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_nome_funcionario
    entry_nome_funcionario = tk.Entry(frame_funcionario)
    entry_nome_funcionario.grid(row=0, column=1, pady=5)

    tk.Label(frame_funcionario, text="Cargo:").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_cargo
    entry_cargo = tk.Entry(frame_funcionario)
    entry_cargo.grid(row=1, column=1, pady=5)

    tk.Label(frame_funcionario, text="Entrada:").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_entrada
    entry_entrada = tk.Entry(frame_funcionario)
    entry_entrada.grid(row=2, column=1, pady=5)

    tk.Label(frame_funcionario, text="Saída:").grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_saida
    entry_saida = tk.Entry(frame_funcionario)
    entry_saida.grid(row=3, column=1, pady=5)

    botao_registrar_funcionario = tk.Button(frame_funcionario, text="Registrar Funcionário", command=lambda: registrar_funcionario_interface(conexao))
    botao_registrar_funcionario.grid(row=4, columnspan=2, pady=10)

    # Aba Visitante
    tk.Label(frame_visitante, text="Nome:").grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_nome_visitante
    entry_nome_visitante = tk.Entry(frame_visitante)
    entry_nome_visitante.grid(row=0, column=1, pady=5)

    tk.Label(frame_visitante, text="Documento:").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_documento_visitante
    entry_documento_visitante = tk.Entry(frame_visitante)
    entry_documento_visitante.grid(row=1, column=1, pady=5)

    tk.Label(frame_visitante, text="Empresa:").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_empresa_visitante
    entry_empresa_visitante = tk.Entry(frame_visitante)
    entry_empresa_visitante.grid(row=2, column=1, pady=5)

    tk.Label(frame_visitante, text="Entrada:").grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_entrada_visitante
    entry_entrada_visitante = tk.Entry(frame_visitante)
    entry_entrada_visitante.grid(row=3, column=1, pady=5)

    tk.Label(frame_visitante, text="Saída:").grid(row=4, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_saida_visitante
    entry_saida_visitante = tk.Entry(frame_visitante)
    entry_saida_visitante.grid(row=4, column=1, pady=5)

    tk.Label(frame_visitante, text="Visitado:").grid(row=5, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_visitado
    entry_visitado = tk.Entry(frame_visitante)
    entry_visitado.grid(row=5, column=1, pady=5)

    tk.Label(frame_visitante, text="Contato:").grid(row=6, column=0, sticky=tk.E, padx=10, pady=5)
    global entry_contato
    entry_contato = tk.Entry(frame_visitante)
    entry_contato.grid(row=6, column=1, pady=5)

    botao_registrar_visitante = tk.Button(frame_visitante, text="Registrar Visitante", command=lambda: registrar_visitante_interface(conexao))
    botao_registrar_visitante.grid(row=7, columnspan=2, pady=10)

    janela.mainloop()
