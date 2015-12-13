from splinter.browser import Browser
from time import sleep
#traceback模块 跟踪异常返回信息
import traceback
#winsound模块 发出声音 only wma,mp3
import winsound

#ConfigParser模块 读取配置文件
import configparser
import string, os, sys


#引用winform来弹窗
import ctypes 

# 读取配置文件
cf = configparser.ConfigParser() 
cf.read("app.conf")

# 设定用户名，密码
uname = cf.get("user", "name")
upasswd=cf.get("user", "password")

print ("username:"+uname);


# 起始地址的cookies值要自己去找
start_sta = u"%u6DF1%u5733%2CSZQ"
end_sta =u"%u5357%u660C%2CNCG"

print (start_sta+"/"+end_sta);


# 时间格式2016-02-01

dtime = u"2016-01-29"

# 车次，选择第几趟，0则从上之下依次点击

order = 2

#设定乘客姓名

pa = u"何抱东"


#设定乘坐类型

train_type = u"Z-直达"


#设定乘坐车次

train_no = u"Z186"


#设定网址

ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"

login_url = "https://kyfw.12306.cn/otn/login/init"

initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"


#登录网站

def login():
    b.find_by_text(u"登录").click();
    sleep(3);
#自动登录，uname是12306账号名，upasswd是12306密码
    b.fill("loginUserDTO.user_name", uname)
    sleep(1)
    b.fill("userDTO.password", upasswd)
    sleep(1)
    print(u"等待验证码，自行输入...")
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break

#购票

def huoche():
    global b
#使用splinter打开chrome浏览器
    b = Browser(driver_name="chrome")
#返回购票页面
    b.visit(ticket_url)
    while b.is_text_present(u"登录"):
        sleep(1)
        login()
        if b.url == initmy_url:
            break;
    try:
        print (u"购票页面...");
        # 跳回购票页面
        b.visit(ticket_url)
        # 加载查询信息
        b.cookies.add({"_jc_save_fromStation": start_sta})
        b.cookies.add({"_jc_save_toStation": end_sta})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()
        sleep(2)
        count = 0
        # 选择车次
        
        #b.find_by_id(u"show_more").click();
        #b.find_by_id(u"inp-train").fill(train_no);
        #b.find_by_id(u"add-train").click();
        #b.find_by_id(u"show_more").click();

        # 选择类型
        b.find_by_text(train_type).click()
        
        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count +=1
                print (u"循环点击查询... 第 %s 次" % count)
                sleep(1)
                try:
                    b.find_by_text(u"预订")[order - 1].click()
                except:
                    print (u"不能预订")
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print (u"循环点击查询... 第 %s 次" % count)
                sleep(1)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except:
                    print (u"不能预订")
                    continue
        sleep(1)
        b.find_by_text(pa)[1].click()
        winsound.Beep(300, 3000);
        ctypes.windll.user32.MessageBoxW(0,u'看票', u'票来了',0)
        print  (u"快输入验证码抢票啊啊  啊")
    except Exception as e:
        print(traceback.print_exc())
if __name__ == "__main__":
    huoche()


