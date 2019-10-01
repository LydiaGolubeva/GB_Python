#Голубева Лидия Ильинична

# Задача-1:
class Person:
    def __init__(self, health, damage, armor, name):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name
    def get_calculate_damage(self, armor):
        return self.damage // armor
    def attack(self, who_defend):
        atack = self.get_calculate_damage(who_defend.armor)
        who_defend.health -= atack
        print(f'{self.name} нанес {who_defend.name} урона {atack}, у того осталось {who_defend.health} жизней.')
class Player(Person):
    def __init__(self, health=100, damage=16, armor=5, name='Player'):
        super().__init__(health, damage, armor, name)
class Enemy(Person):
    def __init__(self, health=100, damage=19, armor=2, name='Enemy'):
        super().__init__(health, damage, armor, name)
class Game():
    def start_game(self):
        player = Player()
        enemy = Enemy()
        last_attacker = player
        while player.health > 0 and enemy.health > 0:
            if last_attacker == player:
                enemy.attack(player)
                last_attacker = enemy
            else:
                player.attack(enemy)
                last_attacker = player

        if player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


a = Game()
a.start_game()