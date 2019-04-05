from tkinter import Frame, Button, Label, Entry
from tkinter import messagebox as mbox
from tkinter import filedialog
import re

class mainFrame(Frame):  
    def __init__(self):
        super().__init__()   
        self.initUI()

        
    def initUI(self):
        self.master.title('App')
        self.master.resizable(0,0)
        self.lb01 = Label(self, text='Developed by Shahram Shaygani under GNU GPLv3')
        self.lb01.grid(row=0, column=0, padx=3, pady=3)
        self.lb02 = Label(self, text='R top')
        self.lb02.grid(row=1, column=0, padx=3, pady=3)
        self.en01 = Entry(self)
        self.en01.grid(row=1, column=1, padx=3, pady=3)
        self.lb03 = Label(self, text='R bottom')
        self.lb03.grid(row=2, column=0, padx=3, pady=3)
        self.en02 = Entry(self)
        self.en02.grid(row=2, column=1, padx=3, pady=3)
        self.btn01 = Button(self, text='Open txt file...', command=self.onOpen1)
        self.btn01.grid(row=3, column=0, padx=3, pady=3)
        self.btn02 = Button(self, text='Open e2k file...', command=self.onOpen2)
        self.btn02.grid(row=4, column=0, padx=3, pady=3)
        self.btn03 = Button(self, text='Change', command=self.onChange)
        self.btn03.grid(row=5, column=0, padx=3, pady=3)
        self.grid()
        

    def onOpen1(self):
        ftypes = [('*.txt', '*.txt')]
        dlg1 = filedialog.Open(self, filetypes = ftypes)
        self.txtPath = dlg1.show()


    def onOpen2(self):
        ftypes = [('*.e2k', '*.e2k')]
        dlg2 = filedialog.Open(self, filetypes = ftypes)
        self.e2kPath = dlg2.show() 
        
    def getTopSt(self):
        fe2k = open(self.e2kPath, 'r')
        me2k = fe2k.read()
        topst = re.search(r'^  STORY "(.+?)"  HEIGHT .+?$', me2k, re.M)
        topst = topst.group(1)
        fe2k.close()
        return topst
    
    def getLc(self):
        fe2k = open(self.e2kPath, 'r')
        me2k = fe2k.read()
        lc = []
        for m in re.finditer(r'^  LOADCASE "(.+?)".+?$', me2k, re.M):
            lc.append(m.group(1))
        fe2k.close()
        return lc

    def getLce(self):
        fe2k = open(self.e2kPath, 'r')
        me2k = fe2k.read()
        lce = []
        for m in re.finditer(r'^  SEISMIC "(.+?)"  .+?$', me2k, re.M):
            lce.append(m.group(1))
        fe2k.close()
        return lce


    def onChange(self):
        if ((self.txtPath) and (self.e2kPath)):
            r = (float(self.en01.get())/float(self.en02.get()))
            fe2k = open(self.e2kPath, 'r+')
            ftxt = open(self.txtPath, 'r+')
            me2k = fe2k.read()
            mtxt = ftxt.read()
            lc = self.getLc()
            lce = self.getLce()
            lc = list(set(lc)-set(lce))
            topst = self.getTopSt()
            strSubt = ''
            for m in re.finditer(r'(^ BASE        \d+?.+?$)', mtxt, re.M):
                strm = m.group(1)
                strm = strm.split()
                if (strm[2] in lc):
                    strload = ('  POINTLOAD  "{}"  "{}"  TYPE "FORCE"  LC "{}"'
                               '  FX {}  FY {}  FZ {}  MX {}  MY {}  MZ {}'
                               .format(strm[1],
                                       topst,
                                       strm[2],
                                       str(-float(strm[3])),
                                       str(-float(strm[4])),
                                       str(-float(strm[5])),
                                       str(-float(strm[6])),
                                       str(-float(strm[7])),
                                       str(-float(strm[8]))))
                    strSubt += strload+'\n'
                elif (strm[2] in lce):
                    strload = ('  POINTLOAD  "{}"  "{}"  TYPE "FORCE"  LC "{}"'
                               '  FX {}  FY {}  FZ {}  MX {}  MY {}  MZ {}'
                               .format(strm[1],
                                       topst,
                                       strm[2],
                                       str(-float(strm[3])*r),
                                       str(-float(strm[4])*r),
                                       str(-float(strm[5])*r),
                                       str(-float(strm[6])*r),
                                       str(-float(strm[7])*r),
                                       str(-float(strm[8])*r)))
                    strSubt += strload+'\n'
            
            
            me2k = re.sub('POINT OBJECT LOADS','POINT OBJECT LOADS\n'
                          +strSubt, me2k, re.M)
            ftxt.close()
            fe2k.close()
            fe2k =  open(self.e2kPath, 'w+')
            fe2k.write(me2k)
            fe2k.close()
            mbox.showinfo('Information', 'Done!')
        else:
            mbox.showinfo('Information', 'No Input')


def main():
    app = mainFrame()
    app.mainloop()


if __name__ == '__main__':
    main()

