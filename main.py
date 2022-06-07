from msilib.schema import Class
import pyodbc


def opcoes():
    print("\n")
    print("Escolha uma opção: \n")
    print("\n")
    print("1 - SELECT")
    print("2 - INSERT")
    print("3 - UPDATE")
    print("4 - DELETE")
    print("\n")
    resp = int(input(">> "))

    if resp == 1:
        conn = Sql()
        conn.select()
    elif resp == 2:
        conn = Sql()
        conn.insert()
    elif resp == 3:
        conn = Sql()
        conn.update()
    elif resp == 4:
        conn = Sql()
        conn.delete()


    

class Sql:

    def conectar(self):
        conexao = pyodbc.connect(infos)
        if conexao:
            opcoes()

    def select(self):
        tabela = input('Insira o nome da tabela: ')
        conexao = pyodbc.connect(infos)
        query = conexao.cursor()

        query.execute("select * from " + tabela + "")
        row = query.fetchall()
        for r in row:
            print(r)
        
        print("Finalizando SELECT...")
        ask = input("Deseja continuar? 1-SIM || 2-NÃO ")
        if ask == 1:
            opcoes()
        elif ask == 2:
            print("Saindo...")
            exit()
        else:
            print("Opção não encontrada, saindo...")
            exit()
        


    def insert(self):
        tabela = input('Insira o nome da tabela >> ')
        colunas = input('Insira o nome das colunas (Ex: nome, email, senha) >> ')
        valores = input('Insira os valores (Ex: Ronaldo, a@gmail.com, 123) entre aspas simples >> ')
        
        conexao = pyodbc.connect(infos)
        query = conexao.cursor()

        query.execute("insert into " + tabela + " (" + colunas + ") values ('" + valores + "')")

        print("Finalizando INSERT...")
        ask = int(input("Deseja continuar? 1-SIM || 2-NÃO >> "))
        if ask == 1:
            opcoes()
        elif ask == 2:
            print("Saindo...")
            exit()
        else:
            print("Opção não encontrada, saindo...")
            exit()
        





    def update(self):
        print("update")



    def delete(self):
        print("delete")
        
    



driver = input('Driver [SQL Server]: ')
host = input('Host [DESKTOP-IJLS6KT]: ')
db = input('Database [pythonsqlteste]: ')

infos = (
    "Driver=" + driver + ";"
    "Server=" + host + ";"
    "Database=" + db + ";"
)



if driver != "" and host != "" and db != "":
    print("Iniciando conexão")
    conn = Sql()
    conn.conectar()
else:
    print("Não foi possível estabelecer uma conexão, tente novamente!")
    exit()



