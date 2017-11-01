"""
We train a simple Q-Learning algorithm for fraud detection.
"""
import state_space
import action_space
import numpy as np


# Q-TABLE
class QLearnAgent:
    def __init__(self, init='zero'):

        # learning rate
        self.lr = 0.01
        # discount factor
        self.discount = 0.1
        # epsilon for eps-greedy policy
        self.epsilon = 0.1

        # initialise a q-table based on the state and action space
        if init == 'zero':
            self.q_table = np.zeros((state_space.SIZE, action_space.SIZE))
        elif init == 'always second':
            self.q_table = np.zeros((state_space.SIZE, action_space.SIZE))
            self.q_table[:, 1] = 1
        elif init == 'random':
            self.q_table = np.random.uniform(0, 1, (state_space.SIZE, action_space.SIZE))
        else:
            raise NotImplementedError('Q-table initialisation', init, 'unknown.')

    def take_action(self, state):
        action_vals = self.q_table[state]
        if np.random.uniform(0, 1) > self.epsilon:
            action = np.argmax(action_vals)
        else:
            action = np.random.choice(action_space.ACTIONS)

        return action

    def update(self, state, action, reward, next_state):

        self.q_table[state, action] += self.lr * (reward + self.discount * np.max(self.q_table[next_state]) - self.q_table[state, action])
