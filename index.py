import os
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_model import Response
import requests

# Define el identificador de tu skill de Alexa
SKILL_ID = 'amzn1.ask.skill.c588197b-f44b-4826-8a17-5b7a4f2a0cd9'

# Define la URL del canal de ThingSpeak y el API Key
THINGSPEAK_URL = 'https://api.thingspeak.com/channels/2136125/fields/field1/last.html?api_key=32ZF0XR41BMLO8AE'
THINGSPEAK_API_KEY = '32ZF0XR41BMLO8AE'

# Crea un objeto SkillBuilder
sb = SkillBuilder()

class humedad(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # Verifica si el intento recibido es 'GetThingSpeakValueIntent'
        return ask_utils.is_intent_name('humedad')(handler_input)

    def handle(self, handler_input):
        # Obtiene el valor de ThingSpeak
        response = requests.get(THINGSPEAK_URL, params={'api_key': THINGSPEAK_API_KEY})
        value = response.json()['field1']

        # Construye la respuesta de Alexa
        speech_text = f"La humedad del jardín es {value} %"

        return (
            handler_input.response_builder
                .speak(speech_text)
                .response
        )

class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        # Maneja cualquier excepción ocurrida durante la ejecución
        speech_text = "Lo siento, ha ocurrido un error."

        return (
            handler_input.response_builder
                .speak(speech_text)
                .response
        )

# Registra los Request Handlers y Exception Handlers en el SkillBuilder
#sb.add_request_handler(GetThingSpeakValueIntentHandler())
#sb.add_exception_handler(CatchAllExceptionHandler())

# Define la función lambda handler
#def lambda_handler(event, context):
    #skill_id = event['session']['application']['applicationId']
    #if skill_id != SKILL_ID:
        #raise ValueError('Invalid Skill ID')

    # Construye el handler de entrada y ejecuta la skill
    #handler = sb.lambda_handler()
    #return handler(event, context)
