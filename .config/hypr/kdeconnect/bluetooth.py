import subprocess

bt_power = 'yes' in subprocess.getoutput(['bluetoothctl show | grep "Powered"']).strip().lower()

if bt_power:
    subprocess.run(['bluetoothctl', 'power', 'off'])
else:
    subprocess.run(['bluetoothctl', 'power', 'on'])