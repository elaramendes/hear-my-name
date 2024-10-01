import pygame as pg

pg.mixer.init()

def play_music(song_fn):

    pg.mixer.music.load(song_fn)

    pg.mixer.music.play()

def stop_song():
    pg.mixer.music.stop()