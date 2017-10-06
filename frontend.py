from tkinter import *
from mysql import Database
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    #sys.exit(0)
#print "I am root now."

mysql=Database()


class Window(object):
    def __init__(self,master):
        self.master=master
        self.master.wm_title("Tabelle")


        self.b_crea=Button(master,text="Crea Tabella",width=12,command=self.open_create_command)
        self.b_crea.grid(row=0,column=0)

        self.b_crea=Button(master,text="Cerca Tabella",width=12,command=self.open_search_command)
        self.b_crea.grid(row=0,column=1)

        self.b_chiudi=Button(master,text="Chiudi",width=12,command=self.master.destroy)
        self.b_chiudi.grid(row=2,column=0)




    def open_create_command(self):
        os.system("create.py")

    def open_search_command(self):
        os.system("search.py")


master=Tk()
Window(master)
master.mainloop()
