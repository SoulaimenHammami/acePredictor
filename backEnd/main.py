import re as regex
from rich import print
from datetime import datetime
with open('./cilicMatch.txt') as f :
    data = f.readlines()[0]

tournaments_lines= data.split('¬~ZA÷ATP - SINGLES: ')[1:]

##### functions : 
def get_tournament_grass(line:str):
    splitted = line.split('¬ZEE÷')
    tournament_grass , matches_encoded= splitted[0].split(', ') , splitted[1]
    tournament = tournament_grass[0] if len(tournament_grass) > 0  else None
    grass = tournament_grass[1] if len(tournament_grass) >= 2  else None
    return tournament , grass , matches_encoded

def extract(start, end , string):
    pattern = rf'{regex.escape(start)}(.*?){regex.escape(end)}'
    return regex.findall(pattern=pattern , string=string)


def get_match_generic_infos(encoded_line:str):
    ids = extract(
        start="¬~AA÷" ,
        end="¬AD÷",
        string=line
        )
    dates =  extract(
        start="¬AD÷",
        end="¬ADE÷",
        string=line
        )

    player_one =  extract(
        start="¬AB÷3¬CR÷3¬AC÷3¬CX÷",
        end="¬RW÷0¬AX÷0¬AO÷",
        string=line
        )
    player_two =  extract(
        start="¬AF÷",
        end="¬FK÷",
        string=line
        )
    score_right =  extract(
        start="¬AT÷",
        end="¬BA÷",
        string=line
        )
    score_left =  extract(
        start="¬AU÷",
        end="¬BB÷",
        string=line
        )
    print("[dark_red] ids: ",ids)
    print("[dark_red] dates: ",dates)
    print("[dark_red] player_one: ",player_one)
    print("[dark_red] player_two: ",player_two)
    print("[dark_red] score_right: ",score_right)
    print("[dark_red] score_left: ",score_left)
    
"""
¬AU÷
¬BB÷


¬AT÷
¬BA÷
"""

for line in tournaments_lines: 
    # print("[yello] {line}".format(line=line))
    tournament , grass , matches_encoded =get_tournament_grass(line)
    print("[red] - Tournament Name " , tournament)
    print("[red] - Grass Type" , grass)
    print("[blue] - Rest" , matches_encoded)

    infos  = get_match_generic_infos(matches_encoded)
    print("--"*20)
