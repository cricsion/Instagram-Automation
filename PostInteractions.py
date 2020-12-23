from time import sleep
from Open_Browser import driver
def LikesPost():                   
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click() #Clicks on the like button in posts which are from hastags
        sleep(1)
        return True
    except:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click() #Clicks on the like button the types of post which are opened directly
            sleep(1)
            return True
        except:
            return False

def CommentsOnPost(comment):
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()#Clicks on the input bar
        sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment)#Sends comment
        sleep(0.3)
    except:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click() #Same as in line 10
            sleep(0.5)                    
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(comment)
            sleep(0.3)
        except:
            return False
    driver.find_element_by_xpath('//button[text()="Post"]').click()
    sleep(0.5)
    return True

def OpensLikesPanel():
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div[2]/button').click()
        sleep(2)
    except:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/span').click()
            sleep(2)
        except:
            try:
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button').click()
                sleep(2)
            except:
                return False
    return True
