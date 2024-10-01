import flet as ft
from song_fn import play_music, stop_song
import cli
import threading


def main(page: ft.Page):
    page.title = "Voice Recorder"
    page.window_width = 350
    page.window_height = 350
    page.bgcolor = "#023047"

    def on_navigation_change(e):
        page.clean()
        if page.navigation_bar.selected_index == 0:
            page.add(record_content)
        else:
            page.add(song_content)
        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_navigation_change,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.MIC,
                label="Record"
            ),
            ft.NavigationDestination(
                icon=ft.icons.PLAY_CIRCLE_FILL_ROUNDED,
                label="Songs",
            )
        ]
    )

    is_recording = False
    page.update()

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

    def play_song(e):
        music_file = "songs/Shotgun Willy - Good Morning Vietnam.mp3"
        play_music(music_file)

    def stop_music(e):
        # ft.Text("Song stopped!")
        stop_song()

    play_song = ft.ElevatedButton(text="Play", on_click=play_song)
    stop_song_button = ft.ElevatedButton(text="Stop", on_click=stop_music)

    # Structure
    record_content = ft.Column(
        [
            ft.Text("Write your name below", size=20, weight=ft.FontWeight.BOLD),
            t,
            tf1,
            ft.Row([button, record_button], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([real_time_text], alignment=ft.MainAxisAlignment.CENTER)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    song_content = ft.Column(
        [
            ft.Text("Song 1", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([play_song, stop_song_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(record_content)
    page.update()

ft.app(main)
