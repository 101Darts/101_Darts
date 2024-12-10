import pandas as pd

class node:
	left_score=0
	best_aim='NULL'
	minimum_step=9999999999
	main_table=pd.DataFrame()
	#result_table=pd.DataFrame()

	#构造函数，初始化的时候，需要输入score，还剩多少分完成比赛
	def __init__(self, score):
		self.left_score=score

	def get_best_aim(self):
		return (self.best_aim, self.minimum_step)


	#将数据库robots表中的数据加载到main table, 并增加left_score这一列，对每次投掷的情况计算还剩多少分
	def load_main_table(self,df_data):
		self.main_table=df_data.copy(deep=True)				#此处注意，用的是深度copy,即不是只拷贝指针或是引用，这样对main table的修改不会改变原来的数据
		self.main_table['left_score']=self.left_score-self.main_table['score']
		#过滤数据，先挑出left_score<0 和只剩下1分的行, 按照飞镖规则，重新投掷
		cond=(self.main_table['left_score'] < 0 ) | (self.main_table['left_score'] == 1)		#过滤条件
		self.main_table.loc[cond,'left_score']=self.left_score
		#过滤数据，再挑出left_score==0，且命中的不是D10这种double ending的行	
		cond=(self.main_table['left_score'] == 0 ) & (~self.main_table['hit'].str.contains('D'))		#过滤条件
		self.main_table.loc[cond,'left_score']=self.left_score				#remove this this if you want to deduce the game difficulties

	#将之前计算的每个分值的最小步数加载到main table中
	def load_previous_steps(self,pstep_hash):
		self.main_table['p_step_num']=-1.0
		for kk,vv in pstep_hash.items():
			cond=self.main_table['left_score'] == kk
			self.main_table.loc[cond,'p_step_num']=vv	

	#在当前分值情况下，计算没给目标位置的步数期望，在还剩2分时候，不用考虑加载之前的数据，需要把p_0,p_c, cc这三个值算出来，看CTB论文		
	def cacu_one_aim(self,atag):
		cond=self.main_table['aim']==atag
		df_tmp=self.main_table.loc[cond]
		
		# 计算p_0,筛选条件：表中left_score=0的
		condition = df_tmp['left_score'] == 0
		p_0 = df_tmp[condition]['pb'].sum()
		
		# 计算p_c,筛选条件：表中left_score= self.left_score的，即无效投掷
		condition = df_tmp['left_score'] == self.left_score
		p_c = df_tmp[condition]['pb'].sum()
		if(p_c>1):			#处理数据表中四舍五入错误，导致概率和>1
			p_c=1
		
		exp_num=9999999999			#期望次数，先设定一个非常大的数
		#下面是计算exp_num的方法，具体推导和公式看CTB论文
		if(self.left_score==2):
			exp_num=1/(p_0+0.0000001)
		else:
			# 计算cc, 筛选条件：表中p_step_num>0
			condition = df_tmp['p_step_num'] >0
			cc = (df_tmp[condition]['pb']*df_tmp[condition]['p_step_num']).sum()
			exp_num=(1+cc)/(1-p_c+0.00001)
			#print("AIM %s\t,p0:%.4f\t,p_c:%.4f\t, cc:%.4f,\texp_num: %.4f"%(atag,p_0,p_c,cc,exp_num))
		return exp_num

	#对所有目标找出最小的步数，即使最佳的目标
	def select_aim(self):
		aims=self.main_table['aim'].unique()
		for one in aims:
			exp_num=self.cacu_one_aim(one)
			if(exp_num<self.minimum_step):
				self.minimum_step=exp_num
				self.best_aim=one
		return 1




