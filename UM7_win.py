from rsl_comm_py import UM7Serial

# Inicializa la comunicación con el sensor UM7 en el puerto COM7
um7_serial = UM7Serial(port_name='COM7')

# Recibe el primer paquete de ángulos de Euler del sensor UM7
packet = next(um7_serial.recv_euler_broadcast())

# Accede a los atributos del paquete para obtener los valores de pitch, roll y yaw
pitch = packet.pitch
roll = packet.roll
yaw = packet.yaw

# Imprime los valores de pitch, roll y yaw
print(f"Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}")
