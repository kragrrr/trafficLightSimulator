import time
import os

def simulate_traffic_lights():
    red_state = "Red"
    yellow_state = "Yellow"
    green_state = "Green"

    while True:
        print(f"L1: {green_state}\nL2: {red_state}\nL3: {red_state}\nL4: {red_state}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {yellow_state}\nL2: {red_state}\nL3: {red_state}\nL4: {red_state}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {red_state}\nL2: {green_state}\nL3: {red_state}\nL4: {red_state}")
        time.sleep(3)  
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {red_state}\nL2: {yellow_state}\nL3: {red_state}\nL4: {red_state}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {red_state}\nL2: {red_state}\nL3: {green_state}\nL4: {red_state}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {red_state}\nL2: {red_state}\nL3: {yellow_state}\nL4: {red_state}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {red_state}\nL2: {red_state}\nL3: {red_state}\nL4: {green_state}")
        time.sleep(3)  
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"L1: {red_state}\nL2: {red_state}\nL3: {red_state}\nL4: {yellow_state}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

simulate_traffic_lights()
