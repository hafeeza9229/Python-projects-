# from pytube import YouTube      # for downloading YouTube videos
import yt_dlp
import os       # for managing file paths

def download_directory():
    """ Create a 'downloads' directory if it doesn't exist. """
    download_path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return download_path

def get_url(url):
    """ Fetch YouTube video information. """
    try:
        ydl_opts = {'quiet': True}
        # Define options (no download, just fetch info)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            yt = ydl.extract_info(url, download=False)
            print(f"\nTitle: {yt['title']}")
            print(f"Uploader: {yt['uploader']}")
            duration = yt.get('duration', 0)
            print(f"Length: {duration // 60} minutes and {duration % 60} seconds")
        return yt
    except Exception as e:
        print(f"Error fetching video info: {e}")
        return None

def display_streams(url):
    """ Display available streams for selection. """

    ydl_opts = {
            'quiet': True,  # Suppress output, we only care about formats
            'force_generic_extractor': True  # In case there is a specific extractor error
        }
        
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        yt = ydl.extract_info(url, download=False)
        formats = yt.get('formats', [])
        options = []
        print("\nAvailable formats:")

        for idx, fmt in enumerate(formats, start=1):
            resolution = fmt.get('resolution', 'Audio only')
            mime_type = fmt.get('ext', 'Unknown format')  # File format (audio/video)
            print(f"{idx}. {resolution} - {mime_type} (ID: {fmt['format_id']})")

            options.append(fmt)

    return options

def download_stream(selected_format, path):
    """ Download the selected stream. """
    print("\nDownloading...")
    try:
        ydl_opts = {
            'quiet': True,
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': selected_format['format_id']
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([selected_format['url']])
        print("Download complete!")
    except Exception as e:
        print(f"Download failed: {e}")

def main():
    print("\n\nWelcome to the YouTube Video Downloader!")
    print("\nYou can download videos or audio files by providing their URLs.\n")
    
    # Create the download directory
    download_path = download_directory()
    print(f"Files will be saved in: {download_path}")

    while True:
        # Input URL(s)
        urls = input("Enter YouTube video URL(s) separated by commas: ").strip().split(',')
        urls = [url.strip() for url in urls if url.strip()]
        
        if not urls:
            print("No valid URLs provided. Please try again.")
            continue
        
        for url in urls:
            print(f"\nProcessing URL: {url}")
            
            # Fetch video information
            yt = get_url(url)
            if not yt:
                print("Skipping invalid or inaccessible URL.")
                continue

            # Display streams and let the user choose
            streams = display_streams(url)
            if not streams:
                print("No available formats found for this video. Skipping...")
                continue
            
            while True:
                choice = input("\nEnter the number of your preferred format (or type 'cancel' to skip): ").strip()
                if choice.lower() == 'cancel':
                    print("Skipping this video.")
                    break
                if choice.isdigit() and int(choice) in range(1, len(streams) + 1):
                    selected_stream = streams[int(choice) - 1]
                    print(f"\nYou selected: {selected_stream.get('resolution', 'Audio only')}")
                    print(f"Estimated file size: {selected_stream.get('filesize', 0) / (1024 * 1024):.2f} MB")
                    download_stream(selected_stream, download_path)
                    break
                else:
                    print("Invalid choice. Please try again or type 'cancel' to skip.")
        
        # Ask if the user wants to download more videos
        retry = input("\nDo you want to download more videos? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thank you for using the YouTube Video Downloader. Goodbye!")
            break

if __name__ == "__main__":
    main()