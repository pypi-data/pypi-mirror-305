import google.generativeai as genai
import os
import subprocess
from PIL import ImageGrab, Image

# Function to save the API key to apikey.txt
def save_api_key(api_key):
    with open("apikey.txt", "w") as file:
        file.write(api_key)

# Function to load the API key from apikey.txt
def load_api_key():
    if os.path.exists("apikey.txt"):
        with open("apikey.txt", "r") as file:
            return file.read().strip()
    return None

# Function to prompt for a new API key
def prompt_for_api_key():
    return input("Enter your Google Gemini API Key: ")

# Function to ask the user if they want to use a new API key
def ask_new_api_key():
    while True:
        use_new_key = input("Use new API Key? (y/n): ").strip().lower()
        if use_new_key in ['y', 'n']:
            return use_new_key == 'y'
        print("Please enter 'y' or 'n'.")

# Initialize the model
def initialize_model():
    if ask_new_api_key():
        API_KEY = prompt_for_api_key()
        save_api_key(API_KEY)
    else:
        API_KEY = load_api_key()
        if API_KEY is None:
            print("No API Key found. Exiting...")
            exit(1)

    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel("gemini-1.5-flash")

# Initialize a memory store
memory = {}

def send_image_to_gemini(image_path, model):
    # Load the image and send it to Gemini
    image = Image.open(image_path)
    response = model.generate_content(["Describe this image", image])
    return response.text

def get_next_screenshot_filename():
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)  # Create the directory if it doesn't exist
    i = 1
    while True:
        filename = os.path.join(screenshot_dir, f"screenshot{i}.png")
        if not os.path.exists(filename):
            return filename
        i += 1

def get_next_tempcode_filename():
    tempcode_dir = "temporarycodes"
    os.makedirs(tempcode_dir, exist_ok=True)  # Create the directory if it doesn't exist
    i = 1
    while True:
        filename = os.path.join(tempcode_dir, f"tempcode{i}.py")
        if not os.path.exists(filename):
            return filename
        i += 1

def chat_with_gemini(model):
    print("Welcome to the Gemini Chat! Type 'exit' to end the chat.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending chat. Goodbye!")
            break

        # Generate response from Gemini, incorporating memory
        prompt = f"You are Gemini, a large language model. Here is the conversation memory: {memory}\nNow respond to: {user_input}"
        response = model.generate_content(prompt)

        # Update memory with the new user input and response
        memory[user_input] = response.text
        
        # Take screenshot if user types "screenshot"
        if user_input.lower() == "screenshot":
            try:
                # Capture screenshot
                screenshot_path = get_next_screenshot_filename()
                screenshot = ImageGrab.grab()
                screenshot.save(screenshot_path)
                print(f"Screenshot captured and saved as {screenshot_path}.")

                # Sending the image to Gemini
                response_text = send_image_to_gemini(screenshot_path, model)
                print(f"Gemini: {response_text}")

            except Exception as e:
                print(f"Error taking screenshot: {e}")

        else:
            # Display Gemini's response
            print(f"Gemini: {response.text}")

            # Check for code blocks and save them
            if "```python" in response.text:
                code_start = response.text.index("```python") + len("```python")
                code_end = response.text.rindex("```")
                code_block = response.text[code_start:code_end].strip()

                # Save the code to the next available tempcode.py
                tempcode_path = get_next_tempcode_filename()
                with open(tempcode_path, "w") as f:
                    f.write(code_block)

                print(f"\nCode saved to {tempcode_path}.")
                run_code = input("Do you want to run this code? (y/n): ")
                if run_code.lower() == 'y':
                    try:
                        output = subprocess.check_output(["python", tempcode_path]).decode()
                        print(f"\nCode Output:\n{output}")
                    except subprocess.CalledProcessError as e:
                        print(f"\nError running code: {e}")

def main():
    model = initialize_model()  # Initialize the model
    chat_with_gemini(model)     # Start the chat session

# Entry point for the script
if __name__ == "__main__":
    main()
