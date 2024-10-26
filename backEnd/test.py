import requests
from rich import print
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

def get_user_agent() -> str:
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value,
                            OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent



def get_player_matches(player_id: str) :
    headers = {
        "User-Agent" : get_user_agent(),
        "x-fsign" : "SW9D1eZo",
        "Origin" : "https://www.tennis24.com"
    }
    url = "https://global.flashscore.ninja/107/x/feed/pr_2_59_{player_id}_{index}_1_en_2_s"
    non_done = True
    index =0
    while non_done :
        response = requests.get(url=url.format(player_id= player_id , index= index) , headers=headers)
        print("Index" , index, "Status code", response.status_code)
        if response.status_code == 200 : 
            if len(response.text) >0 :
                yield response.text
                index+=1
            else:
                return  
        else:
            return
def get_matches_ids(player_matches: str)->list :
    matches_ids =[]
    elements=  player_matches.split('AA÷')
    matches_ids =[match.split("¬AD÷")[0] for match in elements if len(match.split("¬AD÷")[0])==8 ]
    return matches_ids


def process_details(content): 
    matches_informations = []
    tournaments_split = content.split('- SINGLES: ')
    for detail in tournaments_split :
        tournament_surface  , other = detail.split('¬ZEE')
        tournament , surface = tournament_surface.split(', ')
        
if __name__ =="__main__":
    player_id =  "xCD2BANp"
    content= get_player_matches(player_id=player_id)
    matches_ids = []
    for content in get_player_matches(player_id=player_id):
        ids = get_matches_ids(content)
        matches_ids.extend(ids) 
    print(len(matches_ids))