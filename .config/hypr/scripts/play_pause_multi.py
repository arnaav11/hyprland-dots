import sys, subprocess, time

STATE_ICONS = {'paused': ['media-playback-start', 'Playing'], 'playing': ['media-playback-pause', 'Paused']}

args_list = sys.argv[1:]
players_list = subprocess.getoutput('playerctl -l').split('\n')
players_states = subprocess.getoutput('playerctl status -a').lower().split('\n')


try:
    if args_list[0] == 'a':
        args_list = list(range(len(players_list)))
    else:
        args_list = list(map(lambda x: int(x)-1, args_list))

    players_states_display = list(map(lambda x: [STATE_ICONS[players_states[x]][0], STATE_ICONS[players_states[x]][1]], range(len(players_list))))    

    for i in args_list:
        if i < len(players_list):
            subprocess.run(['playerctl', 'play-pause', f'--player={players_list[i]}'])
            subprocess.run(['swayosd-client', f'--custom-icon={players_states_display[i][0]}', f'--custom-message={players_states_display[i][1]} {players_list[i].split('.')[0]}'])
            time.sleep(0.5)


except Exception as e:
    print(f"Error: {e}. \nArguments given: {args_list}")
