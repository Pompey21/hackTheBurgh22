# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import requests
import value_reader
import json
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hi there, you can ask me about the current air pollution levels?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class AQIIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AQIIntent")(handler_input)
        
    def handle(self, handler_input):
        speak_output = "I can't retrieve up to date data right now. Please try later."
        
        # slots = handler_input.request_envelope.request.intent.slots
        # if slots['city'].value:
        #     city = lower(str(slots['city'].value))
        #     data = requests.get('https://api.waqi.info/feed/{}/?token=8d316da0e4caea8439466035511e7bedb1cb31c9'.format(city))
        #     json_data =json.loads(data.content)
            
        #     if json_data['status'] == 'ok':
        #         aqi = value_reader.get_aqi(json_data)
        #         speak_output = "Right now the Air quality index in {} is {}".format(city, str(aqi))
                
        #     return (
        #         handler_input.response_builder
        #             .speak(speak_output)
        #             .response
        #     )
        
        
        data = requests.get('https://api.waqi.info/feed/edinburgh/?token=8d316da0e4caea8439466035511e7bedb1cb31c9')
        json_data =json.loads(data.content)
        
        if json_data['status'] == 'ok':
            aqi = value_reader.get_aqi(json_data)
            speak_output = "Right now the Air quality index is " + str(aqi)
        
        return (
            handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
        )

class CarbonMonoxideIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("CarbonMonoxideIntent")(handler_input)
        
    def handle(self, handler_input):
        speak_output = "I can't retrieve up to date data right now. Please try later."
        data = requests.get('https://api.waqi.info/feed/edinburgh/?token=8d316da0e4caea8439466035511e7bedb1cb31c9')
        json_data =json.loads(data.content)
        
        if json_data['status'] == 'ok':
            co = value_reader.get_measurement(json_data, 'co')
            
            speak_output = "The current carbon monoxide concentration is " + str(co) + " ppm."
        
        return (
            handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
        )

class NitrogenDioxideIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NitrogenDioxideIntent")(handler_input)
        
    def handle(self, handler_input):
        speak_output = "I can't retrieve up to date data right now. Please try later."
        data = requests.get('https://api.waqi.info/feed/edinburgh/?token=8d316da0e4caea8439466035511e7bedb1cb31c9')
        json_data =json.loads(data.content)
        
        if json_data['status'] == 'ok':
            no2 = value_reader.get_measurement(json_data, 'no2')
            
            speak_output = "The current nitrogen dioxide concentration is " + str(no2) + " ppb."
            
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
            )
        return (
            handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
        )

class ParticulateMatterIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ParticulateMatterIntent")(handler_input)
        
    def handle(self, handler_input):
        speak_output = "I can't retrieve up to date data right now. Please try later."
        data = requests.get('https://api.waqi.info/feed/edinburgh/?token=8d316da0e4caea8439466035511e7bedb1cb31c9')
        json_data =json.loads(data.content)
        
        if json_data['status'] == 'ok':
            pm10 = value_reader.get_measurement(json_data, 'pm10')
            
            speak_output = "The current level of particulate matter in the air is " + str(pm10)
        
        return (
            handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
        )

class OzoneIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("OzoneIntent")(handler_input)
        
    def handle(self, handler_input):
        speak_output = "I can't retrieve up to date data right now. Please try later."
        data = requests.get('https://api.waqi.info/feed/edinburgh/?token=8d316da0e4caea8439466035511e7bedb1cb31c9')
        json_data =json.loads(data.content)
        
        if json_data['status'] == 'ok':
            o3 = value_reader.get_measurement(json_data, 'o3')
            
            speak_output = "The current level of ozone in the air is " + str(o3) + " parts per billion by volume."
        return (
            handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
        )

class SulfurDioxideIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("SulfurDioxideIntent")(handler_input)
        
    def handle(self, handler_input):
        speak_output = "I can't retrieve up to date data right now. Please try later."
        data = requests.get('https://api.waqi.info/feed/edinburgh/?token=8d316da0e4caea8439466035511e7bedb1cb31c9')
        json_data =json.loads(data.content)
        
        if json_data['status'] == 'ok':
            so2 = value_reader.get_measurement(json_data, 'so2')
            
            speak_output = "The current level of sulfur dioxide in the air is " + str(so2)
            
        return (
            handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can ask me about current air quality index or the concentration of carbon monoxide or nitrogen dioxide in the air?"
        reprompt = "Hey, ask me about the level of airborne particles or carbon monoxide."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, exception occurred. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AQIIntentHandler())
sb.add_request_handler(CarbonMonoxideIntentHandler())
sb.add_request_handler(NitrogenDioxideIntentHandler())
sb.add_request_handler(ParticulateMatterIntentHandler())
sb.add_request_handler(OzoneIntentHandler())
sb.add_request_handler(SulfurDioxideIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()