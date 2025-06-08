import subprocess, os
home_path = os.path.expanduser("~")

current_mode_file = open("/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode").read()[0]

if current_mode_file == "1":
    subprocess.run(["sh", f"{home_path}/.config/hypr/scripts/conservation_off.sh"])
else:
    subprocess.run(["sh", f"{home_path}/.config/hypr/scripts/conservation_on.sh"])