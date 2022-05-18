from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from hamcrest import *

# URL do site
base_url = "http://www.republicavirtual.com.br/cep/exemplos.php"

# Variáveis com os elementos
input_cep_id = 'campoCEP'
btn_buscar_cep_css_selector = "input[value='buscar cep']"

@given(u'I am on Republica Virtuals CEP code search screen')
def step_impl(context):
    context.web.get(base_url)

@when(u'I inform the CEP code {CEP}')
def step_impl(context, CEP):
    context.web.find_element(By.ID, input_cep_id).send_keys(CEP)

@when(u'I click on the button {button_title}')
def step_impl(context, button_title):
    context.web.find_element(By.CSS_SELECTOR, btn_buscar_cep_css_selector).click()

@then(u'I see the address data')
def step_impl(context):
    time.sleep(2)

    address_data_table = context.web.find_elements(By.CSS_SELECTOR, "#resultado table tbody tr")

    assert_that(address_data_table[0].text.__contains__("Tipo de logradouro: "), is_(True), f"The 'Tipo de logradour' was not found")
    assert_that(address_data_table[1].text.__contains__("Logradouro: "), is_(True), f"The 'Logradouro' was not found")
    assert_that(address_data_table[2].text.__contains__("Bairro: "), is_(True), f"The 'Bairro' was not found")
    assert_that(address_data_table[3].text.__contains__("Logradouro: "), is_(True), f"The 'logradouro' was not found") # the correct title to this row is "Cidade" #bug
    assert_that(address_data_table[4].text.__contains__("UF: "), is_(True), f"The 'UF' was not found")