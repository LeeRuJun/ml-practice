# encoding=utf-8
import jieba

seg_list = jieba.cut("我来到上海东方明珠", cut_all=False)
print("Full Mode:" + "/".join(seg_list))