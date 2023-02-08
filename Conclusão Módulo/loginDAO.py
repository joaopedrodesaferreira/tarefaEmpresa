from login import Login
import mysql.connector

class LoginDAO():
    __login = Login()

    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, login):
        self.__login = login
    


    def conectar(self):
        self.__conexao = mysql.connector.connect(host='', database='', user='', password='')
        self.__cursor = self.__conexao.cursor()


    
    def fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()
    


    def inserirUsuarioSenha(self):
        try:      
            self.conectar()
            
            sql = 'insert into login values(0,%s, %s, %s)'
            dadosSQL = (self.__login.idFuncionario, self.__login.nomeUsuario, self.__login.senha)
            self.__cursor.execute(sql, dadosSQL)
            self.__conexao.commit()

            self.fecharConexao()
            
            return True
        
        except:
            return False
        
    

    def alterarUsuarioSenha(self):
        try:
            self.conectar()
        
            sql = 'update login set usuarioFuncionario=%s, senhaFuncionario=%s where idFuncionario=%s'
            dadosSQL = (self.__login.nomeUsuario, self.__login.senha, self.__login.idFuncionario)
            self.__cursor.execute(sql, dadosSQL)
            self.__conexao.commit()

            self.fecharConexao()
            return True
        except:
            return False


    def logar(self):
        self.conectar()

        sql = 'select * from login where usuarioFuncionario=%s and senhaFuncionario=%s'
        dadosSQL = (self.__login.nomeUsuario, self.__login.senha)
        self.__cursor.execute(sql, dadosSQL)
        respBD = self.__cursor.fetchone()

        if respBD != None:
            self.__login.idLogin = respBD[0]
            self.__login.idFuncionario = respBD[1]
            self.__login.nomeUsuario = respBD[2]
            self.__login.senha = respBD[3]
            return True
        
        else:
            return False