import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from telaPerfil import TelaPerfil
from loginDAO import LoginDAO

class TelaLogin():
    def __init__(self, window):
        self.__loginDAO = LoginDAO()
        
        self.__window = window
        self.__window.withdraw()
        
        self.__window1 = tk.Toplevel()
        self.__window1.title('Login')
        
        
        self.__frame1 = tk.Frame(self.__window1)
        self.__frame1.pack(padx= 5, pady=5)

        ttk.Label(self.__frame1, text='Insira usuário e senha', font=('Arial', 14)).pack(padx=5, pady=5)

        ttk.Label(self.__frame1, text='Usuário').pack(padx=10,pady=10)
        self.__txtUsuario = tk.Entry(self.__frame1)
        self.__txtUsuario.pack(padx=2, pady=2)

        self.__frame2 = tk.Frame(self.__window1)
        self.__frame2.pack(padx=5, pady=5)

        ttk.Label(self.__frame2, text='Senha').pack(padx=2,pady=2)
        self.__txtSenha = tk.Entry(self.__frame2, show='*')
        self.__txtSenha.pack(padx=2, pady=2)

        self.__btnEntrar = ttk.Button(self.__frame2, text='Entrar', command=self.entrar)
        self.__btnEntrar.pack(padx=4, pady=4)
    
    def entrar(self):
        self.__loginDAO.login.nomeUsuario = self.__txtUsuario.get()
        self.__loginDAO.login.senha = self.__txtSenha.get()
        if self.__loginDAO.logar() == True:
            telaperfil = TelaPerfil(self.__window, self.__loginDAO.login.idFuncionario)
            self.__window1.destroy()
        
        else:
            messagebox.showerror("Erro", "Alguma informação não está certa")
    
