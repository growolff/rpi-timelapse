from picamera import PiCamera
from os import system
from time import sleep
import sys
import argparse

parser = argparse.ArgumentParser(description='Este programa permite tomar timelapses con una rPI Cam')
parser.add_argument('-tt','--totaltime', help='Tiempo total del timelapse en segundos', required=False, type=int)
parser.add_argument('-l','--lapse',help='Tiempo entre fotos en segndos', required=True, type=int)
parser.add_argument('-c', '--cantidad', help='Cantidad de imagenes', required=True, type=int)

args = parser.parse_args()

camera = PiCamera()
camera.resolution = (1024,768)
camera.vflip = True
camera.hflip = True

totaltime = args.totaltime
lapse = args.lapse
cantidad = args.cantidad

   
for i in range(cantidad):
    name = 'image{0:04d}.jpg'.format(i)
    camera.capture(name)
    print('photo %s taken'%(name))
    sleep(lapse)

print('done')


