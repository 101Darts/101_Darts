This project investigates how to help elderly individuals improve their dart throwing skills. It consists of four documents and several programs.

* **DartsStrategyForElderly_Paper_V7.2.pdf:** This is the research paper.
* **DartStrategyForElderly_Slides_V5.6.pdf:** This is the PowerPoint presentation.
* **bug_report.pdf:** This document reports a bug encountered in the double integral function in R, and proposes a preliminary solution.
* **dartboard_config.xlsx:** This is the configuration file for the dartboard. The following programs will read this configuration file.

* **cacu_one_target.R:** This R program calculates the probability distribution of landing points after aiming at one target. The calculation may sometimes terminate abnormally.
* **cacu_one_robot.R:** This R program calculates the probability distribution of landing points after aiming at all targets on the dartboard. The calculation may sometimes terminate abnormally.
* **r_functions.R:** This is a supporting file that contains corrections for the discovered bug.
* **reproduce_error.R:** This program reproduces the double integral bug in R.

* **cacu_one_target.py:** This Python program calculates the probability distribution of landing points after aiming at one target using the double integral function.
* **cacu_one_robot.py:** This Python program calculates the probability distribution of landing points after sequentially aiming at all targets on the dartboard using the double integral function.
* **cacu_one_target_fast.py:** This Python program simulates the probability distribution of landing points after aiming at one target using the `random()` function.
* **cacu_one_robot_fast.py:** This Python program simulates the probability distribution of landing points after aiming at all targets on the dartboard using the `random()` function.
* **xy2tag.py:** This program determines the scoring area based on coordinates.
* **trace_one_robot.py:** This program finds the optimal throwing strategies for the elderly.
* **node.py:** This is a dynamic programming library that supports finding the optimal strategy.
