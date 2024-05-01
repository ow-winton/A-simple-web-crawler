[En](/README.md) |[Ch](/README-CH.md)
# A-simple-web-crawler 
 A-simple-web-crawler for novel
# Introduction

This is a simple novel crawler project.

The purpose of this project is to train by crawling novels from novel websites. By running this project, novels can be downloaded into corresponding txt files. As this project is only for practice, specific website URLs and information about saving txt files need to be manually modified. However, implementing these modifications is quite simple. However, due to the different HTML structures of different websites, this crawler is limited to crawling novel content from "https://www.shuxiang8.cc" website.

The example of crawling novels is in the file ["这游戏太真实了.txt"] (/这游戏太真实了.txt)within the project.

## Challenges

During this project, I encountered some challenges:

1. **XPath Issue**: The website saves novels using `<br>` tags instead of the common `<a>` tags. Therefore, I need to use `//div[@class='content']//text()` to get the content.

2. **Pagination Issue**: The novels on the website are divided into multiple pages instead of the common single page. Therefore, when getting the URL of the next page, I cannot infinitely loop using the same URL variable. To solve this problem, I added an if-else statement to determine whether the content is the next page or the next chapter, and then continue the loop. Also, note that the href for the next chapter provided by the website does not include the prefix "https://www.shuxiang8.cc", so it needs to be manually added.

## Outlook

Although I did not continue to advance this small practice project, in fact, as long as a simple nesting layer is added, it should be possible to crawl novels from the entire website. However, since I am running it on a personal host, crawling a thousand chapters of novels would take a long time, so I chose not to continue advancing this small practice project.
