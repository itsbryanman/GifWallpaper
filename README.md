# GifWallpaper
a Python tool that allows users to set a GIF as their wallpaper on Windows or Linux. It opens an undecorated, borderless window that plays the GIF in a loop, making it look like a live wallpaper.


Instructions to Set Up and Run
Install Pillow (if not already installed):

bash
Copy code
pip install pillow
Set the GIF Path:

Replace "path/to/your/wallpaper.gif" with the path to the GIF you want to use.
Run the Script:

On Windows or Linux, open a terminal and run the script:
bash
Copy code
python gifwallpaper.py
Close the Wallpaper Window:

Press Alt + F4 or Ctrl + C in the terminal to close the script and remove the wallpaper effect.
Additional Notes
Cross-Platform Limitations:

This approach works by creating a “live wallpaper” effect using a fullscreen, borderless window with Tkinter. It’s not directly setting the GIF as a desktop background but rather simulating it.
Windows users may need additional configuration (like pygetwindow) to force the window behind desktop icons, as this behavior varies by setup.
System Resource Usage:

This script can be CPU-intensive since it’s rendering frames constantly. It’s best suited for short periods rather than permanent use.
Future Enhancements:

Implement system tray integration to allow for easier control.
Optionally minimize resource usage by adjusting the GIF frame rate or adding an option to pause the animation.
