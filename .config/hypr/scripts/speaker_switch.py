import subprocess

# Change the value in quotes to the MAC address of yout Bluetooth device
mac_address = "34:E3:FB:80:84:13"

default_sink = subprocess.getoutput(["pactl get-default-sink"])
sinks_raw = subprocess.getoutput([f"pactl list sinks | grep \"Sink #\""]).split('\n')
print("pactl list sinks | grep \"{default_sink}\"")
default_sink_num = int(subprocess.getoutput([f"pactl list short sinks | grep \"{default_sink}\""]).split('\t')[0])

sinks = []
for raw_sink_line in sinks_raw:
    sinks.append(int(raw_sink_line.split("#")[1]))

for sink_num in sinks:
    if sink_num != default_sink_num:
        subprocess.run(["pactl", "set-default-sink", str(sink_num)])