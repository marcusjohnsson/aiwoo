from aiwoo_api import *
from config import *
from selenium import webdriver
from orders import *
import time


def login_to_postnord():
    driver = webdriver.Firefox()
    driver.get('https://portal.postnord.com/login/')

    time.sleep(5)

    # Accept cookies
    accept_all_cookies_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
    accept_cookies = driver.find_element_by_xpath(accept_all_cookies_button_xpath)
    accept_cookies.click()

    time.sleep(2)

    # Fill in credentials and login
    email_field_xpath = '//*[@id="email"]'
    password_field_xpath = '//*[@id="password"]'
    login_button_xpath = '/html/body/app-root/app-start/div[1]/form/pn-button-container/button'
    email_element = driver.find_element_by_xpath(email_field_xpath)
    password_element = driver.find_element_by_xpath(password_field_xpath)
    login_button_element = driver.find_element_by_xpath(login_button_xpath)
    email_element.send_keys(POSTNORD_EMAIL)
    password_element.send_keys(POSTNORD_PASSWORD)
    login_button_element.click()

    time.sleep(5)

    # Go to Skicka Direkt Business
    driver.get("https://portal.postnord.com/shippingtoolpro/")

    time.sleep(5)

    # Close introduction screen
    close_intro_xpatch = '/html/body/div[1]/div/onboarding/div/main/material-icon'
    close_intro_element = driver.find_element_by_xpath(close_intro_xpatch)
    close_intro_element.click()

    # Initiate new order
    # press frakt // redir to @Page Mottagare

    # @Page Mottagare
    # State För och Efternamn '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[3]/div/field-label[1]/label/ng-transclude/input'
    # if c/o not empty state co '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[3]/div/field-label[1]/label/ng-transclude/input'
    # state Adress1 '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[1]/field-label/label/ng-transclude/input'
    # state Adress2 '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[2]/field-label/label/ng-transclude/input'
    # state Postnummer '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[2]/field-label/label/ng-transclude/input'
    # state Phone Number: '//*[@id="recipient-tel"]'
    # state Email '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[3]/field-label[1]/label/ng-transclude/input'
    # click Välj försändelse '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/button'

    # Välj Försändelse
    # Click Lätt : '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type/fieldset/div/label[1]/input'
    # Depending on weight: '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-weight/fieldset/label/div[1]/input'
    # 250g valueNow= 3
    # 500g valueNow= 4
    # 1kg valueNow= 5
    # 2kg valueNow= 6
    # Click Klimatkompensation '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-addons/fieldset[2]/div/div[2]/new-shipment-details-addon/div/div/label/input'
    # np_empty / ng_not_empty
    # state Bokningsref '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-description/fieldset/div[1]/field-label[1]/label/ng-transclude/input'
    # state Beskrivning '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-description/fieldset/div[1]/field-label[2]/label/ng-transclude/input'
    # click spara försändelse

    ### @Page Sammanfattning https://portal.postnord.com/shippingtoolpro/new-shipment/summary

    # if more orders:
    # click Lägg till försändelse '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-summary/header/a'
    # repeat from @Page Mottagare
    # else:
    # click Bekräfta Order '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-summary/button"


def main():
    # cred = {
    #     "url": "https://portal.postnord.com/login/"
    # }
    #
    # login_to_postnord()

    orders = get_orders('processing')
    print([o.customer for o in orders])
    # orders = fetch_all_orders("processing")
    # print([is_member(order['customer_id']) for order in orders])
    # for order in orders:
    #
    #     print(is_member(order["customer_id"]), order["id"])


if __name__ == '__main__':
    main()
