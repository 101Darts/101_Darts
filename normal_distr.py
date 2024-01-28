import numpy as np
import operator
import sys
import re
import time
#import random
from xy2tag import xy2tag

rsize=20000						#bootstrap number
uid="NULL"
def is_number(string):
    pattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$')
    return bool(pattern.match(string))

if( is_number(sys.argv[1]) and is_number(sys.argv[2]) ):
	scale1 = float(sys.argv[1])
	scale2 = float(sys.argv[2])
	uid=sys.argv[3]
else:	
	sys.stderr.write("usage : normal_distr.py 1.2 1.2\n");
	exit();

#每个区块的中心位置坐标，作为二维正态分布X,Y方向的均值u的取值，模拟瞄准不同的位置
tag_xy={				
'A20':(0.00,7.50,20),'T20':(0.00,11.50,60),'B20':(0.00,15.00,20),'D20':(0.00,18.50,40),
'A5':(-2.32,7.13,5),'T5':(-3.55,10.94,15),'B5':(-4.64,14.27,5),'D5':(-5.72,17.59,10),
'A12':(-4.41,6.07,12),'T12':(-6.76,9.30,36),'B12':(-8.82,12.14,12),'D12':(-10.87,14.97,24),
'A9':(-6.07,4.41,9),'T9':(-9.30,6.76,27),'B9':(-12.14,8.82,9),'D9':(-14.97,10.87,18),
'A14':(-7.13,2.32,14),'T14':(-10.94,3.55,42),'B14':(-14.27,4.64,14),'D14':(-17.59,5.72,28),
'A11':(-7.50,0.00,11),'T11':(-11.50,0.00,33),'B11':(-15.00,0.00,11),'D11':(-18.50,0.00,22),
'A8':(-7.13,-2.32,8),'T8':(-10.94,-3.55,24),'B8':(-14.27,-4.64,8),'D8':(-17.59,-5.72,16),
'A16':(-6.07,-4.41,16),'T16':(-9.30,-6.76,48),'B16':(-12.14,-8.82,16),'D16':(-14.97,-10.87,32),
'A7':(-4.41,-6.07,7),'T7':(-6.76,-9.30,21),'B7':(-8.82,-12.14,7),'D7':(-10.87,-14.97,14),
'A19':(-2.32,-7.13,19),'T19':(-3.55,-10.94,57),'B19':(-4.64,-14.27,19),'D19':(-5.72,-17.59,38),
'A3':(-0.00,-7.50,3),'T3':(-0.00,-11.50,9),'B3':(-0.00,-15.00,3),'D3':(-0.00,-18.50,6),
'A17':(2.32,-7.13,17),'T17':(3.55,-10.94,51),'B17':(4.64,-14.27,17),'D17':(5.72,-17.59,34),
'A2':(4.41,-6.07,2),'T2':(6.76,-9.30,6),'B2':(8.82,-12.14,2),'D2':(10.87,-14.97,4),
'A15':(6.07,-4.41,15),'T15':(9.30,-6.76,45),'B15':(12.14,-8.82,15),'D15':(14.97,-10.87,30),
'A10':(7.13,-2.32,10),'T10':(10.94,-3.55,30),'B10':(14.27,-4.64,10),'D10':(17.59,-5.72,20),
'A6':(7.50,0.00,6),'T6':(11.50,0.00,18),'B6':(15.00,0.00,6),'D6':(18.50,0.00,12),
'A13':(7.13,2.32,13),'T13':(10.94,3.55,39),'B13':(14.27,4.64,13),'D13':(17.59,5.72,26),
'A4':(6.07,4.41,4),'T4':(9.30,6.76,12),'B4':(12.14,8.82,4),'D4':(14.97,10.87,8),
'A18':(4.41,6.07,18),'T18':(6.76,9.30,54),'B18':(8.82,12.14,18),'D18':(10.87,14.97,36),
'A1':(2.32,7.13,1),'T1':(3.55,10.94,3),'B1':(4.64,14.27,1),'D1':(5.72,17.59,2),
'DBE':(0.00,0.00,50)
}

start_time = time.time()

xy2tag_instance = xy2tag()
hit_dict = {}					#存储每个命中靶位 出现的次数
ln=0									#记录概率大于0的条目数目
for tag in tag_xy:
	u1=tag_xy[tag][0];
	u2=tag_xy[tag][1];
#	print(s1," ",s2," ",tag)
	xx = np.random.normal(loc = u1, scale= scale1 ,size = rsize)    #生成随机正态分布数。
	yy = np.random.normal(loc = u2 , scale= scale2 ,size = rsize)
	hit_dict.clear()					#清空
	i=0
	while(i<rsize):
		hit=xy2tag_instance.get_score(xx[i],yy[i])
		if(hit in hit_dict):
			hit_dict[hit]+=1
		else:
			hit_dict[hit]=1	
		i+=1
		
	sorted_tags=sorted(hit_dict.items(),key=operator.itemgetter(1),reverse=True)
	for hit in sorted_tags:
		val=hit[1]/rsize
		if(hit[0]=="MISSED"):
			score=0;
		elif(hit[0]=="BE"):
			score=25;			
		else:
			score=tag_xy[hit[0]][2];	
		escore=float(score)*val;	
		if(val>0.0001):
			print("%s\t%.2f\t%.2f\t%s\t%s\t%.4f\t%s\t%.4f"%(uid,scale1,scale2,tag,hit[0],val,score,escore));  	
			ln+=1;
			
# 记录运行时间
end_time = time.time()
run_time = end_time - start_time
print("%d lines, time taken：%.3f seconds!"%(ln,run_time), file=sys.stderr)