import random

class Player:
    def __init__(self):
        self.xp = 1000
        self.gold = 2500

    def earn_xp_and_gold(self, enemy_level):
        # Simulating combat and earning XP and gold based on enemy level
        xp_earned = random.randint(10, 50) * enemy_level
        gold_earned = random.randint(5, 25) * enemy_level
        self.xp += xp_earned
        self.gold += gold_earned
        print(f"Earned {xp_earned} XP and {gold_earned} gold.")

    def passive_income(self, duration):
        # Simulating passive XP income over a duration of time
        xp_earned = random.randint(10, 100) * duration
        gold_earned = random.randint(10, 50) * duration
        self.xp += xp_earned
        self.gold += gold_earned
        print(f"Earned {xp_earned} XP and {gold_earned} passively.")

player = Player()
enemy_level = 3
player.earn_xp_and_gold(enemy_level)

# Adding passive XP income for 5 minutes
duration = 5
player.passive_income(duration)

print(f"Total XP: {player.xp}, Total Gold: {player.gold}")
