# Reconocimiento de Voz

Este programa utiliza la biblioteca SpeechRecognition para reconocer y procesar comandos de voz. Permite al usuario hablar a través del micrófono y convierte el audio en texto utilizando el reconocimiento de voz de Google.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes dependencias:

- Python: El lenguaje de programación utilizado.
- SpeechRecognition: Una biblioteca de Python que proporciona funciones para el reconocimiento de voz.
- PyAudio: Una biblioteca de Python para acceder al micrófono y grabar audio.

Puedes instalar SpeechRecognition y PyAudio utilizando el siguiente comando:

```shell
pip install SpeechRecognition pyaudio
```

Si tienes problemas al instalar PyAudio debido a dependencias faltantes, consulta la documentación oficial de PyAudio para obtener instrucciones adicionales.

## Cómo utilizar el programa

1. Ejecuta el código en un entorno de desarrollo de Python.

2. Asegúrate de tener un micrófono conectado a tu dispositivo.

3. Cuando se ejecute el programa, verás el mensaje "Di algo...". Habla claramente en el micrófono para que se pueda capturar el audio.

4. Después de hablar, el programa utilizará el reconocimiento de voz de Google para convertir el audio en texto.

5. El texto reconocido se mostrará en la consola con el mensaje "Has dicho: [texto]".

## Consideraciones adicionales

- Si el audio no se reconoce correctamente, el programa mostrará el mensaje "No se pudo reconocer el audio". Asegúrate de hablar claramente y en un entorno lo más silencioso posible.

- Si deseas utilizar un idioma diferente al español, puedes modificar el parámetro `language` en la línea `texto = reconocedor.recognize_google(audio, language="es-ES")`. Consulta la documentación de SpeechRecognition para obtener información sobre los códigos de idioma compatibles.

¡Disfruta experimentando con el reconocimiento de voz!
