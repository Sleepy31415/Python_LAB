"""
exercise: Object oriented role playing game, part 2 :

As always, read the whole exercise description carefully before you begin to solve the exercise.

Build on your solution of part 1.

Invent two new classes, which inherit from class Character. For example Hunter and Magician.
Your new classes shall have their own additional methods and/or attributes. Maybe they also override methods or attributes from class Character.

In the main program, let objects of your new classes fight against each other until one character is dead.
Print out what happens during the fight.

In each turn, a character uses one of its capabilities (methods). Then it's the other character's turn.
It is up to you, how your program decides in each turn, which capability to use.
For example, the decision may be based on randomness or on a clever strategy

Upgrade 1:
Each time a character uses one of it's capabilities, add some randomness to the used power.

Upgrade 2:
Let your characters fight against each other 100 times.
Keep track of the results.
Try to balance your character's capabilities in such a way that each character wins about half of the fights.

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
import random as rand

class Character:

    def __init__(self, name, health, attackpower, massive_hit):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower
        self.massive_hit = massive_hit

    def __repr__(self):
        # the number behind '=' don´t seem to do anything
        return f"Character: {self.name=:11}   {self.max_health=:4}     {self._current_health=:4}     {self.attackpower=:3}"

    def hit(self, other):
        print("\n", self.name, "hits", other.name, "for", self.attackpower, "damage", "\n")
        other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    def get_healed(self, healpower):
        self._current_health += healpower

    # get from other classes
    def get_shot_by_gun(self, gunpower):
        self._current_health -= gunpower

    # I am not sure why this line is highlighted
    def get_hit_themselves(self, other):
        self._current_health -= self.attackpower

    def get_hail_marry_strike(self, other):
        massive_hit = 100
        self._current_health -= massive_hit

    def health_check(self):
        if self._current_health > 0:
            print(f"{self.name} is alive and well. They still have a fighting spirit and {self._current_health} left!")
        else:
            print(f"{self.name} has fallen.")
            return self._current_health


    def fight(self, other):
        while self.health_check() > 0 and other.health_check() > 0:
            self.battle_plan(other)
            other.health_check()
            other.battle_plan(self)
            self.health_check()


class Healer(Character):

    def __init__(self, name, health, healpower, massive_hit):
        super().__init__(name, health, 0, 75)
        self.healpower = healpower

    def heal(self, other):
        print("\n", self.name, "heals", other.name, "for", self.healpower, "damage", "\n")
        other.get_healed(self.healpower)

    def hail_marry_strike(self, other):
        ran_number = rand.randint(0, 9)
        if ran_number == 1:
            other.get_hail_marry_strike(other)
            print(f" {self.name}´s Hail Marry worked! {other.name} got hit for {self.massive_hit} damage!")


class Human(Character):
    def __init__(self, name, health, attackpower, gunpower, bulletamount, massive_hit):
        super().__init__(name, health, attackpower, 200)
        self.bulletamount = bulletamount
        self.gunpower = gunpower

    def gun(self, other):
        if self.bulletamount > 0:
            print(f"{self.name} used a gun to shoot {other.name} for {self.gunpower} damage")
            other.get_shot_by_gun(self.gunpower)
        else:
            print(f" {self.name} tried to use their gun, but it was empty")

    def hail_marry_strike(self, other):
        ran_number = rand.randint(0, 9)
        if ran_number == 1:
            other.get_hail_marry_strike(other)
            print(f" {self.name}´s Hail Marry worked! {other.name} got hit for {self.massive_hit} damage!")

        else:
            print(f"{self.name} missed {other.name}")

    def battle_plan(self, other):
        if self.bulletamount > 0:
            self.gun(other)
            self.bulletamount -= 1
        else:
            Character.hit(self, other)



class Druid(Character):
    def __init__(self, name, health, attackpower, massive_hit):
        super().__init__(name, health, attackpower, 150)

    def hit_themselves(self, other):
        print(f"{self.name} made {other.name} hit themselves for {other.attackpower} damage")
        other.get_hit_themselves(other.attackpower)

    def battle_plan(self, other):
        if self.attackpower <= other.attackpower:
            self.hit_themselves(other)
        else:
            Character.hit(self, other)

    def hail_marry_strike(self, other):
        ran_number = rand.randint(0, 9)
        if ran_number == 1:
            other.get_hail_marry_strike(other)
            print(f" {self.name}´s Hail Marry worked! {other.name} got hit for {self.massive_hit} damage!")
        else:
            print(f"{self.name} missed {other.name}")




hero1 = Character("Bozeto", 100, 20, 100)
hero2 = Character("Andananda", 110,24, 105)
hero3 = Healer("DoctorX", 75, 15,110)

human1 = Human("Steve", 100, 15, 25, 2, 200)
druid1 = Druid("Shakana", 100, 20, 300)

# fighting x100 needs to work

Character.fight(human1, druid1)

# print(hero1)
# print(hero2)
# print(hero3)
# hero1.hit(hero2)
# print(hero2)
# hero3.heal(hero1)
# print(hero2)
# hero2.get_hit(hero1)
# print(hero1)


