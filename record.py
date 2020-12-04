import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
# clk at 135 kHz for 75 ksps
spi = busio.SPI(135000, MISO=board.MISO, MOSI=board.MOSI)

# chip select
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# pull data from channel 7
chan = AnalogIn(mcp, MCP.P7)

class record:
    # general getlocation intended to create the starting location
    def record():
        x = ((3.3/1024)*chan.value);
        
