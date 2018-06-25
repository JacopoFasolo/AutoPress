# -*- coding: cp1252 -*-
import time
import mouse
import keyboard

icon_market = [1176, 161]
start_drag = [1200, 200]
end_drag = [1200, 900]
button_ad = [1089, 334]
icon_items = [734, 85]
icon_crates = [1146, 959]
icon_crate = [950, 578]
reset_esc = [965, 712]
count = 0

while True:
    count += 1
    
    #click dell'icona della pagina principale e attesa che la pubblicità finisca
    mouse.move(icon_market)
    mouse.click()
    time.wait(1)
    mouse.drag(start_drag, end_drag, duration=1)
    mouse.move(button_ad)
    mouse.click()
    time.wait(60)

    #visione della pubblicità e ritorno alla schermata iniziale
    for i in range(5):
        keyboard.press_and_release('esc')
        time.wait(1)
    mouse.move(reset_esc)
    mouse.click()
    time.wait(1)

    #apertura del forziere
    mouse.move(icon_items)
    mouse.click()
    time.wait(1)
    mouse.move(icon_crates)
    mouse.click()
    time.wait(1)
    mouse.move(icon_crate)
    mouse.click()
    time.wait(10)
    print 'Aperti '+count+' forzieri.'

    #ritorno alla schermata principale dopo aver aperto il forziere
    for i in range(5):
        keyboard.press_and_release('esc')
        time.wait(1)
    mouse.move(reset_esc)
    mouse.click()
    time.wait(1)
    
