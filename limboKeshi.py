import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Feel more like limbo, hands out my window", 0.09),
        ("Chasin' that sunset, that's more my tempo", 0.1),
        ("Yeah, that's more my tempo", 0.1),
        ("Ooooooh, but this is all that I am", 0.10),
        ("I only show you the best of me", 0.10),
        ("The best of meeee", 0.14),
    ]
    delays = [0.3, 2.4, 9.5, 15.1, 20.2, 25.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()




