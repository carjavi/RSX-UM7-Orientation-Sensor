from rsl_comm_py import UM7Serial
um7_serial = UM7Serial(port_name='/dev/ttyS0')
for packet in um7_serial.recv_euler_broadcast():
    print(f"packet: {packet}")