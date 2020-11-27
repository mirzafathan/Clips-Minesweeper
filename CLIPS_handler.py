import clips
import game_functions as Games

env = clips.Environment()
env.load('kbagent.clp')
env.reset()
fact = env.assert_string('(open 1 1)')
#fact.retract()
for i in env.facts():
	print(i)
print('--')
print(env.run())