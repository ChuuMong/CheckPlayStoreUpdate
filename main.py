from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
import time

package_name = input('패키지를 입력하세요 : ')
version_name = input('버전 네임을 입력하세요 : ')

play_store_url = "https://play.google.com/store/apps/details?id=" + package_name
is_not_update_done = True
while is_not_update_done :
    try:
        response = urlopen(play_store_url).read()
    except HTTPError as e:
        if (e.code == 404) :
            print('패지키 명이 잘못 입력되었습니다. 다시 시도해주세요.')
            break
        else :
            continue
        
    html = BeautifulSoup(response, 'html.parser')
    if (html.find('div', {'id' : 'error-section'})) :
        print('패지키 명이 잘못 입력되었습니다. 다시 시도해주세요.')
        break

    htlgbs = html.find_all('span', {'class' : 'htlgb'})
    # 7번 인덱스가 버전 네임
    current_version_name = htlgbs[7]
    if current_version_name.next == version_name : 
        print('업데이트 완료!!!!')
        is_not_update_done = False
        break

    time.sleep(60)
    


