import win32com.client

def speak():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    names = []
    while (name := input("Enter a name (or press Enter to finish): ")):
        names.append(name)
    for name in names:
        speaker.Speak(f"Shout out to {name}")

speak()


