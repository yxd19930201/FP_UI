import json
import random
import time
from time import sleep
import cv2 as cv
import pymysql
import pytest
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import MySQLdb



@pytest.fixture(scope="class")

def productlist():
    productname = '木易测试商品'
    number = str(random.randint(1, 999999999))
    newproductname=productname+number
    return newproductname


@pytest.fixture()
def get_product(get_date):
    product_url='https://pre-console-fp-admin.suuyuu.cn/api/ProductPoolCard/GetPoolProductList'
    product_params={'PageIndex':'1',
            'PageSize':'50',
            'CategoryIdL1':'9402',
            'CategoryIdL2':'9403',
            'CategoryIdL3':'9404',
            'timeStr':'1639470473187'}
    product_head={"Authorization":"Bearer {}".format(get_date),
                  "MerchantId":"64cf60f0-d5d3-449b-95a2-03db1c640ace",
                  "Content-Type":"application/json"}
    supproduct=requests.get(product_url,params=product_params,headers=product_head,verify=False)
    print(f'请求参数：{supproduct.content}')
    print(f'status_code:{supproduct.status_code}')
    print(supproduct.json()['data']['list'][(int(random.randint(1,49)))]['productId'])
    return supproduct.json()['data']['list'][(int(random.randint(1,49)))]['productId']

@pytest.fixture()
def get_date():
    token_url='http://pre.passport.suuyuu.cn/oauth/token'
    token_params={'grant_type':'password',
                  'client_id':'10000169',
                  'client_secret':'39a0feca6d3b4f739d733797e33179e4',
                  'username':'17802711551',
                  'password':'ts123456'}
    token_headers={'Content-Type':'application/x-www-form-urlencoded'}
    token=requests.post(token_url,data=token_params,headers=token_headers)
    print(token.json())
    return token.json()['access_token']

@pytest.fixture()
def sup_token_get():
    sup_token_url='http://pre.passport.suuyuu.cn/oauth/token'
    sup_token_data={'grant_type':'password',
                    'client_id':'10000011',
                    'client_secret':'B570801B9E334E34A0C39FFF886EC3AF',
                    'username':'15926320810',
                    'password':'weihengyi'}
    sup_token_head={'Content-Type':'application/x-www-form-urlencoded'}
    get_sup_token=requests.post(sup_token_url,data=sup_token_data,headers=sup_token_head)
    print(get_sup_token.json())
    return get_sup_token.json()['access_token']




@pytest.fixture()
def query_reported(sup_token_get):
    url='https://pre-manage-sup-api-admin.suuyuu.cn/service/categoryreport/enroll/page'
    params={'pageIndex':'1',
            'pageSize':'10',
            'tabsActiveKey':'11',
            'PurMemberCode':'9025272',
            'reportStatus':'11'}
    header={"Authorization":"Bearer {}".format(sup_token_get),
                "Content-Type":"application/json"}
    reported_list=requests.get(url,params=params,headers=header,verify=False)
    print(reported_list.json())
    data=reported_list.json()['data']['list'][0]['id']
    print('查看接口返回的id:{}'.format(data))
    return data

@pytest.fixture()
def deleta_reported(query_reported,sup_token_get):
    deleta_url="https://pre-manage-sup-api-admin.suuyuu.cn/service/categoryreport/enroll/BatchRejectEnroll"
    data={"reportIds":["{}".format(query_reported)],
          "reason":"测试"}
    header={"Authorization":"Bearer {}".format(sup_token_get),
              "Content-Type":"application/json"}
    reported=requests.post(deleta_url,data=json.dumps(data),headers=header,verify=False)
    print('接口传值头:{}'.format(header))
    print('接口传值数据:{}'.format(data))
    print('接口传值地址:{}'.format(deleta_url))
    print('接口返回数据:{}'.format(reported.text))


@pytest.fixture()
def get_list(get_date):
    get_list_url = 'https://pre-console-fp-admin.suuyuu.cn/api/Product/GetProductPageList'
    get_list_params = {'PageIndex': '1',
                       'PageSize': '10',
                       'Type': '1',
                       'SaleStatus': '1',
                       'timeStr': '1639706512706'}
    get_list_header = {"Authorization": "Bearer {}".format(get_date),
                       "MerchantId": "64cf60f0-d5d3-449b-95a2-03db1c640ace",
                       "Content-Type": "application/json"}
    get_list = requests.get(get_list_url, params=get_list_params, headers=get_list_header, verify=False)
    get_test = get_list.json()['data']['list'][random.randint(1, 9)]['id']
    print(get_list.json())
    print(get_test)
    return get_test

@pytest.fixture()
def add_appman(get_list,get_date):
    add_appman_url='https://pre-console-fp-admin.suuyuu.cn/api/Product/MoveInRecycle'
    add_appman_data={"productIds":["{}".format(get_list)]}
    add_appman_header={"Authorization": "Bearer {}".format(get_date),
                       "MerchantId": "64cf60f0-d5d3-449b-95a2-03db1c640ace",
                       "Content-Type": "application/json"}
    add_appman=requests.post(add_appman_url,data=json.dumps(add_appman_data),headers=add_appman_header,verify=False)
    print(add_appman.text)



@pytest.fixture()
def login():
    print("------开始执行login方法------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    phone = "17802711551"
    password = 'ts123456'
    driver.get('https://pre-console.suuyuu.cn/')
    driver.find_element_by_id('phone').click()
    driver.find_element_by_id('phone').send_keys(phone)
    sleep(2)
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('isRemember').click()
    driver.find_element_by_xpath('//*[@id="app"]/main/div/div/form/button').click()
    time.sleep(2)
    frames = driver.find_elements_by_tag_name('iframe')
    print(frames.__len__())
    # 切换到滑动窗口
    driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[1])
    while True:
        # 获取滑动快的src
        block_path = driver.find_element_by_id("slideBlock").get_attribute("src")
        # 获取模板的src
        template_path = driver.find_element_by_id("slideBg").get_attribute("src")
        print('templatepath:{}'.format(template_path))
        # 获取滑块距离
        x = get_pos(template_path)
        if x == 0:
            driver.find_element_by_id("reload").click()
            time.sleep(2)
        if x != 0:
            break

    move_length = x / 2 - 4
    print(move_length)
    # 获取滑动按钮元素
    button = driver.find_element_by_id('tcaptcha_drag_thumb')
    action = ActionChains(driver)
    action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
    # action.reset_actions()
    ActionChains(driver).move_to_element_with_offset(to_element=button, xoffset=int(move_length),
                                                          yoffset=0).perform()
    ActionChains(driver).release(on_element=button).perform()
    # 切换到商户管理区
    sleep(5)
    driver.find_element_by_xpath('//*[@class="merchant_content"]/div[11]/div[1]').click()
    driver.find_element_by_xpath('//*[@class="inner-app"]/a[2]').click()
    return driver



def get_pos(template_path):
    """
    获取滑块移动距离
    :param template_path: 模板图片
    :return: x 滑块横坐标
    """
    # requests.adapters.DEFAULT_RETRIES = 50 # 增加重连次数

    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    template_img = s.get(template_path)
    # 保存模板图片
    with open('template.png', 'wb') as f:
        f.write(template_img.content)
        f.close()
    image = cv.imread('template.png')
    blurred = cv.GaussianBlur(image, (5, 5), 0)
    canny = cv.Canny(blurred, 200, 400)

    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            x, y, w, h = cv.boundingRect(contour)  # 外接矩形
            print(x, y, w, h)
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # cv.imshow('image', image)
            return x
    return 0

if __name__ == '__main__':
    pytest.main(['-s', 'conftest.py'])
