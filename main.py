import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.button import Button
abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", " "] #abc
def codificar(mensaje,clave): #funcion de codificacion
    resu=""
    longitud = len(mensaje)  # len permite que contemos la cantidad de caracteres
    for i in range(0, longitud):  # este ciclo recorre el texto
        for pos in range(0, 27):  # este ciclo recorre el abc
            if mensaje[i] == abc[pos]:  # comparar las letras
                pos_abc = pos + int(clave)  # desplazarnos en el abc, segun la clave
                if pos_abc < 27:
                    resu+=abc[pos_abc]+""
                if pos_abc > 27:  # en el caso de que nos pasemos, calculamos el resto
                    resu+=abc[pos_abc % 27]+""
            else:
                resu+=""
    return resu
def decodificar(mensaje,clave): #funcion de decodificacion
    resu=""
    longitud = len(mensaje)
    for i in range(0, longitud):
        for pos in range(0, 27):
            if mensaje[i] == abc[pos]:
                pos_abc = pos - int(clave)  #se desplaza de forma inversa
                if pos_abc < 27:
                    resu+=abc[pos_abc]+""
                if pos_abc > 27:
                    resu+=abc[pos_abc % 27]+""
            else:
                resu+=""
    return resu

class MyApp(App): #se crea una clase aplicacion
    def build(self): #funcion que crea esta clase
       return MyGrid()

class MyGrid(GridLayout): #se crea una clase grilla
    def __init__(self, **kwargs): #esta es la funcion que inicia la grilla
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2 #se configura la cantidad de columnas de la grilla

        #self refiere a que la misma clase
        self.add_widget(Label(text="Mensaje ")) #add_widget sirve para agregar un widget a la gui, Label que es etiqueta donde podemos poner un titulo o texto
        self.mensaje = TextInput(multiline=False) #aqui agregamos un cuadro de texto donde se pueda ingresar el texto a codificar
        self.add_widget(self.mensaje) #se inicia el cuadro de texto que agregamos que agregamos

        self.add_widget(Label(text="Clave "))
        self.clave = TextInput(multiline=False)
        self.add_widget(self.clave)

        self.add_widget(Label(text="Tu codigo"))
        self.resultado = TextInput(multiline=True)
        self.add_widget(self.resultado)

        self.codificar = Button(text="Codificar", font_size=40) #aqui creamos un boton utilizando la libreria button
        self.codificar.bind(on_press=self.pressed) #aqui se crea una expresion para nombrar al boton como presionado
        self.add_widget(self.codificar)#agregamos el boton creado
        self.decodificar = Button(text="Decodificar", font_size=40)
        self.decodificar.bind(on_press=self.pressedd)
        self.add_widget(self.decodificar)

    def pressed(self, instance): #se crea una funcion que al presionar el boton, tome los datos del cuadro de texto mensaje y clave.
        mensaje = self.mensaje.text
        clave = self.clave.text
        self.resultado.text=codificar(mensaje, clave)#se configura el cuadro de texto de resultado y los rellenamos con la funcion codificar creada al principio, que tiene como parametros mensaje y clave.

    def pressedd(self, instance):
        mensaje = self.mensaje.text
        clave = self.clave.text
        self.resultado.text = decodificar(mensaje, clave)


MyApp().run()
