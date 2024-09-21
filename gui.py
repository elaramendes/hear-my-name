import flet as ft

import cli
import threading


def main(page: ft.Page):
    page.title = "Voice Recorder"
    page.window_width = 350
    page.window_height = 350
    page.bgcolor = "#e9ecef"
    is_recording = False

    def submit_button(e):
        if tf1.value != "":
            t.value = f"The name you chose is {tf1.value}"
        page.update()

    def update_text_in_gui(text):
        real_time_text.value = text
        page.update()

    def should_exit():
        page.window_destroy()

    def toggle_button(e):
        nonlocal is_recording, should_exit
        if tf1.value != "":
            if not is_recording:
                is_recording = True
                record_button.text = "Exit"
                threading.Thread(target=cli.audio_recorder, args=(tf1.value, update_text_in_gui, lambda: is_recording)).start()
            else:
                is_recording = False
                record_button.text = "Start"
                threading.Thread(target=should_exit).start()
        # cli.audio_recorder(tf1.value)
        page.update()

    t = ft.Text()
    real_time_text = ft.Text("")
    tf1 = ft.TextField(label="Name", width=350, input_filter=ft.TextOnlyInputFilter())

    button = ft.ElevatedButton(text="Submit", on_click=submit_button)
    record_button = ft.ElevatedButton(text="Start", on_click=toggle_button)

    # Structure
    page.add(
        ft.Column(
            [
                ft.Text("Write your name below", size=20, weight=ft.FontWeight.BOLD),
                t, tf1
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
            button, record_button
        ],
            alignment=ft.MainAxisAlignment.CENTER
    ),
        ft.Row(
            [
               real_time_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
)

ft.app(main)
