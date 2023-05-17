from pypresence import Presence
import time
import psutil

time.sleep(0)


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
print(f"test")
while True:
    time.sleep(1)
    ram1=psutil.virtual_memory().percent
    cpu1=psutil.cpu_percent()
    RPC.update(details= f"RAM: {ram1}% CPU: {cpu1}%",   
            large_image='https://media.tenor.com/8znDLN7uJqwAAAAi/b-eat-saber.gif',
            large_text='3.14',
            buttons=ButtonsList,
            small_image='https://cdn3.emoji.gg/emojis/8235-streaming.png',
            
)