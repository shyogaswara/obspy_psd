# obspy_psd

This module used to plot PSD using obspy for BMKG Station.
The module run on python 3.x, preferably python 3.6.

This method will be used to read stream signal from STA_ID input,
that user prepare the mseed data and generating channel that exist 
in those data. For every channel, the code will try to get the trace
and metadata from BMKG fdsnws, which is i believe is locked for now
(2022), so use this method with salts and grains.

Please refer to obspy documentation for more information and 
if name block for how to use
