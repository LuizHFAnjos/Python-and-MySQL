import customtkinter as ctk 
from tkinter import *
import tkinter as tk
import mysql.connector



#Aparência do Sistema
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.apperance()
        self.all_system()
    


    def layout_config(self):
        self.title("Sistema de Gestão de Clientes")
        self.geometry("700x500")


    def apperance(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=['#000', '#fff']).place(x=50,y=430)
        self.opt_tema = ctk.CTkOptionMenu(self, values=['Light', 'Dark', 'System'], command=self.change_apm).place(x=50,y=460)
        

    def all_system(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0,bg_color='teal', fg_color='teal')
        frame.place(x=0,y=10)
        title = ctk.CTkLabel(frame, text='Sistema de Gestão de Clientes', font=('Century Gothic bold', 24), text_color='#fff').place(x=190,y=10)

        span = ctk.CTkLabel(self, text='Por favor, preencha todos os campos do fomulário!', font=('Century Gothic bold',16), text_color=['#000', '#fff']).place(x=50,y=70)

    


        def clear():
            name_value.set('')
            contact_value.set('')
            age_value.set('')
            adress_value.set('')
            obs_entry.delete(0.0, END)

        def Dados_submit():

            if not name_entry.get().strip():
                janela = tk.Tk()
                janela.title('ERROR')
                janela.geometry('300x100')
                texto = tk.Label(janela,text='Os dados não foram salvos!\nExistem campos não preenchidos!',font=("Arial,14"))
                texto.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
                janela.mainloop()
                return

            conexao = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='clientes',

            )

            cursor = conexao.cursor()

            comando = f'INSERT INTO pessoas (nome,contato,endereco,idade,genero,observacoes) VALUES ("{name_entry.get()}","{contact_entry.get()}", "{adress_entry.get()}","{age_entry.get()}","{gender_combox.get()}","{obs_entry.get(1.0, END)}")'
            cursor.execute(comando)
            conexao.commit()#edita o banco de dados


            cursor.close()
            conexao.close()


            janela = tk.Tk()
            janela.title('Dados Salvos')
            janela.geometry('250x100')
            texto = tk.Label(janela,text='Dados Salvos com Sucesso!',font=("Arial,14"))
            texto.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
            janela.mainloop()


        

        #text variables
        name_value = StringVar()
        contact_value = StringVar()
        age_value = StringVar()
        adress_value = StringVar()

        #Entry
        name_entry = ctk.CTkEntry(self, width=350, textvariable=name_value, font=('Century Gothic bold', 16), fg_color='transparent')
        contact_entry = ctk.CTkEntry(self, width=200, textvariable=contact_value,  font=('Century Gothic bold', 16), fg_color='transparent')
        age_entry = ctk.CTkEntry(self, width=150, textvariable=age_value, font=('Century Gothic bold', 16), fg_color='transparent')
        adress_entry = ctk.CTkEntry(self, width=200, textvariable=adress_value,  font=('Century Gothic bold', 16), fg_color='transparent')

        #Combobox
        gender_combox = ctk.CTkComboBox(self, values=['Masculino', 'Feminino'], font=('Century Gothic bold',14), width=150)
        gender_combox.set('Masculino')

        #Entrada de observações
        obs_entry = ctk.CTkTextbox(self, width=500, height=150, font=('arial', 18), border_color='#aaa', border_width=2, fg_color='transparent')




        #Label
        lb_name = ctk.CTkLabel(self, text='Nome comleto:', font=('Century Gothic bold',16), text_color=['#000', '#fff'])
        lb_contact = ctk.CTkLabel(self, text='Contato', font=('Century Gothic bold',16), text_color=['#000', '#fff'])
        lb_age = ctk.CTkLabel(self, text='Idade', font=('Century Gothic bold',16), text_color=['#000', '#fff'])
        lb_gander = ctk.CTkLabel(self, text='Gênero', font=('Century Gothic bold',16), text_color=['#000', '#fff'])
        lb_adress = ctk.CTkLabel(self, text='Endereço', font=('Century Gothic bold',16), text_color=['#000', '#fff'])
        lb_obs = ctk.CTkLabel(self, text='Observações', font=('Century Gothic bold',16), text_color=['#000', '#fff'])

        btn_submit = ctk.CTkButton(self, text='Salvar dados'.upper(),command=Dados_submit, fg_color='#151', hover_color='#131').place(x=300,y=420)
        btn_clear = ctk.CTkButton(self, text='Limpar campos'.upper(),command=clear, fg_color='#555', hover_color='#333').place(x=500,y=420)

        #Posicionando os elementos na janela
        lb_name.place(x=50,y=120)
        name_entry.place(x=50, y=150)

        lb_contact.place(x=450,y=120)
        contact_entry.place(x=450,y=150)

        lb_age.place(x=300,y=190)
        age_entry.place(x=300,y=220)

        lb_gander.place(x=500,y=190)
        gender_combox.place(x=500,y=220)

        lb_adress.place(x=50,y=190)
        adress_entry.place(x=50,y=220)

        lb_obs.place(x=50, y=260)
        obs_entry.place(x=150,y=260)




    def change_apm(self,nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)





if __name__=="__main__":
    app = App()
    app.mainloop()       

