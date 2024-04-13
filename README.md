<p align="center"><img src="./img/um7.jpg" width="400"  alt=" " /></p>
<h1 align="center"> RSX-UM7 Orientation Sensor </h1> 
<h4 align="right">April 24</h4>

<img src="https://img.shields.io/badge/OS-Linux%20GNU-yellowgreen">
<img src="https://img.shields.io/badge/OS-Windows%2011-blue">
<img src="https://img.shields.io/badge/Hardware-Raspberry%20ver%204-red">
<img src="https://img.shields.io/badge/Hardware-Raspberry%203B%2B-red">
<img src="https://img.shields.io/badge/Hardware-Raspberry%20Zero-red">
<img src="https://img.shields.io/badge/Python%20-V3.9.2-orange">

<br>


El sensor de orientación UM7 es un sistema de referencia de actitud y rumbo (AHRS) de cuarta generación. Combina datos de un acelerómetro de tres ejes, un giroscopio y un magnetómetro para producir estimaciones de actitud y rumbo.

El UM7 se conecta al software de interfaz de serie para permitir el trazado en tiempo real de los datos del sensor, el registro, la configuración del dispositivo y la calibración del magnetómetro.
Si no es necesario medir el ángulo de yaw, generalmente no es necesario calibrar el magnetómetro. Sin embargo, si el UM7 está funcionando en modo cuaternión, siempre se requiere la calibración del magnetómetro para un funcionamiento correcto

<br>

# Python Use
## Pre-requisito Modulo comunicación Serial
```
python3 -m pip install pyserial
```
o 
```
pip install pyserial
```
si da error por no tener pip resuelvelo:
```
sudo apt install python3-pip
```

## Testing
```python
pip install rsl-comm-py
```
Windows (usando FTDI convertidor)
```python
from rsl_comm_py import UM7Serial
um7_serial = UM7Serial(port_name='COM3')
for packet in um7_serial.recv_euler_broadcast():
    print(f"packet: {packet}")
```
El puerto COM dependera de cual le asigne el sistema operativo. 

linux (usando FTDI convertidor)
```python
from rsl_comm_py import UM7Serial
um7_serial = UM7Serial(port_name='/dev/ttyUSB0')
for packet in um7_serial.recv_euler_broadcast():
    print(f"packet: {packet}")
```
> :memo: **Note:** En RPi si se conecta si el FTDI al bus serial el puerto puede cambiar ej: ```/dev/ttyS0```

> :memo: **Note:** Es posible configurar el serial del dispositivo y conectarse al UM7 sin importar que puerto le asigne el OS.

<br>

---
Copyright &copy; 2022 [carjavi](https://github.com/carjavi). <br>
```www.instintodigital.net``` <br>
carjavi@hotmail.com <br>
<p align="center">
    <a href="https://instintodigital.net/" target="_blank"><img src="./img/developer.png" height="100" alt="www.instintodigital.net"></a>
</p>