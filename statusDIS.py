from pypresence import Presence
import time
import psutil

time.sleep(1)


client_id = айди Бота дискорда
#Пример client_id = 1107349645656588412
RPC = Presence(client_id)
ButtonsList= [
                {
                    "label": "My Site",
                    "url": "https://github.com/Jastickon"
                },
                {
                    "label": "GitHub",
                    "url": "https://github.com/Jastickon"
                }
            ]

RPC.connect()
while True:
    time.sleep(1)
    ram1=psutil.virtual_memory().percent
    cpu1=psutil.cpu_percent()
    ram=round(psutil.virtual_memory().total/1000000000, 1)
    cpucore=psutil.cpu_count(logical=False)
    cpupot=psutil.cpu_count()
    RPC.update(details= f"RAM({ram}GB):{ram1}% CPU({cpucore}/{cpupot}):{cpu1}%",
            large_image='https://media.tenor.com/8znDLN7uJqwAAAAi/b-eat-saber.gif',
            large_text='3.14',
            buttons=ButtonsList,
            
)
