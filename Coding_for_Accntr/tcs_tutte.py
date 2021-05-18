class Player:
    def __init__(self, Name, Country, Age, noOfMatches, noOfRuns, noOfWickets):
        self.Name = Name
        self.Country = Country
        self.Age = Age
        self.noOfMatches = noOfMatches
        self.noOfRuns = noOfRuns
        self.noOfWickets = noOfWickets


class Team:
    def getMinRuns(self, player_list):
        min_run = []
        for run in player_list:
            min_run.append(run[4])
        mplayer = min_run.index(min(min_run))
        return player_list[mplayer]

    def getMaxWickets(self, player_list):
        max_w = []
        for run in player_list:
            max_w.append(run[4])
        mplayer = max_w.index(max(max_w))
        return player_list[mplayer]


if __name__ == '__main__':

    noOfPlayers = int(input())
    player_list = []
    for i in range(noOfPlayers):
        temp = []
        Name = input()
        Country = input()
        Age = int(input())
        noOfMatches = int(input())
        noOfRuns = int(input())
        noOfWickets = int(input())
        temp.append(Name)
        temp.append(Country)
        temp.append(Age)
        temp.append(noOfMatches)
        temp.append(noOfRuns)
        temp.append(noOfWickets)
        player_list.append(temp)

    obj = Team()
    ans = obj.getMinRuns(player_list)
    print(ans[0])
    print(ans[4])
    print(ans[1])

    ans2 = obj.getMaxWickets(player_list)
    print(ans2[0])
    print(ans2[5])
    print(ans2[1])
