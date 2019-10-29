import random


class Game:
    def start(self):
        print("started game")
        play = "y"
        total_wins = 0
        round = 0
        block = 0
        while play == "y":
            round = round + 1
            new_round = GameRound(round, block)
            won = new_round.start()
            play = input("Do you want to play again? (y/n) ")
            play = play.lower()
            if won:
                total_wins = total_wins + 1
        print("ended game")
        print("You won " + str(total_wins) + " games")
        print("You played " + str(round) + " games")


class GameRound:
    game_round = 0
    player_hp = 10
    enemy_hp = 10

    def __init__(self, game_round, block):
        self.game_round = game_round
        self.block = block

    def start(self):
        print("Round " + str(self.game_round) + ". FIGHT!")

        print("You encounter an enemy!")
        while self.player_hp > 0 and self.enemy_hp > 0:
            self.play_turn()
            self.enemy_turn()

        if self.player_hp <= 0:
            print("You lost!")
            return False
        if self.enemy_hp <= 0:
            print("You won!")
            return True


    def play_turn(self):
        action = ""
        print("player turn")
        while action != "attack" and action != "heal" and action != "block":
            action = input("Do you want to 'attack', 'heal' or 'block' ").lower().strip()
            if action == "attack":
                damage = random.randint(0, 5)
                self.enemy_hp = self.enemy_hp - damage
                print("You dealt " + str(damage) + " damage! The enemy's remaining health is " + str(self.enemy_hp))
            elif action == "heal":
                heal = random.randint(0, 5)
                self.player_hp = self.player_hp + heal
                print("You healed " + str(heal) + " health! Your current health is " + str(self.player_hp))
            elif action == "block":
                self.block = random.randint(0, 5)
                print("You will block " + str(self.block) + " damage next round ")
            else:
                print("Please enter a valid answer")

    def enemy_turn(self):
        if self.enemy_hp > 0:
            print("enemy turn")
            enemy_damage = random.randint(0, 5)
            enemy_damage = enemy_damage - self.block
            if enemy_damage > 0:
                self.player_hp = self.player_hp - enemy_damage
                print("The enemy dealt " + str(enemy_damage) + " damage! Your remaining health is " + str(self.player_hp))
            else:
                print("The enemy dealt no damage!")
