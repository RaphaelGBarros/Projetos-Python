from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('Arialblack', '10')
        self.container1 = Frame(master)
        self.container1['pady'] = '15'
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2['padx'] = '20'
        self.container2['pady'] = '10'
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3['padx'] = '20'
        self.container3['padx'] = '10'
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['padx'] = '20'
        self.container4['padx'] = '10'
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5['padx'] = '20'
        self.container5['padx'] = '10'
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6['padx'] = '20'
        self.container6['padx'] = '10'
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7['padx'] = '20'
        self.container7['padx'] = '10'
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8['padx'] = '20'
        self.container8['padx'] = '10'
        self.container8.pack()

        self.titulo = Label(self.container1)
        self.titulo['text'] = '============== Agendamento de Consulta =============='
        self.titulo['font'] = self.fontePadrao
        self.titulo.pack()

        self.texto = Label(self.container2)
        self.texto['text'] = 'bem vindo ao Hospital do Olho\n Deseja agendar uma consulta ?'
        self.texto.pack(side=LEFT)

        self.botao = Button(self.container7, width=10)
        self.botao['text'] = 'sim'
        self.botao['command'] = self.iniciar
        self.botao['padx'] = '10'
        self.botao.pack(side=RIGHT)

    def iniciar(self):
        
        self.texto['text'] = 'Deseja prosseguir com o agendamento ??'
        
        self.botao['text'] = 'sim'
        self.botao['command'] = self.continuar

        self.botao2 = Button(self.container7, width=10)
        self.botao2['text'] = 'nao'
        self.botao2['command'] = self.sair
        self.botao2['padx'] = '10'
        self.botao2.pack(side=LEFT)

    def sair(self):
        exit()

    def continuar(self):
        self.texto['text'] = 'Antes de prosseguir precisamos saber\n se voce esta de acordo com os protocolos contra a covid 19?'
        
        self.botao['command'] = self.entrada

        self.botao2['command'] = self.sair

    def entrada(self):
        self.texto['text'] = 'Nome Completo: '
        
        self.voce = Entry(self.container2)
        self.voce['width'] = 10
        self.voce.pack(side=RIGHT)

        self.texto2 = Label(self.container3)
        self.texto2['text'] = 'Data de Nascimento: '
        self.texto2.pack(side=LEFT)

        self.olho = Entry(self.container3)
        self.olho['width'] = 10
        self.olho.pack()

        self.texto2 = Label(self.container4)
        self.texto2['text'] = 'Telefone: '
        self.texto2.pack(side=LEFT)

        self.olho = Entry(self.container4)
        self.olho['width'] = 10
        self.olho.pack()

        self.texto2 = Label(self.container6)
        self.texto2['text'] = 'Horario de Agendamento: '
        self.texto2.pack(side=LEFT)

        self.olho = Entry(self.container6)
        self.olho['width'] = 10
        self.olho.pack()
    

        self.botao['text'] = 'agendar'
        self.botao['command'] = self.agendar

        self.botao2['text'] = 'sair'
        self.botao2['command'] = self.sair



    def agendar(self):

        self.resultado = Label(self.container8)
        self.resultado['text'] = 'Agendamento concluído com sucesso!!!!'
        #self.resultado['pady'] = 1
        self.resultado.pack()



root = Tk()
Application(root)
root.title('Hospital do Olho - DC')
root.geometry('500x350')
root.mainloop()
