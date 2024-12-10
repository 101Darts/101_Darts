本项目是一个研究帮助老年人提高飞镖投掷水平的研究，包含四个文件和程序。


DartsStrategyForElderly_Papaer_V7.2.pdf 是研究论文。
DartStrategyForElederly_Slides_V5.6.pdf 是讲解的PowerPoint 文件。
bug_report.pdf 是一个关于R语言中二重积分的错误报告和初步的解决办法。

dartboard_config.xlsx 是飞镖盘的配置文件，下面的程序会读取这个配置文件。
cacu_one_target.R 是用R语言计算一个瞄准一个目标后落点的概率分布,计算中有时会异常退出。
cacu_one_robot.R 是用R语言计算瞄准飞镖盘上所有目标后落点的概率分布，计算中有时会异常退出。
r_functions.R  是支持文件，里面包含对发现bug的修正。
reproduce_error.R  是复现R语言二重积分bug的程序

cacu_one_target.py 是用Python语言的二重积分函数计算一个瞄准一个目标后落点的概率分布。
cacu_one_robot.py 是用R语言的二重积分函数计算依次瞄准飞镖盘上所有目标后落点的概率分布。


cacu_one_target_fast.py 是用Python语言的random()函数模拟计算一个瞄准一个目标后落点的概率分布。
cacu_one_robot_fast.py 是用R语言的random()函数模拟计算瞄准飞镖盘上所有目标后落点的概率分布。
xy2tag.py	根据坐标判断得分区域的程序。
trace_one_robot.py  求解最优投掷策略的程序。
node.py			一个动态规划的库，来支持求解最优策略。
