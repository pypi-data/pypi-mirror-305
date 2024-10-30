import smbus2
import time

class ADS1115:
    # Pointer Register
    POINTER_CONVERSION = 0x00
    POINTER_CONFIG = 0x01

    # Config Register Bits
    OS_SINGLE = 0x8000  # Start a single conversion
    MUX = {
        0: 0x4000,  # AIN0
        1: 0x5000,  # AIN1
        2: 0x6000,  # AIN2
        3: 0x7000   # AIN3
    }
    PGA = {
        6.144: 0x0000,  # +/-6.144V range
        4.096: 0x0200,  # +/-4.096V range
        2.048: 0x0400,  # +/-2.048V range (default)
        1.024: 0x0600,  # +/-1.024V range
        0.512: 0x0800,  # +/-0.512V range
        0.256: 0x0A00   # +/-0.256V range
    }
    MODE = {
        'single': 0x0100,     # Single-shot mode
        'continuous': 0x0000  # Continuous conversion mode
    }
    DATA_RATE = {
        8:    0x0000,  # 8 samples per second
        16:   0x0020,  # 16 samples per second
        32:   0x0040,  # 32 samples per second
        64:   0x0060,  # 64 samples per second
        128:  0x0080,  # 128 samples per second (default)
        250:  0x00A0,  # 250 samples per second
        475:  0x00C0,  # 475 samples per second
        860:  0x00E0   # 860 samples per second
    }
    COMP_DISABLE = 0x0003  # Disable comparator

    def __init__(self, bus=1, address=0x48):
        self.address = address
        self.bus = smbus2.SMBus(bus)
        self.channel = 0
        self.pga = 4.096
        self.mode = 'continuous'
        self.data_rate = 860



    def configure(self, channel=0, pga=4.096, mode='continuous', data_rate=860):
        if channel not in [0, 1, 2, 3]:
            raise ValueError('Invalid channel (int): choose 0-3')

        if pga not in self.PGA:
            raise ValueError('Invalid PGA value (float): choose from 6.144, 4.096, 2.048, 1.024, 0.512, 0.256')

        if mode not in self.MODE:
            raise ValueError("Invalid mode (string): choose 'single' or 'continuous'")

        if data_rate not in self.DATA_RATE:
            raise ValueError('Invalid data rate (int): choose from 8, 16, 32, 64, 128, 250, 475, 860')

        self.channel = channel
        self.pga = pga
        self.mode = mode
        self.data_rate = data_rate

        # Build config register
        config = (
            self.OS_SINGLE |  # Operational status/single-shot start
            self.MUX[channel] |
            self.PGA[pga] |
            self.MODE[mode] |
            self.DATA_RATE[data_rate] |
            self.COMP_DISABLE
        )

        # Write config register
        config_bytes = [(config >> 8) & 0xFF, config & 0xFF]
        write = smbus2.i2c_msg.write(self.address, [self.POINTER_CONFIG] + config_bytes)
        self.bus.i2c_rdwr(write)

    def read(self):
        # Read conversion result
        read = smbus2.i2c_msg.write(self.address, [self.POINTER_CONVERSION])
        result = smbus2.i2c_msg.read(self.address, 2)
        self.bus.i2c_rdwr(read, result)
        raw_adc = (list(result)[0] << 8) | list(result)[1]

        # Convert to signed integer
        if raw_adc > 0x7FFF:
            raw_adc -= 0x10000

        # Calculate voltage
        voltage = raw_adc * (self.pga / 32768.0)

        return voltage


    def read_raw(self):
        # Read conversion result
        read = smbus2.i2c_msg.write(self.address, [self.POINTER_CONVERSION])
        result = smbus2.i2c_msg.read(self.address, 2)
        self.bus.i2c_rdwr(read, result)
        raw_adc = (list(result)[0] << 8) | list(result)[1]

        # Convert to signed integer
        if raw_adc > 0x7FFF:
            raw_adc -= 0x10000

        return raw_adc
        
    def close(self):
        self.bus.close()

