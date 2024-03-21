import gymnasium as gym
env = gym.make('CartPole-v1')

observation, info = env.reset()
print(env.action_space)
print(env.observation_space)

for _ in range(1):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    print(observation)
    if terminated or truncated:
        observation, info = env.reset()

env.close()