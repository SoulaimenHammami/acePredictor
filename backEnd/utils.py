from rich import print 


def process_details(content): 
    matches_informations = []
    tournaments_split = content.split('- SINGLES: ')
    for detail in tournaments_split :
        infos =  detail.split('¬ZEE')
        if len(infos) <=1 :
            continue
        tournament_surface  , other = infos[0] , infos[1]
        tournament , surface = tournament_surface.split(', ')

with open('test.txt') as f:
    content = f.read()

process_details(content=content)