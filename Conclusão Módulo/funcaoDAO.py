from funcao import Funcao
import mysql.connector

class FuncaoDAO():
    __funcao = Funcao()

    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao
    


    def conectar(self):
        self.__conexao = mysql.connector.connect(host= '' , database = '', user = 'root', password = '')
        self.__cursor = self.__conexao.cursor()
    

    def fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()



    def listarFuncao(self):
        self.conectar()
        sql = 'select * from funcao'
        self.__cursor.execute(sql)
        return self.__cursor
    


    def pesquisarID(self):
        self.conectar()
        
        sql = 'select * from funcao where idFuncao=' + str(self.__funcao.idFuncao)
        self.__cursor.execute(sql)
        respBD = self.__cursor.fetchone()
        self.__funcao.idFuncao = respBD[0]
        self.__funcao.nomeFuncao = respBD[1]
        self.__funcao.salario = respBD[2]

        self.fecharConexao()