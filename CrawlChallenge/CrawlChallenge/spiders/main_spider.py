import scrapy
import CrawlChallenge.items as items
from CrawlChallenge.read_files import read_csv, edit_df_data, make_df

class MySpider_group2(scrapy.Spider):
    name = "247wallst"
    allowed_domains = ["247wallst.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 1 and count <= 10:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        # 先找到文章區塊
        article_tags = response.css("div.entry-content")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                byline = article_tag.css("div.byline-container")
                author = byline.css("div.author a::text").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = "None"
                yield output


class MySpider_group3(scrapy.Spider):
    name = "303magazine"
    allowed_domains = ["303magazine.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 11 and count <= 20:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div#cb-author-box")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                byline = article_tag.css("div.cb-title")
                author = byline.css("a span::text").get()

                social_media_block = article_tag.css(
                    "div.cb-author-page-contact")
                social_media_url = social_media_block.css(
                    "a::attr(href)").get()
                if social_media_url:
                    social_media_url = social_media_url.split("/")
                    if "cdn-cgi" not in social_media_url[1]:
                        social_media_url = "www.twitter.com/" + \
                            social_media_url[3]
                    else:
                        social_media_url = "None"

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = social_media_url if social_media_url else "None"
                yield output


class MySpider_group4(scrapy.Spider):
    name = "3dprintingindustry"
    allowed_domains = ["3dprintingindustry.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 21 and count <= 32:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("section.post-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                byline = article_tag.css("div.author-content")
                author = byline.css("h5 a::text").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = "None"
                yield output


class MySpider_group5(scrapy.Spider):
    name = "abovethelaw"
    allowed_domains = ["abovethelaw.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        yield scrapy.Request(url=myList[33], callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("div#single-post-content")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            byline = article_tags.css("p img ~strong")
            author = byline.css("em a::text").get()

            social_media_url = byline.css(
                "a:nth-child(n+4)::attr(href)").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url
            yield output


class MySpider_group6(scrapy.Spider):
    name = "africa"
    allowed_domains = ["africa.cgtn.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 34 and count <= 40:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.author-box-wrap")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                byline = article_tag.css("span.fn")
                author = byline.css("a::text").get()
                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = "None"
                yield output


class MySpider_group7(scrapy.Spider):
    name = "ahoramismo"
    allowed_domains = ["ahoramismo.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 41 and count <= 49:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.l-article__meta")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                byline = article_tag.css("span.author")
                author = byline.css("a::text").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = "None"
                yield output


class MySpider_group8(scrapy.Spider):
    name = "alextimes"
    allowed_domains = ["alextimes.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 50 and count <= 55:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.has-content-area")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                author = article_tag.css("p strong::text").get()
                if author:
                    author = author.split(" ")
                    author = author[1] + " " + author[2]

                email = article_tag.css("p a::text").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = email if email else "None"
                yield output


#FIXME: group9連結是壞的
# class MySpider_group9(scrapy.Spider):


class MySpider_group10(scrapy.Spider):
    name = "americanmilitarynews"
    allowed_domains = ["americanmilitarynews.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 61 and count <= 63:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.singlePostMeta")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                author = article_tag.css("span.fn a::text").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = "None"
                yield output


class MySpider_group11(scrapy.Spider):
    name = "androidcommunity"
    allowed_domains = ["androidcommunity.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 64 and count <= 72:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.td-post-header")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                author = article_tag.css("a::text").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = "None"
                yield output


#FIXME: group12連結是壞的
# class MySpider_group12(scrapy.Spider):


class MySpider_group13(scrapy.Spider):
    name = "arstechnica"
    allowed_domains = ["arstechnica.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 76 and count <= 81:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("section.article-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            for article_tag in article_tags:
                author = article_tag.css(
                    "section.author-bio-top a::text").get()

                social_media_url = article_tag.css(
                    "section.author-social a:nth-child(n+3)::attr(href)").get()

                output["url"] = response.url
                output["author"] = author if author else "None"
                output["social_media"] = social_media_url if social_media_url else "None"
                yield output

# double parse
class MySpider_group14(scrapy.Spider):
    name = "3dnatives"
    allowed_domains = ["www.3dnatives.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        count = -1
        for item in myList:
            count += 1
            if count >= 82 and count <= 92:
                yield scrapy.Request(url=item, callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("div.published-by")
        output = items.ArticleItem()
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        if len(article_tags) > 0:
            author = article_tags.css("strong a::text").get()
            detail_page_url = article_tags.css("strong a::attr(href)").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            yield scrapy.Request(url=detail_page_url, callback=self.detail_parse, meta={'item': output}, headers=headers, dont_filter=True)

    def detail_parse(self, response):
        author_blocks = response.css("div.post-content")
        output = response.meta["item"]
        target = author_blocks.css("div.withsmallpadding:nth-of-type(3)")
        social_media_url = target.css("div.inner div a::attr(href)").get()

        if social_media_url == None:
            target_2 = author_blocks.css(
                "div.withsmallpadding:nth-of-type(n+5)")
            social_media_url_2 = target_2.css(
                "div.inner div a::attr(href)").get()
            output["social_media"] = social_media_url_2
        else:
            output["social_media"] = social_media_url

        yield output


class MySpider_group15(scrapy.Spider):
    name = "3dprintingmedia"
    allowed_domains = ["www.3dprintingmedia.network"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 93 and count <= 99:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.about-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("h3 a::text").get()
            social_media_url = article_tags.css(
                "li.social-icons-item a::attr(href)").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url if social_media_url else "None"
            yield output


class MySpider_group16(scrapy.Spider):
    name = "9and10news"
    allowed_domains = ["www.9and10news.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 100 and count <= 101:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.entry-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group17(scrapy.Spider):
    name = "abccolumbia"
    allowed_domains = ["www.abccolumbia.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 102 and count <= 103:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.entry-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group18(scrapy.Spider):
    name = "abqjournal"
    allowed_domains = ["www.abqjournal.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 104 and count <= 107:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("section.entry-meta")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("h5 a::text").get()

            if "Journal Staff Writer" in author:
                author = author.split("/")[0]

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group19_1(scrapy.Spider):
    name = "accountingtoday_1"
    allowed_domains = ["www.accountingtoday.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 108 and count <= 109:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("span.CreativeWorkPage-authorName")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group19_2(scrapy.Spider):
    name = "accountingtoday_2"
    allowed_domains = ["www.accountingtoday.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 110 and count <= 112:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("span.ArticlePage-authorName")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group20(scrapy.Spider):
    name = "aerotelegraph"
    allowed_domains = ["www.aerotelegraph.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 113 and count <= 118:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.article-content")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output

# FIXME: group21連結是壞的
# class MySpider_group21(scrapy.Spider):


# 125, 126 是指向同一個網址
class MySpider_group22(scrapy.Spider):
    name = "aikenstandard"
    allowed_domains = ["www.aikenstandard.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 123 and count <= 127:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.meta li span.tnt-byline")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = response.css("div.meta li span.tnt-byline::text").get()
            author = author.split("\n")[0].split(" ")
            author = author[1] + " " + author[2]
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output
        else:
            output["url"] = response.url
            output["author"] = "None"
            output["social_media"] = "None"
            yield output


class MySpider_group23(scrapy.Spider):
    name = "ainonline"
    allowed_domains = ["www.ainonline.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 128 and count <= 133:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.byline")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


# # TODO: group24: can't reach
# class MySpider_group24(scrapy.Spider):
#     name = "almasdarnews"
#     allowed_domains = ["www.almasdarnews.com"]
#     custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

#     def start_requests(self):
#         myDF = make_df()
#         myList = [item for item in myDF["url"]]
#         # ua = UserAgent()
#         # user_agent = ua.random
#         # print(user_agent)
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

#         # headers = {
#         #     "User-Agent": user_agent}
#         # request = scrapy.Request(callback=self.parse, headers=headers)
#         # request.cookies["complianz_consent_status"] = "allow"
#         # request.cookies["wpdiscuz_hide_bubble_hint"] = "1"
#         # request.cookies["_pk_id.2.477a"] = "eb39ceed83ac830b"
#         # request.cookies["_pk_ses.2.477a"] = "1"
#         # request.cookies["complianz_policy_id"] = "28"
#         # request.cookies["cmplz_choice"] = "set"
#         # request.cookies["weather_location"] = "unknown"

#         count = -1
#         for item in myList:
#             count += 1
#             if count >= 134 and count <= 143:
#                 yield scrapy.Request(url=item, callback=self.parse, headers=headers,
#                                      cookies={"complianz_consent_status": "allow", "wpdiscuz_hide_bubble_hint": "1",
#                                               "_pk_id.2.477a": "b39ceed83ac830b.1622455600.3.1622491374.1622491374.", "_pk_ses.2.477a": "1",
#                                               "complianz_policy_id": "28", "cmplz_choice": "set", "weather_location": "unknown"})

#     def parse(self, response):
#         article_tags = response.css("div.jeg_author_content")
#         output = items.ArticleItem()
#         if len(article_tags) > 0:
#             author = article_tags.css("div.jeg_author_name a::text").get()
#             social_media_url = article_tags.css(
#                 "div.jeg_author_socials a.twitter::attr(href)").get()
#             output["url"] = response.url
#             output["author"] = author if author else "None"
#             output["social_media"] = social_media_url if social_media_url else "None"
#             yield output


class MySpider_group25(scrapy.Spider):
    name = "altonivel"
    allowed_domains = ["www.altonivel.com.mx"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 144 and count <= 146:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.info")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group26(scrapy.Spider):
    name = "americanbanker"
    allowed_domains = ["www.americanbanker.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 147 and count <= 148:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.ArticlePage-byline-bottom-authorInfo")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css(
                "div.ArticlePage-byline-bottom-authorInfo-bio-name a::text").get()
            social_media_url = article_tags.css(
                "li.SocialBar-items-item a::attr(href)").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url if social_media_url else "None"
            yield output


class MySpider_group27(scrapy.Spider):
    name = "americanninjawarriornation"
    allowed_domains = ["www.americanninjawarriornation.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 149 and count <= 152:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("span.c-byline-wrapper")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("span.c-byline__author-name::text").get()
            social_media_url = article_tags.css(
                "a.c-byline__twitter-handle::attr(href)").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url if social_media_url else "None"
            yield output


class MySpider_group28(scrapy.Spider):
    name = "americanthinker"
    allowed_domains = ["www.americanthinker.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        yield scrapy.Request(url=myList[153], callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group29(scrapy.Spider):
    name = "analyticsindiamag"
    allowed_domains = ["www.analyticsindiamag.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 154 and count <= 158:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.author-content")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()
            social_media_url = article_tags.css(
                "a.twitter::attr(href)").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url if social_media_url else "None"
            yield output


class MySpider_group30(scrapy.Spider):
    name = "anandtech"
    allowed_domains = ["www.anandtech.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 159 and count <= 166:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("div.blog_top_left")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a.b::text").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group31(scrapy.Spider):
    name = "androidcentral"
    allowed_domains = ["www.androidcentral.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]

        count = -1
        for item in myList:
            count += 1
            if count >= 167 and count <= 173:
                yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        article_tags = response.css("span.article-header__author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a::text").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group32(scrapy.Spider):
    name = "androidpolice"
    allowed_domains = ["www.androidpolice.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        count = -1
        for item in myList:
            count += 1
            if count >= 174 and count <= 179:
                yield scrapy.Request(url=item, callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("span.post-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a.author-name::text").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group33(scrapy.Spider):
    name = "androidworld"
    allowed_domains = ["www.androidworld.it"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        count = -1
        for item in myList:
            count += 1
            if count >= 180 and count <= 189:
                yield scrapy.Request(url=item, callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("div.text-leaf")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("span.autcont a::text").get()
            social_media_url = article_tags.css(
                "a.authsocial::attr(href)").get()
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url if social_media_url else "None"
            yield output


# 193 要特別處理
class MySpider_group34_1(scrapy.Spider):
    name = "annistonstar_1"
    allowed_domains = ["www.annistonstar.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        count = -1
        for item in myList:
            count += 1
            if (count >= 190 and count <= 192) or (count >= 194 and count <= 196):
                yield scrapy.Request(url=item, callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("div.meta")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css(
                "span a::text").get()
            author = author.split(",")[0].split(" ")
            author = author[1] + " " + author[2]
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


# 193 要特別處理
class MySpider_group34_2(scrapy.Spider):
    name = "annistonstar_2"
    allowed_domains = ["www.annistonstar.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        yield scrapy.Request(url=myList[193], callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("div.meta")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css(
                "span.tnt-byline::text").get()

            author = author.split(" ")
            author = author[1] + " " + author[2]
            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output


class MySpider_group35(scrapy.Spider):
    name = "applesfera"
    allowed_domains = ["www.applesfera.com"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        count = -1
        for item in myList:
            count += 1
            if count >= 197 and count <= 198:
                yield scrapy.Request(url=item, callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("footer.article-author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css(
                "a.article-author-link::text").get()

            social_media_url = article_tags.css(
                "a.article-author-twitter::attr(href)").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = social_media_url if social_media_url else "None"
            yield output


class MySpider_group36(scrapy.Spider):
    name = "architectsjournal"
    allowed_domains = ["www.architectsjournal.co.uk"]
    custom_settings = {"FEEDS": {"results.json": {"format": "json"}}}

    def start_requests(self):
        myDF = make_df()
        myList = [item for item in myDF["url"]]
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        yield scrapy.Request(url=myList[199], callback=self.parse, headers=headers)

    def parse(self, response):
        article_tags = response.css("span.post_author")
        output = items.ArticleItem()
        if len(article_tags) > 0:
            author = article_tags.css("a.author::text").get()

            output["url"] = response.url
            output["author"] = author if author else "None"
            output["social_media"] = "None"
            yield output
