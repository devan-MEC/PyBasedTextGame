
#definition of fnc which prints story and lets user choose an option and evaluates the change in health(if health is involved with the action)
def corefunction(event,choice1,choice2,choice3,healthpoints=0):
	print("-----------------------------------------------------------------------------------------------------------")
	print(event)
	print("-----------------------------------------------------------------------------------------------------------")
	print("a) "+choice1)
	print("b) "+choice2)
	print("c) "+choice3)
	#print("d) "+choice4)
	chosenchoice=str(input("Enter your choice "))
	#if chosenchoice=='value':
	#	health+=healthpoints( or minus)
	return chosenchoice
#According to the returned chosen choice,another instance of corefunction is executed
health=100
#MAIN PROGRAM
q='''It's almost 8 in the evening when you check your watch. It seems that you had fallen asleep in your college 
     after staying back after college hours to complete your pending work.
     Everyone has obviously left the college. The college seems to be dark and silent..
     The darkness seems to be quite unsettling.. '''
c1='''Shout to see if  anyone's still present in the college '''
c2='''Silently pack your stuff and proceed to get out of the college '''
c3='''Check your phone to see if someone has messaged you'''

next_action=corefunction(q,c1,c2,c3)
if next_action=='a':
	q='''You shout as loud as you possibly can but the sound doesn't seem to evoke any kind of reaction
	     from your surroundings apart from the eerie reverberation you receive from the walls of the building..'''
	c1='''Fire up your phone and text your parents that you need a lift'''
	c2='''Pack you bag and proceed to get out of the college as swiftly as you can'''
	c3='''Walk around the college becuase you're curious to see how it looks during the late hours'''
	next_action=corefunction(q,c1,c2,c3)

