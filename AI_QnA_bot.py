import sys      # for enhanced error handling
import google.generativeai as genai     # for API calls

# set your API key for Google Generative AI
genai.configure(api_key= "AIzaSyBv8CIpXeN4zxvhfE0G0Jb34yr3v6rt6Ak")

# Function to interact with Google Generative AI 
def ask_question(question):
    try:

        model = genai.GenerativeModel("gemini-pro")     # specifies AI model
        # Start a chat session with optional history
        # chat = model.start_chat(history=[{"author": "user", "content": question}])
        chat = model.start_chat()
        reponse = chat.send_message(question)
        # extract generated response
        return reponse.text
    except KeyError:
        return "Error: Unable to parse response from the API."
    except Exception as e:
        return f"An unexpected error occured: {e}"

# Function to save conversation history
def save_conversation(question, answer, file_name= "conversation_history.txt"):
    try:
        with open(file_name, "a") as f:
            f.write(f"User: {question}\nAI: {answer}\n\n")
    except Exception as e:
        print(f"Error saving conversation: {e}")
        sys.exit(1)     # exit program if unable to save the file

# Main Function
def main():
    print("\n\t  Welcome to the AI-Powered Q & A Bot!")
    print("\n" + "_"*30)
    print("\nType your questions below.")
    print("Type 'Exit' to quit")

    while True:
        try:
            question = input("\nQuestion: ").strip()
            if question.lower() == "exit":
                print("\nThankyou for using it. Have a nice day!")
                sys.quit(0)     # for controlled exit..gracefully exits program
            # get response from bot 
            answer = ask_question(question)
            print(f"AI's Answer: {answer}\n")
            # save conversation history
            save_conversation(question, answer)
        except KeyboardInterrupt:
            print("\nSession Interrupted. Exiting...")
            sys.exit(0)     # exit gracefully on Ctrl + C    
        except Exception as e:
            print(f"\nAn unexpected error: {e}")
            sys.exit(1)     # exit program on unforseen error

# Run Program 
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical error encountered: {e}")                
        sys.exit(1)     # catch and exit on any critical error