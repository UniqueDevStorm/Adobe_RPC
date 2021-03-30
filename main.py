from pypresence import Presence
import time
import pygetwindow as gw

client_id = '826404931153821786'
RPC = Presence(client_id)
RPC.connect()
Start = time.time()

while True:
    title = str()
    for i in gw.getAllTitles():
        if '\u200e- Adobe XD' in i:
            title = i.replace(' ‎- Adobe XD', '')
    if title == str():
        print('Adobe XD를 찾지 못했습니다.')
        time.sleep(1)
        continue
    else:
        RPC.update(details=title, buttons=[{"label": "Adobe XD", "url": "https://www.adobe.com/kr/products/xd.html"}],
                   large_image='xd', start=int(Start))
        time.sleep(1)
