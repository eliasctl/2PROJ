import random

class Player:
    def __init__(self):
        self.xp = 0
        self.gold = 100

    def earn_xp_and_gold(self, idTroop):
        idTroop = int(idTroop)
        # Simulating combat and earning XP and gold based on enemy level
        xp_earned = random.randint(4, 10) * idTroop
        gold_earned = random.randint(1, 7) * idTroop
        self.xp += xp_earned
        self.gold += gold_earned
        # print(f"Earned {xp_earned} XP and {gold_earned} gold.")

    def passive_income(self, civilization):
        civilization = int(civilization)
        # Simulating passive XP income based on civilization level
        xp_earned = random.randint(0, 10) * civilization
        gold_earned = random.randint(0, 4) * civilization
        self.xp += xp_earned
        self.gold += gold_earned
        # print(f"Earned {xp_earned} XP and {gold_earned} passively.")

# player = Player()
# idTroop = 3
# player.earn_xp_and_gold(idTroop)

# # Adding passive XP income for 5 minutes
# civilization = 5
# player.passive_income(civilization)

# print(f"Total XP: {player.xp}, Total Gold: {player.gold}")
