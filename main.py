from pytube import YouTube
from tkinter import *
from tkinter import messagebox


def Pass_link():
    link = yt_link_box.get()
    Download(link)


# --------------UI Setup------------

window = Tk()
window.title("YouTube Downloader")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=189)
logo_image = PhotoImage(file="YouTube-Logo.wine.png")
canvas.create_image(200, 100, image=logo_image)
canvas.grid(row=0, column=1)

yt_link = Label(text="Link:")
yt_link.grid(row=1, column=0)

yt_link_box = Entry(width=45)
yt_link_box.focus()
yt_link_box.grid(row=1, column=1)

download = Button(text="Download", width=36, command=Pass_link)
download.grid(row=2, column=1, columnspan=2)

note = Label(text="This is an appliction for Download any Youtube Video in Maximum Resolution\n"
                  "Developer: Adarsh Prakash\n"
                  "Github: https://github.com/mikiadarsh25")
note.grid(row=3, column=0, columnspan=2)


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("Downloads")
    except:
        messagebox.showerror("Error", "An error has occurred")
    messagebox.showinfo("Sucessful", "Download is completed successfully")


window.mainloop()
