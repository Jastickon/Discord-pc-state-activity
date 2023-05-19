from pypresence import Presence
import time
import psutil
import pymgpu #установить вместо pynvml(ВАЖНО!!!!)

client_id = айди Бота дискорда
#Пример client_id = 1107349645656588412
RPC: Presence = Presence(client_id)
ButtonsList= [
                {
                    "label": "GitHub",
                    "url": "https://github.com/Jastickon"
                }
            ]

RPC.connect()

gpu_found = True

def get_gpu_info():
    try:
        gpu_info = pymgpu.get_info()
        return {
            'name': gpu_info['device'][0]['name'],
            'vendor': gpu_info['device'][0]['vendor'],
            'memory': gpu_info['device'][0]['memoryTotal']/1024/1024,
            'max_clock_speed': gpu_info['core'][0]['maxClockFrequency']/1000,
            'compute_units': gpu_info['device'][0]['computingUnits']
        }
    except Exception as e:
        if gpu_found:
            print(f"Error getting GPU info: {e}")
        global gpu_found
        gpu_found = False
        return None

while True:
    time.sleep(1)
    
    ram_percent = psutil.virtual_memory().percent
    cpu_percent = psutil.cpu_percent()
    
    gpu_info = get_gpu_info()
    if gpu_info is not None:
        gpu_utilization = ''
        if gpu_info is None:
    gpu_utilization = 'No GPU found'
else:
    gpu_utilization = f"{gpu_info['utilization']['gpu']:.1f}%"
    else:
        gpu_utilization = 'No GPU found'

    RPC.update(
        details=f"CPU: {cpu_percent}% GPU: {gpu_utilization} ",
        large_image='https://media.tenor.com/8znDLN7uJqwAAAAi/b-eat-saber.gif',
        large_text='3.14',
        buttons=ButtonsList,
        mall_image='https://cdn3.emoji.gg/emojis/8235-streaming.png',
    )

RPC.close()