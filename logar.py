from flet import *
import flet as ft
import datetime
import threading as th
import os
os.system ('cls')

class Input(UserControl):
    def __init__(self, hint_text,icon,password=False):
        super().__init__()
        self.hint_text =hint_text
        self.icon = icon
        self.password = password
    def build(self):
        
        return Container(
            Row([
                Icon(
                    self.icon,
                    color='white',
                    
                ),
                TextField(
                    border='none',
                    color='white',
                    cursor_color='white',
                    height=40,
                    text_style=TextStyle(
                        size=18),                               #Esse bloco é da fonte e color  da senha!
                    password=self.password,
                    hint_text=self.hint_text,
                    hint_style=TextStyle(       
                        size=18,
                        weight='w500',
                        color='white'
                                        
                    )
                )
            ]),border=border.only(bottom=BorderSide(2,'white'))
        )
        
class Button(UserControl):
    def __init__(self,text):                #Criando uma classe de botão, definindo uma função self.
        super().__init__()
        self.text=text
        self.btn = Container(
            Text(
                self.text,                    #Esse bloco é a customização dos botões de cadastro e logar
                color='white',
                font_family='arial'
                
            ) ,
            border=border.all(1,'white'),
            border_radius=3,
            padding=padding.only(10,3,10,3),            
            alignment=alignment.center,
            on_hover=self.Hover,
            animate=animation.Animation(250),
                        
        )
    def Hover(self):        
        if self.btn.bgcolor =='#770b6e65':
            self.btn.bgcolor='transparent'
        else:
            self.btn.bgcolor='#770b6e65'
        self.btn.update()
    def build (self):
        return self.btn

class timeline(UserControl):
    def __init__(self):
        super().__init__()
        self.now = datetime.datetime.now()
        self.date =self.now.strftime("%A, %B, %d")      #Esse é o bloco  que descreve a classe da timeline
        self.time= self.now.strftime("%H, %M")          #da qual irá aparecer a data e a hora!
    
        self.field_date = Text(
                self.date,
                color='white',
                 size=20,
        ),
        self.field_time = Text(
          self.time,
          color='white',
          size=20, 
        ),
        
        
    def build(self):
        return Container(
            Column([
               self.field_date,
               self.field_time,
                ]),
            width=300,
            height=100,
            alignment=alignment.center
            
        ),
   

body = Container(
    Stack([
        Image(
            'fundo9.jpg',      #Coloquei uma imagem do próprio google aqui pela função Stack juntamente com a tag image!
            width=650,
            height=630,             #aqui a configuração de altura e largura!
            top=0,
            
        ),
        Container(
            timeline(),
            top=60,
            width=300,
            left=30,
            height=80,
            
            ),
        Container(
            timeline(),
            top=60,
            width=380,     #Esse é o bloco onde fica o layout do Tempo!
            left=30,        
            height=80,
             
            
        ),
        Container(      
            Column([
               
                Input('Usuário',icons.PERSON),
                Input('Senha',icons.KEY,password=True),  #Aqui onde o usuário irá colocar as suas credenciais!
                Container(
                    Row([
                        Button('cadastrar'),
                        Button('Login'),
                        
                    ],alignment='center',spacing=30)
                ),
            ],spacing='15'),
            width=260,
            height=280,
            top=430,
            left=20,
           
           
        )
    ]),
    width=650,
    height=640, #essa aqui é a configuração
)

def main (page:Page):
    page.window_max_width=650
    page.window_width=650           #Esse bloco aqui é o tamanho da janela page. Denominada Main 
    page.window_max_height= 630
    page.window_height= 630
    
    
    page.padding = 0
    page.add(
        body
    )
app(target=main)   #Essa linha de código é o que faz todo o mini software funcionar, o que traz a interface!