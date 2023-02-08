import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from funcionarioDAO import FuncionarioDAO
from funcaoDAO import FuncaoDAO
from setorDAO import SetorDAO
from telaAlterar import TelaAlterar

class TelaPerfil():
    def __init__(self, window, idFuncionario):
        self.__funcionarioDAO = FuncionarioDAO()
        self.__funcionarioDAO.funcionario.idFuncionario = idFuncionario

        self.__funcionarioDAO.pesquisarID()
        
        self.__funcaoDAO = FuncaoDAO()
        self.__funcaoDAO.funcao.idFuncao = self.__funcionarioDAO.funcionario.idFuncao
        
        self.__funcaoDAO.pesquisarID()

        self.__setorDAO = SetorDAO()
        self.__setorDAO.setor.idSetor = self.__funcionarioDAO.funcionario.idSetor
        
        self.__setorDAO.pesquisarID()

        self.__window = window
        self.__window1 = tk.Toplevel()
        self.__window1.title('Perfil Funcionário')
        self.__window1.wm_protocol('WM_DELETE_WINDOW', self.fecharJanela)
        
        self.__frame1 = ttk.Frame(self.__window1)
        self.__frame1.pack()

        ttk.Label(self.__frame1, text='Perfil do Funcionário', font=('Arial', 14)).grid(row=0, column=0, sticky=tk.W)

        self.__frame2 = tk.Frame(self.__window1)
        self.__frame2.pack()

        nome = tk.StringVar()
        nome.set(str(self.__funcionarioDAO.funcionario.nomeFuncionario))
        ttk.Label(self.__frame2, text='Nome:', font=('Arial', 10)).grid(row=0, column=0, sticky=tk.W)
        self.__txtNome = tk.Entry(self.__frame2, textvariable=nome,font=('Arial', 8), state= tk.DISABLED)
        self.__txtNome.grid(row=0, column=1, sticky=tk.W)
        
        cpf = tk.StringVar()
        cpf.set(str(self.__funcionarioDAO.funcionario.cpfFuncionario))
        ttk.Label(self.__frame2, text='CPF:', font=('Arial', 10)).grid(row=1, column=0, sticky=tk.W)
        self.__txtCPF = tk.Entry(self.__frame2, textvariable=cpf,font=('Arial', 8), state= tk.DISABLED)
        self.__txtCPF.grid(row=1, column=1, sticky=tk.W)

        endereco = tk.StringVar()
        endereco.set(str(self.__funcionarioDAO.funcionario.enderecoFuncionario))
        ttk.Label(self.__frame2, text='Endereço:', font=('Arial', 10)).grid(row=2, column=0, sticky=tk.W)
        self.__txtEndereco = tk.Entry(self.__frame2, textvariable=endereco,font=('Arial', 8), state= tk.DISABLED)
        self.__txtEndereco.grid(row=2, column=1, sticky=tk.W)

        dataNascimento = tk.StringVar()
        dataNascimento.set(str(self.__funcionarioDAO.funcionario.dataNascimento))
        ttk.Label(self.__frame2,text='Data de Nascimento:', font=('Arial', 10)).grid(row=0, column=2, sticky=tk.W)
        self.__txtDataNascimento = tk.Entry(self.__frame2, textvariable=dataNascimento,font=('Arial', 8), state= tk.DISABLED)
        self.__txtDataNascimento.grid(row=0, column=3, sticky=tk.W)

        email = tk.StringVar()
        email.set(str(self.__funcionarioDAO.funcionario.emailFuncionario))
        ttk.Label(self.__frame2,text='E-Mail:', font=('Arial', 10)).grid(row=1, column=2, sticky=tk.W)
        self.__txtEmail = tk.Entry(self.__frame2, textvariable=email,font=('Arial', 8), state= tk.DISABLED)
        self.__txtEmail.grid(row=1, column=3, sticky=tk.W)

        dataContratacao = tk.StringVar()
        dataContratacao.set(str(self.__funcionarioDAO.funcionario.dataContratacao))
        ttk.Label(self.__frame2,text='Data de Contração:', font=('Arial', 10)).grid(row=2, column=2, sticky=tk.W)
        self.__txtDataContratacao = tk.Entry(self.__frame2, textvariable=dataContratacao,font=('Arial', 8), state= tk.DISABLED)
        self.__txtDataContratacao.grid(row=2, column=3, sticky=tk.W)

        self.__frmLinha = ttk.Frame(self.__window1, relief=tk.RAISED, borderwidth=2, width=400, height=5)
        self.__frmLinha.pack(padx=5, pady=5)

        self.__frame3 = tk.Frame(self.__window1)
        self.__frame3.pack(padx=5, pady=5)

        setor = tk.StringVar()
        setor.set(str(self.__setorDAO.setor.nomeSetor))
        ttk.Label(self.__frame3, text='Setor:', font=('Arial', 10)).grid(row=0, column=0, sticky=tk.W)
        self.__txtSetor = tk.Entry(self.__frame3, textvariable=setor,font=('Arial', 8),state= tk.DISABLED)
        self.__txtSetor.grid(row=0, column=1, sticky=tk.W)

        funcao = tk.StringVar()
        funcao.set(str(self.__funcaoDAO.funcao.nomeFuncao))
        ttk.Label(self.__frame3, text='Função:', font=('Arial', 10)).grid(row=0, column=2, sticky=tk.W)
        self.__txtFuncao = tk.Entry(self.__frame3, textvariable=funcao,font=('Arial', 8),state= tk.DISABLED)
        self.__txtFuncao.grid(row=0, column=3, sticky=tk.W)

        
        ttk.Label(self.__frame3, text='Salário R$:', font=('Arial', 10)).grid(row=1, column=2, sticky=tk.W)
        self.__lblSalario = ttk.Label(self.__frame3, text= '', font=('Arial', 8), state= tk.DISABLED)
        self.__lblSalario.grid(row=1, column=3, sticky=tk.W)
        self.__lblSalario['text'] = self.__funcaoDAO.funcao.salario

        self.__btnAlterar = ttk.Button(self.__frame3, text='Alterar', command=self.alterar)
        self.__btnAlterar.grid(row=2, column=1, sticky=tk.NSEW)

        self.__btnExcluir = ttk.Button(self.__frame3, text='Excluir', command=self.excluir)
        self.__btnExcluir.grid(row=2, column=3, sticky=tk.NSEW)
    


    def fecharJanela(self):
        self.__window1.destroy()
        self.__window.deiconify()
    


    def excluir(self):
        resp = messagebox.askokcancel('Excluir Cadastro', 'Tem certeza que quer excluir o cadastro?')

        if resp == True:
            self.__funcionarioDAO.excluirFuncionario()
            self.fecharJanela()
    


    def alterar(self):
        telaalterar = TelaAlterar(self.__window1, self.__funcionarioDAO.funcionario.idFuncionario)