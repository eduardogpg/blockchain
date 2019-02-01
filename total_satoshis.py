reward = 50 #Original reward
reward_interval = 210000
satoshis = 10**8 #100 000 000

def total_bitcoins():
    total = 0
    current_reward = reward

    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2

    return total

total = total_bitcoins()
print("Total bitcoins :" + str(total))
print("Total satoshis :" + str(total * satoshis))
