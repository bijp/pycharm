'''打开百度新歌榜， http://music.baidu.com/top/new

在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者

注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉


最终结果显示的结果如下：
我不能忘记你       :  林忆莲
等                :  严艺丹
飞天              :  云朵
粉墨              :  霍尊
春风十里不如你     : '''
from selenium import webdriver
import time
driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')
driver.maximize_window()
time.sleep(1)
driver.get('http://music.baidu.com/top/new')
#通过层级先去寻找新歌榜的歌曲，分三个层级，div-ul-li
div = driver.find_element_by_id("songListWrapper")
ul = div.find_element_by_tag_name("ul")
liList = ul.find_elements_by_tag_name('li')

for li in liList:
    #查找class="up"
    upTags = li.find_elements_by_class_name("up")
    #status=li.find_element_by_class_name('song-item').find_element_by_class_name("status").find_element_by_tag_name('i').get_attribute('class')
    if upTags:
        #class="song-title" 找到标题，通过a标签找到歌名，通过title标签名获取title元素，打印的文本值为空
        title = li.find_element_by_class_name("song-title")
        titleStr = title.find_element_by_tag_name("a").text
        ##class="author_list" ，通过a标签找到歌手，通过title标签名获取title元素，打印的文本值为空
        singer = li.find_element_by_class_name("author_list")
        # singerStr = title.find_element_by_tag_name("a").text
        singerStr=singer.get_attribute('title')
        #格式化歌名和歌手
        print('{:20s}:{}'.format(titleStr,singerStr))
driver.quit()
