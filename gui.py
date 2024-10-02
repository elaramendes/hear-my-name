import flet as ft
from utils import AudioRecorder, PlaySong
import threading
import os


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
                record_button.text = "Stop"
                recorder = AudioRecorder(tf1.value)
                threading.Thread(target=recorder.audio_recorder, args=(update_text_in_gui, lambda: is_recording)).start()
            else:
                is_recording = False
                record_button.text = "Start"
                threading.Thread(target=should_exit).start()
        page.update()

    t = ft.Text()
    real_time_text = ft.Text("")
    tf1 = ft.TextField(label="Name", width=350, input_filter=ft.TextOnlyInputFilter())

    button = ft.ElevatedButton(text="Submit", on_click=submit_button)
    record_button = ft.ElevatedButton(text="Start", on_click=toggle_button)

    # Songs Section
    songs = [
        "songs/Song 1.mp3",
        "songs/Song 2.mp3",
        "songs/Song 3.mp3"
    ]

    player = PlaySong()
    def play_selected_song(song):
        def inner_play_song(e):
            player.play_song(song)
        return inner_play_song

    def stop_song(e):
        player.stop_song()

    def play_song_thread(player, file):
        player.play_song(file)

    song_buttons = []
    for song in songs:
        song_without_extension = os.path.splitext(song)[0]
        song_name = song_without_extension.split("/")[-1]
        song_buttons.append(ft.ElevatedButton(text=f"Play {song_name}", on_click=lambda e, song=song: threading.Thread(target=play_song_thread, args=(player, song)).start()))

    stop_song_button = ft.ElevatedButton(text="Stop", on_click=stop_song)

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
            ft.Text("Songs", size=20, weight=ft.FontWeight.BOLD),
            *song_buttons,
            ft.Row([stop_song_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(record_content)
    page.update()

ft.app(main)
