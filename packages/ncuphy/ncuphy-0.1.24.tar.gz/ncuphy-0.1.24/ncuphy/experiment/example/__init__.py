import os

__list__ = sorted(['StepperMotor', "ADS1115", "MPU9250", "MPU6050"])

__which__ = input(f"Which module do you want to import? \n{__list__}\nEnter the module name: ")

assert __which__ in __list__, f"Module {__which__} not found in {__list__}"


__ads1115_example = """
from ncuphy.experiment.ads1115 import ADS1115
import time

bus = 1                 # RaspberryPi 上有兩個 i2c 通道，分別是 i2c0, i2c1, 相對應的就是 bus=0, bus=1
address = 0x48          # i2c 地址，ads1115 硬體設計上選擇了 0x48 這個地址
channel = 0             # ads1115 有四個通道，分別是 0, 1, 2, 3
pga = 4.096             # pga 代表的是 programmable gain amplifier, 也就是可程控的電壓放大， 4.096 相對應的是沒放大信號，電壓範圍是 4.096V, 0.256 對應的是放大 16倍， 電壓範圍變成 0.256V
mode = "continuous"     # 單發和連續讀取模式
data_rate = 860         # 取數據的頻率

ads1115 = ADS1115(bus, address)
ads1115.configure(channel=channel, pga=pga, mode=mode, data_rate=data_rate)

while True:
    adc, voltage = ads1115.read()
    print(f"Voltage: {voltage ：.3f}V, ADC: {adc}")
    time.sleep(0.1)
"""

__stepper_motor_example = """
from ncuphy.experiment import StepperMotor
import time

# display log, not necessary ---------------------------------------------

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# -----------------------------------------------------------------------------

# define the pins
pul = 26
dir = 19
ena = 13

# define the delay between pulses
pulse_delay = 0.001

# create the stepper motor object
motor = StepperMotor(pul, dir, ena, pulse_delay)



# move the stepper motor by 1000 steps
motor.step(1000)
time.sleep(2)



# move the stepper motor in the other direction by 1500 steps
motor.step(-1800)
time.sleep(2)



# move the stepper motor to the home position
motor.home()
time.sleep(2)



# move the stepper motor again by 100 steps
motor.step(1200)
time.sleep(2)



# get the current position
position = motor.position
print(f"Current position: {position}")



# set the current position as the home position
motor.sethome()
"""

# get working dir
__working_dir__ = os.getcwd()

if __which__ == "StepperMotor":
    with open('Example_StepperMotor.py', 'w') as f:
        f.write(__stepper_motor_example)
        print(f"Example_StepperMotor.py created in {__working_dir__}")
elif __which__ == "ADS1115":
    with open("Example_ADS1115.py", "w") as f:
        f.write(__ads1115_example)
        print(f"Example_ADS1115.py created in {__working_dir__}")
else:
    print("Example not found.")