from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlsplit

link = []
domain = []
error_count = 0

#open Chrome and sign in to linkedin
browser = webdriver.Chrome()
seconds_before = time.time()
browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")

python_button = browser.find_elements_by_xpath("//*[@id='username']")[0]
python_button.send_keys("1932807205@qq.com")
python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
python_button.send_keys("Meiguo1969")
python_button = browser.find_elements_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")[0]
python_button.submit()

time.sleep(3)

#Go to company linkedin profile
#Go through links in the txt file
with open("link.txt", "r") as l:
    link = l.readlines()
link = [x.strip() for x in link]
#get the number of links
link_number = len(link)
#Go through each link and go to their websites
for i in range(0, link_number):
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
        if(error_count <= 5):
            print("ERROR!")
            error_count += 1
            domain.append("ERROR!")
        else:
            pass
l.close()
d = open("domain.txt", "w")
for i in domain:
    d.write(i)
    d.write("\n")
d.close()
