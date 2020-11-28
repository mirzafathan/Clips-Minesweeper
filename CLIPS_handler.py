import clips
import game_functions as Games


Size = 4

env = clips.Environment()
env.load('kbagent.clp')
env.reset()

env.assert_string('(open 1 1)')
for i in range(-1, Size+1):
	initframe = '(safe ' + str(-1) + ' ' + str(i) + ')'
	print(initframe)
	env.assert_string(initframe)
for i in range(0, Size+1):
	initframe = '(safe ' + str(i) + ' ' + str(-1) + ')'
	print(initframe)
	env.assert_string(initframe)
for i in range(0, Size+1):
	initframe = '(safe ' + str(Size) + ' ' + str(i) + ')'
	print(initframe)
	env.assert_string(initframe)
for i in range(0, Size):
	initframe = '(safe ' + str(i) + ' ' + str(Size) + ')'
	print(initframe)
	env.assert_string(initframe)

#fact.retract()
for i in env.facts():
	print(i)
print('--')
print(env.run())
for i in env.facts():
	print(i)