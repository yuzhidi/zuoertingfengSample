from random import random

total = 5

def moveCar(positions):
	return map(lambda x : x + 1 if random() > 0.4 else x, positions)

def getPosition(position):
	return '-' * position

def moveRound(state):
	return {
		'time' : state['time'] - 1, 
		'positions' : moveCar(state['positions'])
	}

def drawPosition(state):
	print '\n'.join(map(getPosition, state['positions']))

def race(state):
	if state['time'] is total:
		print 'begin:'
	else:
		print 'round: %s' % (total - state['time'])

	drawPosition(state)

	if state['time']:
		race(moveRound(state))

race({
	'time' : total,
	'positions' : [1,1,1]})
