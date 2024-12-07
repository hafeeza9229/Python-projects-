""" Make sure you have installed FFmpeg ensures that pydub can fully utilize its 
functionality for working with a wide range of audio formats and operations. """
from pydub import AudioSegment
from pydub.playback import play       # to play audio 
import os       # for file handling
from gtts import gTTS       # online TTS library for natural voice output

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

def convert_to_speech(text, language="en", output_folder="AudioFiles"):        
    """ Convert text to speech using gTTS """
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Define the audio file path
        temp_file_path = os.path.join(output_folder, "temp_audio.mp3")

        # Convert text to speech and save
        tts = gTTS(text=text, lang=language)
        tts.save(temp_file_path)
        return temp_file_path
    except Exception as e:
        raise RuntimeError(f"Error during TTS conversion: {e}")

def play_audio(audio_file):
    """ Play generated audio using pydub """
    try:
        # Ensure the file is fully closed and accessible
        if os.path.exists(audio_file):
            audio = AudioSegment.from_file(audio_file)
            play(audio)
        else:
            raise FileNotFoundError(f"The audio file '{audio_file}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Error playing audio: {e}")
    
def adjust_speed(audio_file, speed=1.0):
    """ 
    Adjust the playback speed of audio
    :param audio_file: Path to the audio file. 
    :return: Path to the speed-adjusted audio file.
    """
    try:
        audio = AudioSegment.from_file(audio_file)
        if speed != 1.0:
            # create new audio using raw data of original audio
            new_audio = audio._spawn(audio.raw_data,
             overrides= {"frame_rate":int(audio.frame_rate * speed)}
             ).set_frame_rate(audio.frame_rate)
            # save audio to temporary file
            temp_file_path = "temp_audio_speed.mp3"
            new_audio.export(temp_file_path, format="mp3")
            return temp_file_path
        return audio_file
    except Exception as e:
        raise RuntimeError(f"Error adjusting speed: {e}")

def adjust_pitch(audio_file, semitones=0):
    """
    Adjust the pitch of the audio.
    :param audio_file: Path to the audio file.
    :param semitones: Number of semitones to shift the pitch (+ve for higher pitch, -ve for lower pitch).
    :return: Path to the pitch-adjusted audio file.
    """
    try:
        audio = AudioSegment.from_file(audio_file)
        if semitones != 0:
            # calculate speed factor based on semitones
            speed_factor = 2**(semitones / 12)  # each semitone corresponds to factor of 2^(1/12)
            new_audio = audio._spawn(audio.raw_data,
             overrides= {"frame_rate":int(audio.frame_rate * speed_factor)}
             ).set_frame_rate(audio.frame_rate)
             # save audio to temporary file
            temp_file_path = "temp_audio_pitch.mp3"
            new_audio.export(temp_file_path, format="mp3")
            return temp_file_path
        return audio_file
    except Exception as e:
        raise RuntimeError(f"Error adjusting pitch: {e}")

def save_audio(audio_file, output_format="mp3"):
    """ Save the audio file in the specified format """
    try:
        # Prompt the user to get a file name
        output_path = input("Enter the output file name (without extention):").strip()
        if not output_path:
            raise ValueError("File name cannoat be empty..")
        output_path += f"{output_format}"
        # save file 
        audio = AudioSegment.from_file(audio_file)
        audio.export(output_file, format=output_format)
        print(f"Audio saved as {output_path}")
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
        print("\nPlayback Adjustments:")
        speed = float(input("Enter playback speed (default is 1.0): "))
        audio_file = adjust_speed(audio_file, speed)
        pitch = int(input("Enter pitch shift in semitones (e.g., +2 for high, -2 for low | default is 0): "))
        audio_file = adjust_pitch(audio_file, pitch)
        # Play adjusted audio
        print("Playing adjusted audio...")
        play_audio(audio_file)
        # prompt the user to save file or not
        print("Do you want to save the audio file?")
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