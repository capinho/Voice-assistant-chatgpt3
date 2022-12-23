import openai
import pyttsx3
import speech_recognition as sr


# Set up the OpenAI API client
openai.api_key = "YOUR_OPENAI_API_KEY"


# Set up the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set up the speech-to-text engine
r = sr.Recognizer()

# Define a function to generate text using GPT-3
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Define a function to handle user input and generate a response
def chat(user_input):
    # Use the GPT-3 model to generate a response to the user's input
    response = generate_text(user_input)
    return response

# Main loop to run the chatbot
while True:
    # Get user input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Convert the audio to text
    try:
        user_input = r.recognize_google(audio)
        print("User:", user_input)
    except sr.UnknownValueError:
        print("Could not understand audio")
        continue
    except sr.RequestError as e:
        print("Error making request:", e)
        continue

    # Exit the loop if the user says "exit"
    if user_input.lower() == "exit":
        break

    # Get the chatbot's response
    response = chat(user_input)

    # Print the response and convert it to speech
    print("Bot:", response)
    engine.say(response)
    engine.runAndWait()
