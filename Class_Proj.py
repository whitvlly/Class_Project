import sys

def win():
	sys.exit(0)

def lose():
	sys.exit(1)

def get_input():
	while True:
		input = raw_input()
		if input == '1' or input == '2':
			return int(input)
		print "You must enter '1' or '2'"

#MOVE TO NEW FILE - IMPORT
# class Shire_1(object):
# 	def __init__(self, user):

def promptBeginAdventure():	
	print "You Leave with Frodo and meet Grandalf the Grey on the road that borders the Shire"
	print "Gandalf tell you of impending danger to the Shire and that you and Frodo must go a journey to find The Ring"
	print "Enter: '1' If you want to join the adventure  "
	print "Enter: '2' If you want to stay behind. You have enough adventures for one day"
	return get_input()

def promptSelectRoad():
	print "                                                    ##           Lonely Mountain\n\
                  Trollshaw Forest (5-6)            ###              (21-38)\n\
                   /                 |               ##                 | \n\
                  /   Midgewater     |                #                 |\n \
Hobbiton*        /   / Marshes |     |          Misty Mountains      Lake-town*\n\
 THE SHIRE      /   /  (12-19) |     |            path ##             /  |\n\
 |     \       Bree*           |     |           (6-13)<---Beorn's   /   |\n\
 | East Road-->(1-4)   Weathertop    |          /      #    House   /    |\n\
 |                  \    (21-31) \   |  Rivendell*     ##       \  /     |\n\
 |   Ferry           \      |     \  | /      \        ##      Mirkwood  |\n\
 |         Buckland*  \     |      Ford        \      ##        (15-26)  |\n\
Maggot's               \    |                   \   ###        /   |     |\n\
 Farm        Old Forest \   |                  Caradhras      /    |     |\n\
 (3-6)                   \  |                 / (21-50)      /     |     |\n\
                       Barrow Downs          /      ##      /      |     |\n\
                          (5-20)            /      ###     /       |     |\n\
                                        West gates  ##    /        |     |\n\
                                         of Moria <--- East gates  |     |\n\
                                          (7-24)  ####  of Moria   |     |\n\
                                            |      ###             |     |\n\
                                            |      ##            Dol Guldur\n\
                                            |     ##Lorien*     /  (41-65)\n\
                                            |    ##            /  \n\
                                            |   ##            /\n\
                                            |  ###    Fangorn/\n\
                                            |   ##   /\n\
                                            Isengard/\n\
                                             (7--35)             Parth Galen\n\
                                                   \              \n\
                                               ##   \                  Marshes\n\
                                  #################  Edoras*        of the Dead\n\
                        ##############            ## (1-22)             \n\
                                             Paths #####\n\
                                          of the Dead ######\n\
                                                          ############## Minas\n\
                                                                         Tirith*"
	print "Sorry! The Shire is in trouble you are going on an Adventure!"
	print "You are off on a grand adventure with Gandalf and Frodo! You come to the end of the road. Check the map above to see if you should go North or East" 
	print "Enter: 1 - to take the East Road"
	print "Enter: 2 - to take the North Road"
	return get_input()

def promptEastRoadBB():	
		print "You take the East Road and end up at the Brandywine river. Gandalf says you must cross the river\n to get to the Old Forest on the other side. You have 2 options:" 
		print "Enter: 1 - cross the river by boat" 
		print "Enter: 2 - cross the river by the old decaying bridge"
		return get_input()
	
def promptNorthOrcs():
		print "You take the North Road and are attacked by Orcs! You immediately:"
		print "Enter: 1 - jump into the fray to fight them off and are injured"
		print "Enter: 2 -  hide and hope Frodo and Gandalf can handle the murderous Orcs"
		return get_input()

def promptRescueElevesHurt():
		print "You wake up in Rivendale, home of the Elves. Gandalf and Frodo are with you.\nThey have healed you and are providing you weapons for your journey"
		print "To protect you on your journey the Elves present you with two options:\nsword or bow & arrow. Select '1' for Sword or '2' for bow and arrow?"
		return get_input()

def promptHideElves():
		print "YYou hide and hear a great comotion, the Elves have come and are fighting off the orcs!\nThe Elves take you back to Rivendale and give you food and weapons on your journey"
		print "To protect you on your journey the Elves present you with two options:\nsword or bow & arrow. Select '1' for Sword or '2' for bow and arrow?"
		return get_input()

def promptRiver_CrossingTrolls():
 		print "You have made it across the rive in the Boat! You enter the Forest. It has grown late and\nyou setup camp for the night Suddenly you are attacked by Trolls! " 
 		print "Enter: 1 - To fight the Trolls"
		print "Enter: 2 -  hide and hope Frodo and Gandalf can handle the trio of Trolls"
 		return get_input()

def prompt_TrollsAttack():
		print " You have been capture by the Trolls and will be their next delicious meal! Your Adventure is OVER"
		lose()

def prompt_TrollsGandalf():
		print "Gandalf drives the Tolls back with a blinding light. You emerge from your hiding place to Frodo and Gandalf's franctic cries.\nYou continue on your journey into the Forest. Gandalf senses a dark magic from deep within the woods and wants to go to it!"
		print "Enter: 1 - to follow Gandalf deeper into the woods"
		print "Enter : 2 - are you crazy? you were almost killed by trolls! You are abandoing the quest!"
		return get_input()

def prompt_darkmagic():
	print "You follow Gandalf deeper into the forest and he brings you to a hidden Cave. In the cave is all sorts of riches and boxes.\nGandalf walks over to a small box and flips it open\n Its the Ring "
	print "Congratulations! You have completed your quest! Middle Earth & The Shire are safe!"
	win()

def prompt_abandonquest():
		print "You have abandon your quest. You have doomed all of Middle Earth and the Shire. YOU DIE"
		lose()

def promptriver_bridge():
 		print "You take the old bridge, it collapses and you die! Your Adventure is OVER!"
 		lose()

def promptLeaveShire():
	print "\t\t\t ----------------"
	print "\t\t\t THE SHIRE ADVENTURES"

	print "\t\t\t"
	print "\t\t\t ----------------"

	print "You find yourself in the Shire with Frodo. Frodo has decided to leave\nto go on an Adventure Walk to meet Gandalf"
	print "Frodo invites you to come on the walk you must decide if you want to go with\nFordo or stay and being boring in the Shire"
	print "Enter: '1' To go with Frodo and have a grand Adventure"
	print "Enter: '2' To stay in the Shire and have a second breakfast"
	return get_input()


input = promptLeaveShire()
if input == 1:
	input = promptBeginAdventure()
	if input == 1:
		print "Let's do it!"
		input = promptSelectRoad()
		if input == 1:
			input = promptEastRoadBB()
			if input == 1:
				input = promptRiver_CrossingTrolls()
				if input == 1:
					input = prompt_TrollsAttack()
				else:
					input = prompt_TrollsGandalf()
					if input == 1:
						input = prompt_darkmagic()
					else:
						input = prompt_abandonquest()
			else:
				input = promptriver_bridge()
		else:
			input = promptNorthOrcs()
			if input == 1:
				input == promptRescueElevesHurt()
			else:
				input = promptHideElves()
	else:
		input = promptSelectRoad()
else:
	print "The Shire is in trouble and you have failed them!"
	lose()

sys.exit(0)

user = get_input()

Gandalf_Adv(user)

user = get_input()

Roads_NE(user)

user = get_input()

River_Crossing(user)
North_Orcs(user)


user = get_input()

#def North_Orcs(user):
