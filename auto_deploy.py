#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
import os

PostsDir = "./source/_posts"
Contents = "- [{0}](/source/_posts/{1}.md)\n"
README = 'README.md'

AlreadyExists = [line for line in open(README)]

# 事实上，list中任何一个元素包含了目标值，都返回True
def isInList(lst, tar):
    for it in lst:
        print(it)
        if tar in it:
            return True
    return False

lst = os.listdir(PostsDir)
MyPosts = []
for it in lst:
    MyPosts.append(it[:-3])  # 去除最后'.md'格式的文件名

Need2Add = [it for it in MyPosts if not isInList(AlreadyExists, it)]

if len(Need2Add) > 0:
    with open(README, 'a+') as f:
        for it in Need2Add:
            f.write(Contents.format(it,it))

    os.system('cp README.md public/')
    os.system('hexo clean')
    os.system('hexo g')
    os.system('hexo d')

    log = 'add a post'
    os.system('git pull')
    os.system('git add .')
    os.system("git commit -m 'add a post'")
    os.system('git push origin hexo')
