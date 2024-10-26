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


class PlayerCollector:

    def get_player_matches(self, player_id: str, index: int )-> str | None:
        headers = {
            "User-Agent" : get_user_agent(),
            "x-fsign" : "SW9D1eZo",
            "Origin" : "https://www.tennis24.com"
        }
        url = "https://global.flashscore.ninja/107/x/feed/pr_2_59_{player_id}_{index}_1_en_2_s"
        response = requests.get(url=url.format(player_id= player_id , index= index) , headers=headers)
        print( "Player ID" , player_id, "Index" , index, "Status code", response.status_code)
        if response.status_code == 200  :
            if len(response.text ) > 0: 

                return response.text
            print( "Player ID" , player_id, "Index" , index, "Status code", response.status_code , "Content Empty")
        
        return  None
    
    def match_informations(self, content: str)-> list | None:
        # tournaments = content.split('÷ATP -')
        # tournaments = tournaments[1:]
        tournaments = content.split('- SINGLES:')[1:] if len(content.split('- SINGLES:')) > 0 else []
        details = [x.split('¬ZEE÷') for x in tournaments]
        # d = [(i[0] ,i[1].split("¬~AA÷")) for i in details if len(i) > 0]
        d = [(i[0] ,i[1].split("¬~AA÷")[1]) for i in details if len(i) > 1 and len(i[1].split("¬~AA÷"))> 1 ]
        return d

    def matches_stats(self ,player_id: str )-> dict | None :
        index = 1
        matches_encoded = self.get_player_matches(player_id=player_id , index=index)
        with open('cilicMatch.txt' ,"w") as f:
            f.write(matches_encoded)
            print("[red] has been saved")
        if 'v3L4xQnC' in matches_encoded:
            print('[green] It exists')
        print("match encoded" , matches_encoded)
        infos = self.match_informations(content=matches_encoded)
        import re
        patterns = [
            r"¬AD÷(.*?)¬ADE÷",  # Pattern 1
            r"¬CX÷(.*?)¬RW÷",   # Pattern 2
            r"¬AF÷(.*?)¬FK÷"    # Pattern 3
        ]
        if infos:
            h =[(i[0] , [re.search(pattern , i[1]).group(1) for pattern in patterns])  for i in infos]
            print(h)    