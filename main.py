import subprocess
from brdc import BrdcController
import platform
import os
import json

system_platform = platform.system()

os.makedirs("./assets/brdc", exist_ok=True)
os.makedirs("./assets/binaries", exist_ok=True)

with open("./auth.json", "r") as file:
    authCookies = json.load(file)

brdcController = BrdcController(authCookies)
filename = brdcController.get_file()

print("[!] Starting to generate binary file...")
create_binary_executable = f"./assets/app/gps-sdr-sim/{'gps-sdr-sim' if system_platform == 'Linux' else 'gps-sdr-sim.exe'}"
create_binary_command = f"./assets/app/gps-sdr-sim -b 8 -e ./assets/brdc/{filename} -l 39.087822,-94.577656,100 -o ./assets/binaries/gps-sim-{filename.replace('.', '-')}.bin"
subprocess.run(create_binary_command, shell=True, capture_output=True, text=True)
print("[!] Binary file generated!")

print("[!] Launching HackRF script...")
start_hackrf_command = f"hackrf_transfer -t ./assets/binaries/gps-sim-{filename.replace('.', '-')}.bin  -f 1575420000 -s 2600000 -a 1 -x 0"
start_hackrf_result = subprocess.run(
    start_hackrf_command, shell=True, capture_output=True, text=True
)
print("[!] HackRF stopped execution!")

if start_hackrf_result.stderr:
    print(f"[E] Errors:\n {start_hackrf_result.stderr}")
