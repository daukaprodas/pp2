class Sportsman:
    
    def __init__(self,sport_id,sport_name) -> None:
        self.sport_id = int(sport_id)
        self.sport_name =sport_name
        
    def __str__(self) -> str:
        return '{} {}'.format(self.sport_id, self.sport_name)
    
    
class TeamSport(Sportsman):

    def __init__(self,sport_id,sport_name,  num_players) -> None:
        super().__init__(sport_id,sport_name)
        
        self.num_players = int(num_players)
    
    def __str__(self) -> str:
        return super().__str__()+' '+'{} {}'.format(self.num_players)
    
class classFootball(TeamSport):
    def __init__(self,sport_id,sport_name, num_players,team_name) -> None:
        super().__init__(sport_id,sport_name, num_players)
        self.team_name=team_name
       
    def __str__(self) -> str:
        return super().__str__()+' '+'{} {}'.format(self.team_name)


s1 = classFootball(123456,'Football',11,'Kaysar')

l = [s1]

for i in l:
    print(i)