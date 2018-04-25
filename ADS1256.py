# This module just holds a convience function for calling the ads1256_read_diff program
# It expects to be run on a bash shell on a RPi
#
# Matt Ebert 04/2018

from subprocess import Popen, PIPE
import os.path


MAX_DATA_RATE = 30000  # SPS


def read_diff(channel, log2_avgs):
    if(channel >= 4 or channel < 0):
        raise KeyError
    if log2_avgs > 15:
        log2_avgs = 15
    script = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ads1256_read_diff')
    p = Popen(map(str, [script, channel, log2_avgs]), stdout=PIPE)
    output, err = p.communicate()
    output = output.strip()
    if p.returncode:
        print("Process exited on error with msg: `{}`".format(output))
        raise IOError
    return float(output)


if __name__ == "__main__":
    # run test
    channel = 0
    log2_avgs = 4  # 2**4 = 16 avgs
    try:
        volt = read_diff(channel, log2_avgs)
    except IOError:
        print("Error reading ADC")
    else:
        print("ADC channel: {}, voltage {} V".format(channel, volt))
