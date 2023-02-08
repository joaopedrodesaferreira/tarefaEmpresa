from datetime import datetime
from funcionario import Funcionario
import mysql.connector

class FuncionarioDAO():
    __funcionario = Funcionario()

    @property
    def funcionario(self):
        return self.__funcionario
    
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario
    


    def conectar(self):
        self.__conexao = mysql.connector.connect(host='', database='', user='', password='')
        self.__cursor = self.__conexao.cursor()
    


    def fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()


    def listarFuncionario(self):
        self.conectar()
        sql = 'select * from funcionario'
        self.__cursor.execute(sql)
        return self.__cursor
    


    def inserirCadastro(self):
        try:
        
            self.conectar()
            
            sql = 'insert into funcionario values(0,%s, %s, %s, %s, %s, %s, %s, %s)'
            dataDT1 = datetime.strptime(self.__funcionario.dataContratacao, '%d/%m/%Y')
            dataMYSQL1 = datetime.strftime(dataDT1, '%Y/%m/%d')
            dataDT2 = datetime.strptime(self.__funcionario.dataNascimento, '%d/%m/%Y')
            dataMYSQL2 = datetime.strftime(dataDT2, '%Y/%m/%d')
            dadosSQL = (self.__funcionario.nomeFuncionario, self.__funcionario.cpfFuncionario, self.__funcionario.enderecoFuncionario, 
            dataMYSQL2, self.__funcionario.emailFuncionario, self.__funcionario.idSetor, self.__funcionario.idFuncao, dataMYSQL1)

            self.__cursor.execute(sql, dadosSQL)
            self.__conexao.commit()
            
            self.fecharConexao()

            return True
        
        except:
            return False
        


    def pesquisarID(self):
        self.conectar()
        
        sql = 'select * from funcionario where idFuncionario=' + str(self.__funcionario.idFuncionario)
        self.__cursor.execute(sql)
        respBD = self.__cursor.fetchone()
        self.__funcionario.idFuncionario = respBD[0]
        self.__funcionario.nomeFuncionario = respBD[1] 
        self.__funcionario.cpfFuncionario = respBD[2]
        self.__funcionario.enderecoFuncionario = respBD[3]
        self.__funcionario.dataNascimento = respBD[4]
        self.__funcionario.emailFuncionario = respBD[5]
        self.__funcionario.idSetor = respBD[6]
        self.__funcionario.idFuncao = respBD[7]
        self.__funcionario.dataContratacao = respBD[8]
        
        self.fecharConexao()
    


    def pesquisarCPF(self):
        self.conectar()
        
        sql = 'select * from funcionario where cpfFuncionario= "' + str(self.__funcionario.cpfFuncionario) + '"'
        self.__cursor.execute(sql)
        respBD = self.__cursor.fetchone()
        self.__funcionario.idFuncionario = respBD[0]
        self.__funcionario.nomeFuncionario = respBD[1] 
        self.__funcionario.cpfFuncionario = respBD[2]
        self.__funcionario.enderecoFuncionario = respBD[3]
        self.__funcionario.dataNascimento = respBD[4]
        self.__funcionario.emailFuncionario = respBD[5]
        self.__funcionario.idSetor = respBD[6]
        self.__funcionario.idFuncao = respBD[7]
        self.__funcionario.dataContratacao = respBD[8]
        
        self.fecharConexao()



    def verificarCPF(self):
        self.conectar()

        sql = 'select count(cpfFuncionario) from funcionario where cpfFuncionario= "' +str(self.__funcionario.cpfFuncionario)+'"'
        self.__cursor.execute(sql)
        respBD = self.__cursor.fetchone()

        if respBD[0] == 0:
            return True
        
        else:
            return False
        
    


    def excluirFuncionario(self):
        self.conectar()

        sql = 'delete from funcionario where idFuncionario=' + str(self.__funcionario.idFuncionario)
        self.__cursor.execute(sql)
        self.__conexao.commit()

        self.fecharConexao()
    


    def alterar(self):
        try:
            self.conectar()
                
            sql = 'update funcionario set nomeFuncionario=%s, endereco=%s, emailFuncionario=%s, idSetor=%s, idFuncao=%s where idFuncionario=%s'
            dadosSQL = (self.__funcionario.nomeFuncionario, self.__funcionario.enderecoFuncionario, 
        self.__funcionario.emailFuncionario, self.__funcionario.idSetor, self.__funcionario.idFuncao, self.__funcionario.idFuncionario)

            self.__cursor.execute(sql, dadosSQL)
            self.__conexao.commit()
        
            return True
            
        except:
            return False

