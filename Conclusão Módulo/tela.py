import tkinter as tk
from tkinter import W, ttk
from tkinter import messagebox
from telaLogin import TelaLogin
from telaCadastrar import TelaCadastrar

class Tela():
    def __init__(self, window):
        self.__window = window

        self.__frame1 = tk.Frame(window, relief= tk.RAISED, borderwidth=1)
        self.__frame1.pack(padx=5, pady=5)

        ttk.Label(self.__frame1, text='Seja Bem-Vindo ao Sistema da Empresa', font=('Arial', 14)).pack()

        self.__frame2 = tk.Frame(window)
        self.__frame2.pack()

        self.__btnLogin = tk.Button(self.__frame2, text='   Login   ', font=('Arial', 10), command=self.Login)
        self.__btnLogin.grid(row=0, column=1, sticky=tk.W) 

        self.__btnCadastrar = tk.Button(self.__frame2, text='Cadastrar', font=('Arial', 10), command=self.cadastrar)
        self.__btnCadastrar.grid(row=1, column=1, sticky=tk.W)


    def Login(self):
        telaLogin = TelaLogin(self.__window)


    def cadastrar(self):
        telacadastrar = TelaCadastrar(self.__window)        