import vlc     # for media playback
import yt_dlp     # for downloading YouTube Audio
import time     # for sleep functionality
import os     # used for cleaning console

# Function to fetch audio url
def fetch_vedio_url(youtube_video_url):
    """
    Fetches the audio stream URL from the given YouTube video URL.
    Returns the audio URL if successful, or None if an error occurs.
    """
    try:
        ydl_opts = {
            'format':'bestaudio',     # Fetch the best quality audio
            'extract_flat': True    # Extract metadata without downloading
        }
        # extract audio stream URL
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_video_url, download= False)
            return info["url"]
    
    except Exception as e:
        print(f"\nError fetching audio: {e}")
        print("Wait for 2 seconds...")
    time.sleep(2)
    return None

# Function to play audio
def play_audio(audio_url):
    """
    Plays the given audio URL using VLC.
    Returns a VLC MediaPlayer instance.
    """
    try:
        print("\nStarting song....")

        url = fetch_vedio_url(audio_url)
        if not url:
            print("\nCould not fetch the audio url.")
            print("Wait for 2 seconds...")
            time.sleep(2)
            return

        player = vlc.MediaPlayer(audio_url)
        player.play()
        return player     # start playback
        # Function for contrls        
        """
        Provides user controls for the music player: pause, resume, restart, and quit.
        """
        # try:
        while True:
            print("\nControls:  [P] Pause/Resume || [R] Restart || [Q] Quit")
            command = input("Enter command:").strip().lower()

            if command == 'p':
                if player.is_playing:
                    player.paused()
                    print("Music paused.")
                else:
                    player.play()
                    print("Music resumed.")
            elif command == 'r':
                player.stop()
                player.play()
                print("Music restart.")
            elif command == 'q':
                player.stop()
                print("Exiting player..")
                break                
            else:
                print("\nInvalid command. Please try again!")
    # except Exception as e:
    #     print(f"\nError : {e}")
    #     print("Wait for 2 seconds and try again...")
    #     time.sleep(2)
    except KeyError as e:
        # Handle case when the 'url' key is not found in the info dictionary
        print(f"KeyError: Missing expected data in the response. {e}")   
    except Exception as e:
        print(f"\nError playing audio: {e}")
        print("Wait for 2 seconds...")
        time.sleep(2)


# def audio_controls(player):


# Funcrion to display my list of songs
def my_list():

    songs = [
        "https://youtu.be/kyjg5kX4pT0?si=QKSHUocD6HVORbBW",
        "https://youtu.be/XO8wew38VM8?si=9qG5id8bC5f-Mxaq",
        "https://youtu.be/VCNLZflKQ7o?si=mCTy9U26-TU0X3lA",
        "https://www.youtube.com/watch?v=J7bYXNM9oBQ",
        "https://www.youtube.com/watch?v=QgnaMy8C2A0"
    ]
    while True:
        os.system("cls")
        print("\n" + "_"*50)
        print("\nList of songs:")
        print("\n1. Dil Tu Jaan Tu by Gurnazar Ft. Kritika Yadav")
        print("2. Millionaire by YoYo Honey Singh")
        print("3. Tere Hawaale by Arijit Singh")
        print("4. Paar chanaa de by Ali Wasif Kazmi")
        print("5. Hasse by Shahid Khan")
        print("6. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            play_audio(songs[0])
        elif choice == 2:
            play_audio(songs[1]) 
        elif choice == 3:
            play_audio(songs[2])
        elif choice == 4:
            play_audio(songs[3])
        elif choice == 5:
            play_audio(songs[4])
        elif choice == 6:  
            # exit the list and return to main menu
            print("\nThanks for listening.")
            break
        else:
            print("\nInvalid choice...")

# Main Function 
def main():
    """
    Main function to run the Python Music Player.
    Prompts the user for a YouTube URL, fetches the audio stream, and starts playback.
    """
    while True:
        os.system("cls")  
        print("\n           Welcome to my music player")
        print("\n" + "_"*30)
        print("\n1. Wanna play your own song?")
        print("2. Wanna play my list of songs?")
        print("3. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            os.system("cls")
            song_url = input("Enter the YouTube URL of song:")
            play_audio(song_url)
        elif choice == 2:
            my_list()   
        elif choice == 3:
            print("\nThankyou for using Music Player.")     
            break
        else:
            print("\nInvalid choice. Try again...")

# Entry point of program
if __name__ == "__main__":
    main()    
