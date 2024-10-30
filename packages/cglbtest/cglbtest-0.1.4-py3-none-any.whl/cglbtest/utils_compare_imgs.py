import cv2,numpy as np
class UtilsCompareImgs:
	def __init__(A,filpath_1,filpath_2):A.filpath_1=filpath_1;A.filpath_2=filpath_2
	def compare(A):
		B=False;C='';D=cv2.imread(A.filpath_1);E=cv2.imread(A.filpath_2);print(A.filpath_1);print(A.filpath_2)
		if D.shape!=E.shape:B=True;C='Different sizes'
		else:
			G=cv2.cvtColor(D,cv2.COLOR_BGR2GRAY);H=cv2.cvtColor(E,cv2.COLOR_BGR2GRAY);I=cv2.absdiff(G,H);F=np.count_nonzero(I)
			if F>0:B=True;C=f"detect {F} differences"
		return B,C