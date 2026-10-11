
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Mini Notepad")
app.geometry("500x400")


textbox = ctk.CTkTextbox(
    app,
    width=460,
    height=270,
    font=("Arial", 14),
    wrap="word"
)
textbox.pack(pady=10)


counter_label = ctk.CTkLabel(app, text="Characters: 0")
counter_label.pack()

status_label = ctk.CTkLabel(app, text="")
status_label.pack()


def update_counter(event=None):
    text = textbox.get("1.0", "end-1c")
    counter_label.configure(text=f"Characters: {len(text)}")


def clear_text(event=None):
    textbox.delete("1.0", "end")
    update_counter()
    status_label.configure(text="Text cleared")


def save_text():
    text = textbox.get("1.0", "end-1c")

    with open("note.txt", "w", encoding="utf-8") as f:
        f.write(text)

    status_label.configure(text="Saved to note.txt")


textbox.bind("<KeyRelease>", update_counter)

buttons_frame = ctk.CTkFrame(app, fg_color="transparent")
buttons_frame.pack(pady=10)

clear_button = ctk.CTkButton(
    buttons_frame,
    text="Clear",
    command=clear_text
)
clear_button.pack(side="left", padx=5)

save_button = ctk.CTkButton(
    buttons_frame,
    text="Save",
    command=save_text
)
save_button.pack(side="left", padx=5)


app.mainloop()
