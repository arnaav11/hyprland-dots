import subprocess

# Change the value in quotes to the MAC address of yout Bluetooth device
mac_address = "34:E3:FB:80:84:13"

if subprocess.getoutput(["pactl get-default-sink"]) == "alsa_output.pci-0000_04_00.6.analog-stereo":
    subprocess.run(["pactl", "set-default-sink", f"bluez_output.{mac_address}"])
else:
    subprocess.run(["pactl", "set-default-sink", "alsa_output.pci-0000_04_00.6.analog-stereo"])