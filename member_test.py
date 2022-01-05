from time import sleep

import pytest

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, EventFiringWebElement
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class Test_Member():
    def setup(self):
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        # self.driver.maximize_window()
        # self.phone = "17802711551"
        # self.password = 'ts123456'
        # number=randint(1,9999999)
        # yangxudong='木易新建链接'+number
        pass



    def teardown(self):
        # self.driver = WebDriver(self.driver)
        self.driver.quit()

    @pytest.mark.skip
    @pytest.mark.parametrize('membername,GroupName,operation,groupname',[('木易-pre商户测试','测试分组','陈峰','全部')])
    def test_member_list(self,login,membername,GroupName,operation,groupname):
        self.driver = login
        sleep(3)
        self.driver.find_element_by_xpath('//span[contains(text(),"进货商户列表")]').click()
        # 查询商户名称
        self.driver.find_element_by_id('name')
        self.driver.find_element_by_id('name').send_keys(membername)
        print("确定按钮")
        sleep(5)
        # self.driver.find_element_by_xpath('//button[@type="submit" and @class="ant-btn ant-btn-primary"]').click()
        # # 创建分组
        # sleep(3)
        # self.driver.find_element_by_xpath('//*[@class="ant-tabs-extra-content"]/button[2]').click()
        # # 输入分组名称
        # self.driver.find_element_by_xpath('//*[@id="GroupName"]').send_keys(GroupName)
        # self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button[2]').click()
        # sleep(2)
        # # 获取新增分组
        groupname=self.driver.find_element_by_xpath('//*[@class="ant-tabs-nav-scroll"]').text
        print('获取现有分组信息：{}'.format(groupname))

        print('测试分组（0）' in groupname)
        if '测试分组（0）' not in groupname:
            # 创建分组
            sleep(3)
            self.driver.find_element_by_xpath('//*[@class="ant-tabs-extra-content"]/button[2]').click()
            # 输入分组名称
            self.driver.find_element_by_xpath('//*[@id="GroupName"]').send_keys(GroupName)
            self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button[2]').click()
            sleep(5)
            Groupname_list = self.driver.find_element_by_xpath('//*[@class="ant-tabs-nav-scroll"]').text
        else:
            print("删除现有分组")
            self.driver.find_element_by_xpath(
                '//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[3]/div/i').click()
            # 删除分组
            self.driver.find_element_by_xpath('//*[@class="ant-modal-body"]/div/div[2]/button[2]')
            sleep(2)
            self.driver.find_element_by_xpath('//*[@class="ant-modal-body"]/div/div[2]/button[2]').click()
            # 创建分组
            sleep(3)
            self.driver.find_element_by_xpath('//*[@class="ant-tabs-extra-content"]/button[2]').click()
            # 输入分组名称
            self.driver.find_element_by_xpath('//*[@id="GroupName"]').send_keys(GroupName)
            self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button[2]').click()
            sleep(5)
        groupname_list=self.driver.find_element_by_xpath('//*[@class="ant-tabs-nav-scroll"]').text
        memberlist=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-scroll-position-left ant-table-layout-fixed"]').text
        print(GroupName)
        print(memberlist)
        print(groupname_list)
        assert GroupName in groupname_list
        assert membername in memberlist



    # @pytest.mark.skip
    @pytest.mark.parametrize('linkname,promoterMembername,profitCentername,cooperationCompanyname,username',[('yangxudong','新注册商户','腾讯组','武汉福禄集团','杨旭东')])
    def test_create_link(self,login, linkname, promoterMembername,profitCentername,cooperationCompanyname,username):
        self.driver = login
        number = str(randint(1, 9999999))

        sleep(2.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"邀请注册链接")]').click()
        sleep(2.5)
        # iframe = self.driver.find_element_by_tag_name("kfiframe")
        # self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('//*[@class="ant-spin-container"]/div[2]/button').click()
        sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="linkName"]').click()
        self.driver.find_element_by_xpath('//*[@id="linkName"]').send_keys(linkname+number)
        sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="promoterMemberId"]').click()
        self.driver.find_element_by_xpath('//*[@id="promoterMemberId" and @class="ant-select-search__field"]').send_keys(promoterMembername)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="profitCenterId"]').click()
        self.driver.find_element_by_xpath('//*[@id="profitCenterId" and @class="ant-select-search__field"]').send_keys(profitCentername)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="cooperationCompanyId"]').click()
        self.driver.find_element_by_xpath('//*[@id="cooperationCompanyId" and @class="ant-select-search__field"]').send_keys(cooperationCompanyname)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="userId"]').click()
        self.driver.find_element_by_xpath('//*[@id="userId" and @class="ant-select-search__field"]').send_keys(username)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(2.5)
        self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button[2]').click()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        sleep(5)
        # 获取链接名称
        elem=self.driver.find_element_by_xpath('//tbody[@class="ant-table-tbody"]/tr[1]/td[1]/span').text
        print("获取元素：{}".format(elem))
        print("定位元素：{}".format(linkname+number))
        assert elem == linkname+number

    @pytest.mark.skip
    @pytest.mark.parametrize('num,name',[('20','测试规则')])
    def test_ambassador_rule(self,login,num,name):
        self.driver = login
        sleep(4)
        self.driver.find_element_by_xpath('//span[contains(text(),"推广规则设置")]').click()
        sleep(3)
        # 获取返佣规则列表
        rule_list=self.driver.find_element_by_xpath('//*[@class="RebateRulesBase-containter"]').text
        print(rule_list)
        if "暂无数据" in rule_list :
            self.driver.find_element_by_xpath('//*[@class="ant-spin-container"]/div[2]/button').click()  # 创建返佣规则
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="name"]').click()
            self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="commisionRate"]').click()
            self.driver.find_element_by_xpath('//*[@id="commisionRate"]').send_keys(num)
            sleep(3)
            #       创建返佣规则
            self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-offset-4"]/button[1]').click()
            # 获取新增数据属性
            rules = self.driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr[1]/td[2]').text
            text_s = self.driver.find_element_by_xpath('//*[@class="fulu-table small-padding fl-tb-ellipsis"]/div').text
            print(text_s)
        else:
            sleep(3)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/section/main/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div/div/table/tbody/tr/td/div/span[2]').click()
            sleep(2)
            elem = self.driver.find_element_by_xpath('//*[@class="ant-modal-content"]/div[2]').text
            if elem == '是否确认删除该规则？':
                self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/div/button[2]').click()
                sleep(3)
                self.driver.find_element_by_xpath('//*[@class="ant-spin-container"]/div[2]/button').click()  # 创建返佣规则
                sleep(3)
                self.driver.find_element_by_xpath('//*[@id="name"]').click()
                self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
                sleep(3)
                self.driver.find_element_by_xpath('//*[@id="commisionRate"]').click()
                self.driver.find_element_by_xpath('//*[@id="commisionRate"]').send_keys(num)
                sleep(3)
                #       创建返佣规则
                self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-offset-4"]/button[1]').click()
                # 获取新增数据属性
                rules = self.driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr[1]/td[2]').text
                text_s = self.driver.find_element_by_xpath(
                    '//*[@class="fulu-table small-padding fl-tb-ellipsis"]/div').text
                print(text_s)
            else:
                print('弹窗缺失')

        assert rules == name


    @pytest.mark.skip
    @pytest.mark.parametrize('ProductId,number',[('17105404','30')])
    def test_ambassador_tool(self,login,ProductId,number):
        self.driver = login
        sleep(2.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"推广价格设置")]').click()
        sleep(2.5)
        # 查询私有商品
        self.driver.find_element_by_xpath('//*[@id="ProductId"]').send_keys(ProductId)
        self.driver.find_element_by_xpath('//*[@type="submit" and @class="ant-btn ant-btn-primary"]').click()
        sleep(2.5)
        Productnumber=self.driver.find_element_by_xpath('//*[@class="ant-table-fixed-columns-in-body ant-table-row-cell-break-word"]/span').text
        print(Productnumber)
        if Productnumber==ProductId:
            self.driver.find_element_by_xpath('//*[@class="ant-table-row ant-table-row-level-0"]/td[9]/span').click()
            self.driver.find_element_by_xpath('//*[@class="ant-table-row ant-table-row-level-0"]/td[9]/input').send_keys(number)
            self.driver.find_element_by_xpath('//*[@type="submit" and @class="ant-btn ant-btn-primary"]').click()
            #获取弹窗
            elem=self.driver.find_element_by_xpath('//*[@class="ant-modal-confirm-body"]/div').text
            if elem:
                self.driver.find_element_by_xpath('//*[ @class="ant-modal-confirm-btns"]/button[2]').click()
            else:
                print('设置失败')
        else:
            print('无此商品')

        value = self.driver.find_element_by_xpath('//*[@class="ant-table-row ant-table-row-level-0"]/td[9]/input').text
        print(value)
        assert value==number

    @pytest.mark.skip
    @pytest.mark.parametrize('membercode,dealerMemberCode,DealerMemberCode',[('9673565','9105603','9105603')])
    def test_ambassador_manage(self,login,membercode,dealerMemberCode,DealerMemberCode):
        self.driver = login
        sleep(2.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"推广大使管理")]').click()
        # 查询推广大使
        self.driver.find_element_by_xpath('//*[@id="fpMemberCode"]').send_keys(membercode)
        self.driver.find_element_by_xpath('//*[@type="submit" and @class="ant-btn ant-btn-primary"]').click()
        sleep(2)
        #获取商户
        membernumber=self.driver.find_element_by_xpath('//*[@class="ant-table-row ant-table-row-level-0"]/td[2]/span').text
        print(membernumber)
        sleep(2)
        if membernumber==membercode:
            self.driver.find_element_by_xpath('//*[@class="operation-col ant-table-row-cell-break-word"]/div/a[1]').click()
            # 查看绑定进货商
            self.driver.find_element_by_xpath('//*[@id="dealerMemberCode"]').send_keys(dealerMemberCode)
            sleep(3)
            self.driver.find_element_by_xpath('//*[@type="submit" and @class="ant-btn ant-btn-primary"]').click()
            # 获取列表用户信息
            member= self.driver.find_element_by_xpath('//*[@class="ant-table-wrapper"]/div/div/div').text
            if dealerMemberCode not in member:
                self.driver.find_element_by_xpath('//*[@class="ant-spin-container" ]/button').click() # 绑定进货商
                self.driver.find_element_by_xpath('//*[@id="DealerMemberCode"]').send_keys(DealerMemberCode)
                sleep(2)
                self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-8 searchFormBtnBox"]/button[1]').click()
                #获取进货商户
                Dealer=self.driver.find_element_by_xpath('//*[@class="ant-modal-body"]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/span').text
                if Dealer:
                    sleep(2)
                    self.driver.find_element_by_xpath('//*[@class="ant-modal-body"]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td/span/label/span/input').click()
                    # 确定
                    self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button[2]').click()
                    # 重置
                    self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-6 searchFormBtnBox"]/button[2]').click()
                    sleep(2)
                    # 获取绑定进货商数据
                    DealerMemberlist=self.driver.find_element_by_xpath('//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left ant-table-scroll-position-right"]').text
                else:
                    print('没有绑定进货商')
            else:
                self.driver.find_element_by_xpath('//*[@class="operation-col ant-table-row-cell-break-word"]/a').click() # 移除进货商
                self.driver.find_element_by_xpath('//*[@class="ant-modal-confirm-body-wrapper"]/div[2]/button[2]').click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@class="ant-spin-container" ]/button').click() # 绑定进货商
                self.driver.find_element_by_xpath('//*[@id="DealerMemberCode"]').send_keys(DealerMemberCode)
                sleep(2)
                self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-8 searchFormBtnBox"]/button[1]').click()
                sleep(2)
                self.driver.find_element_by_xpath(
                    '//*[@class="ant-modal-body"]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td/span/label/span/input').click()
                # 确定
                self.driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button[2]').click()
                sleep(2)
                # 重置
                self.driver.find_element_by_xpath('//*[@class="ant-col ant-col-6 searchFormBtnBox"]/button[2]').click()
                sleep(2)
                # 获取绑定进货商数据
                DealerMemberlist = self.driver.find_element_by_xpath(
                    '//*[@class="ant-table ant-table-small ant-table-bordered ant-table-layout-fixed ant-table-scroll-position-left ant-table-scroll-position-right"]').text
        else:
            print('无此商户')

        assert DealerMemberCode in DealerMemberlist









#
if __name__ == '__main__':
    pytest.main(['-s','member_test.py::test_ambassador_manage'])
