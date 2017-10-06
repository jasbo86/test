from tkinter import *
from tkinter import messagebox
from mysql import Database

mysql=Database()


class Window(object):
    def __init__(self,master):
        self.master=master
        self.master.wm_title("Crea Tabella")

        global n
        global row

        n=2
        row={}

        l_nome=Label(master,text="Nome")
        l_nome.grid(row=0,column=1)

        l_nomcol=Label(master,text="Nome Colonna")
        l_nomcol.grid(row=1,column=1)

        l_tipocol=Label(master,text="Tipo Colonna")
        l_tipocol.grid(row=1,column=2)

        l_num=Label(master,text="1")
        l_num.grid(row=2,column=0)

        #campo nome
        self.v_nome=StringVar()
        self.e_nome=Entry(master,textvariable=self.v_nome)
        self.e_nome.grid(row=0,column=2)

        #campo riga
        row["self.v_nom1"]=StringVar()
        row["self.e_nom1"]=Entry(master,textvariable=row["self.v_nom1"])
        row["self.e_nom1"].grid(row=2,column=1)

        #campo tipo
        row["self.v_tipo1"] = StringVar()
        row["self.v_tipo1"].set("TEXT") # default value
        row["self.e_tipo1"] = OptionMenu(master, row["self.v_tipo1"], "TEXT", "INTEGER")
        row["self.e_tipo1"].grid(row=2,column=2)


        self.b_crea=Button(master,text="Crea Tabella",width=12,command=self.create_command)
        self.b_crea.grid(row=0,column=3)

        self.b_chiudi=Button(master,text="Chiudi",width=12,command=self.master.destroy)
        self.b_chiudi.grid(row=0,column=4)

        self.b_add=Button(master,text="Add",width=12,command=self.add_row)
        self.b_add.grid(row=1,column=3)

    def add_row(self):
        global n
        global row
        l_num=Label(master,text=n)
        l_num.grid(row=n+1,column=0)
        row["self.v_nom"+str(n)]=StringVar()
        row["self.e_nom"+str(n)]=Entry(master,textvariable=row["self.v_nom"+str(n)])
        row["self.e_nom"+str(n)].grid(row=n+1,column=1)

        row["self.v_tipo"+str(n)] = StringVar()
        row["self.v_tipo"+str(n)].set("TEXT") # default value
        row["self.e_tipo"+str(n)] = OptionMenu(master, row["self.v_tipo"+str(n)], "TEXT", "INTEGER")
        row["self.e_tipo"+str(n)].grid(row=n+1,column=2)

        n=n+1

    def create_command(self):

        col=[]
        x=1
        while x != n:
            if row["self.v_nom"+str(x)].get():
                col.append(row["self.v_nom"+str(x)].get())
                col.append(row["self.v_tipo"+str(x)].get())
            else:
                messagebox.showerror("Errore", "Inserire Riga "+ str(x))
                return
            x=x+1

        if not self.v_nome.get():
            messagebox.showerror("Errore", "Inserire Nome Tabella")
            return

        if mysql.show_tables(self.v_nome.get()):
            messagebox.showerror("Errore", "Tabella già esistente")
            return

        if mysql.create_table(self.v_nome.get(),col):
            messagebox.showinfo("Creazione", "La Tabella '"+ self.v_nome.get() +"' è stata creata correttamente")


master=Tk()
Window(master)
master.mainloop()
