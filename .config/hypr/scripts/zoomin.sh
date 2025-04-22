hyprctl keyword cursor:zoom_factor $(($(hyprctl getoption cursor:zoom_factor -j | jq '.float?') + 0.1))
