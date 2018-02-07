---
title: 手贱设置gnome-terminal之Profile Prefferences之后
date: 2018-02-07 22:25:30
tags: 杂合集
---

心血来潮，Ctrl+Alt+T打开terminal之后右键看见可以设置首选项，emmmm，作为好奇宝宝，有必要看看可以做什么设置。

一通风骚走位之后点击OK,看看效果如何，exit后流利的Ctrl+Alt+T，WTF，terminal一闪而逝，喵了个咪的，写错剧本了。

<!--more-->

寄出搜索引擎“how to reset terminal profile on ubuntu”,"terminal cannot open on ubuntu","where to find the profile prefferences config file of terminal on ubuntu",胡乱找了一圈，在一个犄角旮旯里找到了一句：

> dconf dump /org/gnome/terminal/legacy/profiles:/

![dconf dump示意图](http://p3sbcwagu.bkt.clouddn.com/dconf_dump.png)

当然我这里是已经恢复的结果，比如我当时手贱，将use-custom-command勾选了，并在custom-command中设置了一个可能与terminal有冲突的命令。

到了这一步，就可以手动修改了，比如我要把use-custom-command改为false，那么使用dconf write进行修改配置：

> dconf write /org/gnome/terminal/legacy/profiles:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/use-custom-command false

以上语法如下：
![dconf write命令帮助](http://p3sbcwagu.bkt.clouddn.com/image/png/dconf_write.png)

更多参考可见：

> dconf help

真是愉快的一天，好奇心害死喵。
