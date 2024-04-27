# import necessary modules.
import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
from IPython.display import Markdown
from google.colab import userdata

#initialize GeminiAPI
API_KEY=""
genai.configure(api_key=API_KEY)
model = 'gemini-1.0-pro' # @param {isTemplate: true}
contents_b64 = '' # @param {isTemplate: true}
generation_config_b64 = '' # @param {isTemplate: true}
safety_settings_b64 = '' # @param {isTemplate: true}
user_input_b64 = '' # @param {isTemplate: true}

contents = json.loads(base64.b64decode(contents_b64))
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
user_input = base64.b64decode(user_input_b64).decode()
stream = False
contents
generation_config
safety_settings
user_input="generate planUML code for booking an appointment for a lung X ray in apollo hospital"
gemini = genai.GenerativeModel(model_name=model)

chat = gemini.start_chat(history=contents)

response = chat.send_message(
    user_input,
    stream=stream)
display(Markdown(response.text))
response.prompt_feedback

#planUML on Python
response.candidates
!pip install plantweb
%load_ext plantweb
!pip install plantuml
%load_ext plantuml
  f= open("/content/plantUML.txt","w+")
f.write(f"""participant Patient
participant Doctor
participant Receptionist
Patient->Receptionist: Request appointment for lung X-ray in Apollo Hospital
Receptionist->Doctor: Check availability
Doctor->Receptionist: Availability confirmed
Receptionist->Patient: Appointment confirmed""")

f.close()

!python -m plantuml plantUML.txt
