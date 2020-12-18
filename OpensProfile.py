from Open_Browser import driver
from time import sleep
from Login import username

driver.get('https://www.instagram.com/{}/'.format(username))
sleep(3)