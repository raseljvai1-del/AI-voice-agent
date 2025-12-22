# system_control/volume.py
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def change_volume(command):
    if "up" in command:
        return "Volume increased"
