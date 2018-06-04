import  urllib
import  urllib.request
import  re
import  sys
#__author__ = 'rj_li'

class QSBK:
    #初始化方法
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers =  { 'User-Agent' : self.user_agent }
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        self.enable = False

    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib.request.Request(url,headers = self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return  pageCode
        except urllib.request.URLError as e :
            # httpError
            if hasattr(e,'code'):
                print(e.code)
            # urlError
            elif hasattr(e,'reason'):
                print(e.reason)

    #获取页面，不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode :
            print("页面加载失败")
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
                             'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',
                             re.S)
        items = re.findall(pattern, pageCode)
        # 存储每页的段子们
        pageStories = []
        for item in items:
             pageStories.append([item[0].strip(), item[2].strip(), item[4].strip()])
        return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories)< 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    #每次敲回车打印输入一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input_tmp = input("请输入:")
            self.loadPage()
            if input_tmp == 'Q':
                self.enable = False
                return
            print(story[0],story[2],story[4])

    #开始方法
    def start(self):
        print("正在读取糗事百科，按回车查看新段子，Q退出")
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)> 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()