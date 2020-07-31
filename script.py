from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Firefox(executable_path='C:/Users/rkjus/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe')

print('Step-1 Passesd...')
valid_url_list = []


def datacheck():
    url_list = ['http://blog.0800handyman.co.uk', 'https://gochatclub.com', 'http://blog.gardenmediagroup.com']
    valid_count = 0
    count_total = 0
    invalid_count = 0
    for i in url_list:
        try:
            driver.get(i)
            count_total += 1
            print(i)
            # press_comment = driver.find_element_by_class_name("comment-link")
            # press_comment.click()
            comment = driver.find_element_by_id('comment')
            author = driver.find_element_by_id('author')
            email = driver.find_element_by_id('email')
            submit = driver.find_element_by_id('submit')
            if (comment and author and email and submit):
                print('All parameters are available.')
                # print('Step-2 Passed')
                valid_count += 1
                print("Valid URL - ", valid_count)
                # print("URL - ", driver.current_url)
                valid_url_list.append(i)
            else:
                print('Oops check another blog')
                print('Step-2 Failed')
                invalid_count += 1
                print("InValid URL - ", invalid_count)
        except FileNotFoundError:
            print("File not found")
            continue
        except ConnectionError:
            print("Connection error")
            continue
        except Exception as e:
            print(e)
            continue
        print("Total URL Count - ", count_total)
        # print("Valid URL - ", valid_count)
        # print("InValid URL - ", invalid_count)


datacheck()
print('Final Step Passed')
# file2 = open("list of urls.txt", "a")
# for link in valid_url_list:
#     file2.write("'")
#     file2.write(link)
#     file2.write("'")
#     file2.write(",")
# # print(valid_url_list)
# file2.close()
