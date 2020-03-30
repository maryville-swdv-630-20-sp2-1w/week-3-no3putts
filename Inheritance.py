
class CharacterClass:
    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race

    def attack(self):
        raise NotImplementedError()

    def dance(self):
        raise NotImplementedError()


# SUBCLASSES
class Warrior(CharacterClass):
    def __init__(self, name, gender, race):
        CharacterClass.__init__(self,name, gender, race)
        self.main_hand = 'sword'
        self.off_hand = 'shield'
        self.range = 'gun'

    def attack(self):
        print(self.name + " raise + to strike monster")

    def dance(self):
        print(self.name + " doing the irish jig")

    def raise_shield(self):
        print(self.name + " raised shiedl, blocking enemy attack")

    def activate_whirlwind(self):
        print(self.name + " casting whirlwind, hits 10 enemy combatants")

    def activate_challenging_shout(self):
        print(self.name + " challenging shout activated, agro all enemies")


class Mage(CharacterClass):
    def __init__(self, name, gender, race):
        CharacterClass.__init__(self, name, gender, race)
        self.main_hand = 'Wand'
        self.off_hand = 'Orb'

    def attack(self):
        print(self.name + " casting with wand")

    def dance(self):
        print(self.name + " Started to Break Dance")

    def summon_portal(self,location):
        print(self.name + " activated portal to " + location)

    def cast_ice_barrier(self):
        print(self.name + " casting ice barrier, 100% damage absorbed")


class Hunter(CharacterClass):
    def __init__(self,  name, gender, race):
        CharacterClass.__init__(self, name, gender, race)
        self.main_hand = 'Bow'
        self.quiver = 0

    def attack(self):
        print(self.name + " start shooting with Bow and Arrow")

    def dance(self):
        print(self.name + " doing the Macarena")

    def summon_pet(self, pet):
        print(self.name + " summoning pet " + pet)

    def lay_trap(self, type):
        print(self.name + " yaying " + type + " trap")

    def play_dead(self):
        print(self.name + " cast play dead")

    def refil_quiver(self, count):
        self.quiver = count
        print("Loaded quiver with " + count + " arrows")


# Instantiating all classes
print('\nInstantiating a Warrior, Mage and Hunter classes')
w = Warrior('Dragon', 'male', 'human')
m = Mage('Ewalanikoa', 'female', 'goblin')
h = Hunter('kukanaloa', 'male', 'elf')

print('\n********* The Heroes***************')
print(w.name, 'race:', w.race, 'class:', w.__class__)
print(m.name, 'race:', m.race, 'class:', m.__class__)
print(h.name, 'race:', h.race, 'class:', h.__class__)

# TESTING EACH CLASS
print('\n********* WARRIOR CLASS TEST ***************')
w.attack()
w.activate_challenging_shout()
w.activate_whirlwind()

print('\n********* MAGE CLASS TEST ***************')
m.attack()
m.cast_ice_barrier()
m.summon_portal('Stormwind')

print('\n********* HUNTER CLASS TEST ***************')
h.summon_pet('Ape')
h.attack()
h.lay_trap('ice')
h.play_dead()

print('\n********* Adventure Ends For ***************')
print(w.name, ',', m.name, 'and', h.name)
