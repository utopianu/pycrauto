# _*_ coding: utf-8 _*_

import crawler
import logging


def test_spider():
    """
    test spider
    """
    # 定义fetcher, parser和saver, 你也可以重写这三个类中的任何一个
    fetcher = crawler.Fetcher(max_repeat=3, sleep_time=0)
    parser = crawler.Parser(max_deep=1)
    saver = crawler.Saver(save_pipe=open("out_spider_thread.txt", "w"))

    # 定义Url过滤, UrlFilter使用Set, 适合Url数量不多的情况
    black_patterns = (crawler.CONFIG_URLPATTERN_FILES, r"binding", r"download",)
    white_patterns = ("^http[s]{0,1}://(www\.){0,1}(zhushou\.360)\.(com|cn)",)
    url_filter = crawler.UrlFilter(black_patterns=black_patterns, white_patterns=white_patterns)

    # 初始化WebSpider
    test = crawler.WebSpider(fetcher, parser, saver, url_filter=url_filter, monitor_sleep_time=5)

    # 添加种子Url
    test.set_start_url("http://zhushou.360.cn/", keys=("360web",))

    # 开始抓取任务并等待其结束
    test.start_work_and_wait_done(fetcher_num=10, is_over=True)
    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s\t%(levelname)s\t%(message)s")
    # test_spider()
    # test_spider_async()
    # test_spider_distributed()
    exit()
