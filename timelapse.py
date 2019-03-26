from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)

for i in range(240):
    name = 'image{0:04d}.jpg'.format(i)
    camera.capture(name)
    print('photo %s taken'%(name))
    sleep(600)

print('done')

