import os       # for validating file paths 
import qrcode       # for QR Code generation
from PIL import Image       # to display QR Code

def validate_color(color):
    """
    Validate if the given color input is a valid hexadecimal or color name.
    """
    try:
        Image.new("RGB", (1, 1), color)     # PIL raises error if color is invalid
        return True
    except ValueError:
        return False

def generate_qr(data, fg="black", bg="white", box_size=10, border=4):
    """
    Generate a QR code with the specified parameters, display QR Code and save it as an image file.
    """
    try:
        # create a QR object with custom dimensions
        qr = qrcode.QRCode(
            version=1,      # (21x21 grid)
            error_correction=qrcode.constants.ERROR_CORRECT_H,      # ~30% of  data can be recovered
            box_size=box_size,
            border=border
        )
        # add data to QR Code
        qr.add_data(data)
        qr.make(fit=True)
        # create QR Code image
        img = qr.make_image(fill_color=fg,back_color=bg)
        img.show()      # display QR Code preview
        
        # save QR Code in specified file
        while True:
            option = input("Do you want to save this QR as an image in file? (yes/no) ").strip().lower()
            if option == "yes" or option == "no":
                if option == "yes":
                    file_name = input("Enter file name (e.g., qr_code.png) : ")
                    if not file_name.endswith(".png"):
                        raise ValueError("File name must ends with .png")
                    img.save(file_name) 
                    print("QR Code successfully saved!")
                    break
                elif option == "no":
                    print("QR Code is not saved.")
                    break
            else:
                print("Invalid input. Try again...") 

    except Exception as e:
        print(f"An error occured while generating QR Code: {e}")         

def main():

    while True:
        try:

            print("\n\t--QR Code Generator--")
            print("\n"+"_"*30)
            print("\n1. Generate QR Code (Default settings)")
            print("2. Generate QR Code (Custom settings)")
            print("3.Exit")
            choice = int(input("Enter your choice:"))

            if choice == 1:
                while True:
                    try:
                        data = input("Enter data (text, URL, etc.) to encode:").strip()
                        if not data:
                            raise ValueError("Input cannot be empty. Please provide valid data.")
                        generate_qr(data)
                        break
                    except ValueError:
                        print("Invalid input. Try again...")  
                    except Exception as e:
                        print(f"An unexpected error occured: {e}")    

            elif choice == 2:   
                data = input("Enter data (text, URL, etc.) to encode:").strip()
                if not data:
                    raise ValueError("Input cannot be empty. Please provide valid data.")
                    
                while True:   
                    try:
                        # ask the user for custom settings
                        fg = input("Enter the foreground colour: ")     
                        bg = input("Enter the backround colour: ") 
                        if validate_color(fg) == False or validate_color(bg) == False:
                            raise ValueError("Invalid color input. Use valid color names or hex codes.")
                        box_size = int(input("Enter the box size:"))
                        border = int(input("Enter the border size:"))       
                        generate_qr(data, fg, bg, border, box_size)
                        break
                    except Exception as e:
                        print(f"An error occured: {e}") 

            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again...")

        except ValueError:
            print("Invalid input....")          

if __name__ == "__main__":
    main()          
