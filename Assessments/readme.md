# project 2019-09-12
## 1:file processing -- extract information from a text file
   
   * use "qbdata.txt" file, read the file, for each line( corresponds to each person) get the rating score (the last field) only. 
   * e.g. "Colt McCoy has a rating of 74.5". 
   * Select all the ones with a rating >= 60, then output the processed info on the screen and save them in a new text file. 
    
submit your code:  Daniel, Harry, Nico, [Jack](https://github.com/jyd1222/Jack-s-homework/tree/Daily-HK), James, Brian, Tim, Lisa, Cathy, Julian, Shirley, Andy

## 2: 词频统计 --  哈姆莱特
统计所有出现的单词和出现的频率，结果输出到一个新的文件中。

参考：
https://codeleading.com/article/90751228040/

https://codeleading.com/article/7665136841/

submit your code: Daniel, Harry, Nico, [Jack](https://github.com/jyd1222/Jack-s-homework/tree/Daily-HK), James, Brian, Tim, Lisa, Cathy, Julian, Shirley, Andy

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

submit your code: Daniel, Harry, Nico, [Jack](https://github.com/jyd1222/Jack-s-homework/tree/Daily-HK), James, Brian, Tim, Lisa, Cathy, Julian, Shirley, Andy

