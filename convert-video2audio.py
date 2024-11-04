import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

def convert_video_to_audio():
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv *.flv")]
    )
    if not video_path:
        return

    output_format = format_var.get()
    output_extension = f".{output_format}"
    output_path = filedialog.asksaveasfilename(
        title="Save Audio File",
        defaultextension=output_extension,
        filetypes=[(f"{output_format.upper()} files", f"*{output_extension}")]
    )
    
    if not output_path:
        return

    try:
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(output_path)
        messagebox.showinfo("Success", f"Audio file saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Video to Audio Converter")
root.geometry("400x200")
root.config(bg="#333333")

# Header Label
header_label = tk.Label(root, text="Video to Audio Converter", font=("Arial", 18, "bold"), fg="white", bg="#333333")
header_label.pack(pady=10)

# Output Format Label and Dropdown
format_label = tk.Label(root, text="Choose Output Format:", font=("Arial", 12), fg="white", bg="#333333")
format_label.pack(pady=5)

format_var = tk.StringVar(value="mp3")
format_options = ["mp3", "wav", "aac"]
format_dropdown = tk.OptionMenu(root, format_var, *format_options)
format_dropdown.config(width=10, font=("Arial", 12), bg="#555555", fg="white", highlightthickness=0)
format_dropdown.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert to Audio", font=("Arial", 14), bg="#4CAF50", fg="white", command=convert_video_to_audio)
convert_button.pack(pady=20)

# Run the Application
root.mainloop()
