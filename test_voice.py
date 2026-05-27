import pyttsx3

try:

    # Initialize engine
    engine = pyttsx3.init()

    # Voice speed
    engine.setProperty("rate", 150)

    # Voice volume
    engine.setProperty("volume", 1.0)

    # Text speak
    text = "Hello Arpit,Ashvin and Yash. Voice system is working successfully."

    print("Speaking:", text)

    engine.say(text)

    engine.runAndWait()

    print("Voice test completed successfully.")

except Exception as e:

    print("Error:", e)