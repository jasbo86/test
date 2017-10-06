from mysql import Database

mysql=Database()
nome="prova"
col=[]
col.append("nome")
col.append("TEXT")
col.append("cognome")
col.append("TEXT")
col.append("eta")
col.append("INTEGER")


mysql.create_table(nome,col)
