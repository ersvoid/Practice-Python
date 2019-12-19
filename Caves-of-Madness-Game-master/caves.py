class Item(object):
	def __init__(self):
		self.cost = 0
		self.lvl = 0

	def __del__(self):
		pass

class Weapon(Item):
	def __init__(self):
		Item.__init__(self)
		self.mod = 0
		self.lvl = 0

	def attack_mod(self):
		return self.mod
		
class Monster_Attack(Weapon):
	def __init__(self,name="Bite"):
		Weapon.__init__(self)
		self.name = name
		self.lvl = 0
		self.mod = (1 + (self.lvl * 1))
		
class Sword(Weapon):
	def __init__(self,name="Sword"):
		Weapon.__init__(self)
		self.name = name
		self.lvl = 0
		self.mod = (4 + (self.lvl * 2))

class Staff(Weapon):
	def __init__(self,name="Staff"):
		Weapon.__init__(self)
		self.name = name
		self.lvl = 0
		self.mod = (1 + (self.lvl * 1))

class Bow(Weapon):
	def __init__(self,name="Bow"):
		Weapon.__init__(self)
		self.name = name
		self.lvl = 0
		self.mod = (2 + (self.lvl * 2))

class Armour(Item):
	def __init__(self):
		Item.__init__(self)
		
class Monster_armour(Armour):
	def __init__(self):
		Armour.__init__(self)
		self.lvl = 0
		
	def def_mod(self):
		return (1 + (self.lvl * 1))
		
class No_Shield(Armour):
	def __init__(self):
		Armour.__init__(self)
		self.lvl = 0
		
	def shield_mod(self):
		return 0

class Leather(Armour):
	def __init__(self,name):
		Armour.__init__(self)
		self.name = name
		self.lvl = 0

	def def_mod(self):
		return (10 + (self.lvl * 5))

class Steel(Armour):
	def __init__(self,name):
		Armour.__init__(self)
		self.name = name
		self.lvl = 0

	def def_mod(self):
		return (25 + (self.lvl * 5))

class Robe(Armour):
	def __init__(self,name):
		Armour.__init__(self)
		self.name = name
		self.lvl = 0

	def def_mod(self):
		return (50 + (self.lvl * 5))

class Shield(Armour):
	def __init__(self,name):
		Armour.__init__(self)
		self.name = name
		self.lvl = 0

	def shield_mod(self):
		return (10 + (self.lvl * 5))

class Magic_Item(Item):
	def __init__(self):
		Item.__init__(self)
		self.lvl = 0

class Ring(Magic_Item):
	def __init__(self,name):
		Magic_Item.__init__(self)
		self.name = name
		self.lvl = 0

	def ring_mod(self):
		return (1 + (self.lvl * 1))

class Amulet(Magic_Item):
	def _init__(self,name):
		Magic_Item.__init__(self)
		self.name = name
		self.lvl = 0

	def amulet_mod(self):
		return (10 + (self.lvl * 1))

class Creature(object):

	def __init__(self):
		self.Undead = False
		self.Construct = False
		self.sneak = False
		self.parry = False
		self.cleave = False
		self.exp = 0
		self.str = 0
		self.wis = 0
		self.dex = 0
		self.hp = 0
		self.mp = 0
		self.lvl = 0
		self.coins = 0
		self.weapon = []
		self.armour = []
		self.magic = []
		self.inv = []
		self.inv.extend(self.weapon)
		self.inv.extend(self.armour)
		self.inv.extend(self.magic)

	def speed(self):
		return self.dex

	def attack(self,Weapon):
		return ((self.str % 2) + Weapon.attack_mod())

	def defend(self,Armour,Shield):
		return ((self.dex % 2) + Armour.def_mod() + Shield.shield_mod())

	def magic(self):
		return (self.wis % 2)

	def __del__(self):
		pass

class Player(Creature):

	def __init__(self):
		Creature.__init__(self)
		print("Player created.")

class Human(Player):

	def __init__(self):
		Player.__init__(self)
		print("A human is born!")

class HFighter(Human):

	def __init__(self,name):
		Human.__init__(self)
		print("This human has trained to become a fighter!")
		self.name = name
		self.parry = True
		self.cleave = True
		self.hp = (10 + self.lvl * 30)
		self.mp = (10 + self.lvl * 10)
		self.str = (10 + self.lvl * 3)
		self.wis = (10 + self.lvl * 2)
		self.dex =(10 + self.lvl * 1)

class HSorceror(Human):

	def __init__(self,name):
		Human.__init__(self)
		print("This human has studied to become a sorceror!")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (10 + self.lvl * 30)
		self.str = (10 + self.lvl * 1)
		self.wis = (10 + self.lvl * 3)
		self.dex =(10 + self.lvl * 2)

class HRougue(Human):

	def __init__(self,name):
		Human.__init__(self)
		print("This human is a real shady character...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (10 + self.lvl * 20)
		self.str = (10 + self.lvl * 2)
		self.wis = (10 + self.lvl * 1)
		self.dex =(10 + self.lvl * 3)

class Dwarf(Player):

	def __init__(self):
		Player.__init__(self)
		print("A dwarf is born!")

class DFighter(Dwarf):

	def __init__(self,name):
		Dwarf.__init__(self)
		print("This dwarf has trained to become a fighter!")
		self.name = name
		self.hp = (20 + self.lvl * 40)
		self.mp = (10 + self.lvl * 10)
		self.str = (12 + self.lvl * 4)
		self.wis = (10 + self.lvl * 2)
		self.dex =(8 + self.lvl * 0)

class DSorceror(Dwarf):

	def __init__(self,name):
		Dwarf.__init__(self)
		print("This dwarf has studied to become a sorceror!")
		self.name = name
		self.hp = (20 + self.lvl * 30)
		self.mp = (10 + self.lvl * 30)
		self.str = (12 + self.lvl * 2)
		self.wis = (10 + self.lvl * 3)
		self.dex =(8 + self.lvl * 1)

class DRougue(Dwarf):

	def __init__(self,name):
		Dwarf.__init__(self)
		print("This dwarf is real shady character...")
		self.name = name
		self.hp = (20 + self.lvl * 30)
		self.mp = (10 + self.lvl * 20)
		self.str = (12 + self.lvl * 3)
		self.wis = (10 + self.lvl * 1)
		self.dex =(8 + self.lvl * 2)

class Elf(Player):

	def __init__(self):
		Player.__init__(self)
		print("An elf is born!")

class EFighter(Elf):

	def __init__(self,name):
		Elf.__init__(self)
		print("This elf has trained to become a fighter!")
		self.name = name
		self.parry = True
		self.cleave = True
		self.hp = (10 + self.lvl * 30)
		self.mp = (20 + self.lvl * 20)
		self.str = (8 + self.lvl * 2)
		self.wis = (12 + self.lvl * 3)
		self.dex =(10 + self.lvl * 1)

class ESorceror(Elf):

	def __init__(self,name):
		Elf.__init__(self)
		print("This elf has studied to become a sorceror!")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (20 + self.lvl * 40)
		self.str = (8 + self.lvl * 0)
		self.wis = (12 + self.lvl * 4)
		self.dex =(10 + self.lvl * 2)

class ERougue(Elf):

	def __init__(self,name):
		Elf.__init__(self)
		print("This elf is a real shady character...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (20 + self.lvl * 30)
		self.str = (8 + self.lvl * 1)
		self.wis = (12 + self.lvl * 2)
		self.dex =(10 + self.lvl * 3)

class Monster(Creature):

	def __init__(self):
		Creature.__init__(self)
		print("The smell of the cave-denizens reaches you first...")

class Animal(Monster):

	def __init__(self):
		Monster.__init__(self)
		print("You hear the scurrying of claws on the stone cave floor.")

class Rat(Animal):

	def __init__(self,name="Rat"):
		Animal.__init__(self)
		print("Oh, yeah, just kill some fucking rats. Is your life really anymore valuable?")
		self.name = name
		self.hp = (5 + self.lvl * 5)
		self.mp = (0 + self.lvl * 0)
		self.str = (5 + self.lvl * 1)
		self.wis = (5 + self.lvl * 0)
		self.dex =(12 + self.lvl * 2)
		self.coins = 1 + (self.lvl * 1)
		self.exp = 1 + self.lvl

class Wolf(Animal):

	def __init__(self,name="Wolf"):
		Animal.__init__(self)
		print("This wolf looks like that dog that bit you when you were a kid...")
		self.name = name
		self.hp = (30 + self.lvl * 5)
		self.mp = (0 + self.lvl * 0)
		self.str = (12 + self.lvl * 2)
		self.wis = (8 + self.lvl * 0)
		self.dex =(16 + self.lvl * 3)
		self.coins = 2 + (self.lvl * 2)
		self.exp = 1 + self.lvl * 2

class Cave_Cat(Animal):

	def __init__(self,name="Cave Cat"):
		Animal.__init__(self)
		print("This cave cat has their claws ready, arms weak, knees are heavy...")
		self.name = name
		self.hp = (50 + self.lvl * 10)
		self.mp = (0 + self.lvl * 0)
		self.str = (20 + self.lvl * 5)
		self.wis = (10 + self.lvl * 0)
		self.dex =(16 + self.lvl * 3)
		self.coins = 5 + (self.lvl * 5)
		self.exp = 5 + self.lvl * 5

class Cave_Bear(Animal):

	def __init__(self,name="Cave Bear"):
		Animal.__init__(self)
		print("This cave bear wasn't bothering anyone until you showed up...")
		self.name = name
		self.hp = (100 + self.lvl * 25)
		self.mp = (0 + self.lvl * 0)
		self.str = (30 + self.lvl * 10)
		self.wis = (12 + self.lvl * 0)
		self.dex =(16 + self.lvl * 3)
		self.coins = 10 + (self.lvl * 10)
		self.exp = 10 + self.lvl * 10

class Construct(Monster):

	def __init__(self):
		Monster.__init__(self)
		self.Construct = True
		print("Slow, continuous thuds shake the very walls of the cave...")

class Golem(Construct):

	def __init__(self,name="Golem"):
		Construct.__init__(self)
		print("This golem was set loose upon the world by a real jackass...")
		self.name = name
		self.hp = (500 + self.lvl * 100)
		self.mp = (0 + self.lvl * 0)
		self.str = (100 + self.lvl * 50)
		self.wis = (0 + self.lvl * 0)
		self.dex =(2 + self.lvl * 2)
		self.coins = 100 + (self.lvl * 100)
		self.exp = 100 + self.lvl * 50

class Undead(Monster):

	def __init__(self):
		Monster.__init__(self)
		self.Undead = True
		print("The smell is getting way worse...")

class Zombie(Undead):

	def __init__(self,name="Zombie"):
		Undead.__init__(self)
		print("This zombie is fucking annoying...")
		self.name = name
		self.hp = (10 + self.lvl * 5)
		self.mp = (0 + self.lvl * 0)
		self.str = (8 + self.lvl * 1)
		self.wis = (0 + self.lvl * 0)
		self.dex =(6 + self.lvl * 1)
		self.coins = 10 + (self.lvl * 5)
		self.lvl = 10 + self.lvl * 10

class Skeleton(Undead):

	def __init__(self,name="Skeleton"):
		Undead.__init__(self)
		print("This skeleton looks all jankity-janked...")
		self.name = name
		self.hp = (25 + self.lvl * 5)
		self.mp = (0 + self.lvl * 0)
		self.str = (10 + self.lvl * 2)
		self.wis = (0 + self.lvl * 0)
		self.dex =(10 + self.lvl * 1)
		self.coins = 20 + self.lvl * 10
		self.exp = 20 + self.lvl * 10

class Ghoul(Undead):

	def __init__(self,name="Ghoul"):
		Undead.__init__(self)
		print("This ghoul is a fast bitch...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (0 + self.lvl * 0)
		self.str = (8 + self.lvl * 1)
		self.wis = (0 + self.lvl * 0)
		self.dex =(10 + self.lvl * 3)
		self.coins = 50 + self.lvl * 25
		self.exp = 50 + self.lvl * 15

class Tribe(Monster):

	def __init__(self):
		Monster.__init__(self)
		print("You can hear the drums in the deep...")

class Goblin(Tribe):

	def __init__(self,name="Goblin"):
		Tribe.__init__(self)
		print("This goblin is a dick to everyone...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (20 + self.lvl * 30)
		self.str = (8 + self.lvl * 1)
		self.wis = (12 + self.lvl * 2)
		self.dex =(10 + self.lvl * 3)
		self.coins = 50 + self.lvl * 10
		self.exp = 10 + self.lvl * 10

class Hobgoblin(Tribe):

	def __init__(self,name="Hobgoblin"):
		Tribe.__init__(self)
		print("This hobgoblin is hobblin' along and then he saw you...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (20 + self.lvl * 30)
		self.str = (8 + self.lvl * 1)
		self.wis = (12 + self.lvl * 2)
		self.dex =(10 + self.lvl * 3)
		self.coins = 75 + self.lvl * 25
		self.exp = 20 + self.lvl * 15

class Orc(Tribe):

	def __init__(self,name="Orc"):
		Tribe.__init__(self)
		print("This orc looks like a real asshole...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (20 + self.lvl * 30)
		self.str = (8 + self.lvl * 1)
		self.wis = (12 + self.lvl * 2)
		self.dex =(10 + self.lvl * 3)
		self.coins = 100 + self.lvl * 50
		self.exp = 30 + self.lvl * 20

class Ogre(Tribe):

	def __init__(self,name="Ogre"):
		Tribe.__init__(self)
		print("This ogre is a real smelly guy...")
		self.name = name
		self.hp = (10 + self.lvl * 20)
		self.mp = (20 + self.lvl * 30)
		self.str = (8 + self.lvl * 1)
		self.wis = (12 + self.lvl * 2)
		self.dex =(10 + self.lvl * 3)
		self.coins = 250 + self.lvl * 50
		self.exp = 50 + self.lvl * 30
		

def speed(creature1,creature2):
	#DETERMINES WHO GOES FIRST IN BATTLE
	if creature1.speed() > creature2.speed():
		return True
	else:
		return False

def attack(creature):
	#DETERMINES AMOUNT OF ATTACK POWER
	return creature.attack() + creature.lvl

def defense(creature):
	#DETERMINES ARMOUR CLASS RATING
	return creature.defend() + creature.lvl
	
	
import random

def hit_or_dodge(creature1,weapon,creature2):
	#DETERMINES IF THE ATTACK IS SUCCESSFUL
	global hit,dodge
	player_roll = random.randint(1,20) + creature1.attack(weapon)
	monster_roll = random.randint(1,20) + (creature2.speed() % 2)
	if player_roll > monster_roll:
		hit = True
	else:
		hit = False
		dodge = True

def sword_damage(creature,Sword):
	#DETERMINES AMOUNT OF DAMAGE
	if creature.cleave == False:
		return ((random.randint(1,8) + (4 + (Sword.lvl * 2))))
	else:
		creature.cleave = True
		return ((random.randint(1,8) + (4 + (Sword.lvl * 2) + (creature.lvl * 5))))

def	staff_damage(Staff):
	#DETERMINES AMOUNT OF DAMAGE
	return ((random.randint(1,6) + (1 + (Staff.lvl * 1))))
	
def	monster_damage(Monster_Attack):
	#DETERMINES AMOUNT OF DAMAGE
	return ((random.randint(1,4) + (1 + (Monster_Attack.lvl * 1))))

def bow_damage(Bow):
	#DETERMINES AMOUNT OF DAMAGE
	return ((random.randint1,8) + (2 + (Bow.lvl * 2)))

def parry_damage(Creature):
	#SKILL THAT ALLOWS AN EXTRA ATTACK IF ATTACK DODGED
	return ((random.randint(1,6) + (Creature.lvl * 1)))

def magic_missile(Creature):
	#SORCEROR SPELL THAT ATTACKS AND NEVER MISSES
	if self.lvl < 5:
		return (random.randint(1,8) + Creature.magic)
	elif self.lvl < 10:
		return ((random.randint(1,8) * 2) + Creature.magic)
	elif self.lvl < 15:
		return ((random.randint(1,8) * 3) + Creature.magic)
	elif self.lvl < 20:
		return ((random.randint(1,8) * 4) + Creature.magic)
	else:
		return ((random.randint(1,8) * 5) + Creature.magic)

def heal(Creature1,Creature2):
	#SORCEROR SPELL THAT RESTORES HP
	heal_amt = Creature1.lvl * 10 + Creature1.magic
	if Creature2.Undead == True:
		Creature.hp -= heal_amt
	elif Creature2.Construct == True:
		print("THE SPELL FAILS TO AFFECT THE CONSTRUCT")
	else:
		Creature2.hp += heal_amt

def sneak_attack(Bow,Creature):
	#THIEF SKILL THAT ALLOWS EXTRA ATTACK AND DAMAGE IF FIRST ATTACK IN BATTLE
	return (random.randint(1,8) + 2 + (Bow.lvl * 2) + (Creature.speed % 2) + (Creature.lvl * 5))

def buy(user_buy):
	#FUNCTION THAT BUYS AN ITEM FROM THE STORE
	item_name = input("CHOOSE A NAME FOR THIS ITEM")
	
def sell(user_sell):
	#FUNCTION THAT SELLS AN ITEM FROM PLAYER INVENTORY
	Creature.inv.remove(user_sell)

def upgrade_item(Item):
	#FUNCTION THAT UPGRADES A WEAPON, ARMOUR, RING, OR AMULET
	Item.lvl += 1
	
	
	
	
d_race = {1:"Human",2:"Dwarf",3:"Elf"}
d_class = {1:"Fighter",2:"Sorceror",3:"Rogue"}


def generate_player():
	"""This function generates the player character."""
	global player_name
	global player_character
	print(d_race)
	p_race = int(input("Please choose a race by number: "))
	if p_race == 1:
		print(d_class)
		p_class = int(input("Please choose a class by number: "))
		if p_class == 1:
			player_name = input("What is your name hero? ")
			player_character = HFighter(player_name)
		elif p_class == 2:
			player_name = input("What is your name hero? ")
			player_character = HSorceror(player_name)
		else:
			player_name = input("What is your name hero? ")
			player_character = HRougue(player_name)
	elif p_race == 2:
		print(d_class)
		p_class = int(input("Please choose a class by number: "))
		if p_class == 1:
			player_name = input("What is your name hero? ")
			player_character = DFighter(player_name)
		elif p_class == 2:
			player_name = input("What is your name hero? ")
			player_character = DSorceror(player_name)
		else:
			player_name = input("What is your name hero? ")
			player_character = DRougue(player_name)
	else:
		print(d_class)
		p_class = int(input("Please choose a class by number: "))
		if p_class == 1:
			player_name = input("What is your name hero? ")
			player_character = EFighter(player_name)
		elif p_class == 2:
			player_name = input("What is your name hero? ")
			player_character = ESorceror(player_name)
		else:
			player_name = input("What is your name hero? ")
			player_character = ERougue(player_name)

def generate_battle():
	"""
	This function generates a random monster to battle.
	"""
	gen_roll_1 = random.randint(1,101)
	if gen_roll_1 < 65:
		gen_roll_2 = random.randint(1,101)
		if gen_roll_2 < 50:
			return Rat()
		elif gen_roll_2 < 85:
			return Wolf()
		elif  gen_roll_2 < 95:
			return Cave_Cat()
		else:
			return Cave_Bear()
	elif gen_roll_1 < 80:
		gen_roll_2 = random.randint(1,101)
		if gen_roll_2 < 50:				
			return Zombie()
		elif  gen_roll_2 < 90:
			return Skeleton()
		else:
			return Ghoul()
	elif gen_roll_1 < 99:
		gen_roll_2 = random.randint(1,101)
		if gen_roll_2 < 50:
			return Goblin()
		elif gen_roll_2 < 75:
			return Hobgoblin()
		elif  gen_roll_2 < 99:
			return Orc()
		else:
			return Ogre()
	else:
		return Golem()

def leveler():
	global battle_monster
	battle_monster = generate_battle()
	level_up(battle_monster)

play_exp = 0

def death_check(creature1,creature2):
	global battle_on, play_exp
	if creature1.hp <= 0:
		print("You have been killed.")
		battle_on = False
	elif creature2.hp <= 0:
		print("You have defeated the {}!".format(creature2.name))
		play_exp += creature2.exp
		print("Total Experience: " + str(play_exp))
		level_up(creature1)
		battle_on = False
	else:
		pass
		
def level_up(Creature):
	#FUNCTION THAT LEVELS UP PLAYERS AND MONSTERS
	if play_exp < 5:
		Creature.lvl = 0
	elif play_exp < 10:
		Creature.lvl = 1
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 20:
		Creature.lvl = 2
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 40:
		Creature.lvl = 3
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 80:
		Creature.lvl = 4
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 150:
		Creature.lvl = 5
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 250:
		Creature.lvl = 6
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 400:
		Creature.lvl = 7
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 600:
		Creature.lvl = 8
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 800:
		Creature.lvl = 9
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 1000:
		Creature.lvl = 11
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 1200:
		Creature.lvl = 12
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 1400:
		Creature.lvl = 13
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 1600:
		Creature.lvl = 14
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 2000:
		Creature.lvl = 15
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 2500:
		Creature.lvl = 16
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 3000:
		Creature.lvl = 17
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 4000:
		Creature.lvl = 18
		print("Now you are Level {}!".format(Creature.lvl))
	elif play_exp < 5000:
		Creature.lvl = 19
		print("Now you are Level {}!".format(Creature.lvl))
	else:
		Creature.lvl = 20
		print("Now you are Level {}!".format(Creature.lvl))
	
player_sword = Sword("Bane")
player_shield = Shield("Virtue")
player_armour = Steel("Courage")
player_ring = Ring("Ring")
player_amulet = Amulet()
goblin_armour = Leather("Goblin Armour")
monster_attack = Monster_Attack()
monster_armour = Monster_armour()
null_shield = No_Shield()


game_on = True
replay = True

print("Welcome to the Caves of Madness!")
print(
"""Ever since you were young, you wished to follow all the town's heroes who venture 
into the caves of madness to forestall the onslaught of the Plane of Darkness never 
to return...""")
print(
"""It has been some time since a young hero has entered the Caves of Madness... The 
pounding of drums in the deep and piercing shrieks awaken the villagers at all hours 
of the night and cause the children to cry throughout the day... Someone must enter 
the caves and fight back the hordes that challenge the existence of humanity.""")

generate_player()

print("""It is good that you have come, {}, for the denizens of the Underworld threaten 
the lives of the good folk of the village. You must protect them now.""".format(player_name))

while game_on == True:
	battle_setup = True
	while battle_setup == True:
		creature1 = player_character
		leveler()
		creature2 = battle_monster
		print("Starting LVL:")
		print(creature2.lvl)
		print(creature2.hp)
		battle_on = True
		if speed(creature1,creature2) == True:
			print("You are faster than the {}!".format(creature2.name))
			
			while battle_on == True:
			
				death_check(creature1,creature2)
				
				print("You swing your weapon towards your foe...")
				
				hit_or_dodge(creature1,player_sword,creature2)
				
				if hit == True:
				
					print("You make contact with your foe!")
				
					s_dam = sword_damage(creature1,player_sword)
					
					hit = False
					
					if creature1.attack(player_sword) > creature2.defend(monster_armour,null_shield):
					
						print("The monster has {} HP".format(creature2.hp))
					
						creature2.hp -= s_dam
						
						print("Your enemy takes {} damage.".format(s_dam))
						
						print("Now, the monster has {} HP".format(creature2.hp))
						
					else:
						
						print("Your blow glances off the hide of the monster.")
					
				elif dodge == True and creature2.parry == True:
				
					print("The monster swiftly dodges your clumsy swing and parries your attack!")
				
					p_dam = parry_damage(creature2)
					
					creature1.hp -= p_dam
					
					print("You take {} damage.".format(p_dam))
					
					print("You have {} HP remaining.".format(creature1.hp))
					
					dodge = False
					
				else:
					
					print("You have missed this attack.")
				
					pass
				
				death_check(creature1,creature2)
				
				print("The monster is coming right for you!")
					
				hit_or_dodge(creature2,monster_attack,creature1)
				
				if hit == True:
				
					print("Your foe makes contact!")
				
					m_dam = monster_damage(monster_attack)
					
					hit = False
					
					if creature2.attack(monster_attack) > creature1.defend(player_armour,player_shield):
					
						creature1.hp -= m_dam
						
						print("You take {} damage.".format(p_dam))
					
						print("You have {} HP remaining.".format(creature1.hp))
						
					else:
					
						print("Your armour protects you.")
					
				elif dodge == True and creature1.parry == True:
				
					print("You dodge and parry!")
					
					print("The monster has " + str(creature2.hp) + " hp remaining.")
				
					p_dam = parry_damage(creature1)
					
					creature2.hp -= p_dam
					
					print("The monster takes {} damage.".format(p_dam))
					
					print("The monster has " + str(creature2.hp) + " hp remaining.")
					
					dodge = False
					
				else:
				
					print("You have dodged the attack!")

				death_check(creature1,creature2)
					
		else:
		
			#first_attack = MONSTER
			
			print("Your attacker is faster!")
			
			while battle_on == True:
			
				death_check(creature1,creature2)
				
				print("The monster is coming right for you!")
				
				hit_or_dodge(creature2,monster_attack,creature1)
				
				if hit == True:
				
					print("Your foe makes contact!")
				
					m_dam = monster_damage(monster_attack)
					
					hit = False
					
					if creature2.attack(monster_attack) > creature1.defend(player_armour,player_shield):
					
						creature1.hp -= m_dam
						
						print("You take {} damage.".format(m_dam))
					
						print("You have {} HP remaining.".format(creature1.hp))
						
					else:
					
						print("Your armour protects you.")
					
				elif dodge == True and creature1.parry == True:
				
					print("You dodge and parry!")
				
					p_dam = parry_damage(creature1)
					
					creature2.hp -= p_dam
					
					print("The monster takes {} damage.".format(p_dam))
					
					print("The monster has {} HP remaining.".format(creature2.hp))
					
					dodge = False
					
				else:
				
					print("You have dodged the attack!")
				
					pass

				death_check(creature1,creature2)
				
				print("You swing mightily towards your foe...")
					
				hit_or_dodge(creature1,player_sword,creature2)
				
				if hit == True:
				
					print("You make contact with your foe!")
				
					s_dam = sword_damage(creature1,player_sword)
					
					hit = False
					
					if creature1.attack(player_sword) > creature2.defend(monster_armour,null_shield):
					
						creature2.hp -= s_dam
						
						print("The monster takes {} damage.".format(s_dam))
					
						print("The monster has {} HP remaining.".format(creature2.hp))
						
					else:
						
						print("Your weapon glances off the monster's hide.")
					
				elif dodge == True and creature2.parry == True:
				
					print("The monster feints and parries your attack!")
				
					p_dam = parry_damage(creature2)
					
					creature1.hp -= p_dam
					
					print("You take {} damage.".format(p_dam))
					
					dodge = False
					
				else:
					print("You have missed!")
				death_check(creature1,creature2)
		if battle_on == False:
			battle_setup = False
	if battle_setup == False:
		player_input = str(input("Would you ike to continue?(Y/N) "))
		player_input.lower()
		if player_input[0] == "y":
			pass
		else:
			game_on = False
print("GAME OVER")