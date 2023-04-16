from pypresence import Presence
import time
import psutil

time1 = time.ctime()
client_id = id бота дискорда
RPC = Presence(client_id)

RPC.connect()
while True:
    time.sleep(1)
    ram1=psutil.virtual_memory().percent
    cpu1=psutil.cpu_percent()
    ram2= psutil.swap_memory()
    RPC.update(details= f"RAM: {ram1}% CPU: {cpu1}%", 
            large_image='https://media.tenor.com/sKSw-rqsFxQAAAAi/foxy-foxplushy.gif',  
)
