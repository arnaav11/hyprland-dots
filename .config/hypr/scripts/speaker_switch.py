import subprocess

if subprocess.getoutput(["pactl get-default-sink"]) == "alsa_output.pci-0000_04_00.6.analog-stereo":
    subprocess.run(["pactl", "set-default-sink", "bluez_output.F0_AE_66_F5_8A_AD.1"])
else:
    subprocess.run(["pactl", "set-default-sink", "alsa_output.pci-0000_04_00.6.analog-stereo"])