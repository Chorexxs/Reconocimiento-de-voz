import speech_recognition as sr

def reconocer_comandos_voz():
    # Crear un objeto de reconocimiento de voz
    reconocedor = sr.Recognizer()

    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = reconocedor.listen(source)

    try:
        # Utilizar el reconocedor de voz para convertir el audio en texto
        texto = reconocedor.recognize_google(audio, language="es-ES")
        print("Has dicho:", texto)
        # Aquí puedes procesar el texto reconocido y realizar acciones según los comandos

    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")

    except sr.RequestError as e:
        print("Error al solicitar resultados al servicio de reconocimiento de voz; {0}".format(e))

# Programa principal
reconocer_comandos_voz()
