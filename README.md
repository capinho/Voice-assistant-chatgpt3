# Voice-assistant-chatgpt3

# Voice Assistant

This is a Python script that creates a voice assistant that uses the OpenAI GPT-3 language model to generate responses to user input. It accepts voice input from the user using the `speech_recognition` library and converts text to speech using the `pyttsx3` library.

## Requirements

To use this script, you will need to install the following libraries:

- openai
- pyttsx3
- speech_recognition

You can install these libraries using `pip`, the Python package manager.
Or, use the following command to install the required libraries:

```
pip install -r requirements.txt
```

## Usage

To run the script, enter the following command in your terminal:

```
python speech.py
```


The script will prompt you to speak, and the voice assistant will respond with a generated response. You can continue the conversation by speaking to the voice assistant. To exit the conversation, say "exit".

## Configuration

You will need to provide your own OpenAI API key to use the GPT-3 language model. To do so, replace YOUR_API_KEY in the following line of code with your API key:

```
openai.api_key = "YOUR_API_KEY"
```

You can also customize the text-to-speech engine by specifying a different voice or language. To do so, you can use the setProperty() function of the pyttsx3 library. For example, to use a native English speaker, you can use the following code:

```
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
```

You can also specify a specific voice by its name. For example, to use the voice "Daniel," you can use the following code:

```
engine = pyttsx3.init()
engine.setProperty('voice', 'english-us')
```

Keep in mind that the available voices may vary depending on your operating system and the version of pyttsx3 you are using. You can use the getProperty() function to get a list of available voices and choose the one that best meets your needs.


# Voice-assistant-chatgpt3
