from tkinter import *
from mysql import Database

mysql=Database()


class Window(object):
    def __init__(self,master):
        self.master=master
        self.master.wm_title("Crea Tabella")

        l_nome=Label(master,text="Nome")
        l_nome.grid(row=0,column=0)

        l_nomcol=Label(master,text="Nome Colonna")
        l_nomcol.grid(row=1,column=0)

        l_tipocol=Label(master,text="Tipo Colonna")
        l_tipocol.grid(row=1,column=1)

        self.v_nome=StringVar()
        self.e_nome=Entry(master,textvariable=self.v_nome)
        self.e_nome.grid(row=0,column=1)



        self.b_mostra=Button(master,text="Mostra Tabella",width=12,command=self.show_command)
        self.b_mostra.grid(row=0,column=2)

        self.b_chiudi=Button(master,text="Chiudi",width=12,command=self.master.destroy)
        self.b_chiudi.grid(row=0,column=3)



    global entrato
    global row
    global n

    entrato=False
    def show_command(self):
        global entrato
        global row
        global n
        
        if entrato:
            if row["self.v_nom"+str(n)]:
                row["self.v_nom"+str(n)].grid_remove()

        rows=mysql.describe_table(self.v_nome.get())
        n=1
        for row in rows:
            print(row['Field'],row['Type'])

            row["self.v_nom"+str(n)]=StringVar(master,value=row['Field'])
            row["self.e_nom"+str(n)]=Entry(master,textvariable=row["self.v_nom"+str(n)])
            row["self.e_nom"+str(n)].grid(row=n+1,column=0)

            row["self.v_tipo"+str(n)] = StringVar()
            row["self.v_tipo"+str(n)].set(row['Type']) # default value
            row["self.e_tipo"+str(n)] = OptionMenu(master, row["self.v_tipo"+str(n)], "TEXT", "INTEGER", "int(11)")
            row["self.e_tipo"+str(n)].grid(row=n+1,column=1)
            n=n+1

            entrato=True
        #print(rows)



master=Tk()
Window(master)
master.mainloop()
