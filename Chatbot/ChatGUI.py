import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import requests
import time
from PIL import ImageTk, Image
from io import BytesIO
import pyttsx3

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rasa Chatbot")
        self.root.geometry("600x400")
        
        # Create chat area
        self.chat_display = scrolledtext.ScrolledText(self.root, state='disabled', height=20, width=50)
        self.chat_display.pack(pady=10)
        
        # Create user input 
        self.user_input = ttk.Entry(self.root, width=50)
        self.user_input.pack(pady=10)
        
        #  send button
        self.send_button = ttk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()
        
        # Rasa server URL
        self.rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
        
        # Bind Enter key to send message
        self.user_input.bind('<Return>', lambda event: self.send_message())

        # speech engine
        self.engine = pyttsx3.init()
        
    def send_message(self):
        message = self.user_input.get()
        self.user_input.delete(0, 'end')
        
        # Send user message 
        response = self.process_message(message)
        
        
        self.add_message_with_animation("You: " + message, 'user')
        

        if response:
            bot_response = response[0]['text']
        else:
            bot_response = "Sorry, I couldn't understand that."
        

        self.add_message_with_animation("Chatbot: " + bot_response, 'chatbot')

        # Speaks the response
        self.speak(bot_response)
        
    def process_message(self, message):
        payload = {
            "sender": "user",
            "message": message
        }
        
        try:
            response = requests.post(self.rasa_url, json=payload)
            return response.json()
        except requests.exceptions.RequestException:
            return None
        
    def add_message_with_animation(self, message, sender):
        self.chat_display.configure(state='normal')
        if self.chat_display.get(1.0, 'end') != '\n':
            self.chat_display.insert('end', '\n')
        self.chat_display.tag_config('user', foreground='blue')
        self.chat_display.tag_config('chatbot', foreground='green')
        chars_per_second = 20
        for i in range(len(message)):
            self.chat_display.insert('end', message[i], sender)
            self.chat_display.yview('end')
            self.chat_display.update()
            time.sleep(1 / chars_per_second)
        self.chat_display.insert('end', '\n')
        self.chat_display.configure(state='disabled')
        self.chat_display.yview('end')

        # Display image 
        if message.startswith('Image:'):
            image_url = message[6:]  # Extract image from message
            self.display_image(image_url)

    def display_image(self, image_url):
        try:
            response = requests.get(image_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img.thumbnail((200, 200))  
            photo = ImageTk.PhotoImage(img)
            self.chat_display.image_create('end', image=photo)
            self.chat_display.yview('end')
        except Exception as e:
            self.show_error_message(str(e))

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

if __name__ == '__main__':
    root = tk.Tk()
    chat_gui = ChatGUI(root)
    root.mainloop()
