import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from setorDAO import SetorDAO
from funcaoDAO import FuncaoDAO
from funcionarioDAO import FuncionarioDAO
from loginDAO import LoginDAO

class TelaCadastrar():
    def __init__(self, window):
        self.__setorDAO = SetorDAO()
        self.__funcaoDAO = FuncaoDAO()
        self.__funcionarioDAO = FuncionarioDAO()
        self.__loginDAO = LoginDAO()

        self.__window = window
        self.__window.withdraw()
        self.__window1 = tk.Toplevel()
        self.__window1.title('Cadastro de Funcionário')
        self.__window1.wm_protocol('WM_DELETE_WINDOW', self.fecharJanela)
        
        self.__frame1 = tk.Frame(self.__window1)
        self.__frame1.pack()

        ttk.Label(self.__frame1, text='Cadastre as informações do funcionário', font=('Arial', 14)).grid(row=0, column=0, sticky=tk.W)

        self.__frame2 = tk.Frame(self.__window1)
        self.__frame2.pack()

        ttk.Label(self.__frame2, text='Nome:', font=('Arial', 10)).grid(row=0, column=0, sticky=tk.W)
        self.__txtNome = tk.Entry(self.__frame2, font=('Arial', 8))
        self.__txtNome.grid(row=0, column=1, sticky=tk.W)
        ttk.Label(self.__frame2,text='*', foreground='red').grid(row=0,column=2,sticky=tk.W)
        
        ttk.Label(self.__frame2, text='CPF:', font=('Arial', 10)).grid(row=1, column=0, sticky=tk.W)
        self.__txtCPF = tk.Entry(self.__frame2, font=('Arial', 8))
        self.__txtCPF.grid(row=1, column=1, sticky=tk.W)
        ttk.Label(self.__frame2,text='*', foreground='red').grid(row=1,column=2,sticky=tk.W)

        ttk.Label(self.__frame2, text='Endereço:', font=('Arial', 10)).grid(row=2, column=0, sticky=tk.W)
        self.__txtEndereco = tk.Entry(self.__frame2, font=('Arial', 8))
        self.__txtEndereco.grid(row=2, column=1, sticky=tk.W)
        ttk.Label(self.__frame2,text='*', foreground='red').grid(row=2,column=2,sticky=tk.W)

        ttk.Label(self.__frame2,text='Data de Nascimento:', font=('Arial', 10)).grid(row=0, column=3, sticky=tk.W)
        self.__txtDataNascimento = tk.Entry(self.__frame2, font=('Arial', 8))
        self.__txtDataNascimento.grid(row=0, column=4, sticky=tk.W)
        ttk.Label(self.__frame2,text='*', foreground='red').grid(row=0,column=5,sticky=tk.W)

        ttk.Label(self.__frame2,text='E-Mail:', font=('Arial', 10)).grid(row=1, column=3, sticky=tk.W)
        self.__txtEmail = tk.Entry(self.__frame2, font=('Arial', 8))
        self.__txtEmail.grid(row=1, column=4, sticky=tk.W)
        ttk.Label(self.__frame2,text='*', foreground='red').grid(row=1,column=5,sticky=tk.W)

        ttk.Label(self.__frame2,text='Data de Contração:', font=('Arial', 10)).grid(row=2, column=3, sticky=tk.W)
        self.__txtDataContratacao = tk.Entry(self.__frame2, font=('Arial', 8))
        self.__txtDataContratacao.grid(row=2, column=4, sticky=tk.W)
        ttk.Label(self.__frame2,text='*', foreground='red').grid(row=2,column=5,sticky=tk.W)

        self.__frmLinha = ttk.Frame(self.__window1, relief=tk.RAISED, borderwidth=2, width=400, height=5)
        self.__frmLinha.pack(padx=5, pady=5)

        self.__frame3 = tk.Frame(self.__window1)
        self.__frame3.pack(padx=5, pady=5)

        ttk.Label(self.__frame3, text='Setor:', font=('Arial', 10)).grid(row=0, column=0, sticky=tk.W)
        self.__cmbSetor = ttk.Combobox(self.__frame3)
        self.__cmbSetor['state'] = 'readonly'
        self.__cmbSetor.grid(row=0, column=1, sticky=tk.W)
        self.__cmbSetor.bind('<<ComboboxSelected>>', self.selecionarIDSetor)
        ttk.Label(self.__frame3,text='*', foreground='red').grid(row=0,column=2,sticky=tk.W)

        ttk.Label(self.__frame3, text='Função:', font=('Arial', 10)).grid(row=0, column=3, sticky=tk.W)
        self.__cmbFuncao = ttk.Combobox(self.__frame3)
        self.__cmbFuncao['state'] = 'readonly'
        self.__cmbFuncao.grid(row=0, column=4, sticky=tk.W)
        self.__cmbFuncao.bind('<<ComboboxSelected>>', self.pesquisarSalario)
        ttk.Label(self.__frame3,text='*', foreground='red').grid(row=0,column=5,sticky=tk.W)

        ttk.Label(self.__frame3, text='Salário R$:', font=('Arial', 10)).grid(row=1, column=2, sticky=tk.W)
        self.__lblSalario = ttk.Label(self.__frame3, text= '', font=('Arial', 8))
        self.__lblSalario.grid(row=1, column=3, sticky=tk.W)

        self.__frmLinha = ttk.Frame(self.__window1, relief=tk.RAISED, borderwidth=2, width=400, height=5)
        self.__frmLinha.pack(padx=5, pady=5)
        
        self.__frame4 = tk.Frame(self.__window1)
        self.__frame4.pack(padx=8, pady=8)

        ttk.Label(self.__frame4, text='Nome de Usuário', font=('Arial', 10)).grid(row=0, column=0, sticky=tk.W)
        self.__txtUsuario = tk.Entry(self.__frame4)
        self.__txtUsuario.grid(row=0, column=1, sticky=tk.W)
        ttk.Label(self.__frame4,text='*', foreground='red').grid(row=0,column=2,sticky=tk.W)

        ttk.Label(self.__frame4, text='Senha', font=('Arial', 10)).grid(row=1, column=0, sticky=tk.W)
        self.__txtSenha = tk.Entry(self.__frame4, show='*')
        self.__txtSenha.grid(row=1, column=1, sticky=tk.W)
        ttk.Label(self.__frame4,text='*', foreground='red').grid(row=1,column=2,sticky=tk.W)

        ttk.Label(self.__frame4,text='(*) Campos Obrigatórios', foreground='red').grid(row=2,column=0,sticky=tk.W)
        self.__btnCadastrar = ttk.Button(self.__frame4, text='Salvar', command=self.cadastrar)
        self.__btnCadastrar.grid(row=2, column=1, sticky=tk.NSEW)


        self.__listaSetor = []
        self.__listaIdSetor = []
        self.carregarComboSetor()

        self.__listaFuncao = []
        self.__listaIdFuncao = []
        self.carregarComboFuncao()
    


    def carregarComboSetor(self):
        cursor = self.__setorDAO.listarSetor()

        self.__listaIdSetor.clear()
        self.__listaSetor.clear()
        
        for (idSetor, nomeSetor) in cursor:
            self.__listaSetor.append(nomeSetor)
            self.__listaIdSetor.append(idSetor)
        
        self.__cmbSetor['values'] = self.__listaSetor



    def carregarComboFuncao(self):
        cursor = self.__funcaoDAO.listarFuncao()

        self.__listaIdFuncao.clear()
        self.__listaFuncao.clear()

        for(idFuncao, nomeFuncao, salario) in cursor:
            self.__listaFuncao.append(nomeFuncao)
            self.__listaIdFuncao.append(idFuncao)
        
        self.__cmbFuncao['values'] = self.__listaFuncao
    


    def pesquisarSalario(self, event):
        textoSelecionado = self.__cmbFuncao.get()
        numLinhaSelecionada = self.__listaFuncao.index(textoSelecionado)
        self.__idFuncao = self.__listaIdFuncao[numLinhaSelecionada]

        self.__funcaoDAO.funcao.idFuncao = self.__idFuncao

        self.__funcaoDAO.pesquisarID()

        self.__lblSalario['text'] = self.__funcaoDAO.funcao.salario
    

    def selecionarIDSetor(self, event):
        textoSelecionado = self.__cmbSetor.get()
        numLinhaSelecionada = self.__listaSetor.index(textoSelecionado)
        self.__idSetor = self.__listaIdSetor[numLinhaSelecionada]

        

    def fecharJanela(self):
        self.__window1.destroy()
        self.__window.deiconify()  
                


    def cadastrar(self):
        self.__funcionarioDAO.funcionario.nomeFuncionario = self.__txtNome.get()
        self.__funcionarioDAO.funcionario.cpfFuncionario = self.__txtCPF.get()
        self.__funcionarioDAO.funcionario.enderecoFuncionario = self.__txtEndereco.get()
        self.__funcionarioDAO.funcionario.dataNascimento = self.__txtDataNascimento.get()
        self.__funcionarioDAO.funcionario.emailFuncionario = self.__txtEmail.get()
        self.__funcionarioDAO.funcionario.idSetor = self.__idSetor
        self.__funcionarioDAO.funcionario.idFuncao = self.__idFuncao
        self.__funcionarioDAO.funcionario.dataContratacao = self.__txtDataContratacao.get()
        
        if self.__funcionarioDAO.verificarCPF() == True:

            respCadastro = self.__funcionarioDAO.inserirCadastro()

            self.__funcionarioDAO.pesquisarCPF()
            self.__loginDAO.login.idFuncionario = self.__funcionarioDAO.funcionario.idFuncionario

            self.__loginDAO.login.nomeUsuario = self.__txtUsuario.get()
            self.__loginDAO.login.senha = self.__txtSenha.get()

            respLogin = self.__loginDAO.inserirUsuarioSenha()

        
            if respCadastro == True and respLogin == True:
                resp = messagebox.showinfo('Sucesso', 'Cadastro efetuado com sucesso!')
                if resp == 'ok':
                    self.fecharJanela()            
            
            else:
                messagebox.showerror('Error', 'Cadastro não efetuado')
        
        else:
            messagebox.showerror('Erro', 'Alguma informação repetida ou campo incoerente')
    

    