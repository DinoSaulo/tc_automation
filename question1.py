from selenium import webdriver
import time
import unittest
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.republicavirtual.com.br/cep/exemplos.php")

    def testAddressData(self):
        self.driver.find_element(By.ID, "campoCEP").send_keys('50030230')
        self.driver.find_element(By.CSS_SELECTOR, "input[value='buscar cep']").click()

        time.sleep(2)

        address_data_table = self.driver.find_elements(By.CSS_SELECTOR, "#resultado table tbody tr")

        self.assertTrue(address_data_table[0].text.__contains__("Tipo de logradouro: "))
        self.assertTrue(address_data_table[1].text.__contains__("Logradouro: "))
        self.assertTrue(address_data_table[2].text.__contains__("Bairro: "))
        self.assertTrue(address_data_table[3].text.__contains__("Logradouro: "))
        self.assertTrue(address_data_table[4].text.__contains__("UF: "))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
	unittest.main()