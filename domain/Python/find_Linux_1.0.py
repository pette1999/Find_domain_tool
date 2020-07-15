from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlsplit
import manageData
#https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

link = []
domain = []
final_domain = []
error_index = []
dot_index = []
error_count = 0
dot_count = 0

#https://intoli.com/blog/running-selenium-with-headless-chrome/
#open Chrome and sign in to linkedin
options = webdriver.ChromeOptions()
# tell selenium to use the dev channel version of chrome
# options.binary_location = '/usr/bin/google-chrome-unstable'
options.add_argument('headless')
# set the window size
options.add_argument('window-size=1200x600')

# initialize the driver
browser = webdriver.Chrome(chrome_options=options)
browser.set_page_load_timeout(9)

seconds_before = time.time()
browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
print("Connecting to Linkedin.com...")

python_button = browser.find_elements_by_xpath("//*[@id='username']")[0]
python_button.send_keys("1932807205@qq.com")
python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
python_button.send_keys("Meiguo1969")
python_button = browser.find_elements_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")[0]
python_button.submit()
print("Logging in...")

time.sleep(3)

# get links from Googlesheets
print("Getting domains...\n")
link = manageData.getList();

link = [x.strip() for x in link]
#get the number of links
link_number = len(link)
#Go through each link and go to their websites
for i in range(0,link_number):
    #switch to the first webpage in the browser
    browser.switch_to_window(browser.window_handles[0])
    browser.get(link[i] + "/about/")

    time.sleep(2)

    #https://stackoverflow.com/questions/43021434/click-button-by-find-element-by-class-name-not-working-python-selenium-webdriver
    try:
        python_button = browser.find_elements_by_xpath("//a[@data-control-name='page_details_module_website_external_link']")[0]
        python_button.click()

        browser.switch_to_window(browser.window_handles[1])

        time.sleep(2)

        #get current URl from the browser
        company_url = browser.current_url
        #get the domain name from the URL
        company_domain = "{0.scheme}://{0.netloc}/".format(urlsplit(company_url))
        print(company_domain)
        #add the domain to the DOMAIN LIST
        domain.append(company_domain)
        seconds_after = time.time()
        total_time = "{:.2f}".format(seconds_after - seconds_before)
        print(i, ", ", "Total time use =", total_time)
        print("=================================")
        browser.close()
    except:
        # if(error_count<=5):
        #     print("ERROR!")
        #     error_count += 1
        #     domain.append("ERROR!")
        # else:
        #     pass
        print("ERROR!")
        error_count += 1
        domain.append("ERROR!")
# l.close()

def replacement(a,b):
    global domain
    final_domain = []
    for i in domain:
        final_domain.append(i.replace(a,b))
    domain = []
    for i in final_domain:
        domain.append(i)


replacement("https://www.", "")
replacement("https://www2.", "")
replacement("http://www.", "")
replacement("www.", "")
replacement("jobs.", "")
replacement("careers.", "")
replacement("https://", "")
replacement("http://", "")
replacement("/", "")

for i in domain:
    if i == "ERROR":
        error_count += 1
        print(domain.index(i))
        error_index.append(domain.index(i) + 1)
    else:
        continue

for j in domain:
    dot_count = 0

    for k in j:
        if k == '.':
            dot_count += 1
        else:
            continue
            
    if dot_count > 1:
         dot_index.append(domain.index(j) + 1)
    else:
        continue

# write output domains to google sheets
manageData.writeList(domain)

print("ERROR#: ", error_count)
print("ERROR index: ", error_index)
print("Dot index: ", dot_index)
