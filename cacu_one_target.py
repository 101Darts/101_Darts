import scipy.integrate as integrate				#求积分需要的库
import numpy as np												#求极坐标表达式需要
import time				#获得程序运行时间
import pandas as pd				#读取和访问excel中数据
import sys				#需要用到标准错误输出，读入命令行参数
import re					#用正则表达式 regular expression 判断输入的参数是合法

# 读取飞镖盘配置 Excel 文件
df = pd.read_excel('dartboard_config.xlsx',sheet_name='main')
# 过滤出 tag 列中不为空的元素
tag_list = df['tag'].dropna().tolist()


#定义需要用到的变量,一个水平是(2.0,2.2)的人，瞄准T19投掷，落在不同区域的结果,再程序执行过程中会动态修改这些变量
sigma_x=2.2
sigma_y=2.2
u_x=-3.55
u_y=-10.94

#定义一个函数is_number，判断一个字符串是不是合法的数字类型
def is_number(string):
	pattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$')
	return bool(pattern.match(string))

# 定义极坐标下的二维正态分布联合概率密度函数,ploar_noral_pdf, 输入两个参数是radius和角度因为要计算二重积分，极坐标需要补一个r
def polar_normal_pdf(theta,r):
	coeff = 1 / (2 * np.pi * sigma_x * sigma_y)
	cos_theta = np.cos(theta)
	sin_theta = np.sin(theta)
	exp_part = np.exp(-((r * cos_theta - u_x)**2) / (2 * sigma_x**2) - ((r * sin_theta - u_y)**2) / (2 * sigma_y**2))
	rr= coeff * exp_part * r 				#此处补了一个r
	return rr


#计算前的数据检查1：判读命令行是否有三个参数，否则打印使用方法并退出
argc=len(sys.argv)
if(argc!=4):
	sys.stderr.write("usage : normal_distr.py 1.2 1.2 T20 \n");
	exit();

#计算前的数据检查2：读取命令行后的参数，并判读是否合法，如不合法就退出
if( is_number(sys.argv[1]) and is_number(sys.argv[2]) ):
	s1 = float(sys.argv[1])
	s2 = float(sys.argv[2])
	aim =sys.argv[3]
else:	
	sys.stderr.write("usage : normal_distr.py 1.2 1.2 T20 \n")
	exit()

#计算前的数据检查3： 判断输入的目标是否合法
if not (aim in tag_list):
	sys.stderr.write("usage : normal_distr.py 1.2 1.2 T20 \n")
	sys.stderr.write("%s 不是合法的目标位置标签！"%(aim));
	exit()

#记录开始计算时间
start_time = time.time()

pb_missed=1;			#用以记录没有命中的概率
for hit in tag_list:
	u_x=df[df['tag'] == aim]['ux'].values[0]
	u_y=df[df['tag'] == aim]['uy'].values[0]
	sigma_x=s1
	sigma_y=s2
	b1=df[df['tag'] == hit]['floor'].values[0]
	b2=df[df['tag'] == hit]['ceiling'].values[0]
	d1=df[df['tag'] == hit]['angle1'].values[0]
	d2=df[df['tag'] == hit]['angle2'].values[0]
	score=df[df['tag'] == hit]['score'].values[0]
	pb, error = integrate.dblquad(polar_normal_pdf, b1,b2,d1,d2)			# 计算二重积分
	escore=score*pb
	if(pb>0.0001):
		print("%s\t%s\t%.3f\t%d\t%.4f"%(aim,hit,pb,score,escore))		
#		print("%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f"%(u_x,u_y,b1,b2,d1,d2))
		pb_missed=pb_missed-pb
print("%s\t%s\t%.3f\t%d\t%.4f"%(aim,"MISSED",pb_missed,0,0))		

end_time = time.time()
run_time = end_time - start_time
print("time taken：%.3f seconds!"%(run_time), file=sys.stderr)