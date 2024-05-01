[En](/README.md) |[Ch](/README-CH.md)
# 简介

这是一个简单的小说爬虫项目。

本项目旨在通过爬取小说网站的小说内容来进行训练。通过运行本项目，可以将小说下载到相应的txt文件中。由于本项目仅作为练手项目，因此具体的网站和保存小说的txt文件信息等内容需要手动修改。当然，实现这些修改其实很简单，但由于不同网站的HTML结构不同，因此此爬虫仅限于对"https://www.shuxiang8.cc" 网站小说内容的爬取。

爬取小说示例在项目的[”这游戏太真实了.txt“](/这游戏太真实了.txt)文件中


## 遇到的问题

在这个项目中，我遇到了一些问题：

1. **XPath获取问题**：该网站保存小说使用的是`<br>`标签而不是常见的`<a>`标签，因此需要使用`//div[@class='content']//text()`来获取内容。

2. **分页问题**：网站上的小说被分成了多页而不是常见的一页，因此在获取下一页的URL时不能无限循环使用同一个URL变量。为解决这个问题，我添加了一层if-else判断条件，判断内容是下一页还是下一章，然后继续循环。另外，注意网站提供的下一章的href没有提供前缀"https://www.shuxiang8.cc" ，需要手动添加。
3. **写权限问题**： 还有一个小点需要注意就是withopen中我最开始使用”w“，但是当循环开始后会对这个文件进行重写，所以正确的方法是要使用”a“，这样就不会对文件进行重写了
## 展望

虽然我没有继续推进这个小的练手作，但实际上只要简单再嵌套一层结构，应该可以实现将整个网站的小说都爬取下来。然而，由于我是在个人主机上运行，爬取一千章的小说需要花费很长时间，因此我选择不继续推进这个小的练手项目。
