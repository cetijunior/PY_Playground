import tkinter
from pytube import YouTube
import customtkinter
import traceback

# Global variable to store video qualities and associated streams
quality_stream_map = {}

def populateQualityOptions(*args):
    global quality_stream_map
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        quality_stream_map = {}
        for stream in ytObject.streams.filter(progressive=True, file_extension='mp4'):
            quality_stream_map.setdefault(stream.resolution, []).append(stream)
        quality_option_menu.configure(values=list(quality_stream_map.keys()))
    except Exception as e:
        quality_option_menu.configure(values=["No qualities available"])
        print(traceback.format_exc())  # For debugging purposes

def onP(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    perc_of_comp = (bytes_downloaded / total_size) * 100
    per = str(int(perc_of_comp))
    pPerc.configure(text = per + '%')
    pPerc.update()
    
    #prog Bar
    progressBar.set(float(perc_of_comp) / 100 )
    

def startDownload():
    global quality_stream_map
    try:
        selected_quality = quality_var.get()
        if selected_quality in quality_stream_map:
            stream = quality_stream_map[selected_quality][0]
            yt = YouTube(link.get(), on_progress_callback=onP)  # Added on_progress_callback
            stream = yt.streams.get_by_itag(stream.itag)  # Get the stream from the updated yt object
            # Modify the filename to include the selected quality
            custom_filename = f"{yt.title}-{selected_quality}.{stream.mime_type.split('/')[1]}"
            stream.download(filename=custom_filename)
            finishLabel.configure(text="Downloaded", text_color="white")
        else:
            finishLabel.configure(text="Please select a valid quality", text_color="red")
    except Exception as e:
        finishLabel.configure(text=f"An error occurred: {e}", text_color="red")
        print(traceback.format_exc())  # 

# sys settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# title
title = customtkinter.CTkLabel(app, text="Paste the YouTube Link: ")
title.pack(padx=10, pady=10)

# link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Automatically load qualities when link is pasted/changed
url_var.trace_add("write", populateQualityOptions)

# finish download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# progress %
pPerc = customtkinter.CTkLabel(app, text="0.00%")
pPerc.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text="Download")
download.configure(command=startDownload)
download.pack(padx=10, pady=10)

# Dropdown for quality selection
quality_var = customtkinter.StringVar()
quality_option_menu = customtkinter.CTkOptionMenu(app, variable=quality_var, values=["Select a quality"])
quality_option_menu.pack(padx=10, pady=10)

# warning label
warning = customtkinter.CTkLabel(app, text="Videos should not be age restricted for the downloader to work", text_color="red")
warning.pack(pady=50)



app.mainloop()
