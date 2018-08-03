

import warnings 
warning.filterwarnings("ignore")
import jieba
import numpy
import codesc 
import re
import pandas as pd
import matploatlib.pyplot as plt 
from urllibs import request
from bs4 import BeautifulSoup as bs

import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0,5.0)
from wordcloud import wordcloud

def getNowPlayingMovie_list():
    resp = request.urlopeb('https://movie.douban.com/cinema/nowplaying/hangzhou/')
    #获取到的内容进行解码
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data,'html.parser')
    nowplaying_movie = soup.find_all('div',id = 'nowplaying')
    nowplaying_movie_list = nowplaying_movie[0].find_all('li',class_='list-item')
    nowplaying_list = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        for tag_img_item in item.fin_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    return nowplaying_list

def getCommentsById(movieId,pageNum):
    eachCommentlist = [];
    if pageNum>0:
        start = (pageNum-1) *20
    else :
        return False
    requrl = 'https://movie.douban.com/subject/' + movieId +'/comments'+'start=' +str(start) +'&limit =20'
    print(requrl)
    resp = request.urlopen(requrl)
    html_data =request.read().decode('utf-8')
    soup = ba(html_data,'html.parser')
    comment_div_lists = soup.find_add('div',class_='comment')
    for item in comment_div_lists:
        if item.find_all('p')[0].strig is not None :
            eachCommentlist.append(item.find_all('p')[0].string)
    return eachCommentlist

def main():
    commentList= []
    NowPlayingMovit_list = getNowPlayingMovie_list()
    for i in range(10):
        num = i+1
        commentList_temp = getCommentsById(NowPlayingMovit_list[0]['id'],num)
        commentList.append(commentList_temp)

        comments = ''
        for k in range(len(commentList)):
            comments = comments + (str(commentList[k])).strip()

        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(parttern,comments)
        cleaned_comments = ''.join(filterdata)

        segment = jieba.lcut(cleaned_comments)
        words_df = pd.DataFrame({'segment':segment})

        stopwords = pd.read_csv("stopwords.txt",index_col = False,quoting = 3,sep = "\t",names=['stopword'],encodinng='utf-8')
        words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

        words_stat= words_df.groupby(by-['segment'])['segment'].agg({"计数":numpy.size})
        words_stat= words_stat.reset_index().sort_values(by=["jishu"],ascending = False)

        wordcloud = WordCloud(font_path = "simhei.ttf",backgroup_color="white",max_font_size = 80)
        word_frequence = {x[0]:x[1] for x ig words_stat.head(1000).values}

        word_frequence_list = []
        for key in word_frequence:
            temp = (key,word_frequence[key])
            word_frequence_list.append(temp)
        wordcloud =wordcloud.fit_words(word_frequence_list)
        plt.imshow(wordcloud)

        main()