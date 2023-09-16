# -*- coding: utf-8 -*-
"""Qlearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19uJfpvkA-sK2yvj4emuzAbWPtLM-6nyc
"""

import gym
import numpy as np
import random
!pip install gym-minigrid
import matplotlib.pyplot as plt
import time
env = gym.make('MiniGrid-Empty-6x6-v0',render_mode='rgb_array')
#env = gym.make('MiniGrid-Empty-8x8-v0')
env.reset()
Q = {}
number_of_episodes = 100
epsilon = 1
alpha = 0.1
policy = []
gamma = 0.99
max_steps = 300
steps_to_goal = []
reward = []
epds = []
def epsilon_greedy(epsilon, state_space):
    if np.random.rand() < epsilon:
        action = np.random.randint(0, 3)
    else:
        action = np.argmax(Q[state_space])
    return action


for i in range(number_of_episodes+20):
  env.reset()
  state = (1, 1, 0)
  done = False
  truncate = False
  policy = []
  steps = 1
  max_steps
  while not done and not truncate:
    steps += 1
    # if trunctation == True:
    #   break
    state_space = state
    if state not in Q:
      Q[state_space] = np.zeros(3)

    action = epsilon_greedy(epsilon, state_space)
    policy.append(action)
    next_obs, reward, done, truncate, info = env.step(action)

    new_state = env.agent_pos
    # print('newstate',new_state)
    new_direction = env.agent_dir
    # print('newdirec',new_direction)
    next_state_space = (new_state[0], new_state[1], new_direction)
    # print('newstatespace',next_state_space)
    if next_state_space not in Q:
      Q[next_state_space] = np.zeros(3)

    maxof_next_action = np.argmax(Q[next_state_space])
    Q[state_space][action] = Q[state_space][action] + alpha * (reward + gamma*(Q[next_state_space][maxof_next_action]) - Q[state_space][action])
    state = next_state_space
    epsilon = ((-i)/number_of_episodes) + 1
  epds.append(i+1)
  steps_to_goal.append(steps)
  # print("epd_no: ",i+1)
  # print("steps: ",steps)
plt.title("MiniGrid-Empty-6x6-v0 using Q learning Algo")
#plt.title("MiniGrid-Empty-8x8-v0 using Q learning Algo")
plt.plot(epds,steps_to_goal)
plt.xlabel("Number of episodes")
plt.ylabel("Steps to reach goal")
plt.show()
print('policy :',policy)
# env = gym.make('MiniGrid-Empty-6x6-v0', render_mode='human')
# env.reset()
# epd_rew = 0
# for i in range(len(policy)):
#     n_obs, rew, done, trunc, info = env.step(policy[i])
#     time.sleep(0.25)
#     epd_rew += rew
#     env.render()
# env.close()

# print(Q)