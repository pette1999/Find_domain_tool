from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlsplit
import manageData
import validators  # https://validators.readthedocs.io/en/latest/#
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

seconds_before = time.time()
record = seconds_before

def login():
    browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
    print("Connecting to Linkedin.com...")
    python_button = browser.find_elements_by_xpath("//*[@id='username']")[0]
    python_button.send_keys("1932807205@qq.com")
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys("Meiguo1969")
    python_button = browser.find_elements_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")[0]
    python_button.submit()
    print("Logging in...")
login()

time.sleep(3)

# get links from Googlesheets
print("Getting domains...")
link = manageData.getList();
print("Got Lists..\n")

link = [x.strip() for x in link]
#get the number of links
link_number = len(link)
#Go through each link and go to their websites
for i in range(0,link_number):
    # check if it is a link
    if validators.url(link[i]):
        pass
    else:
        print("This is not a valid link!")
        domain.append("ERROR")
        error_count += 1
        continue

    #switch to the first webpage in the browser
    browser.switch_to_window(browser.window_handles[0])
    try:
        browser.set_page_load_timeout(10)
        browser.get(link[i] + "/about/")

        time.sleep(2)
    except:
        print(link[i] + "/about/")

    #https://stackoverflow.com/questions/43021434/click-button-by-find-element-by-class-name-not-working-python-selenium-webdriver
    try:
        python_button = browser.find_elements_by_xpath("//a[@data-control-name='page_details_module_website_external_link']")[0]
        python_button.click()

        browser.switch_to_window(browser.window_handles[1])

        time.sleep(2)
        pin = time.time()
        #get current URl from the browser
        company_url = browser.current_url
        #get the domain name from the URL
        company_domain = "{0.scheme}://{0.netloc}/".format(
            urlsplit(company_url))
        print(company_domain)
        #add the domain to the DOMAIN LIST
        domain.append(company_domain)
        seconds_after = time.time()
        session = seconds_after - record
        # take a record of current time
        record = seconds_after
        total_time = "{:.2f}".format(seconds_after - seconds_before)
        session_time = "{:.2f}".format(session)
        print(i, ", ", "Total time use =", total_time,
              ", Session time use =", session_time)
        print("=================================")
        browser.close()
    except:
        print("ERROR!")
        domain.append("ERROR")
        error_count += 1
        # browser.close()
        # if(error_count<=5):
        #     print("ERROR!")
        #     error_count += 1
        #     domain.append("ERROR!")
        # else:
        #     pass
# l.close()

print("domain list length: ", len(domain))

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

# https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
# get Index of duplicates items in a python list
def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc+1)
            start_at = loc
    return locs


error_index = list_duplicates_of(domain, "ERROR")

def check_dot_domain():
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

check_dot_domain()

# clean the dot domains
# arr1 -> dot_index
# arr2 -> domain
def clean_domain(arr1, arr2):
    for i in arr1:
        temp = arr2[i-1]
        temp_length = len(temp)
        tail = temp[temp_length-3:temp_length]
        if tail == "com":
            index = temp.index(".")
            temp = temp[index+1:temp_length]
            replacement(arr2[i-1], temp)
        else:
            print("Something is wrong with clean_domain function")

clean_domain(dot_index, domain)

# write output domains to google sheets
manageData.writeList(domain)

dot_index = []
check_dot_domain()

print("ERROR#: ", error_count)
print("ERROR index: ", error_index)
print("Dot index: ", dot_index)