import sys
import os
import platform
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

# Directory path to the GIF you want to use as wallpaper
GIF_PATH = "path/to/your/wallpaper.gif"

class AnimatedGIF(tk.Label):
    """
    Class to handle animated GIF as a Tkinter Label
    """
    def __init__(self, master, gif_path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.gif_path = gif_path
        self.frames = []
        self.delay = 100
        self.load_gif()
        self.current_frame = 0
        self.show_frame()

    def load_gif(self):
        """
        Loads frames of the GIF into a list
        """
        gif = Image.open(self.gif_path)
        try:
            for i in count(1):
                frame = ImageTk.PhotoImage(gif.copy().convert("RGBA"))
                self.frames.append(frame)
                gif.seek(i)
        except EOFError:
            pass
        self.delay = gif.info.get("duration", 100)  # GIF frame duration

    def show_frame(self):
        """
        Displays the next frame in the list
        """
        frame = self.frames[self.current_frame]
        self.configure(image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(self.delay, self.show_frame)

def set_gif_as_wallpaper():
    """
    Opens a borderless window to display the GIF on the desktop as a wallpaper
    """
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)  # Keep window on top
    root.overrideredirect(True)  # Remove borders and title

    # Set up the animated GIF as a full-screen label
    gif_wallpaper = AnimatedGIF(root, GIF_PATH)
    gif_wallpaper.pack(expand=True, fill="both")

    # Position the window behind desktop icons if possible
    if platform.system() == "Linux":
        root.lower()
    elif platform.system() == "Windows":
        # Windows-specific behavior if additional libraries like pygetwindow are installed
        try:
            import pygetwindow as gw
            win = gw.getWindowsWithTitle(root.title())[0]
            win.minimize()
            win.restore()  # To push it back behind icons, works on some setups
        except ImportError:
            print("Optional: Install pygetwindow for better Windows control.")

    root.mainloop()

if __name__ == "__main__":
    if not os.path.isfile(GIF_PATH):
        print(f"Error: GIF file not found at '{GIF_PATH}'")
        sys.exit(1)
    set_gif_as_wallpaper()
