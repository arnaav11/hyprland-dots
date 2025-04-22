import sys, subprocess


def main(argv: list[str]):
    mac_address = argv[0]

    if mac_address in subprocess.getoutput(["bluetoothctl devices Connected"]):
        subprocess.run(["bluetoothctl", "disconnect", mac_address])
    else:
        subprocess.run(["bluetoothctl", "connect", mac_address])

    
if __name__ == "__main__":
    print("Number of arguments:", len(sys.argv))
    print("Arguments:", sys.argv)

    main(sys.argv)