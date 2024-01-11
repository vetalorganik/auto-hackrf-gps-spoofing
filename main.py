import subprocess
from brdc import BrdcController
import platform
import os

system_platform = platform.system()
print(system_platform)

os.makedirs("./assets/brdc", exist_ok=True)
os.makedirs("./assets/binaries", exist_ok=True)

proxy_auth_token = "uz7FetoBRH+bWebbSW94ktM8dddic6HhCAxO1i2eX/gdWNJ/ZfPY+xQ28XkCY9V7UEC8SQe0JZsYPzb1mVaAOLKZKj3WMfAMpGrXXDQScV+3kROrztbu32jJRJXBTi554HYfCK08pPenETPY1m3bV+tk0EYUzL+XhLjjVky21Hy2dSFl+lVLUNq2Zu0aQGQNsu0p9ZXA3shl1XC+rcFjjjFvQPHYY6KL4ycWgJ/G6wZkrJTR2otDE/zNbs4ji7hQJQ8LuK9ygrskgaaWZHvjnu5NN3g4MDTrEbLMlpXTCNCiq1GojOEA1cxRimjG1E/1q9cTSRfdoHnSQqKOO0xoR6swXeS8RwkotTQ111rTS3zE4fJvzMl6jkDP4FD0pJQ0JU9Q6ID+So2zBRJY4x1FxT/9nrK1GbBbUeOuzBhi9BU+otKLw5RcmvfQvylLkcHAwnYTL/A4xGdqxVg0Z3pOvUM44RKYT6uq3PqDbUgaUXlcc/d8zcXb9Rp3Du3QTv3AsiPEiN09unDBY3uuhEcbHRsK3lt1H++RqcBTLF9Qy3M/5PdsOQWocWsaSZZ7qs9Wgp9tpNN2vIRPucg2EgZyygIil7QodB+c5aSPu7NFIwLfHbFcKaQr/Iy8QzNLbahc5/pHAUFWSBfp7tgRHccALOM4mx/WtVs/687Ih4vob+9XhEr2QpZyi4LiipN3bhuCzJELbFbwOdSlgZlaOpEL2tb7joZz8ywfokz3PDIor0bO9b7gZxL4FBkTp5XNECDTZnoKdjoaSsTrcg57u2eNkk5KdiZa1LmgNoWibP/SRX2WovrrwpR4c6PjPUw8iQggSINCimdeikmumKlIFwlfdLGHgrLDsxMbnr5UUGipqB33PEoFM/2bSaSkR/tASGBIfwtiOQ+cALlFuLq0TGx7Qn4phSIrIRMnanYIBpfeNKWVxP95TjcMT17wEqbBqIno4KrPn5TjB4h/QRMMySM6bg=="
urs_guid_ops = "6dbd7c46-117f-44db-a91f-5b267c46f3c5"

brdcController = BrdcController(proxy_auth_token, urs_guid_ops)
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
