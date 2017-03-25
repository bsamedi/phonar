import matplotlib.pyplot as plt
import random
import numpy as np
import math

from phonoSensors2D import phonoSensors2D

def square_sensors(square_edge):
    p = phonoSensors2D()
    p.add((0,0))
    p.add((0,square_edge))
    p.add((square_edge,0))
    p.add((square_edge,square_edge))
    return p

def triangle_sensors(edge):
    p = phonoSensors2D()
    p.add((0,0))
    p.add((edge, 0))
    p.add((edge/2, edge * 1.5))
    p.add((edge/2, edge * 0.3))
    return p


def err(sigma, mean = 0):
    e = random.normalvariate(mean, sigma)
    #print('sigma {}, mean {}, val {}'.format(sigma, mean, e))
    return e
    
def distort(readings, err_xy, err_t):
    fozzy = [ (r[0]+err(err_xy), r[1]+err(err_xy), r[2] + err(err_t)) for r in readings]
    return fozzy

def run_detection(num_tests, sensors, sound, err_xy, err_t):
    ideal_readings = sensors.idealReadings(sound)
    #print('ideal_detection {}'.format(sensors.detectSource(ideal_readings, 1)))
    #print(' ideal_readings {}'.format(ideal_readings))
    #print(' err_readings {}'.format(distort(ideal_readings, err_xy, err_t)))
    x, y = [], []
    for i in range(num_tests):
        err_readings = distort(ideal_readings, err_xy, err_t)
        #print(' err_readings {}'.format(err_readings))
        err_snd = sensors.detectSource(err_readings, 1)
        #print(' err_snd {}'.format(err_snd))
        x.append(err_snd[0])
        y.append(err_snd[1])
    fig, subplot = plt.subplots(1)
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit)
    xFit = x + [sound[0], sound[0]+100, sound[0]-100]
    xFit.sort()
    subplot.plot( xFit, fit_fn(xFit), color = 'grey', linewidth = .5)
    subplot.scatter(x, y, color = 'blue', s = 18)
    subplot.scatter(np.median(x), np.median(y), color = 'red', s = 36)
    subplot.scatter(sound[0], sound[1], color = 'green', s = 36)
    plt.show()

def compact():
    # 1 meter sized square
    ph = square_sensors(150)
    #ph = triangle_sensors(10)
    sound = (4000,9000,0)
    #print('sound {}'.format(sound))
    # 1 mm and 1 ms error
    run_detection(5, ph, sound, .005, 0.002)

def widespread():
    # 20 Km sized square
    ph = square_sensors(20000)
    #ph = triangle_sensors(10)
    sound = (4000,9000,0)
    #print('sound {}'.format(sound))
    # 1 mm and 1 ms error
    run_detection(5, ph, sound, 15, 0.010)

widespread()