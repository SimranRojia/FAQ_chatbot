import tkinter as tk
from tkinter import scrolledtext
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chatbot import chatbot

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FAQ Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")

        self.header_frame = tk.Frame(self.root, bg="#34495e")
        self.header_frame.pack(fill=tk.X)

        self.header_label = tk.Label(self.header_frame, text="FAQ Chatbot", fg="white", bg="#34495e", font=("Arial", 16, "bold"))
        self.header_label.pack(pady=10)

        self.chat_log_frame = tk.Frame(self.root, bg="#2c3e50")
        self.chat_log_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.chat_log = scrolledtext.ScrolledText(self.chat_log_frame, bd=1, bg="#ecf0f1", font=("Arial", 12), wrap=tk.WORD)
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.root, bg="#2c3e50")
        self.entry_frame.pack(fill=tk.X, padx=10, pady=10)

        self.entry_box = tk.Entry(self.entry_frame, bd=1, bg="#ecf0f1", font=("Arial", 14))
        self.entry_box.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        self.entry_box.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.entry_frame, text="Send", width=12, bd=0, bg="#3498db", fg="white", activebackground="#2980b9", font=("Arial", 12), command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        user_message = self.entry_box.get()
        if user_message:
            self.chat_log.config(state=tk.NORMAL)
            self.chat_log.insert(tk.END, "You: " + user_message + "\n\n")
            self.chat_log.config(foreground="#34495e", font=("Arial", 12))

            response = chatbot(user_message)
            self.chat_log.insert(tk.END, "Bot: " + response + "\n\n")
            self.chat_log.config(state=tk.DISABLED)
            self.chat_log.yview(tk.END)

            self.entry_box.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
