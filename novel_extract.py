# 怎么发送？
# pip install requests
# pip install lxml
import requests
from lxml import etree
# 发送给谁
url = "https://www.shuxiang8.cc/0_3131/2257741.html"

while True:
#伪装自己
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    # 发送请求
    resp = requests.get(url,headers= headers)
    #设置编码
    # 尝试使用其他编码格式
    resp.encoding = "GBK"

    # 响应信息

    e =etree.HTML(resp.text)
    info = e.xpath("//div[@class='content']//text()")
    title = e.xpath("string(//h1/text())")
    filtered_info = [text.strip() for text in info if text.strip() != "" and text.strip() != "，" and text.strip() != "\r\n"]
    content_text = "".join(filtered_info)

    url = e.xpath("string(//div[@class='section-opt']/a[@href and contains(text(), '下一页')]/@href)")
    # 提取下一页按钮的链接
    next_page_link = e.xpath("string(//div[@class='section-opt']/a[@href and contains(text(), '下一页')]/@href)")

    # 判断是否存在下一页按钮
    if next_page_link:
        # 下一页链接存在，使用下一页链接作为新的URL
        url = next_page_link
    else:
        # 下一页链接不存在，可能是最后一页，尝试提取下一章链接
        next_chapter_link = e.xpath("string(//div[@class='section-opt']/a[contains(text(), '下一章')]/@href)")
        if next_chapter_link:
            # 下一章链接存在，使用下一章链接作为新的URL
            url = "https://www.shuxiang8.cc" + next_chapter_link
        else:
            # 如果下一页按钮和下一章链接都不存在，则可能已经到达最后一页或者最后一章
            print("已经到达最后一页或最后一章")

    # print(url)
    # 保存
    with open("这游戏太真实了.txt", "a",encoding="UTF-8") as f:#如果不是要覆盖之前的内容，应该用a，而不是w
        f.write(title + "\n\n" + content_text + "\n\n")

