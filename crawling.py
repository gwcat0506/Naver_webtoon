from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time
import pyperclip
import re
import tqdm

driver = webdriver.Chrome()

def naver_login():
    #네이버 이동

    url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
    driver.get(url)
    time.sleep(30)
    driver.implicitly_wait(30)

    # # 아이디 입력
    # log_ID = driver.find_element(By.
    # NAME, 'id')
    # log_ID.click()
    # pyperclip.copy('gwcat0506')
    # log_ID.send_keys(Keys.CONTROL, 'v')
    # time.sleep(1)

    # # 비밀번호 입력
    # log_PID = driver.find_element(By.NAME, 'pw')
    # log_PID.click()
    # pyperclip.copy('dd')
    # log_PID.send_keys(Keys.CONTROL, 'v')
    # time.sleep(1)

    # # # 로그인 클릭
    # log_ENT = driver.find_element(By.XPATH, '//*[@id="log.login"]')
    # log_ENT.click()


def get_naver_webtoon_info():
    
    naver_login()

    id_list = []
    title_list = []
    age_list = []
    author_list = []
    day_list = []
    category_list = []
    rating_list = []
    heart_list = []
    story_list = []
    webtoon_url_list = []
    
    algorithm1_list = []
    algorithm2_list = []
    algorithm3_list = []
    algorithm4_list = []
    algorithm5_list = []
    algorithm6_list = []
    algorithm7_list = []
    algorithm8_list = []
    algorithm9_list = []
    algorithm10_list = []

    webtoon_id = 0
    
    for day7 in ['mon','tue','wed','thu','fri','sat','sun']:
        # 네이버 웹툰 페이지 열기
        nw_url = 'https://comic.naver.com/webtoon?tab='+day7
        driver.get(nw_url)
        time.sleep(3)

        # 클릭할 수 있는 제목 리스트 가져오기
        titles = driver.find_elements(By.CLASS_NAME, "ContentTitle__title_area--x24vt")
        titles[3:-10]
        print("titles",len(titles))
        
        # 웹툰 개수만큼 반복하기
        if day7 =='sun':
            titles = titles[:-1]
        for i in tqdm.tqdm(range(3,len(titles)-10)):
            print("\rprocess: " +day7+" "+ str(i + 1) + " / " + str(len(titles)-10))

            # 웹페이지가 로딩되기도 전에 코드가 실행되는 것을 방지하기 위한 기다림
            sleep(1)
            
            # 0번째 웹툰, 즉 월요일 첫번재 웹툰부터 클릭해서 해당 페이지로 이동하기
            titles = driver.find_elements(By.CLASS_NAME, "ContentTitle__title_area--x24vt")
            ratings = driver.find_elements(By.CLASS_NAME, "rating_area")
            
            rating = ratings[i].text
            rating = rating.replace("\n", "")
            rating = rating[2:]
            print("rating",rating)
            
            titles[i].click()

            # 이동한 페이지의 html 코드 가져오기
            html = driver.page_source
            soup = bs(html, 'html.parser')

            sleep(1)
            # 제목 정보 가져오기
            title = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListInfo__comic_info--yRAu0 > div > h2").text
            title = title.replace("\n", "")
            title = title.replace("휴재", "")
            print("title", title)
            
            # 작가 정보 가져오기
            author = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListInfo__comic_info--yRAu0 > div > div.ContentMetaInfo__meta_info--GbTg4 > span > a").text
            print("author", author)
            
            # 줄거리 정보 가져오기
            story = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListInfo__comic_info--yRAu0 > div > div.EpisodeListInfo__summary_wrap--ZWNW5 > p").text
            story = story.replace("\n", "")
            print("story", story)
            
            # 요일 및 연령 정보 가져오기
            info = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListInfo__comic_info--yRAu0 > div > div.ContentMetaInfo__meta_info--GbTg4 > em").text
            
            info_list = info.split('\n')
            filtered_text = [t for t in info_list if t]  # 빈 문자열 제거
            day = filtered_text[0]
            age = filtered_text[2]
            print("day",day)
            print("age",age)
            
            # 카테고리 정보 가져오기
            category = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListInfo__comic_info--yRAu0 > div > div.EpisodeListInfo__summary_wrap--ZWNW5 > div > div").text
            category = category.replace("\n", "")
            category = category.replace("#", ",")
            category = category[1:]
            print("category", category)
            
            # 관심수
            heart = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListView__user_wrap--S_pYn > div > button.EpisodeListUser__item--Fjp4R.EpisodeListUser__favorite--DzoPt > span.EpisodeListUser__count--fNEWK").text
            heart = heart.replace(",", "")
            print("heart", heart)
            
            # 총 회차수
            cnt = driver.find_element(By.CSS_SELECTOR, "#content > div.EpisodeListView__episode_list_wrap--q0VYg > div.EpisodeListView__episode_list_head--PapRv > div.EpisodeListView__count--fTMc5").text
            cnt = re.sub(r'\D', '', cnt)
            print("cnt", cnt)
            
            # 이 작품 독자들이 많이 본 웹툰
            
            algorithm1 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > div > a.ContentTitle__title_area--x24vt > span > span").text
            algorithm2 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > div > a.ContentTitle__title_area--x24vt > span > span").text
            algorithm3 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > div > a.ContentTitle__title_area--x24vt > span > span").text
            algorithm4 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div > a.ContentTitle__title_area--x24vt > span > span").text
            algorithm5 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > div > a.ContentTitle__title_area--x24vt > span > span").text
            
            # 관련 작품 더보기 1/2 버튼 유무에 따라 
            try:
                algorithm6 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) > div > a.ContentTitle__title_area--x24vt > span > span").text
                algorithm7 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > div > a.ContentTitle__title_area--x24vt > span > span").text
                algorithm8 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > div > a.ContentTitle__title_area--x24vt > span > span").text
                algorithm9 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) > div > a.ContentTitle__title_area--x24vt > span > span").text
                algorithm10 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > div > a.ContentTitle__title_area--x24vt > span > span").text
                print("버튼이 없음")
                    
            except:
                try:
                    button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[5]/a')
                    button.click()
                    
                    print("버튼이 있음")
                    algorithm6 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm7 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm8 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm9 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm10 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > div > a.ContentTitle__title_area--x24vt > span > span").text
                
                except:
                    button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[4]/a')
                    button.click()
                    
                    print("버튼이 있음")
                    algorithm6 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm7 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm8 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm9 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    algorithm10 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > div > a.ContentTitle__title_area--x24vt > span > span").text
                    
            print(algorithm1)
            print(algorithm2)
            print(algorithm3)
            print(algorithm4)
            print(algorithm5)
            print(algorithm6)
            print(algorithm7)
            print(algorithm8)
            print(algorithm9)
            print(algorithm10)
            
            # 만약 연재 요일이 2개 이상이라서 이미 저장했던 웹툰이라면 요일만 추가하고 넘어가기
            if title in title_list:
                driver.back()
                continue
            

            # 정보들을 리스트에 담기
            id_list.append(webtoon_id)
            rating_list.append(rating)
            title_list.append(title)
            age_list.append(age)
            author_list.append(author)
            day_list.append(day)
            category_list.append(category)
            heart_list.append(heart)
            story_list.append(story)
            webtoon_url_list.append(driver.current_url)
            
            algorithm1_list.append(algorithm1)
            algorithm2_list.append(algorithm2)
            algorithm3_list.append(algorithm3)
            algorithm4_list.append(algorithm4)
            algorithm5_list.append(algorithm5)
            algorithm6_list.append(algorithm6)
            algorithm7_list.append(algorithm7)
            algorithm8_list.append(algorithm8)
            algorithm9_list.append(algorithm9)
            algorithm10_list.append(algorithm10)

            # 뒤로 가기
            driver.back()
            webtoon_id += 1
            sleep(0.5)

    # DataFrame 형태로 저장하기
    total_data = pd.DataFrame()

    total_data['id'] = id_list
    total_data['title'] = title_list
    total_data['author'] = author_list
    total_data['rating'] = rating_list
    total_data['age'] = age_list
    total_data['day'] = day_list
    total_data['category'] = category_list
    total_data['heart'] = heart_list
    total_data['story'] = story_list
    total_data['webtoon_url'] = webtoon_url_list

    total_data['algorithm1'] = algorithm1_list
    total_data['algorithm2'] = algorithm2_list
    total_data['algorithm3'] = algorithm3_list
    total_data['algorithm4'] = algorithm4_list
    total_data['algorithm5'] = algorithm5_list
    total_data['algorithm6'] = algorithm6_list
    total_data['algorithm7'] = algorithm7_list
    total_data['algorithm8'] = algorithm8_list
    total_data['algorithm9'] = algorithm9_list
    total_data['algorithm10'] = algorithm10_list

    # 따로 인덱스를 생성하지 않고 id를 인덱스로 정하기
    total_data.set_index('id', inplace=True)

    return total_data


naver_webtoon_filename = "네이버 웹툰 정보.csv"
# if os.path.isfile(naver_webtoon_filename):
#     # 파일이 있다면 웹 크롤링 하지 않고 읽어오기
#     total_data = pd.read_csv(naver_webtoon_filename, encoding='utf-8-sig')
# else:
# 파일이 없다면 웹 크롤링 하기
total_data = get_naver_webtoon_info()
# CSV 파일로 저장하기
total_data.to_csv("네이버 웹툰 정보.csv", encoding='utf-8-sig')