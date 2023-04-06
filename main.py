import speech_recognition as sr
import pyttsx3
import os
from email.message import EmailMessage
import ssl
import smtplib
import pywhatkit
import eel
import wikipedia
import unidecode
import subprocess as sub
import csv

eel.init("web")


r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def enviar_correo(comando):
    try:
        correo = "svsm2403@gmail.com"

        #CLAVE GENERADO POR GOOGLE GUARDADA COMO VARIABLE DE ENTORNO PARA MAYOR SEGURIDAD
        clave = os.environ.get("EMAIL_CLAVE")
        #PROCEDIMIENTO PARA ENVIAR CORREOS (LIBRERIA: email.message)

        with open('contactos.csv', mode='r') as infile:
            reader = csv.reader(infile)
            contactos = {rows[0]:rows[1] for rows in reader}


        for contacto in contactos:
            if contacto in comando:
                destinatario = contacto

        em = EmailMessage()
        em["From"] = correo
        em["To"] = contactos[destinatario]


        with sr.Microphone() as source:
            print("Escuchando...")
            engine.say("Cual es el asunto?")
            engine.runAndWait()
            audio = r.listen(source)

            try:
                comando = r.recognize_google(audio, language="es-MX")
                print(f"Asunto: {comando}")
                engine.say(f"Entendido. {comando}")
                engine.runAndWait()
                asunto = comando

            except Exception as e:
                print(f"No se pudo reconocer el comando: {e}")
                engine.say("No se pudo reconocer el asunto")
                engine.runAndWait()


        with sr.Microphone() as source:
            print("Escuchando...")
            engine.say("Cual es el mensaje?")
            engine.runAndWait()
            audio = r.listen(source)

            try:
                comando = r.recognize_google(audio, language="es-MX")
                print(f"Mensaje: {comando}")
                engine.say(f"Entendido. {comando}")
                engine.runAndWait()
                mensaje = comando

            except Exception as e:
                print(f"No se pudo reconocer el comando: {e}")
                engine.say("No se pudo reconocer el mensaje")
                engine.runAndWait()

        em["Subject"] = asunto
        em.set_content(mensaje)

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(correo,clave)
            smtp.sendmail(correo, contactos[destinatario], em.as_string())

        print("Correo enviado")
        engine.say("Correo enviado")
        engine.runAndWait()
    except Exception as e:
        print(f"No se pudo enviar el correo: {e}")
        engine.say("No se pudo enviar el correo")
        engine.runAndWait()

def abrir_aplicacion(comando):

    with open('programas.csv', mode='r') as infile:
        reader = csv.reader(infile)
        programas = {rows[0]:rows[1] for rows in reader}


    try:
        for app in programas:
            if app in comando:
                engine.say(f"Abriendo {app}")
                engine.runAndWait()
                os.startfile(programas[app])
        
    except Exception as e:
        print(f"No se pudo abrir la aplicación: {e}")
        engine.say("No se pudo abrir la aplicación")
        engine.runAndWait()

def musica(comando):
    com = comando
    if "reproduce" in com:
        music = com.replace("reproduce", "")
    elif "pon" in com:
        music = com.replace("pon", "")
    print("Reproduciendo" + music)
    engine.say("Reproduciendo" + music)
    engine.runAndWait()
    pywhatkit.playonyt(music)
    
def wiki(comando):
    search = comando
    if  "busca que es el" in search:
        search = search.replace("busca que es el", "")
    if  "busca que es la" in search:
        search = search.replace("busca que es la", "")
    elif "busca" in search:
        search = search.replace("busca", "")
    elif "que es el" in search:
        search = search.replace("que es el", "")
    elif "que es la" in search:
        search = search.replace("que es la", "")
    elif  "que es" in search:
        search = search.replace("que es", "")

    wikipedia.set_lang("es")
    wiki = wikipedia.summary(search, 1)
    print(search + ": "+ wiki)
    engine.say(wiki)
    engine.runAndWait()

def write(f,com):
    com = com.replace("escribe", "")
    com = com.strip()
    f.write(com + os.linesep)
    f.close()
    engine.say("Listo, puedes revisar tu archivo")
    engine.runAndWait()
    sub.Popen("nota.txt", shell=True)

def asistente():
    with sr.Microphone() as source:
        print("Escuchando...")
        engine.say("¿En qué puedo ayudarte?")
        engine.runAndWait()
        audio = r.listen(source)

        try:
            comando = r.recognize_google(audio, language="es-MX")
            if "Jules" in comando:
                comando = comando.replace("Jules", "")
            print(f"Comando: {comando}")
            engine.say(f"Entendido. {comando}")
            engine.runAndWait()
            comando = comando.lower()
            comando = unidecode.unidecode(comando)
            
            if "correo" in comando:
                enviar_correo(comando)


            #PALABRAS QUE MANDAN A LLAMAR LA BUSQUEDA EN WIKIPEDIA
            elif "busca" in comando:
                wiki(comando)

            elif "que es" in comando:
                wiki(comando)


            #PALABRAS QUE ABREN APLICIONES
            elif "abrir" in comando:
                abrir_aplicacion(comando)
            
            elif "abre" in comando:
                abrir_aplicacion(comando)

            elif "inicia" in comando:
                abrir_aplicacion(comando)


            #PALABRAS QUE REPRODUCEN MUSICA
            elif "reproduce" in comando:
                musica(comando)

            elif "pon" in comando:
                musica(comando)


            elif "escribe" in comando:
                try:
                    with open("nota.txt", "a") as f:
                        write(f,comando)

                except FileNotFoundError as e:
                    file = open("nota.txt", "w")
                    write(file,comando)


            #SOLAMENTE PASA EL COMANDO
            elif "adios" in comando:
                print("Accion cancelada")

            elif "nada" in comando:
                print("Accion cancelada")

            else:
                engine.say("Comando no reconocido")
                engine.runAndWait()

        except Exception as e:
            print(f"No se pudo reconocer el comando: {e}")
            engine.say("No se pudo reconocer el comando")
            engine.runAndWait()


@eel.expose
def agregar_aplicacion(x,y):
    list_data = [x, y]
    with open('programas.csv', 'a', newline='') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow(list_data)

    return "Aplicacion agregada correctamente"

@eel.expose
def agregar_contacto(x,y):
    list_data = [x, y]
    with open('contactos.csv', 'a', newline='') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow(list_data)

    return "Contacto agregado correctamente"


@eel.expose
def main():
    engine.say("Hola soy Jules tu asistente virtual")
    engine.runAndWait()
    asistente()

    return "Starting python script"


print("Inicializando")
eel.start("index.html", size=(1000,600))