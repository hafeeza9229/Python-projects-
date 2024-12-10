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

    print("\nFetching available formats...\n")
    options = {
        'listformats': True,  # List available formats without downloading
        'quiet': True,  # Suppress unnecessary output
    }

    formats = {}

    # Use yt-dlp to extract formats
    with yt_dlp.YoutubeDL(options) as ydl:
        yt = ydl.extract_info(url, download=False)
        for fmt in yt['formats']:
            if fmt.get("ext") and fmt.get("format_note"):
                formats[fmt["format_id"]] = f"{fmt['format_note']} ({fmt['ext']})"

    # Display formats
    print("Available formats:")
    for fmt_id, description in formats.items():
        print(f"{fmt_id}: {description}")

    return formats

# def download_stream(selected_format, path):
def download_stream(url, format_id, path):
    """ Download the selected stream. """
    print("\nDownloading...")
    try:
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': format_id
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
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

            # # Display streams and let the user choose
            streams = display_streams(url)
            if not streams:
                print("No available formats found for this video. Skipping...")
                continue
            
            while True:
                format_id = input("\nEnter the number of your preferred format (or type 'cancel' to skip): ").strip()
                if format_id.lower() == 'cancel':
                    print("Skipping this video.")
                    break
                elif format_id not in streams:
                        print("Invalid choice. Please try again or type 'cancel' to skip.")
                else:
                    # Download video in selected format
                    download_stream(url, format_id, download_path)
                    break
                    
        # Ask if the user wants to download more videos
        retry = input("\nDo you want to download more videos? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thank you for using the YouTube Video Downloader. Goodbye!")
            break

if __name__ == "__main__":
    main()
