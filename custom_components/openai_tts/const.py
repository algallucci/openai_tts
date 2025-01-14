""" Constants for OpenAI TTS custom component"""

DOMAIN = "openai_tts"
CONF_API_KEY = 'api_key'
CONF_MODEL = 'model'
CONF_VOICE = 'voice'
CONF_SPEED = 'speed'
MODELS = ["tts-1", "tts-1-hd", "kokoro"]
VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer", "batman","af_sky+af_bella", "af_sky", "af_bella"]
URL = ["http://192.168.68.52:8000/v1/audio/speech", "http://192.168.68.52:8880/v1/audio/speech"]
