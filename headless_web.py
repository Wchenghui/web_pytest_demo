from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import platform

print(platform.system())
if platform.system() == 'Windows':
    chrome_options =  Options()
    chrome_options.add_argument('--window-size=1920,1080')
    # 设置当前窗口的宽度和高度
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
else:
    # linux启动
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')  #禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
    driver = webdriver.Chrome(options=chrome_options)

driver.get("https://blog.csdn.net/qq_23378119")
time.sleep(2)
print(driver.title)
print(driver.page_source)
driver.quit()