import gym
import numpy as np
from urchin import URCHINEnv


env = URCHINEnv() 
env.reset()

for i in range(100000):
    env.render()
    action = .175*np.sin(i/150)+.175
    print(action)
    env.step(action)

env.close()