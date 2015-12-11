import sys

print "\t\t\t ----------------"
print "\t\t\t THE SHIRE ADVENTURES"

print "\t\t\t"
print "\t\t\t ----------------"

print "You find yourself in the Shire with Frodo. Frodo has decided to leave\nto go on an Adventure Walk to meet Gandalf"
print "Frodo invites you to come on the walk you must decide if you want to go with\nFordo or stay and being boring in the Shire"
print "Enter: '1' To go with Frodo and have a grand Adventure"
print "Enter: '2' To stay in the Shire and have a second breakfast"

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

user = get_input()

#MOVE TO NEW FILE - IMPORT
# class Shire_1(object):
# 	def __init__(self, user):

def LeavingShire(user):	
	if user == 1:
		print "You Leave with Frodo and meet Grandalf the Grey on the road that borders the Shire"
		print "Gandalf tell you of impending danger to the Shire and that you and Frodo must go a journey to find The Ring"
		print "Enter: '1' If you want to join the adventure  "
		print "Enter: '2' If you want to stay behind. You have enough adventures for one day"
	else:
		print "Sorry! The Shire is in trouble you are going on an Adventure!"


#FILENAME.LeavingShire(user)
LeavingShire(user)

user = get_input()

def Gandalf_Adv(user):
	if user == 1:
		print "You are off on a grand adventure with Gandalf and Frodo! You come to the end of the road. You can either:" 
		print "Enter: 1 - to take the East Road"
		print "Enter: 2 - to take the North Road"
# 		print "                                                    ##           Lonely Mountain\n\
#                   Trollshaw Forest (5-6)            ###              (21-38)\n\
#                    /                 |               ##                 | \n\
#                   /   Midgewater     |                #                 |\n \
# Hobbiton*        /   / Marshes |     |          Misty Mountains      Lake-town*\n\
#  THE SHIRE      /   /  (12-19) |     |            path ##             /  |\n\
#  |     \       Bree*           |     |           (6-13)<---Beorn's   /   |\n\
#  | East Road-->(1-4)   Weathertop    |          /      #    House   /    |\n\
#  |                  \    (21-31) \   |  Rivendell*     ##       \  /     |\n\
#  |   Ferry           \      |     \  | /      \        ##      Mirkwood  |\n\
#  |         Buckland*  \     |      Ford        \      ##        (15-26)  |\n\
# Maggot's               \    |                   \   ###        /   |     |\n\
#  Farm        Old Forest \   |                  Caradhras      /    |     |\n\
#  (3-6)                   \  |                 / (21-50)      /     |     |\n\
#                        Barrow Downs          /      ##      /      |     |\n\
#                           (5-20)            /      ###     /       |     |\n\
#                                         West gates  ##    /        |     |\n\
#                                          of Moria <--- East gates  |     |\n\
#                                           (7-24)  ####  of Moria   |     |\n\
#                                             |      ###             |     |\n\
#                                             |      ##            Dol Guldur\n\
#                                             |     ##Lorien*     /  (41-65)\n\
#                                             |    ##            /  \n\
#                                             |   ##            /\n\
#                                             |  ###    Fangorn/\n\
#                                             |   ##   /\n\
#                                             Isengard/\n\
#                                              (7--35)             Parth Galen\n\
#                                                    \              \n\
#                                                ##   \                  Marshes\n\
#                                   #################  Edoras*        of the Dead\n\
#                         ##############            ## (1-22)             \n\
#                                              Paths #####\n\
#                                           of the Dead ######\n\
#                                                           ############## Minas\n\
#                                                                          Tirith*"

	elif user == 2:
		print "Sorry! The Shire is in trouble you are going on an Adventure! You come to the border of the Shire.\nYou are presented with 2 roads:"
		print "Enter: 1 - to take the East Road"
		print "Enter: 2 - to take the North Road"
# 		print "                                                    ##           Lonely Mountain\n\
#                   Trollshaw Forest (5-6)            ###              (21-38)\n\
#                    /                 |               ##                 | \n\
#                   /   Midgewater     |                #                 |\n \
# Hobbiton*        /   / Marshes |     |          Misty Mountains      Lake-town*\n\
#  |    \         /   /  (12-19) |     |            path ##             /  |\n\
#  |     \       Bree*           |     |           (6-13)<---Beorn's   /   |\n\
#  | East Road-->(1-4)   Weathertop    |          /      #    House   /    |\n\
#  |                  \    (21-31) \   |  Rivendell*     ##       \  /     |\n\
#  |   Ferry           \      |     \  | /      \        ##      Mirkwood  |\n\
#  |         Buckland*  \     |      Ford        \      ##        (15-26)  |\n\
# Maggot's               \    |                   \   ###        /   |     |\n\
#  Farm        Old Forest \   |                  Caradhras      /    |     |\n\
#  (3-6)                   \  |                 / (21-50)      /     |     |\n\
#                        Barrow Downs          /      ##      /      |     |\n\
#                           (5-20)            /      ###     /       |     |\n\
#                                         West gates  ##    /        |     |\n\
#                                          of Moria <--- East gates  |     |\n\
#                                           (7-24)  ####  of Moria   |     |\n\
#                                             |      ###             |     |\n\
#                                             |      ##            Dol Guldur\n\
#                                             |     ##Lorien*     /  (41-65)\n\
#                                             |    ##            /  \n\
#                                             |   ##            /\n\
#                                             |  ###    Fangorn/\n\
#                                             |   ##   /\n\
#                                             Isengard/\n\
#                                              (7--35)             Parth Galen\n\
#                                                    \              \n\
#                                                ##   \                  Marshes\n\
#                                   #################  Edoras*        of the Dead\n\
#                         ##############            ## (1-22)             \n\
#                                              Paths #####\n\
#                                           of the Dead ######\n\
#                                                           ############## Minas\n\
#                                                                          Tirith*"

Gandalf_Adv(user)

user = get_input()

def Roads_NE(user):	
	if user == 1: 
		print "You take the East Road and end up at the Brandywine river. Gandalf says you must cross the river\n to get to the Old Forest on the other side. You have 2 options:" 
		print "Enter: 1 - cross the river by boat" 
		print "Enter: 2 - cross the river by the old decaying bridge"
	elif user == 2 :
		print "You take the North Road and are attacked by Orcs! You immediately:"
		print "Enter: 1 - jump into the fray to fight them off and are injured"
		print "Enter: 2 -  hide and hope Frodo and Gandalf can handle the murderous Orcs"

Roads_NE(user)


user = get_input()


def River_Crossing(user):
 	if user == 1: 
 		print "You have made it across the rive in the Boat! You enter the Forest. It has grown late and\nyou setup camp for the night Suddenly you are attacked by Trolls! " 
 	if user == 2:
 		print "You take the old bridge, it collapses and you die! Your Adventure is OVER!"
 		lose()

River_Crossing(user)


user = get_input()

#def North_Orcs(user):
