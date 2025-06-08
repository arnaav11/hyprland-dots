import os, subprocess, time
from datetime import datetime as dt

os.chdir('/'.join(__file__.split('/')[::-1][1:][::-1])+'/')

bookmarks = ['Documents', 'Music', 'Pictures', 'Videos', 'Downloads']
dirs = [i for i in os.listdir() if os.path.isdir(i) and i != '.git']
dirs__ = [i for i in dirs if i != '.local']
dirs__.append('.local/share')
dirs_to_copy = {}
for i in dirs__:
    dirs_to_copy[i] = os.listdir(i)


backup_path = os.path.expanduser(f'~/.config/dots-backup-{dt.date(dt.now())}-{str(dt.time(dt.now())).split('.')[0]}')
home_path = os.path.expanduser('~')


print("Welcome to dotfiles installer for hyprland\n")

print("[i]nstall, [q]uit")
choice = input('>>> ')

if choice in ['i', 'install']:

    print("\nStarting installation...")
    time.sleep(0.5)


    print(f"\n{dirs_to_copy} \n\nDo you want to back up the above directories to {backup_path}?")
    print('[y]es, [n]o, [e]xit')
    choice = input('>>> ')

    if choice in ['e', 'exit']:
        print("Exiting...")
        time.sleep(0.3)
        exit()

    elif choice in ['y', 'yes']:
        os.mkdir(backup_path)
        for i in dirs:
            os.mkdir(f'{backup_path}/{i}')
        for i in dirs_to_copy.keys():
            for j in dirs_to_copy[i]:
                path_from = f'{home_path}/{i}/{j}'
                print(f'Copying {path_from} to {backup_path}')
                subprocess.run(['cp', '-r', f'{home_path}/{i}/{j}', f'{backup_path}/{i}/'])
        print("\nBackup Complete!")

    elif choice not in ['n', 'no']:
        print("Exiting...")
        time.sleep(0.3)
        exit()


    print(f"\n\nDo you want to complete the installation?")
    print('[y]es, [n]o')
    choice = input('>>> ')

    if choice in ['n', 'no'] or choice not in ['y', 'yes']:
        print("Exiting...")
        time.sleep(0.3)
        exit()

    print("Installing required packages...")
    time.sleep(0.3)    
    subprocess.run('yay -Syu --needed kitty firefox nemo gpu-screen-recorder-gtk gpu-screen-recorder anyrun-git swayosd swaync playerctl waybar hyprpaper hyprlock hyprpicker grim slurp swappy wlogout qt5ct qt6ct nwg-look nwg-displays kvantum starship thefuck pokemon-colorscripts-git'.split())

    print('Copying dotfiles...')
    time.sleep(0.3)
    for i in dirs_to_copy.keys():
        for j in dirs_to_copy[i]:
            # os.rmdir(f'{home_path}/{i}/{j}')
            print(f'Copying ./{i}/{j} to {home_path}/{i}/{j}')
            subprocess.run(['rm', '-rf', f'{home_path}/{i}/{j}'])
            subprocess.run(['cp', '-r', f'./{i}/{j}', f'{home_path}/{i}/'])
    
    lines = [f'{home_path}/{i} {i}\n' for i in bookmarks]
    with open(f'{home_path}/.config/gtk-3.0/bookmarks', 'w') as file:
        file.writelines(lines)
    with open(f'{home_path}/.config/gtk-4.0/bookmarks', 'w') as file:
        file.writelines(lines)

    print("Installation is complete, a reboot is needed to see changes")
    print('Reboot now?')
    print('[y]es, [n]o')
    choice = input('>>> ')

    if choice in ['y', 'yes']:
        print("rebooting...")
        time.sleep(0.3)
        subprocess.run(['systemctl', 'reboot'])

    

    
    
