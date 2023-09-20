from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

c = 270
r = True

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    if(r)
        character.draw(math.cos(r/360*2*math.pi),math.sin(r/360*2*math.pi))
    else
        character.draw(c/2,c/2)
    update_canvas()
    delay(0.05)
    get_events()
    c += 5
    if(c>=630)
        c-=360
        r = not r
close_canvas()
