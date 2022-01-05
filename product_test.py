import json
import re
from time import sleep

import pytest
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Test_Product():
    def setup(self):
        pass

    def teardown(self):
        # pass
        self.driver.quit()


    # @pytest.mark.skip
    @pytest.mark.parametrize('SupProductId',[('500002344')])
    def test_supbazaar_choose(self,login,SupProductId):
        self.driver = login
        sleep(3)
        self.driver.find_element_by_xpath('//span[contains(text(),"供货市场选货")]').click()
        # 展开筛选
        WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="ant-row"]/div[15]/span')))
        self.driver.find_element_by_xpath('//*[@class="ant-row"]/div[15]/span').click()
        # 查询商品编号
        self.driver.find_element_by_xpath('//*[@id="SupProductId"]').send_keys(SupProductId)
        self.driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary" and @type="submit"]').click()
        sleep(3)
        getsupproduct=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left"]').text
        sleep(2)
        if SupProductId in getsupproduct:
            # 查看关联商品
            # self.driver.find_elements_by_class_name('iconfont')[2].click()
            # self.driver.execute_script('document.getElementsByClassName("iconfont")[2].click()')
            self.driver.find_element_by_xpath('//*[@class="ant-table-content"]/div[2]/div/div/table/tbody/tr/td/div/i[1]').click()
            # 获取商品关联平台商品
            sleep(3)
            getproductcode=self.driver.find_element_by_xpath('//*[@class="ant-table-content"]/div/div[2]/table/tbody/tr/td[1]/span').text
            if getproductcode:
                print('SUP商品关联的平台商品{}'.format(getproductcode))
            else:
                print('SUP关联的平台商品是空')

        else:
            print('查询无此{}商品'.format(SupProductId))
        assert getproductcode


    # @pytest.mark.skip
    @pytest.mark.parametrize('categoryIdL1,categoryIdL2,categoryIdL3,categoryIdL4,sort',[('虚拟货币','腾讯','Q币','1元','1')])
    def test_create_product(self,login,productlist,categoryIdL1,categoryIdL2,categoryIdL3,categoryIdL4,sort):
        self.driver= login
        self.driver.implicitly_wait(4)
        # driver=WebDriver(self.driver)
        number=str(randint(1,999999999))
        numno=randint(0,8)
        print(numno)
        WebDriverWait(self.driver,50,1).until(EC.visibility_of_all_elements_located((By.XPATH, '//span[contains(text(),"我的商品列表")]')))
        self.driver.find_element_by_xpath('//span[contains(text(),"我的商品列表")]').click()
        WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="ant-spin-container"]/div[2]/button[2]')))
        # 新增商品
        self.driver.find_element_by_xpath('//*[@class="ant-spin-container"]/div[2]/button[2]').click()
        sleep(3)
        # 选择一级类目
        self.driver.find_element_by_xpath('//*[@id="categoryIdL1"]/div/div/div[1]').click()
        self.driver.find_element_by_xpath('//input[@id="categoryIdL1"]').send_keys(categoryIdL1)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(3)
        # 选择二级类目
        self.driver.find_element_by_xpath('//*[@id="categoryIdL2"]/div/div/div[1]').click()
        self.driver.find_element_by_xpath('//input[@id="categoryIdL2"]').send_keys(categoryIdL2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(3)
        # 选择三级类目
        self.driver.find_element_by_xpath('//*[@id="categoryIdL3"]/div/div/div[1]').click()
        self.driver.find_element_by_xpath('//input[@id="categoryIdL3"]').send_keys(categoryIdL3)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(3)
        # 选择四级类目
        self.driver.find_element_by_xpath('//*[@id="categoryIdL4"]/div/div/div[1]').click()
        self.driver.find_element_by_xpath('//input[@id="categoryIdL4"]').send_keys(categoryIdL4)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(3)
        # 选择充值类型
        self.driver.find_element_by_xpath('//*[@id="productType"]/div/div/div').click()
        sleep(1.5)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div/ul/li[1]').click()
        # 选择票据信息
        self.driver.find_element_by_xpath('//*[@id="secondInvoiceType"]/div/div/div').click()
        sleep(1.5)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[2]').click()
        sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="invoiceRate"]/div/div').click()
        sleep(1.5)
        self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul/li[3]').click()
        # 获取生成的商品名称
        productname=self.driver.find_element_by_xpath('//*[@id="productName"]').get_attribute('value')
        sleep(2)
        if productname:
            self.driver.find_element_by_xpath('//*[@id="productName"]').clear()
            # global newproductname
            # newproductname=productname+number
            print('新商品：{}'.format(productlist))
            self.driver.find_element_by_xpath('//*[@id="productName"]').send_keys(productlist)
            #  销售状态
            self.driver.find_element_by_xpath('//*[@id="saleStatus"]/div/div').click()
            self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div/ul/li[1]').click()
            sleep(2)
            # 选择关联货源商品,获取货源商品
            self.driver.find_element_by_xpath('//*[@type="button" and @class="ant-btn primary ant-btn-primary"]').click()
            supproductcode_list = []
            print(supproductcode_list)
            for num in range(1,10):
                WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left ant-table-layout-fixed"]/div/div/div/table/tbody/tr[2]/td[4]')))
                supproductcode=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left ant-table-layout-fixed"]/div/div/div/table/tbody/tr[{}]/td[4]'.format(num)).text
                supproductcode_list.append(supproductcode)
            # 搜索商品编号
            print(supproductcode_list)
            self.driver.find_element_by_xpath('//*[@id="SupProductId"]').send_keys(supproductcode_list[numno])
            self.driver.find_element_by_xpath('//button[@type="submit" and @class="ant-btn ant-btn-primary"]').click()
            # 勾选商品
            sleep(3)
            self.driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr/td[2]/span/label/span/input').click()
            # 保存按钮
            self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/div/button[2]').click()
            # 获取关联的SUP商品
            getsupproduct=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left"]').text
            if supproductcode_list[numno] in getsupproduct:
                self.driver.find_element_by_xpath('//*[@class="ant-table-content"]/div[2]/div/div/table/tbody/tr/td/div/div/div/span/input').send_keys(sort)
                # 发布商品
                sleep(2)
                self.driver.find_element_by_xpath('//*[@class="detailfooter"]/button[1]').click()
                WebDriverWait(self.driver, 50, 1).until_not(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="detailfooter"]/button[1]')))
                # 获取已发布的
                self.driver.find_element_by_xpath('//*[@id="ProductName"]').send_keys(productlist)
                # 进行查询
                WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="ant-col ant-col-6 searchFormBtnBox"]/button[1]')))
                sleep(1)
                self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-6 searchFormBtnBox"]/button[1]').click()
                WebDriverWait(self.driver, 50, 1).until(
                    EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left"]')))
                getproductlist=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left"]').text
            else:
                print('没有获取到关联的SUP商品')
        else:
            print('没有生成商品名称')

        assert productlist in getproductlist

    # @pytest.mark.skip
    @pytest.mark.parametrize('MemberCode',[('9079788')])
    def test_set_price(self,login,productlist,MemberCode):
        self.driver = login
        # driver=WebDriver(self.driver)
        self.driver.implicitly_wait(4)
        WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH, '//span[contains(text(),"商品密价设置")]')))
        self.driver.find_element_by_xpath('//span[contains(text(),"商品密价设置")]').click()
        sleep(2)
        # 查询进货商
        self.driver.find_element_by_xpath('//*[@id="MemberCode"]').send_keys(MemberCode)
        self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-6 searchFormBtnBox"]/button[1]').click()
        WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left ant-table-scroll-position-right"]')))
        # 获取查询结果
        sleep(3)
        get_member=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left ant-table-scroll-position-right"]').text
        print('获取查询结果：{}'.format(get_member))
        if MemberCode in get_member:
            # 查看商户密价
            self.driver.find_element_by_xpath('//*[@class="operation-col ant-table-row-cell-break-word"]/div/i[1]').click()
            WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="btngroups"]/button[2]')))
            # 新增商品
            sleep(3)
            self.driver.find_element_by_xpath('//*[@class="btngroups"]/button[2]').click()
            sleep(2)
            print('添加的密价商品：{}'.format(productlist))
            self.driver.find_elements_by_id('productName')[1].send_keys(productlist)
            self.driver.find_elements_by_xpath('//*[@class="ant-btn ant-btn-primary"]')[2].click()
            sleep(3)
            # 获取查询出来的商品数据
            getproduct=self.driver.find_element_by_xpath('//*[@class="tableBox"]').text
            if productlist in getproduct:
                # 选择筛选的商品
                # self.driver.find_elements_by_xpath('//input[@type="checkbox" and @class="ant-checkbox-input"]')[-1].click()
                self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left ant-table-layout-fixed"]/div/div/div/table/tbody/tr/td/span/label/span').click()
                sleep(1.5)
                self.driver.find_element_by_xpath('//*[@class="footerstaff"]/button[1]').click()
                WebDriverWait(self.driver, 50, 1).until(
                    EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left"]')))
                # 获取页面添加的商品
                sleep(5)
                get_product_list=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left"]').text
                print('获取的商品列表：{}'.format(get_product_list))

            else:
                print('没有查询到SUP商品')

        else:
            print('查询密价商户错误')

        assert productlist in get_product_list


    # @pytest.mark.parametrize('MemberCode,saleRoute,estimatedSalesNumber',[('9025272','木易渠道','8')])
    def test_product_report(self,login,deleta_reported,get_product,MemberCode,saleRoute,estimatedSalesNumber):
        file_path='C:\\Users\\EDZ\\Pictures\\Saved Pictures\\截图上传.jpg'
        self.driver=login
        # driver=WebDriver(self.driver)
        WebDriverWait(self.driver, 50, 1).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//span[contains(text(),"商品报备管理")]')))
        self.driver.find_element_by_xpath('//span[contains(text(),"商品报备管理")]').click()
        # 查看报备进货商
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="MemberCode"]').send_keys(MemberCode)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-6 searchFormBtnBox"]/button[1]').click()
        # 获取进货商
        sleep(3)
        report_member=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left ant-table-layout-fixed"]').text
        print('获取的进货商{}'.format(report_member))
        if MemberCode in report_member:
            print('发起报备')
            WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@title="发起报备"]')))
            sleep(3)
            self.driver.find_element_by_xpath('//*[@title="发起报备"]').click()
            sleep(3)
            get_date1 = self.driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]').text
            print('获取审核数量：{}'.format(get_date1))
            num1 = re.findall('[0-9]',get_date1)
            print('初次获取提交的数量：{}'.format(num1))
            # WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="ant-table-scroll"]/div/table/tbody/tr[1]/td[1]/span/label/span/input')))
            # self.driver.find_element_by_xpath('//*[@class="ant-table-scroll"]/div/table/tbody/tr[1]/td[1]/span/label/span/input').click()
            WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="app"]/section/section/main/div[2]/div[3]/div/div/div[2]/button[2]')))
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div[3]/div/div/div[2]/button[2]').click()
            sleep(2)
            # 查询数据
            self.driver.find_element_by_xpath('//*[@placeholder="请输入货源商品编号"]').send_keys(get_product)
            # 输入销售渠道
            self.driver.find_element_by_xpath('//*[@id="saleRoute"]').send_keys(saleRoute)
            # 输入销售形式
            self.driver.find_element_by_xpath('//*[@id="salesTypeName"]').send_keys(saleRoute)
            # 输入预估销量
            self.driver.find_element_by_xpath('//*[@id="estimatedSalesNumber"]').send_keys(estimatedSalesNumber)
            # 提交入口截图
            self.driver.find_element_by_xpath('//input[@type="file"]').send_keys(file_path)
            # 提交报备
            self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-22 ant-col-offset-2"]/button[2]').click()
            WebDriverWait(self.driver, 50, 1).until_not(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="ant-col ant-col-22 ant-col-offset-2"]/button[2]')))
            sleep(2)
            WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]')))
            get_date2 = self.driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]').text
            text_list2=[]
            for text2 in get_date2:
                text_list2.append(text2)
            num2 = text_list2[4:-1]
            print('再次获取提交的数量：{}'.format(num2))
        else:
            print('没有报备的进货商')

        assert num2 > num1

    # pytest.mark.skip
    def test_add_appman(self,add_appman,get_list,login):
        self.driver = login
        # driver=WebDriver(self.driver)
        self.driver.implicitly_wait(4)
        WebDriverWait(self.driver, 50, 1).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//span[contains(text(),"商品回收站")]')))
        self.driver.find_element_by_xpath('//span[contains(text(),"商品回收站")]').click()
        WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="ProductId"]')))
        self.driver.find_element_by_xpath('//*[@id="ProductId"]').send_keys(get_list)
        self.driver.find_element_by_xpath('//*[@class="ant-row"]/div[10]/button[1]').click()
        get_list_data=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left ant-table-scroll-position-right"]').text
        print('添加到回收站的数据：{}'.format(get_list))
        print('获取当前页面的数据：{}'.format(get_list_data))
        if str(get_list) in get_list_data:
            # 商品移除回收站
            WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="operation-col ant-table-row-cell-break-word"]/div/a')))
            self.driver.find_element_by_xpath('//*[@class="operation-col ant-table-row-cell-break-word"]/div/a').click()
            # 二次确认
            WebDriverWait(self.driver, 50, 1).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="ant-popover-buttons"]/button[2]')))
            self.driver.find_element_by_xpath('//*[@class="ant-popover-buttons"]/button[2]').click()
            # 断言
            assdata=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-empty ant-table-layout-fixed ant-table-scroll-position-left ant-table-scroll-position-right"]').text
        else:
            print('没有查询到商品')
        assert str(get_list) not in assdata



















if __name__ == '__main__':
    pytest.main(['-s','porduct_test.py'])


