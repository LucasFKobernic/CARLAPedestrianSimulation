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
    print("Start recording")
    client.start_recorder("D:/carla/PythonAPI/examples/recording_test_01.log")
    while True:
        world.wait_for_tick()
finally:
    print("Stop recording")
    client.stop_recorder()
