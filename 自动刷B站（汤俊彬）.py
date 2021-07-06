from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

import time
server = "http://localhost:4723/wd/hub"
param = {
			  "deviceName": "cb409526",
			  "platformName": "Android",
			  "platformVersion": "10",
			  "appPackage": "tv.danmaku.bili",
			  "appActivity": "tv.danmaku.bili.MainActivityV2"
}
driver=webdriver.Remote(server,param)
time.sleep(20)
TouchAction(driver).tap(x=590, y=1706).perform()
time.sleep(5)

a=0
while True:
	if a<5:
		driver.swipe(500,1500,500,500,800)
		time.sleep(5)
		a+=1
	else:
		break


