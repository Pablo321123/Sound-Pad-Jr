import ctypes
from ctypes import wintypes

winmm = ctypes.WinDLL('winmm')

WAVE_MAPPER = -1
WIM_SETDEFAULTDEVICE = 0x3C3

def set_default_microphone(device_id):
    winmm.waveInMessage(WAVE_MAPPER, WIM_SETDEFAULTDEVICE, device_id, 0)

# Chame a função para definir o dispositivo de microfone padrão
set_default_microphone(3)
