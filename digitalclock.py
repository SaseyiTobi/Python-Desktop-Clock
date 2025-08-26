import tkinter as tk
from time import strftime

# Constants
BACKGROUND_COLOR = "#282c34"
TIME_COLOR = "#61dafb"
DATE_COLOR = "#ffffff"
FONT_STYLE = ("Helvetica", 48, "bold")
DATE_FONT_STYLE = ("Helvetica", 24)

class DigitalClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Digital Clock")
        self.master.geometry("400x250")
        self.master.resizable(False, False)
        self.master.configure(bg=BACKGROUND_COLOR)

        self.time_label = tk.Label(self.master, font=FONT_STYLE, bg=BACKGROUND_COLOR, fg=TIME_COLOR)
        self.time_label.pack(anchor="center", pady=20)

        self.date_label = tk.Label(self.master, font=DATE_FONT_STYLE, bg=BACKGROUND_COLOR, fg=DATE_COLOR)
        self.date_label.pack(anchor="center")

        self.toggle_button = tk.Button(self.master, text="Toggle 12/24 Hour", command=self.toggle_format, bg=TIME_COLOR, fg=BACKGROUND_COLOR, font=DATE_FONT_STYLE)
        self.toggle_button.pack(pady=10)

        self.is_24_hour_format = False  # Default to 12-hour format
        self.update_time()

    def update_time(self):
        if self.is_24_hour_format:
            current_time = strftime("%H:%M:%S")
        else:
            current_time = strftime("%I:%M:%S %p")  # 12-hour format

        current_date = strftime("%A, %B %d, %Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.master.after(1000, self.update_time)

    def toggle_format(self):
        self.is_24_hour_format = not self.is_24_hour_format  # Toggle the format
        self.update_time()  # Update the time display immediately

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()