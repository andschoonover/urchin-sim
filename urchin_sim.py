import gym
import numpy as np
from urchin import URCHINEnv


env = URCHINEnv() 
env.reset()

for i in range(100000):
    env.render()
    action = np.array([])
    env.step(action)

env.close()