# Flappy_bird_RL

## ~Sub-projects for main project:
 - Frozen lake
 * Empty room environment using openai gym
    * Using MonteCarlo , Q learning, Sarsa , Sarsa-Lambda Algorithms 

# 1)Frozen lake: 
**Description**: For better understanding of the **Policy** and **Value** Iteration using the Frozen lake environment for both Deterministic and Stochastic of fully observable environments.

![Frozen Lake Gym](https://www.gymlibrary.dev/_images/frozen_lake.gif)

**ALGORITHM**
* Policy and Value iteration algorithms are used in this Environment to get the optimal policy.

**STATE SPACE**

* For 4x4 grid there are 16 cells and each cell represents a integer starting from 0 to 15.
* Any cell may contain a obstacle (Hole) or Frozen lake and the aim of the agent is to reach the Goal in optimal way using policy and value iteration.


**ACTION SPACE**

The action space consists of 4 actions -

	LEFT - 0
	DOWN - 1
	RIGHT- 2
	UP   - 3

 **REWARD FUNCTION**

* +1 if the agent reaches the goal cell.
* 0 otherwise.

![Frozen lake code(results without slippery)](https://github.com/DipanshuK04/Flappy_bird_RL/blob/main/Frozen_lake.ipynb)

# Frozen lake with slippery environment
![Frozen Lake Gym]

