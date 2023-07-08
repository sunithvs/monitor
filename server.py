import socket
from pynput import mouse, keyboard


def on_move(x, y):
    data = f'Mouse moved to ({x}, {y})'
    conn.send(data.encode())


def on_click(x, y, button, pressed):
    data = f'Mouse {"clicked" if pressed else "released"} at ({x}, {y}) with {button}'
    conn.send(data.encode())


def on_scroll(x, y, dx, dy):
    data = f'Mouse scrolled at ({x}, {y}) with ({dx}, {dy})'
    conn.send(data.encode())


def on_press(key):
    data = f'Key {key} pressed'
    conn.send(data.encode())


def on_release(key):
    data = f'Key {key} released'
    conn.send(data.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as m_listener, keyboard.Listener(
                on_press=on_press, on_release=on_release) as k_listener:
            m_listener.join()
            k_listener.join()
