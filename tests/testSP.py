import pyaudio
import wave
from pydub import AudioSegment

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

#Conversão de um arquivo mp3 para wav
def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

#Gravação e reprodução ao mesmo tempo
def play_audio_from_microphone(input_device_index: int, output_device_index: int):
    p = pyaudio.PyAudio()

    wf = wave.open("Phone Ringing.wav", "rb")

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        input=True,
        frames_per_buffer=CHUNK,
    )

    input_stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=input_device_index,
        frames_per_buffer=CHUNK,
    )

    output_stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        output_device_index=output_device_index,
        frames_per_buffer=CHUNK,
    )

    print("Reproduzindo áudio. Pressione Ctrl+C para parar.")

    try:
        while True:
            data = input_stream.read(CHUNK)
            # Aqui você pode fazer o processamento adicional do áudio, se necessário
            # E depois reproduzi-lo
            output_stream.write(data)

            data = wf.readframes(CHUNK)
            if not data:
                break

            output_stream.write(data)

    except KeyboardInterrupt:  # Controlar o "Ctrl C"
        print("Parando a reprodução.")

    input_stream.stop_stream()
    input_stream.close()

    output_stream.stop_stream()
    output_stream.close()
    p.terminate()

#listar os dispositovos disponiveis
def list_audio_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        print(f"Dispositivo {i}: {device_info['name']}")


list_audio_devices()
print("Especifique o dispositivo de saída")
# microphoneIndex = input()

convert_mp3_to_wav("audio/Phone Ringing.mp3", "Phone Ringing.wav")

#play_audio_from_microphone(2, 5)  #
play_audio_from_microphone(3, 5)
