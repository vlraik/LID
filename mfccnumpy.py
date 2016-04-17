from features import mfcc
import scipy.io.wavfile as wav
import numpy as np
nparr=np.array([])
for i in range(1,100):
	if i<10:
		fname = "0" + str(i)+"kal.wav"
	else:
		fname = str(i) +"kal.wav"
	(rate,sig) = wav.read(fname)
	mfcc_feat = mfcc(sig,rate)
	nparr = np.append(nparr,mfcc_feat)
print nparr.shape
arr2=nparr.reshape(99,9,13)
print arr2
np.savetxt("01kal.csv",arr2,delimiter=",")