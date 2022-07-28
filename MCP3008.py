from spidev import Spidev
class MCP3008:
    def __init__(self, bus = 0, device = 0) :
        self.bus, self.device = bus, device
        self.spi = Spidev()
        self.open()
        self.spi.max_speed_hz = 1000000 # 1MHz
    
    def open(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1000000 # 1MHz
        
     #def read(self, channel = 0):
     #cmd1 = 4 | 2 | (( channel & 4) >> 2)
     #cmd2 = (channel & 3) <<6
     #self.spi.max_speed_hz = 1000000 # 1MHz
     #adc = self.spi.xfer2)([cmd1, cmd2, 0])
        
    def read(self, channel = 0):
        self.spi.max_speed_hz = 1350000
        adc = self.spi.xfer2([1, (8+channel) <<4,0])
        #print ("raw data",adc)
        data = ((adc[1]&3)<<8)+adc[2]
        return data
     
    def close(self):
        self.spi.close()
        