import subprocess
# import time


default_sink = subprocess.getoutput(["pactl get-default-sink"])
sinks_raw = subprocess.getoutput([f"pactl list sinks | grep \"Sink #\""]).split('\n')
print("pactl list sinks | grep \"{default_sink}\"")
default_sink_num = int(subprocess.getoutput([f"pactl list short sinks | grep \"{default_sink}\""]).split('\t')[0])
to_change = -1


sinks = []
for raw_sink_line in sinks_raw:
    sinks.append(int(raw_sink_line.split("#")[1]))

for sink_num in sinks:
    if sink_num != default_sink_num:
        # subprocess.run(["pactl", "set-default-sink", str(sink_num)])
        to_change = sink_num

# time.sleep(2)

current_window_name = subprocess.getoutput(["hyprctl activewindow | grep \"title: \""]).strip().split(": ")[1]
sink_inputs_info_raw = subprocess.getoutput(["pactl list sink-inputs"]).split('\n')

print(current_window_name)


for sink_input_info_raw in sink_inputs_info_raw:

    sink_input_info_raw = sink_input_info_raw.strip()
    found_sink_input_num = sink_input_info_raw.find(f"Input #")

    if found_sink_input_num >= 0:
        sink_input_num = sink_input_info_raw.split("#")[1]
        print(f"found sink input: {sink_input_num}")

    found_sink_input_sink = sink_input_info_raw.find("Sink: ")
    if found_sink_input_sink >= 0:
        sink_input_sink_num = sink_input_info_raw.split(": ")[1]
        print(f"Found sink: {sink_input_sink_num}")
    
    found_sink_input_name = sink_input_info_raw.find("media.name")
    if found_sink_input_name >= 0:
        sink_input_name = sink_input_info_raw.split(" = ")[1].strip("\"")
        sink_input_name = sink_input_name[:len(sink_input_name)-1]
        print(sink_input_name)

        if current_window_name in sink_input_name or sink_input_name in current_window_name:
            print(f"Match found {sink_input_name}")

            if to_change >= 0:
                subprocess.run(["pactl", "move-sink-input", f"{sink_input_num}", f"{to_change}"])
            
            break
