# Recorder.



import glob
import os
import sys
import time

#!!!Adapt Carla's path to your case
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

client = carla.Client("127.0.0.1", 2000)
client.set_timeout(10.0)
world = client.get_world()
List = world.get_actors()

try:
    print("Start replaying")
    client.set_replayer_time_factor(0.5)
    client.replay_file('D:\carla\PythonAPI\examples\SelberCodes\EuroNCAP_cases\CPNA_50_30.0_0.05\Recording.log', 0, 0, 0)

finally:
    print("Stop recording")
    pass