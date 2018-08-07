from functools import partial
import maya.cmds as cmds
from random import *

#def checkBoxes(pTail, pTop, pSide, pRotation):
#	print cmds.checkBox(pTail, query=True, value=True)
#	print cmds.checkBox(pTop, query=True, value=True)
#	print cmds.checkBox(pSide, query=True, value=True)
#	print cmds.checkBox(pRotation, query=True, value=True)

def removeSideFinKeys():

		remFinKeys('L_Fin_Large_01_CTRL')
		remFinKeys('L_Fin_Large_02_CTRL')
		remFinKeys('R_Fin_Large_02_CTRL')
		remFinKeys('R_Fin_Large_02_CTRL')

		remFinKeys('L_Fin_Medium_01_CTRL')
		remFinKeys('L_Fin_Medium_02_CTRL')
		remFinKeys('R_Fin_Medium_01_CTRL')
		remFinKeys('R_Fin_Medium_02_CTRL')

		remFinKeys('L_Fin_Small_01_CTRL')
		remFinKeys('L_Fin_Small_02_CTRL')
		remFinKeys('R_Fin_Small_01_CTRL')
		remFinKeys('R_Fin_Small_02_CTRL')



def removeTopFinKeys():
		remFinKeys('Top_Fin_Large_01_CTRL')
		remFinKeys('Top_Fin_Large_02_CTRL')

		remFinKeys('Top_Fin_Medium_01_CTRL')
		remFinKeys('Top_Fin_Medium_02_CTRL')

		remFinKeys('Top_Fin_Small_01_CTRL')
		remFinKeys('Top_Fin_Small_02_CTRL')

def removeTailKeys():
		remFinKeys('Tail_01_CTRL')
		remFinKeys('Tail_02_CTRL')
		remFinKeys('Tail_03_CTRL')
		remFinKeys('Tail_04_CTRL')
		remFinKeys('Tail_05_CTRL')


def removeRootKeys():
	remFinKeys( 'Root_CTRL')

def remFinKeys(name):
	cmds.cutKey(name, option="keys")
	cmds.xform(name, ro=(0, 0, 0))


def removeAllKeys():
	result = cmds.confirmDialog( 	title='Confirm', message='Are you sure you want to delete ALL the keyframes?',
									icon="question", button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )

	if result == 'Yes':
		removeRootKeys()
		removeTailKeys()
		removeSideFinKeys()
		removeTopFinKeys()

def keyObjectMovement( pObjectName, pStartTime, pTargetAttribute, pValue ):   
		cmds.setKeyframe( pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pValue )	

def generateAnimation(pArrCheck, pArrVal):

	##############################################
	#####################INFO#####################
	##############################################
	#cycles will be a minimum of 3 cycles (360 frames)
	#2 main cycles ups (120 each), half-cycle warm up (60), half-cycle cool down (60)
	
	#30 base frames per cycle
	#30, 5, 5 are standard.
	
	
	##############################################
	####################INPUTS####################
	##############################################
	
	#framerate is 60 fps
	#60 / 2 = 30

	speed = pArrVal[0]
	intensity = pArrVal[1]
	cycleCount = pArrVal[2]
	rotateIntensity = pArrVal[3]
		
	bAnimateTail = pArrCheck[0]	
	bAnimateTopFin =  pArrCheck[1]
	bAnimateSideFinL =  pArrCheck[2]
	bAnimateRotation =  pArrCheck[3]
	##############################################
	#####################CODE#####################
	##############################################
	
	def setupSideFinAnimation(pSpeed, pIntensity):
		removeSideFinKeys()
	
	
		###setup middle fin angle
		##setup small fin angle
	
		for x in range (0, cycleCount):
			keyTime= x*pSpeed
			rootOfset = speed / 3
			
			middleRotateZ = 0;
	
	
			if x == 0:
				keyObjectMovement('L_Fin_Large_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('L_Fin_Large_02_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('R_Fin_Large_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('R_Fin_Large_02_CTRL', keyTime, 'rotateY', 0)
	
				keyObjectMovement('L_Fin_Medium_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('L_Fin_Medium_02_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('R_Fin_Medium_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('R_Fin_Medium_02_CTRL', keyTime, 'rotateY', 0)
		
				if pSpeed < 10:
					keyObjectMovement('L_Fin_Medium_01_CTRL', keyTime, 'rotateZ', 20)
					keyObjectMovement('R_Fin_Medium_01_CTRL', keyTime, 'rotateZ', 20)
					keyObjectMovement('L_Fin_Small_01_CTRL', keyTime, 'rotateZ', 10)
					keyObjectMovement('R_Fin_Small_01_CTRL', keyTime, 'rotateZ', 10)
				elif (pSpeed >=10) and (pSpeed <30):
					keyObjectMovement('R_Fin_Medium_01_CTRL', keyTime, 'rotateZ', 30 - pSpeed)
					keyObjectMovement('L_Fin_Medium_01_CTRL', keyTime, 'rotateZ', 30 - pSpeed)
					keyObjectMovement('R_Fin_Small_01_CTRL', keyTime, 'rotateZ', 15 - pSpeed / 2)
					keyObjectMovement('L_Fin_Small_01_CTRL', keyTime, 'rotateZ', 15 - pSpeed / 2)
	
	
			else:
				if x % 2 != 0:
					#keyframe @ 30, 90, 150, etc
	
					if (pSpeed >=10) and (pSpeed <30):
						if (x + 1) % 4 == 0:
							keyVal_Side_L_Fin_01 = (pSpeed * -1) + 45
							keyVal_Side_L_Fin_02 = (pSpeed * -1) + 40
						else:
							keyVal_Side_L_Fin_01 = (pSpeed * -1) + 40
							keyVal_Side_L_Fin_02 = (pSpeed * -1) + 35
	
					elif (pSpeed < 10):
						if (x + 1) % 4 == 0:
							keyVal_Side_L_Fin_01 = (pSpeed * -1) + 40
							keyVal_Side_L_Fin_02 = 0
						else:
							keyVal_Side_L_Fin_01 = (pSpeed * -1) + 45
							keyVal_Side_L_Fin_02 = 0					
	
					else:
						if (x + 1) % 4 == 0:
							keyVal_Side_L_Fin_01 = (pIntensity * 4)
							keyVal_Side_L_Fin_02 = (pIntensity * 3)
		
						else:
							keyVal_Side_L_Fin_01 = (pIntensity * 2)
							keyVal_Side_L_Fin_02 = 0
					#print "Left: "
					#print keyVal_Side_L_Fin_01
					#print keyVal_Side_L_Fin_02	
					keyObjectMovement('L_Fin_Large_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_L_Fin_01 + randint(0, pIntensity ))
					#print keyVal_Side_L_Fin_01 + randint(0, pIntensity )
					keyObjectMovement('L_Fin_Large_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_L_Fin_02 + randint(0, pIntensity ))
					#print keyVal_Side_R_Fin_01 + randint(0, pIntensity )
					keyObjectMovement('L_Fin_Medium_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_L_Fin_01 * 0.5 + randint(0, pIntensity ))
					keyObjectMovement('L_Fin_Medium_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_L_Fin_02 * 0.5 + randint(0, pIntensity ))
					keyObjectMovement('L_Fin_Small_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_L_Fin_01 * 0.25 + randint(0, pIntensity ))
					keyObjectMovement('L_Fin_Small_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_L_Fin_02 * 0.25 + randint(0, pIntensity ))
					#print ""	
	
				else:
					if (pSpeed >=10) and (pSpeed <=30):
						if (x + 2) % 4 == 0:
							keyVal_Side_R_Fin_01 = (pSpeed * -1) + 40
							keyVal_Side_R_Fin_02 = (pSpeed * -1) + 35
						else:
							keyVal_Side_R_Fin_01 = (pSpeed * -1) + 45
							keyVal_Side_R_Fin_02 = (pSpeed * -1) + 40
	
					elif (pSpeed < 10):
						if (x + 2) % 4 == 0:
							keyVal_Side_R_Fin_01 = (pSpeed * -1) + 40
							keyVal_Side_R_Fin_02 = 0
						else:
							keyVal_Side_R_Fin_01 = (pSpeed * -1) + 45
							keyVal_Side_R_Fin_02 = 0					
	
					else:
						if (x + 2) % 4 == 0:
							keyVal_Side_R_Fin_01 = (pIntensity * 4)
							keyVal_Side_R_Fin_02 = (pIntensity * 3)		
						else:
							keyVal_Side_R_Fin_01 = (pIntensity * 2)
							keyVal_Side_R_Fin_02 = 0
	
	
					keyVal_Side_R_Fin_01 = -keyVal_Side_R_Fin_01
					keyVal_Side_R_Fin_02 = -keyVal_Side_R_Fin_02


					#print "Right: "
					#print keyVal_Side_R_Fin_01
					#print keyVal_Side_R_Fin_02	
					keyObjectMovement('R_Fin_Large_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_R_Fin_01 - randint(0, pIntensity ))
					#print keyVal_Side_R_Fin_01 - randint(0, pIntensity )
					keyObjectMovement('R_Fin_Large_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_R_Fin_02 - randint(0, pIntensity ))
					#print keyVal_Side_R_Fin_01 - randint(0, pIntensity )
					keyObjectMovement('R_Fin_Medium_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_R_Fin_01 * 0.5 - randint(0, pIntensity ))
					keyObjectMovement('R_Fin_Medium_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_R_Fin_02 * 0.5 - randint(0, pIntensity ))
					keyObjectMovement('R_Fin_Small_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_R_Fin_01 * 0.25 - randint(0, pIntensity ))
					keyObjectMovement('R_Fin_Small_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_Side_R_Fin_02 * 0.25 - randint(0, pIntensity ))
					#print ""	
	
	def setupTopFinAnimation(pSpeed, pIntensity):
		removeTopFinKeys()
	
		for x in range (0, cycleCount):
			keyTime= x*pSpeed
			topFinOffset = speed / 3
			topFinOffset2 = speed / 1.5
	
			if x == 0:
				keyObjectMovement('Top_Fin_Large_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Top_Fin_Large_02_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Top_Fin_Medium_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Top_Fin_Medium_02_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Top_Fin_Small_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Top_Fin_Small_02_CTRL', keyTime, 'rotateY', 0)
			else:
				if x % 2 != 0:
					#keyframe @ 30, 90, 150, etc
					if (x + 1) % 4 != 0:
						keyVal_L_Fin_01 = (pIntensity)
						keyVal_L_Fin_02 = (pIntensity * 2) * -1
						keyVal_M_Fin_01 = (pIntensity) * -1
						keyVal_M_Fin_02 = (pIntensity * 2) * -1
						keyVal_S_Fin_01 = (pIntensity) * -1
						keyVal_S_Fin_02 = (pIntensity * 2) * -1
					else:
						keyVal_L_Fin_01 = (pIntensity ) * -1
						keyVal_L_Fin_02 = (pIntensity * 2)
						keyVal_M_Fin_01 = (pIntensity )
						keyVal_M_Fin_02 = (pIntensity * 2)
						keyVal_S_Fin_01 = (pIntensity )
						keyVal_S_Fin_02 = (pIntensity * 2)
	
					keyObjectMovement('Top_Fin_Large_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_L_Fin_01 + randint(0, pIntensity ))
					keyObjectMovement('Top_Fin_Large_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_L_Fin_02 + randint(0, pIntensity ))
					keyObjectMovement('Top_Fin_Medium_01_CTRL', keyTime + randint(0, pSpeed / 5) + topFinOffset, 'rotateY', keyVal_M_Fin_01 + randint(0, pIntensity ))
					keyObjectMovement('Top_Fin_Medium_02_CTRL', keyTime + randint(0, pSpeed / 5) + topFinOffset, 'rotateY', keyVal_M_Fin_02 + randint(0, pIntensity ))
					keyObjectMovement('Top_Fin_Small_01_CTRL', keyTime + randint(0, pSpeed / 5) + topFinOffset2, 'rotateY', keyVal_S_Fin_01 + randint(0, pIntensity ))
					keyObjectMovement('Top_Fin_Small_02_CTRL', keyTime + randint(0, pSpeed / 5)+ topFinOffset2, 'rotateY', keyVal_S_Fin_02 + randint(0, pIntensity ))
	
	def setupRootAnimation(pSpeed, pRotateIntensity):
		removeRootKeys()
		for x in range (0, cycleCount):
			rootOfset = speed / 3
			keyTime= x*pSpeed
			if x == 0:
				keyObjectMovement('Root_CTRL', keyTime, 'rotateY', 0)
			else:
				if x % 2 == 0:
					print ""
				else:
					if (x + 1) % 4 == 0:
						keyVal_Root   = (pRotateIntensity * 2) * -1
					else:
						keyVal_Root   = (pRotateIntensity * 2)

					keyObjectMovement('Root_CTRL', keyTime + randint(0, pSpeed / 5) + rootOfset, 'rotateY', keyVal_Root)

	def setupTailAnmiation(pSpeed, pIntensity, pRoot, pRotateIntensity):
		removeTailKeys()
	
		#if pRoot:
		#	removeRootKeys()

		for x in range (0, cycleCount):
			keyTime= x*pSpeed
			#rootOfset = speed / 3
		
			if x == 0:
				keyObjectMovement('Tail_01_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Tail_02_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Tail_03_CTRL', keyTime, 'rotateY', 0)
				keyObjectMovement('Tail_04_CTRL', keyTime, 'rotateY', 0)	
				keyObjectMovement('Tail_05_CTRL', keyTime, 'rotateY', 0)	
	
				#if pRoot:
				#	keyObjectMovement('Root_CTRL', keyTime, 'rotateY', 0)
			else:
				if x % 2 == 0:
					#keyfrmae @ 0, 60, 120, 180
					if (x + 2) % 4 == 0:
						keyVal_tail03 = (pIntensity * 6) * -1
						keyVal_tail04 = (pIntensity * 6) * -1
					else:
						keyVal_tail03 = (pIntensity * 6)
						keyVal_tail04 = (pIntensity * 6)
					
					keyObjectMovement('Tail_03_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_tail03 + randint(0, pIntensity ))
					keyObjectMovement('Tail_04_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_tail04 + randint(0, pIntensity ))
		
		
				else:
					#keyframe @ 30, 90, 150, etc
					if (x + 1) % 4 == 0:
						keyVal_tail01 = (pIntensity * 3)
						keyVal_tail02 = (pIntensity * 6)
						keyVal_tail05 = (pIntensity * 4) * -1
					#	keyVal_Root   = (pRotateIntensity * 2) * -1
					else:
						keyVal_tail01 = (pIntensity * 3) * -1
						keyVal_tail02 = (pIntensity * 6) * -1
						keyVal_tail05 = (pIntensity * 4)
					#	keyVal_Root   = (pRotateIntensity * 2)
		
					keyObjectMovement('Tail_01_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_tail01 + randint(0, pIntensity ))
					keyObjectMovement('Tail_02_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_tail02 + randint(0, pIntensity ))
					keyObjectMovement('Tail_05_CTRL', keyTime + randint(0, pSpeed / 5), 'rotateY', keyVal_tail05 + randint(0, pIntensity ))
	
					#if pRoot:
					#	keyObjectMovement('Root_CTRL', keyTime + randint(0, pSpeed / 5) + rootOfset, 'rotateY', keyVal_Root)
				
	def setPlaybackOptions(pSpeed):
		cmds.playbackOptions( loop='continuous' )
		cmds.playbackOptions( ast=pSpeed * 2, min=pSpeed*2, aet=pSpeed * (cycleCount - 2), max=pSpeed * (cycleCount - 2) )
	
	
	#######MAIN#########
	if bAnimateTail == True:
		setupTailAnmiation(speed, intensity, bAnimateRotation, rotateIntensity)
	if bAnimateTopFin == True:
		setupTopFinAnimation(speed, intensity)	
	if bAnimateSideFinL == True:
		setupSideFinAnimation(speed, intensity)
	if bAnimateRotation == True:
		setupRootAnimation(speed, intensity)
	setPlaybackOptions(speed)


def errorChecking(pArrCheck, pArrVal):
	boolCheck = False
	intCheck = True
	boolArr = []
	intArr = []

	for x in pArrCheck:
		boolArr.append(cmds.checkBox(x, query=True, value=True))
		if cmds.checkBox(x, query=True, value=True):
			boolCheck = True
	for x in pArrVal:
		intArr.append(cmds.intField(x, query=True, value=True))
	if not boolCheck:
		cmds.confirmDialog( icon="warning",title='Error:', 
							message='Please select 1 of the sections to animate!', 
							button=['Ok, sorry'], defaultButton='Ok, sorry')
	else:
		generateAnimation(boolArr, intArr)




	#print cmds.checkBox(boolArr[0], query=True, value=True)
	#print cmds.checkBox(boolArr[1], query=True, value=True)
	#print cmds.checkBox(boolArr[2], query=True, value=True)
	#print cmds.checkBox(boolArr[3], query=True, value=True)

	#print cmds.intField(intArr[0], query=True, value=True)
	#print cmds.intField(intArr[1], query=True, value=True)
	#print cmds.intField(intArr[2], query=True, value=True)
	#print cmds.intField(intArr[3], query=True, value=True)



##window generation

windowID = 'myWindowID'

if cmds.window(windowID, exists=True):
    cmds.deleteUI (windowID)

cmds.window(windowID, title='Creature Animation Generation Options.', sizeable = True, resizeToFitChildren = True)

cmds.rowColumnLayout(numberOfColumns=3, columnOffset=[(1, 'right', 25), (1, 'left', 10), (3, 'left', 10)], rowOffset=[1, 'top', 10])

cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')

cmds.text("Sections to Animate: ")
chkTail = cmds.checkBox(label='Tail', enable=True)
cmds.button(label='Delete Tail Keys', command="removeTailKeys()")

cmds.separator(h=10, style='none')
chkTopFins = cmds.checkBox(label='Top Fins', enable=True)
cmds.button(label='Delete Top Fins Keys', command="removeTopFinKeys()")

cmds.separator(h=10, style='none')
chkSideFins = cmds.checkBox(label='Side Fins', enable=True)
cmds.button(label='Delete Sode Fins Keys', command="removeSideFinKeys()")

cmds.separator(h=10, style='none')
chkRotation = cmds.checkBox(label='Root Rotation', enable=True)
cmds.button(label='Delete Rotation Keys', command="removeRootKeys()")

cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')

cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')
cmds.button(label='Delete ALL Keys', command="removeAllKeys()")

cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')

cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')
cmds.separator(h=10, style='none')

cmds.text("Speed (frames per cycle): ")
intSpeed = cmds.intField( value=30)
cmds.text("30 is Standard.    Multiple's of 6 work best", font='smallPlainLabelFont')

cmds.text("Intensity: ")
intIntensity = cmds.intField( value=5)
cmds.text("5 is Standard.      Multiple's of 5 work best", font='smallPlainLabelFont')

cmds.text("Cycle count: ")
intCycleCount = cmds.intField( value=12)
cmds.text("12 is Standard.    Multiple's of 4 work best", font='smallPlainLabelFont')

cmds.text("Rotate Intensity: ")
intRotateCount = cmds.intField( value=5)
cmds.text("5 is Standard.      Multiple's of 5 work best", font='smallPlainLabelFont')

arrayChk = [chkTail, chkTopFins, chkSideFins, chkRotation]
arrayVal = [intSpeed, intIntensity, intCycleCount, intRotateCount]

cmds.separator(h=20, style='none')
cmds.separator(h=20, style='none')
cmds.separator(h=20, style='none')

cmds.button(label='Generate', command="errorChecking(arrayChk, arrayVal)")


cmds.showWindow(windowID)