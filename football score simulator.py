import random

class Team:
    def __init__(self, market: str, nickname: str) -> None:
        """Takes in market and nickname then inits stats to zero"""
        self.market = market
        self.nickname = nickname
        self.fullname = f"{market} {nickname}"
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.points_for = 0
        self.points_against = 0

    def __repr__(self) -> str:
        """Return a string that can recreate this object."""
        return f'Team("{self.market}", "{self.nickname}")'
    
    def __str__(self) -> str:
        """Returns selfs fullname with their record, points for, and points against"""
        return f"{self.fullname} ({self.record}) PF: {self.points_for} | PA: {self.points_against}"
    
    @property
    def record(self) -> str:
        """Returns selfs record, based if there are any recorded ties"""
        if self.ties > 0:
            return f"{self.wins}-{self.losses}-{self.ties}"
        else: 
            return f"{self.wins}-{self.losses}"
    
    def add_win(self, points_for: int, points_against: int) -> None:
        """Adds win and calls _add_points"""
        self.wins += 1
        self._add_points(points_for, points_against)

    def add_loss(self, points_for: int, points_against: int) -> None:
        """Adds loss and calls _add_points"""
        self.losses += 1
        self._add_points(points_for, points_against)
 
    def add_tie(self, points_for: int, points_against: int) -> None:
        """Adds tie and calls _add_points"""
        self.ties += 1
        self._add_points(points_for, points_against)

    def _add_points(self, points_for: int, points_against: int) -> None:
        """Private function to add points for and points against"""
        self.points_for += points_for
        self.points_against += points_against


def main():
    """Initializes two teams, simulates 5 games, then prints their records"""
    team1 = Team("Las Vegas", "Raiders")
    team2 = Team("New England", "Patriots")
    simulate_game(team1, team2, 5)
    print(team1, team2, sep="\n")


def simulate_game(home: Team, away: Team, times=1) -> None:
    """Simulates games n times, printing the result each time and updating team stats"""
    for _ in range(times):    
        home_score = random_football_score()
        away_score = random_football_score()
        if home_score > away_score:
            home.add_win(home_score, away_score)
            away.add_loss(away_score, home_score)
            print(f"{home.nickname} beat the {away.nickname} {home_score} to {away_score}!")
        elif away_score > home_score:
            away.add_win(away_score, home_score)
            home.add_loss(home_score, away_score)
            print(f"{away.nickname} beat the {home.nickname} {away_score} to {home_score}!")
        else:
            home.add_tie(home_score, away_score)
            away.add_tie(away_score, home_score)
            print("Tie game!")

def random_football_score() -> int:
    """Returns simple valid football score"""
    touchdowns = 6 * random.randint(0,7)
    pats = 0
    for _ in range(touchdowns // 6):
        if random.random() < 0.94:
            pats += 1
    fieldgoals = 3 * random.randint(0,4)
    return touchdowns + fieldgoals + pats





if __name__ == "__main__":
    main()