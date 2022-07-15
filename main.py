#!/usr/bin/env python

''' This module used to plot PSD using obspy for BMKG Station. 
The module run on python 3.x, preferably python 3.6.'''

import obspy
from obspy import read, read_inventory
from obspy.io.xseed import Parser
from obspy.signal import PPSD
from obspy.imaging.cm import pqlx
import matplotlib.pyplot as plt

__author__ = 'Shandy Yogaswara'
__license__= None
__version__ = '26.10.2021'
__email__ = 'sh.yogaswara@gmail.com'
__status__ = 'Finished'




def main(STA_ID):
    '''This method will be used to read stream signal from STA_ID input,
    that user prepare the mseed data and generating channel that exist 
    in those data. For every channel, the code will try to get the trace
    and metadata from BMKG fdsnws, which is i believe is locked for now
    (2022), so use this method with salts and grains.

    Please refer to obspy documentation for more information and 
    if __name__ block for how to use'''

    st = read(f'{STA_ID}.mseed')
    STA_CH = []
    for i in range(len(st)):
        STA_CH.append(st[i].stats.channel)
    
    for ch in STA_CH:
        ch_trace = st.select(channel=ch)
        tr = ch_trace[0]
        STA_META = f'https://geof.bmkg.go.id/fdsnws/station/1/query?station={STA_ID}&level=response&nodata=404'
        inv = read_inventory(STA_META)
        ppsd = PPSD(tr.stats, metadata=inv)

        ppsd.add(st)
        print("number of psd segments:", len(ppsd.times_processed))
        ppsd.plot(cmap=pqlx)




if __name__ == '__main__':
    '''
    Change the STA_ID parameter value with station code, example
    is DSRI for Dabo Singkep Riau, Indonesia
    '''
    STA_ID = 'DSRI'
    main(STA_ID=STA_ID)

