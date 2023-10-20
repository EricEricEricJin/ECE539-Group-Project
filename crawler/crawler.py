from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=chrome_options)

homepage_url = "https://space.bilibili.com/1465615902/video"
browser.get(homepage_url)

time.sleep(2)

page_cnt = 0
video_cnt = 0
valid_cnt = 0

while True:
    page_cnt += 1
    video_list = browser.find_elements(By.XPATH, '//ul[@class="clearfix cube-list"]//a[@class="title"]')

    for video in video_list:
        video_cnt += 1
        link = video.get_attribute("href") 
        BV = re.findall("BV[0-9a-zA-Z]*", link)[0]

        # enter and switch to video tab
        video.click()
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[1])

        # get description text
        desc = browser.find_element(By.XPATH, '//span[@class="desc-info-text"]').text

        # parse timestamp from desc
        hms_list = []
        for line in desc.split('\n'):
            re_ret = re.findall(r"([0-9]{1,2}:)?([0-9]{1,2}):([0-9]{1,2})", line)
            if (len(re_ret)):
                re_ret = re_ret[0]
                hms = (0 if re_ret[0] == '' else int(re_ret[0][:-1])), int(re_ret[1]), int(re_ret[2])
                hms_list.append(hms)

        if (len(hms_list)):
            with open(BV+".csv", "w") as f:
                for hms in hms_list:
                    f.write(str(hms).strip("()")+"\n")
            valid_cnt += 1
            print("PAGE {},\t CNT {},\t BV {},\t VALID.".format(page_cnt, video_cnt, BV))
        else:
            print("PAGE {},\t CNT {},\t BV {},\t INVALID.".format(page_cnt, video_cnt, BV))
        # close tab and go to homepage
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    
    # next page
    try:
        browser.find_element(By.XPATH, '//li[@class="be-pager-next"]/a').click()
        time.sleep(2)
    except:
        # End reached, no next page
        break;

print("Finished with {} pages, {} videos, {} valids".format(page_cnt, video_cnt, valid_cnt))
