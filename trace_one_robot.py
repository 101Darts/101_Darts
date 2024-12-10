import pandas as pd
import sqlite3
import sys
import time
from node import node			#the node.py is a class file created by 101dart club

max_score=501		#max_score,设定为501的比赛
s1=0.9			
s2=1.4


#建立数据库连接，数据库是去年（2023年）CTB项目中生成的飞镖投掷数据库
conn = sqlite3.connect('101darts.sldb')

#编写SQL查询语句
my_query="select uid,s1,s2,aim,hit,pb,score,escore from robots where s1='{}' and s2='{}' order by aim,hit".format(s1,s2)

#执行查询，并将查询的结果存储到pandas里面的dataframe中
df = pd.read_sql_query(my_query, conn)


#全局hash,存储每个得分点node的最佳aim,minimum_step
mstep_hash={}
baim_hash={}

start_time = time.time()
for i in range(2,max_score+1):
	snode=node(i)
	snode.load_main_table(df)
	snode.load_previous_steps(mstep_hash)
	snode.select_aim()
	baim_hash[i]=snode.best_aim
	mstep_hash[i]=snode.minimum_step
	#print("NODE%d , best aim %s , minumu step %.4f"%(snode.left_score,snode.best_aim,snode.minimum_step),file=sys.stderr)
	print("%d\t%s\t%.4f"%(snode.left_score,snode.best_aim,snode.minimum_step))

end_time = time.time()
run_time = end_time - start_time
print("time taken：%.3f seconds!"%(run_time), file=sys.stderr)


