# 测试传递参数
library(pracma, warn.conflicts = FALSE)
library(readxl)
library(dplyr, warn.conflicts = FALSE)


#pracma是积分和数值计算的库，dplyr是处理数据的库，读写excel文件

arg <- commandArgs(T)
# 读取 Excel 文件
# 将 "your_excel_file.xlsx" 替换为你的 Excel 文件路径
config <- read_excel("dartboard_config.xlsx")

# 提取 "tag" 列的元素到列表中
tag_list <- config$tag
# 打印列表
#print(tag_list)

if( length(arg)!=3){
	cat("Argument: argv error!\n run as: test1.R 1.2 2.4 T20\n")
	quit('no')
	}
source("r_functions.R");


#e1,e2 就是sigma_x,sigma_y 

e1=as.numeric(arg[1])
e2=as.numeric(arg[2])
otag=arg[3]

u1  <- config %>%  filter(tag == otag) %>%  select(ux)
u2  <- config %>%  filter(tag == otag) %>%  select(uy)
u1=as.numeric(u1)
u2=as.numeric(u2)

#过滤空元素
tag_list <- tag_list[!sapply(tag_list, function(x) is.null(x) || x == "")]

start_time <- Sys.time()
pb_missed=1;			#用以记录没有命中的概率

#for 循环遍历
for (atag in tag_list) {
	r1 <- config %>%  filter(tag == atag) %>%  select(floor)
	r2 <- config %>%  filter(tag == atag) %>%  select(ceiling)
	d1 <- config %>%  filter(tag == atag) %>%  select(angle1)
	d2 <- config %>%  filter(tag == atag) %>%  select(angle2)	  	
	score <- config %>%  filter(tag == atag) %>%  select(score)	  

	r1=as.numeric(r1)
	r2=as.numeric(r2)
	d1=as.numeric(d1)
	d2=as.numeric(d2)
	score=as.numeric(score)
		
#	cat(sprintf("#AIM %s (%.3f, %.3f) => OBJ %s dg(%.3f,%.3f) Radius(%.3f, %.3f) \n",otag,u1,u2,atag,d1,d2,r1,r2));
#	val=new_integral2(fp,d1,d2,r1,r2);
	val=integral2(fp,d1,d2,r1,r2);
	pb=val[['Q']];
	escore=pb*score;
  	if(pb>0.0001){
  		cat(sprintf("%s\t%s\t%.3f\t%d\t%.4f\n",otag,atag,pb,score,escore));
  		pb_missed=pb_missed-pb
  		}
  	}
cat(sprintf("%s\t%s\t%.3f\t%d\t%.4f\n",otag,"MISSED",pb_missed,0,0));
end_time <- Sys.time()
run_time = end_time - start_time
message(sprintf("time taken：%.3f seconds!",run_time))
