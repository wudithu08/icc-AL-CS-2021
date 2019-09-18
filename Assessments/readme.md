# project 190916: file processing practice project (40 minutes)
##	 1. create a new file named "AS_CS_opt2_gradebook.txt", which includes:

	###	1.   12  rows, each represents a student in our class
	###	2.  5 columns: 
		*	1. column #1  -- English Name,
		*	2. column #2 -- Chinese last name,
		*	3. column #3 -- Math grade (0-100), average:90,   
		*	4. column #4 -- CS grade(0-100), average: 95
		*	5. column #5 -- Phy grade(0-100), average: 88
##	 2. insert a new column "ID" to the left of column#1 -- English name,  the ID is from 1 to 12, represent the unique number for each student
##	 3. for each student calculate the average score for Math, CS and Phy.  Add the average result at the right most column. 
##	 4. search for the student with English name "Daniel", modify his math score to  1.1*original score.
##  5. search for the student with the lowest Phy score, delete this student and save the rest as a new file "new-gradebook.txt"

submit your code here: Daniel, [:trollface:Harry](https://github.com/haoyuF996/0916Homework), [Nico](https://github.com/jby0107/Homework/tree/assessment-9.16), Jack, James, Brian, Tim, [Lisa](https://github.com/ZeroxAlone/190916), [Cathy](https://github.com/CathyYang1118/9.16-test), [Julian](https://github.com/GodspeedyJulian/9.18), Shirley, [Andy](https://github.com/Loskiz/AS_CS_Homework/tree/master/2019-09-16)




# project 2019-09-12
## 1:file processing -- extract information from a text file
   
   * use "qbdata.txt" file, read the file, for each line( corresponds to each person) get the rating score (the last field) only. 
   * e.g. "Colt McCoy has a rating of 74.5". 
   * Select all the ones with a rating >= 60, then output the processed info on the screen and save them in a new text file. 
    
submit your code:  [Daniel](https://github.com/Yuudachi530/assignment_19-9-14_q1), [:trollface:Harry](https://github.com/haoyuF996/0911Homework-1), [Nico](https://github.com/jby0107/Homework/tree/assessment-9.12/Task1), [Jack](https://github.com/jyd1222/Jack-s-homework/tree/Daily-HK), [James](https://github.com/JamessssLiu/project-and-work-of-ICC-AL-CS-course-James-Liu/tree/master/exercises/File%20processing), [Brian](https://github.com/BrianShan974/Hello-World/tree/assessment), Tim, [Lisa](https://github.com/ZeroxAlone/190912), [Cathy](https://github.com/CathyYang1118/HW), [Julian](https://github.com/GodspeedyJulian/9.14/tree/master/qbdata), [Shirley](https://github.com/ShirleyAiko/S2/tree/%23Week2), [Andy](https://github.com/Loskiz/AS_CS_Homework/tree/master/2019-9-12)

## 2: 词频统计 --  哈姆莱特
统计所有出现的单词和出现的频率，结果输出到一个新的文件中。

参考：
https://codeleading.com/article/90751228040/

https://codeleading.com/article/7665136841/

submit your code: Daniel, [:trollface:Harry](https://github.com/haoyuF996/0911Homework-2), [Nico](https://github.com/jby0107/Homework/tree/assessment-9.12/Task2), [Jack](https://github.com/jyd1222/Jack-s-homework/tree/Daily-HK), [James](https://github.com/JamessssLiu/project-and-work-of-ICC-AL-CS-course-James-Liu/tree/master/word%20frequency%20count), [Brian](https://github.com/BrianShan974/Hello-World/tree/assessment), Tim, [Lisa](https://github.com/ZeroxAlone/190912), [Cathy](https://github.com/CathyYang1118/HW), [Julian](https://github.com/GodspeedyJulian/9.14/tree/master/hamlet), [Shirley](https://github.com/ShirleyAiko/S2/tree/%23Week2), [Andy](https://github.com/Loskiz/AS_CS_Homework/tree/master/2019-9-12)

## 3：词频统计 -- 三国演义
统计三国演义中出场人物的出场频率。

[visualization]

create word cloud result for the visualization:

https://amueller.github.io/word_cloud/index.html 

reference code:

import wordcloud              

text = open("AI.txt").read()    #读取整个文件的内容为一个字符串text
wc = wordcloud.WordCloud()      
wc.generate(text)               #生成词云图
wc.to_file("AI.png")            #将词云图保存在该py文件所在的路径下

submit your code: Daniel, [:trollface:Harry](https://github.com/haoyuF996/0911Homework-3), [Nico](https://github.com/jby0107/Homework/tree/assessment-9.12/Task3), [Jack](https://github.com/jyd1222/Jack-s-homework/tree/Daily-HK), James, [Brian](https://github.com/BrianShan974/Hello-World/tree/assessment), Tim, [Lisa](https://github.com/ZeroxAlone/190912), [Cathy](https://github.com/CathyYang1118/HW), [Julian](https://github.com/GodspeedyJulian/9.14/tree/master/三国演义), Shirley, [Andy](https://github.com/Loskiz/AS_CS_Homework/tree/master/2019-9-12)

