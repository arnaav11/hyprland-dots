import subprocess, time

# subprocess.run(["pactl", "set-default-sink", "bluez_output.F0_AE_66_F5_8A_AD.1"])

# time.sleep(2)

s1 = subprocess.getoutput(["hyprctl activewindow"]).split("\n")[10].strip()[7:]
s2 = subprocess.getoutput(["pactl list sink-inputs"])

sinks = subprocess.getoutput(["pactl list short sinks"])

sinks = sinks.splitlines()
for i in sinks:
    i = i.strip()
    
    if "bluez" in i:
        bluetooh_id = ""
        x = 0
        while i[x].isdigit():
            bluetooh_id += i[x]
            x += 1

        print(f"Found device ID: {bluetooh_id}")

print(s1)


for i in s2.splitlines():
    i = i.strip()
    found = i.find("Input #")
    if found >= 0:
        s3 = i[found+7:]
        print(f"Found ID {s3}\n")

    found_x = i.find("Sink: ")
    if found_x >= 0:
        s5 = i[found_x+6:]
        print(f"Found sink: {s5}")
    
    found_2 = i.find("media.name")
    if found_2 >= 0:
        s4 = i[found_2+14:]
        s4 = s4[:len(s4)-1]

        print(s4)

        if s1 in s4 or s4 in s1:
            print(f"Found name {s4}")

            if s5 != bluetooh_id:
                subprocess.run(["pactl", "move-sink-input", f"{s3}", f"bluez_output.F0_AE_66_F5_8A_AD.1"])
                print("pactl", "move-sink-input", f"{s3}", f"bluez_output.F0_AE_66_F5_8A_AD.1")
            else:
                subprocess.run(["pactl", "move-sink-input", f"{s3}", f"alsa_output.pci-0000_04_00.6.analog-stereo"])
                print("pactl", "move-sink-input", f"{s3}", f"alsa_output.pci-0000_04_00.6.analog-stereo")
            
            break
