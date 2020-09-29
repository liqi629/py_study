from threading import Thread
from selenium.webdriver.common.by import By
# import time
#
# def demo():
#     print("我爱北京")
#     time.sleep(1)
#
# for i in range(5):
#     t = Thread(target=demo)
#     t.start()

class ABC:

    def mysql(self):
        self.name = (By.XPATH, 'aasdasd')

    def oracle(self):
        self.name = (By.XPATH, 'aasASDfASDFdasd')
if __name__ == '__main__':
    a = ABC()
    name = a.mysql()
    print(name)