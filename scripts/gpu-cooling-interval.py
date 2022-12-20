from tqdm import tqdm
from time import sleep

# GPU cooling interval
gpu_cooling_interval = 500

# GPU cooling
print("\n\n" + "GPU COOLING TIME STARTED")
for i in tqdm (range (gpu_cooling_interval), desc="Waiting for cooling..."):
    sleep(0.001)
print("GPU COOLING TIME ENDED" + "\n\n")
