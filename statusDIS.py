from pypresence import Presence
import time
import psutil

time.sleep(1)


client_id = id Бота дискорда
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
    ram2= psutil.swap_memory()
    RPC.update(details= f"RAM: {ram1}% CPU: {cpu1}%",   
            large_image='https://media.tenor.com/8znDLN7uJqwAAAAi/b-eat-saber.gif',
            large_text='3.14',
            buttons=ButtonsList,
            
)
