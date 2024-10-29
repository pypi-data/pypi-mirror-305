import google.generativeai as genai
import os
import subprocess
import time
from PIL import ImageGrab, Image
import tkinter as tk

# Initialize memory
memory = {}

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

# Function to prompt for the API key using Tkinter
def prompt_for_api_key():
    def on_save():
        api_key = api_key_entry.get()
        save_api_key(api_key)
        window.destroy()
        print("API Key saved.")

    # Create the main window
    window = tk.Tk()
    window.title("Gemini API Key")

    # Create and place widgets
    label = tk.Label(window, text="What's the API KEY for your Google Gemini?")
    label.pack(pady=10)

    api_key_entry = tk.Entry(window, width=40)
    api_key_entry.pack(pady=5)

    save_button = tk.Button(window, text="Save", command=on_save)
    save_button.pack(pady=10)

    # Start the GUI main loop
    window.mainloop()

# Load the API key from file, or prompt the user if it doesn't exist
API_KEY = load_api_key()
if API_KEY is None:
    prompt_for_api_key()
    API_KEY = load_api_key()  # Reload the API key after saving

# Initialize the model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def send_image_to_gemini(image_path):
    # Load the image
    image = Image.open(image_path)
    # Send the image and a prompt
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

def chat_with_gemini():
    print("Welcome to the Gemini Chat! Type 'exit' to end the chat.")

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending chat. Goodbye!")
            break

        # Generate response from Gemini, incorporating memory
        prompt = f"You are Gemini, a large language model. Here is the conversation so far: {memory}\nNow, respond to the user's query: {user_input}"
        response = model.generate_content(prompt)

        # Update memory with the new conversation turn
        memory[user_input] = response.text

        # Display response
        print(f"Gemini: {response.text}")

        # Take screenshot if user types "screenshot"
        if user_input.lower() == "screenshot":
            try:
                # Capture screenshot
                screenshot_path = get_next_screenshot_filename()
                screenshot = ImageGrab.grab()
                screenshot.save(screenshot_path)
                print(f"Screenshot captured and saved as {screenshot_path}.")

                # Sending the image to Gemini
                response_text = send_image_to_gemini(screenshot_path)
                print(f"Gemini: {response_text}")

            except Exception as e:
                print(f"Error taking screenshot: {e}")

        # Check for code blocks and save them
        if "```python" in response.text:
            code_start = response.text.index("```python") + len("```python")
            code_end = response.text.rindex("```")
            code_block = response.text[code_start:code_end]

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
    chat_with_gemini()

if __name__ == "__main__":
    main()
