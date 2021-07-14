import PySimpleGUI as sg
import googletrans
from googletrans import Translator
import threading
import webbrowser
translator = Translator()

class traductor:
    def __init__(self):
        self.datos_lenguajes = googletrans.LANGUAGES
        self.frame_de = [
            [sg.Multiline(default_text='',size=(40, 20), key='-txt_a_traducir_')]
        ]
        frame_a = [
            [sg.Multiline(disabled=True, size=(40, 20), key= '-txt_traduccion_')]
        ]
        lenguajesA = ['Detectar idioma']
        lenguajesB = []
        for lenguaje in self.datos_lenguajes.values():
            lenguajesA.append(lenguaje)
            lenguajesB.append(lenguaje)
        #lenguajes= self.lenguajes.keys()
        #print(lenguajes)
        frame_lenguajes = [
            [sg.Text('De')],
            [sg.Combo(values= lenguajesA, key='-lenguaje_de-', default_value='Detectar idioma')],
            [sg.Text('A')],
            [sg.Combo(values=lenguajesB, key='-lenguaje_a-', default_value= 'english')],
            [sg.Button('Traducir', key='-traducir-')]
        ]

        self.layout_traductor = [[sg.Text('Traductor')],
                                 [sg.Frame('Texto a traducir', self.frame_de,  ),sg.Frame('Lenguajes', frame_lenguajes),  sg.Frame('Texto Traducido', frame_a)],

                                 ]
        self.frame_about = [
            [sg.Text('Contacto', font='Any 20', justification='c')],
            [sg.Text(
                'Si te gusto esta aplicacion, tienes alguna sugerencia, ocurrio un error, deseas apoyar el desarrollo o ponerte en contacto conmigo, te dejo mis redes sociales.\n'
                'Si quieres reportar un problema, por favor añade la siguiente informacion: Sistema operativo, Version de Python, Detalles del problema.\n'
                '', )],
            [sg.Button('Facebook', size=(15, 1)), sg.Button('Twitter', size=(15, 1)), sg.Button('Blog', size=(15, 1)),
             sg.Button('Correo', size=(15, 1)), sg.Button('Invitame un Cafe', size=(15, 1))]
        ]

        self.estado_traduccion =  False
        self.texto_traduccion = ''

def traducir(self, texto, de, a):
    self.estado_traduccion =  True
    try:
        traduccion = translator.translate(text=texto, src=de, dest = a)
        self.estado_traduccion = False
        return traduccion.text
    except:
        self.estado_traduccion = False
        self.texto_traduccion = "Error en la traduccion"


def detectar_idioma(self, texto, a):
    self.estado_traduccion =  True
    try:
        traduccion =  translator.translate(text=texto, dest = a)
        self.estado_traduccion = False
        self.texto_traduccion = traduccion.text
    except:
        self.estado_traduccion = False
        self.texto_traduccion = "Error en la traduccion"


def getKeyIdioma(self, lenguaje):
    for valores in self.datos_lenguajes.items():
        if valores[1]==lenguaje:
            return valores[0]

def ventana_espera(self):
    self.blue_dots = ""
    self.gif = self.blue_dots
    self.layout_espera = [
        [sg.Image(data=self.blue_dots, enable_events=True, background_color='white', key='_IMAGE_',
                  right_click_menu=['UNUSED', 'Exit'])],
        [sg.Button('Cancelar', key='-cancelar-')]]

    self.window_espera = sg.Window('My new window', no_titlebar=True, grab_anywhere=True, keep_on_top=True,
                                   background_color='white',
                                   alpha_channel=.8, margins=(0, 0)).Layout(self.layout_espera)

def iniciar_ejecucion(self):
    tab3 = sg.Tab('Traductor', self.layout_traductor, tooltip=Translator, title_color='red')
    tab4 = sg.Tab('Acerca de', self.frame_about , tooltip="Acerca De", title_color='red')
    layout = [
        [sg.TabGroup([[tab3, tab4]], key='_TAB_GROUP_', )]
    ]
    window = sg.Window('Traductor Facialix', layout)
    traduccion = window['-txt_traduccion_']

    while True:
        event, value = window.read(10)
        #print(value)
        #print("dasdasd")
        if event in ('Exit', None):
            window.close()

        if self.texto_traduccion != '':
            #print("asdasd")
            traduccion.update(self.texto_traduccion)
            self.texto_traduccion = ''
        if event == '-traducir-':
            if value['-lenguaje_de-'] == 'Detectar idioma':
                a = self.getKeyIdioma(value['-lenguaje_a-'])
                #texto_traduccion = self.detectar_idioma(value['-txt_a_traducir_'], a = a)
                #traduccion.update(texto_traduccion)
                d = threading.Thread(target=self.detectar_idioma, args=(value['-txt_a_traducir_'], a,),
                                     daemon=True)
                d.start()
            else:
                de = self.getKeyIdioma(value['-lenguaje_de-'])
                a = self.getKeyIdioma(value['-lenguaje_a-'])
                #texto_traduccion = self.traducir(value['-txt_a_traducir_'], de = de, a = a)
                #traduccion.update(texto_traduccion)
                d = threading.Thread(target=self.traducir, args=(value['-txt_a_traducir_'],de, a,),
                                     daemon=True)
                d.start()

            self.ventana_espera()
            while True:
                if self.estado_traduccion == True:
                    event, values = self.window_espera.read(timeout=0)
                    self.window_espera.Element('_IMAGE_').UpdateAnimation(self.gif, time_between_frames=50)
                    if event == '-cancelar-':
                        self.window_espera.close()
                        break
                else:
                    self.window_espera.close()
                    break
        elif event == 'Facebook':
            webbrowser.open('https://www.facebook.com/facialix')
        elif event == 'Twitter':
            webbrowser.open('https://www.twitter.com/facialix')
        elif event == 'Blog':
            webbrowser.open('http://blog.facialix.com')
        elif  event == 'Correo':
            recipent = 'julio16101@facialix.com'
            webbrowser.open("mailto:?to=" + recipent)
        elif event == 'Invitame un Cafe':
            webbrowser.open('https://www.buymeacoffee.com/kUh9e5D')

