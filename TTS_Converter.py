""" Ensure pyttsx3 is installed for offline text-to-speech conversion. """
import pyttsx3  # Offline TTS library
import os  # For file handling

def get_text():
    """ Get input data from user (typed or file-based) """
    print("\nChoose input method:")
    print("1. Type text manually")
    print("2. Load text from file")
    choice = int(input("\nEnter your choice:"))
    if choice == 1:
        text = input("\nEnter your text:").strip()
        if not text:
            raise ValueError("Input text cannot be empty.")
        return text 
    elif choice == 2:
        file_path = input("\nEnter the file path (.txt):").strip()
        if not os._path_isfile(file_path):
            raise FileNotFoundError("File not found. Please enter a valid path..")
        with open(file_path, 'r') as f:
            text = f.read().strip()
            if not text:
                raise ValueError("The file is empty. Please provide a valid text file..")
        return text
    else:
        raise ValueError("Invalid input. Try again..")
        return get_text()

def set_language(engine, language="en"):
    """ Set the language/voice for TTS """
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voices[0].id)  # Default English voice
    elif language == "fr":
        engine.setProperty('voice', voices[1].id)  # Example for French
    else:
        raise ValueError("Unsupported language code! Please use 'en' or 'fr'.")
    return engine

def convert_to_speech(text, language="en", rate=150, volume=1.0, output_folder="AudioFiles"):        
    """
    Convert text to speech using pyttsx3.
    
    Parameters:
    - text: The text to be converted to speech.
    - output_folder: The filename to save the generated audio.
    - rate: Speed of speech (default is 150 words per minute).
    - volume: Volume level (default is 1.0, range: 0.0 to 1.0).
    """
    try:
        engine = pyttsx3.init()
        
        # Set properties
        engine.setProperty("rate", rate)  # Set speed of speech
        engine.setProperty("volume", volume)  # Set volume level

        # Set language/voice
        engine = set_language(engine, language)
        
        # Save speech to file
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Define the audio file path
        output_file = os.path.join(output_folder, "output_audio.mp3")

        # Save the speech to a file
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        return output_file

    except Exception as e:
        raise RuntimeError(f"Error during TTS conversion: {e}")

def play_audio(audio_file):
    """ Play generated audio using pyttsx3 """
    try:
        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # Play the audio file directly
        print("Playing audio...")
        os.system(f"start {audio_file}")  # Opens the file in the default media player

    except Exception as e:
        raise RuntimeError(f"Error playing audio: {e}")

def save_audio(audio_file, output_format="mp3"):
    """ Save the audio file in the specified format """
    try:
        output_name = input("Enter the output file name (without extension): ").strip()
        if not output_name:
            raise ValueError("File name cannot be empty.")
        output_name += ".mp3"
        os.rename(audio_file, output_name)
        print(f"Audio saved as {output_name}")

    except Exception as e:
        raise RuntimeError(f"Error saving audio file: {e}")

def main():
    """ Main Program Flow """
    print("\n\n\tWelcome to the Text-To-Speech Converter")
    try:
        text = get_text()

        # Get language for TTS
        language = input("\nEnter the language code:").strip()
        if len(language) != 2:
            raise ValueError("Invalid language code! Please use a two-letter code (e.g., 'en', 'fr').")

        # Convert text to speech
        audio_file = convert_to_speech(text, language)
        print("Audio generated successfully!")

        # Playback adjustments
        rate = int(input("\nEnter speech rate (default 150): ") or 150)
        volume = float(input("Enter volume level (0.0 to 1.0, default 1.0): ") or 1.0)

        # Play adjusted audio
        print("\nPlaying adjusted audio...")
        play_audio(audio_file)

        # prompt the user to save file or not
        print("\nDo you want to save the audio file?")
        # Save the audio file
        save_option = input("Enter 'y' to save or any other key to skip:").strip().lower()
        if save_option == "y":
            save_audio(audio_file)

    except Exception as e:
        print(f"An error occured: {e}")   

    finally:
        print("Thankyou for using the TTC Converter!")

if __name__ == "__main__":
    main()            