import tkinter as tk
from tkinter import ttk
# Ensure desktop.py exists in the same directory or is correctly installed
import desktop.desktop as desktop  

def show_splash_screen():
    splash_root = tk.Tk()
    splash_root.overrideredirect(True)
    splash_root.geometry("300x180+500+300")

    tk.Label(splash_root, text="ChipOS", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    status_label = tk.Label(splash_root, text="Starting...", font=("Helvetica", 10))
    status_label.pack(pady=5)

    # Indeterminate mode creates the bouncing animation
    progress = ttk.Progressbar(splash_root, orient="horizontal", length=220, mode="indeterminate")
    progress.pack(pady=10)
    
    # Start the animation (moves every 10ms)
    progress.start(10)

    def launch_main():
        # Stop the progress bar and close splash screen
        progress.stop()
        splash_root.destroy()
        # Call the main function of your desktop module
        desktop.main() 

    # Wait 5000ms (5 seconds) without freezing the UI, then launch
    splash_root.after(5000, launch_main)
    
    splash_root.mainloop()

if __name__ == "__main__":
    show_splash_screen()
