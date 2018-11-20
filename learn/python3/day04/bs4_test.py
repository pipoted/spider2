#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup


html = '''

    	<a name="a" id="a"></a>
    	<div class="left wcont_b box">
		    <div class="blueline"><div class="butzwss"></div></div>
		    <form id="searchform" class="buts1">
		    	<div id="searchrow1">
		    		<div id="search1"><input id="search2" name="keywords" t="请输入关键词" value="" class="left" style="color: rgb(136, 136, 136);"><input class="left" id="search3" type="submit" value=""><div class="clr"></div></div>
		    		<input type="hidden" name="lid" value="0">
		    		<input type="hidden" name="tid" value="87">
		    	</div>
		    	<div id="searchrow2">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9 itemnone" id="additems">
		    			<a href="position.php?keywords=&amp;tid=87" class="item active"><span><font>全部</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2218"><span><font>深圳</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2156"><span><font>北京</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2175"><span><font>上海</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2196"><span><font>广州</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2268"><span><font>成都</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2426"><span><font>昆明</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2459"><span><font>中国香港</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2355"><span><font>武汉</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;tid=87&amp;lid=2252"><span><font>杭州</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=33"><span><font>美国</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2226"><span><font>重庆</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=32"><span><font>韩国</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=62"><span><font>欧洲</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=60"><span><font>马来西亚</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=90"><span><font>荷兰</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=66"><span><font>印度尼西亚</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=59"><span><font>日本</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2436"><span><font>贵阳</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2442"><span><font>呼和浩特</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=95"><span><font>雄安新区</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2393"><span><font>太原</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2346"><span><font>郑州</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2314"><span><font>南宁</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2439"><span><font>兰州</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2320"><span><font>合肥</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2407"><span><font>大连</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2453"><span><font>乌鲁木齐</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2294"><span><font>青岛</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2406"><span><font>沈阳</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=2381"><span><font>西安</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=&amp;tid=87&amp;lid=45"><span><font>泰国</font></span></a>
		    					    		</div>
							    		<div class="left"><a href="javascript:;" class="more2">更多</a></div>
							    		<div class="clr"></div>
		    	</div>
		    	<div id="searchrow3">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9">
		    			<a href="position.php?keywords=&amp;lid=0" class="item"><span><font>全部</font></span></a>
		    					    				<a class="item active" href="position.php?keywords=&amp;lid=0&amp;tid=87"><span><font>技术类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=82"><span><font>产品/项目类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=83"><span><font>市场类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=84"><span><font>职能类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=81"><span><font>设计类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=85"><span><font>内容编辑类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=86"><span><font>客户服务类</font></span></a>
		    					    		</div>
		    		<div class="clr"></div>
		    	</div>
		    </form>
		    <table class="tablelist" cellspacing="0" cellpadding="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45638&amp;keywords=&amp;tid=87&amp;lid=0">WXG08-121 微信推荐数据挖掘工程师PW（广州）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45637&amp;keywords=&amp;tid=87&amp;lid=0">WXG08-121 微信机器学习算法工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45639&amp;keywords=&amp;tid=87&amp;lid=0">WXG08-122 微信搜索算法工程师PW（广州）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45641&amp;keywords=&amp;tid=87&amp;lid=0">TEG05-高级网络安全工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45619&amp;keywords=&amp;tid=87&amp;lid=0">18428-金融云后台开发</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45625&amp;keywords=&amp;tid=87&amp;lid=0">GY0-VOOV Andriod开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45626&amp;keywords=&amp;tid=87&amp;lid=0">29303-大数据及人工智能高级研究员（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45627&amp;keywords=&amp;tid=87&amp;lid=0">大数据及人工智能组长/总监（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45617&amp;keywords=&amp;tid=87&amp;lid=0">25924-营销平台测试工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45618&amp;keywords=&amp;tid=87&amp;lid=0">25924-运营开发工程师（上海）</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>上海</td>
					<td>2018-11-13</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1393</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1390#a">140</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody></table>
		</div>
		<div class="right wcont_s box">
		    <div class="blueline"><div class="butcjwt"></div></div>
		    <div class="module_faqs square"><a href="faq.php?id=5" title="如何应聘腾讯公司的职位？">如何应聘腾讯公司的职位？</a><a href="faq.php?id=3" title="应届生如何应聘？">应届生如何应聘？</a><a href="faq.php?id=19" title="腾讯应聘流程是什么？">腾讯应聘流程是什么？</a><a href="faq.php?id=20" title="我注册了简历，但为什么没有人联系我？">我注册了简历，但为什么没...</a><a href="faq.php?id=22" title="我忘记密码了，怎么办？">我忘记密码了，怎么办？</a><a href="faq.php?id=23" title="如何进行简历修改？">如何进行简历修改？</a></div>		</div>
		<div class="clr"></div>
'''


# print(bs.prettify())


soup = BeautifulSoup(html, 'lxml')


# 1. 获取所有的tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     # print(tr)
#     # print('^' * 30)
#     print(type(tr))

# 2. 获取第二个tr标签
# tr = soup.find_all('tr', limit=2)[1]
# print(tr)

# 3. 获取所有class等于even的标签
# trs = soup.find_all('tr', attrs = {'class': 'even'})
# # trs = soup.find_all('tr', class_ = 'even')
# for tr in trs:
#     print(tr)
#     print('*' * 100)
    
# 4. 将所有id，class都等于test的a标签提取出来
# a_list = soup.find_all('a', id='test', class_='test')
# for a in a_list:
#     print(a)

# 5. 获取所有a标签href属性

    # 通过下标的方式
    # href = a['href']
    # print(href)
    # href = a.attrs['href']
    # print(href)


# 6.获取所有的职位信息（纯文本）
# trs = soup.find_all('tr')[1:]
# movies = []
# try:
#     for tr in trs:
        # tds = tr.find_all('td')
        # title = tds[0].string
        # category = tds[1].string
        # nums = tds[2].string
        # city = tds[3].string
        # pubtime = tds[4].string

        # movie = {
        #     'title': title,
        #     'category': category,
        #     'nums': nums,
        #     'city': city,
        #     'pubtime': pubtime,
        # }

        # movies.append(movie)

        # infos = list(tr.stripped_strings)
        # movie = {
        #     'title': infos[0],
        #     'category': infos[1],
        #     'nums': infos[2],
        #     'city': infos[3],
        #     'pubtime': infos[4],
        # }
        # movies.append(movie)

# except Exception:
    # pass

# print(movies)


# 使用css选择器
soup = BeautifulSoup(html, 'lxml')
print(type(soup))
# 1. 获取所有的tr标签
# trs = soup.select('tr')
# for tr in trs:
#     print(type(tr))
#     print('-' * 50)

# 2. 获取第二个tr标签
# tr = soup.select('tr')[1]
# print(tr)

# 3. 获取所有class等于even的标签
# trs = soup.select('tr[class="even"]')
# for tr in trs:
#     print(tr)
#     print('_' * 50)

# 4. 获取所有a标签href属性
# a_list = soup.select('a')
# for a in a_list:
#     href = a['href']
#     print(href)

# 5. 获取所有的职位信息
trs = soup.select('tr')
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)


