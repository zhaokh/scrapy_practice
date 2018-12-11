由于scrapy安装在Acaconda3中，运行scrapy命令要在 Acaconda Promp中
1. 运行 scrapy startproject jd   当前目录下生成名为jd的scrapy爬虫工程，其中
    spiders文件夹就是用来存放爬虫文件
    settings文件可以设置User-Agent，IP以及爬取时间等等
    items用来编写字段的，类似数据库的字段
    pipelines则是处理爬取好的文件的
2. 进入spiders文件夹，开始用命令创建爬虫文件，运行scrapy genspider jd "爬取网页的url"，来生成爬虫文件jd.py:
    name不要改，parse函数也不要改，不然报错。在parse里面写解析规则即可
3. 运行爬虫文件：
    运行爬虫文件scrapy crawl jd


XPath更适合网页抓取，学习XPath

Selenium （浏览器自动化测试框架）

学习 scrapy框架
http://www.cnblogs.com/wuxl360/p/5567631.html  

Scrapy分布式爬虫之ES搜索引擎网站
分享网盘地址——https://pan.baidu.com/s/1htA3zX6 密码: ebwm
备用地址（腾讯微云）：http://url.cn/51n4soD 密码：SyRADx

scrapy示例地址：https://github.com/scrapy/quotesbot

