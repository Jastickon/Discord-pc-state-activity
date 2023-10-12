from pypresence import Presence
import pypresence
import time
import psutil
import pynvml
import random

pynvml.nvmlInit()

client_id = 
#Пример client_id = 1107349645656588412
RPC: Presence = Presence(client_id)
ButtonsList= [
                {
                    "label": "Vizo Studio",
                    "url": "https://discord.gg/zuuwz2bUmQ"
                },
                {
                    "label": "Subterrania project",
                    "url": "https://discord.gg/Hh5XAebxHu"
                }
            ]
try:
    RPC.connect()
    error = 0
except pypresence.exceptions.DiscordNotFound:
    print("Жду запуска дисорда")
    time.sleep(1)
    error = 1

device_count = pynvml.nvmlDeviceGetCount()
if device_count == 0:
    print("Video not found")
    has_video_card = False
else:
    has_video_card = True

proc = 0
text = "Loading..."
while True:
    time.sleep(1)

    rasudok = random.randint(0, 30)


    ram_percent=psutil.virtual_memory().percent
    cpu_percent=psutil.cpu_percent()
    
    if has_video_card:
        device_count = pynvml.nvmlDeviceGetCount()
        gpu_utilization = ''
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            gpu_utilization += f"{pynvml.nvmlDeviceGetUtilizationRates(handle).gpu / 1:.1f}% "
    else:
        gpu_utilization = ''

    proc += 1

    if proc == 1:
        text = "10% [■_________]"
    elif proc == 2:
        text = "20% [■■________]"
    elif proc == 3:
        text = "30% [■■■_______]"
    elif proc == 4:
        text = "40% [■■■■______]"
    elif proc == 5:
        text = "50% [■■■■■_____]"
    elif proc == 6:
        text = "60% [■■■■■■____]"
    elif proc == 7:
        text = "70% [■■■■■■■___]"
    elif proc == 8:
        text = "80% [■■■■■■■■__]"
    elif proc == 9:
        text = "90% [■■■■■■■■■_]"
    elif proc == 10:
        text = "100% [■■■■■■■■■■]"
    elif proc >= 11:
        if proc == 12:
            text = "{}"
        elif proc == 13:
            text = "{=}"
        elif proc == 14:
            text = "{==}"
        elif proc == 15:
            text = "{===}"
        elif proc == 16:
            text = "{====}"
        elif proc == 17:
            text = "{𝙊𝙥𝙚𝙣}"
        elif proc > 17:
            text = f"Возраст: 𝐍𝐨𝐧𝐞  Рассудок: {rasudok}"
    if proc > 37:
        proc = 0
        text = "Loading..."

    try:
        if error == 1:
            try:
                try:
                    RPC.connect()
                    error = 0
                except pypresence.exceptions.DiscordError:
                    pass
            except pypresence.exceptions.DiscordNotFound:
                error = 1
        if error == 0:
            try:
                # здесь отоброжение в приложение
                RPC.update(details=f"𝐂𝐏𝐔: {cpu_percent}% 𝐆𝐏𝐔: {gpu_utilization} 𝐑𝐀𝐌: {ram_percent}%",
                           state=text,
                           large_image='https://i.pinimg.com/originals/bf/2a/85/bf2a85f922ef8589dd4ccc180edb3e30.gif',
                           large_text='Кирилл',
                           buttons=ButtonsList,
                           small_image='https://cdn.discordapp.com/emojis/790045045813542912.gif?size=96&quality=lossless',
                           small_text='𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝'
                           )
            except pypresence.exceptions.PipeClosed:
                print("Дискорд закрыт")
                RPC.close()
                error = 1
                time.sleep(1)

    except pypresence.exceptions.DiscordNotFound:
        RPC.close()
        error = 1


pynvml.nvmlShutdown()
