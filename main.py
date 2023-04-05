import speech_recognition as sr
import pyttsx3
import os
from email.message import EmailMessage
import ssl
import smtplib
import pywhatkit
import eel


eel.init("web")

programas = {
    "discord": r"C:\Users\Usuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
    "zoom": r"C:\Users\Usuario\AppData\Roaming\Zoom\bin\Zoom.exe",
    "Epic": r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
}

def enviar_correo(destinatario, asunto, mensaje):
    try:
        correo = "svsm2403@gmail.com"

        #CLAVE GENERADO POR GOOGLE GUARDADA COMO VARIABLE DE ENTORNO PARA MAYOR SEGURIDAD
        clave = os.environ.get("EMAIL_CLAVE")
        #PROCEDIMIENTO PARA ENVIAR CORREOS (LIBRERIA: email.message)
        em = EmailMessage()
        em["From"] = correo
        em["To"] = destinatario
        em["Subject"] = asunto
        em.set_content(mensaje)

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(correo,clave)
            smtp.sendmail(correo, destinatario, em.as_string())

        engine.say("Correo enviado")
        engine.runAndWait()
    except Exception as e:
        print(f"No se pudo enviar el correo: {e}")
        engine.say("No se pudo enviar el correo")
        engine.runAndWait()

def abrir_aplicacion(comando):
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
    if "pon" in com:
        music = com.replace("pon", "")
    print("Reproduciendo" + music)
    engine.say("Reproduciendo" + music)
    engine.runAndWait()
    pywhatkit.playonyt(music)

    
r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def asistente():
    with sr.Microphone() as source:
        print("Escuchando...")
        engine.say("¿En qué puedo ayudarte?")
        engine.runAndWait()
        audio = r.listen(source)

        try:
            comando = r.recognize_google(audio, language="es-ES")
            print(f"Comando: {comando}")
            engine.say(f"Entendido. {comando}")
            engine.runAndWait()
            comando = comando.lower()
            
            if "correo" in comando:
                destinatario = input("Indica el correo del destinatario: ")
                asunto = input("Indica el asunto del correo: ")
                mensaje = input("Indica el mensaje del correo: ")
                enviar_correo(destinatario, asunto, mensaje)

            elif "abrir" in comando:
                abrir_aplicacion(comando)

            elif "reproduce" in comando:
                musica(comando)

            elif "pon" in comando:
                musica(comando)

            elif "adiós" in comando:
                exit()

            else:
                engine.say("Comando no reconocido")
                engine.runAndWait()

        except Exception as e:
            print(f"No se pudo reconocer el comando: {e}")
            engine.say("No se pudo reconocer el comando")
            engine.runAndWait()

@eel.expose
def main():
    engine.say("Hola soy Julieta tu asistente virtual")
    engine.runAndWait()
    asistente()

    return "Starting python script"


print("Inicializando")
eel.start("index.html", size=(1000,600))