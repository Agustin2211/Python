from typing import MutableSequence
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes 

engine = pyttsx3.init()

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M")
    speak("La hora actual es")
    speak(time)

def date():
    año = int(datetime.datetime.now().year)
    mes = int(datetime.datetime.now().month)
    dia = int(datetime.datetime.now().day)

    speak("La fecha de hoy es: ")
    speak(dia)
    speak("del")
    speak(mes)
    speak("del año")
    speak(año)

def saludo():
    hora = datetime.datetime.now().hour
    if hora >= 6 and hora <= 12:
        speak("Buenos Dias")
    elif hora > 12 and hora <= 19:
        speak("Buenas Tardes")
    else:
        speak ("Buenas Noches")

def wishme():
    saludo()
    speak("Bienvenido, soy tu asistente")
    speak("¿Con que puedo ayudarlo en esta ocacion?")

def tomarComando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.paused_threshold = 1
        audio = r.listen(source)   
    try:
        print("Reconociendo")
        query = r.recognize_google(audio, 'en=ES')
        print(query)
    except Exception as e:
        print(e)
        speak("No te entendi, por favor, repita")
        return "Nada"
    return query

def mandarMail(persona, contenido):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test") #ESTE MAIL SE TIENE QUE CAMBIAR POR UNO REAL
    server.sendmail("test@gmail.com", persona, contenido)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\Escritorio")

def cpu():
    usage = str(psutil.cpu_ercent())
    speak("Se esta usando" + usage + "de CPU")

def battery():
    battery = psutil.sensors_battery
    speak("Actualmente hay un" + battery.percent + "porciento de bateria")

def chistes():
    speak(pyjokes.get_joke())

#Funcion Principal

if __name__ == "__main__":

    wishme()

    while True:
        query = tomarComando().lower()
        print (query)

        if "hora" in query:
            time()

        elif "fecha" in query:
            date()

        elif "buscar" in query:
            speak("Buscando en Wikipedia")
            query = query.replace("wikipedia", "")
            wikipedia.languages("es")
            resultado = wikipedia.summary(query, 2)
            speak(resultado)

        elif "mandar mail" in query:
            try:
                speak("¿Que quieres que escriba en el mail?")
                contenido = tomarComando()
                persona = "xyz@gmail.com" #CAMBIAR POR MAIL A LA PERSONA QUE LE QUIERO ENVIAR
                mandarMail(persona, contenido)
                speak("El contenido del mail es el siguiente: ", contenido)
                speak("El mail se ha enviado correctamente")
            except Exception as e:
                speak(e)
                speak("No he podido enviarte el email")
        
        elif "abrir pestaña" in query:
            speak("¿Que es lo que quieres buscar?")
            chromepath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            buscar = tomarComando().lower()
            wb.get(chromepath).open_new_tab(buscar + ".com")
        
        elif "cerrar sesion" in query:
            os.system("shutdown - 1")

        elif "reiniciar" in query:
            os.system("shutdown /r /t 1")

        elif "apagar" in query:
            os.system("shutdown /s /t 1")

        elif "escuchar musica" in query:
            carpetaConMusica = "C:\Música"
            canciones = os.listdir(carpetaConMusica)
            os.startfile(os.path.join(carpetaConMusica, canciones[0]))

        elif "recordar" in query:
            speak("¿Que quieres que te haga recordar?")
            queHagoRecordar = tomarComando()
            speak("Lo que quieres recordar es:" + queHagoRecordar)
            recordar = open("data.txt", "w")
            recordar.write(queHagoRecordar)
            recordar.close()  

        elif "necesito saber algo" in query:
            recordar = open("data.txt", "r")
            speak("Te hago recordar lo siguiente: " + recordar.read())

        elif "screenshot" in query:
            screenshot()
            speak("La Screenshot se ha realizado")

        elif "cpu" in query:
            cpu()

        elif "bateria" in query:
            battery()

        elif "chiste" in query:
            chistes()

        elif "adios" in query:
            quit()