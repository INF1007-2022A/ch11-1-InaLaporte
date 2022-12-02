"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	UNARMED_POWER = 20
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, nom:str, niveau_attack:int, niveau_min: int):
		self.__nom=nom
		self.niveau_attack=niveau_attack
		self.niveau_min=niveau_min

	@property
	def nom(self):
		return self.__nom

	@classmethod
	def make_unarmed(cls):
		return cls ("Unarmed", cls.UNARMED_POWER, 2 )  

class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, nom, max_hp, attack, defense, level, weapon:Weapon, hp):
		self.nom=nom
		self.max_hp=max_hp
		self.attack=attack
		self.defense=defense
		self.level=level
		self.weapon=weapon
		self.hp=hp 

def compute_damage(a: Character, d: Character):
	if random.random(0,100) <= 6.25:
		crit=2
	else:
		crit=1

	valeur_random=random.random(0.85,1)

	modifier=crit*valeur_random
	division_1=a.attack/d.defense
	division_2=(2*a.level/5) +2
	damage=(((division_2 * a.weapon.niveau_attack *division_1)/50)+2)*modifier 

	return damage 



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	
	dmg=compute_damage(attacker,defender)      #dans le read me, ça va dans le main

	return dmg #en string 

#deal_damage(c1, c2)


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass
