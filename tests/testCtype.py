import ctypes

winmm = ctypes.WinDLL("winmm.dll")

def set_default_microphone(device_id):
    winmm.waveInMessage(0, winmm.WIM_SETDEFAULTDEVICE(), device_id, 0)


# wMid (Word, Manufacturer ID): Identifica o ID do fabricante do dispositivo de áudio.
# wPid (Word, Product ID): Identifica o ID do produto do dispositivo de áudio.
# vDriverVersion (DWORD, Driver Version): Indica a versão do driver do dispositivo de áudio.
# szPname (Char Array, Product Name): Armazena o nome do dispositivo de áudio.
# dwFormats (DWORD, Supported Formats): Indica os formatos de áudio suportados pelo dispositivo.
# wChannels (Word, Number of Channels): Representa o número de canais de áudio suportados pelo dispositivo.
# wReserved1 (Word, Reserved): Campo reservado para uso futuro.

class WAVEINCAPS(ctypes.Structure):
    _fields_ = [
        ("wMid", ctypes.c_uint16),
        ("wPid", ctypes.c_uint16),
        ("vDriverVersion", ctypes.c_uint32),
        ("szPname", ctypes.c_char * 32),
        ("dwFormats", ctypes.c_uint32),
        ("wChannels", ctypes.c_uint16),
        ("wReserved1", ctypes.c_uint16),
    ]

def list_audio_devices():
    device_count = winmm.waveInGetNumDevs()

    print("Dispositivos de Áudio Disponíveis:")

    for i in range(device_count):
        device_info = WAVEINCAPS()
        winmm.waveInGetDevCapsA(i, ctypes.byref(device_info), ctypes.sizeof(device_info))
        device_name = device_info.szPname.decode('utf-8')
        print(f"ID: {i}, Nome: {device_name}")

    
device_id = 2
list_audio_devices()
#set_default_microphone(2)