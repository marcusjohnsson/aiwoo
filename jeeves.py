from config import *
from selenium import webdriver
import time

class Jeeves:
    def __init__(self, orders):
        self.orders = orders
        if self.orders:
            print(f'Jeeves was handed {len(orders)} orders to be processed.')
            self.login_to_postnord()
            for order in self.orders:
                print(f'{order.id} | {order.customer["first_name"]} {order.customer["last_name"]} | {len(order.products)} product(s) worth {order.total}kr')
                # manage order using selenium.
        else:
            print(f'Jeeves got {len(self.orders)} to process, jeeves is done.')

    @staticmethod
    def login_to_postnord():
        driver = webdriver.Firefox()

        print('Jeeves is loading Postnord')
        driver.get('https://portal.postnord.com/login/')

        time.sleep(10)

        print('Jeeves gratefully accept cookies')
        accept_all_cookies_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
        accept_cookies = driver.find_element_by_xpath(accept_all_cookies_button_xpath)
        accept_cookies.click()

        time.sleep(5)

        print('Jeeves fills in the credentials and logs in to postnord')
        email_field_xpath = '//*[@id="email"]'
        password_field_xpath = '//*[@id="password"]'
        login_button_xpath = '/html/body/app-root/app-start/div[1]/form/pn-button-container/button'
        email_element = driver.find_element_by_xpath(email_field_xpath)
        password_element = driver.find_element_by_xpath(password_field_xpath)
        login_button_element = driver.find_element_by_xpath(login_button_xpath)
        email_element.send_keys(POSTNORD_EMAIL)
        password_element.send_keys(POSTNORD_PASSWORD)
        login_button_element.click()

        time.sleep(3)

        print('Jeeves goes to shippingtoolpro')
        # Go to Skicka Direkt Business
        driver.get("https://portal.postnord.com/shippingtoolpro/")

        time.sleep(3)

        print('Jeeve dont need no silly introduction')
        close_intro_xpatch = '/html/body/div[1]/div/onboarding/div/main/material-icon'
        close_intro_element = driver.find_element_by_xpath(close_intro_xpatch)
        close_intro_element.click()



    def new_order(order_object):
        # Initiate new order
        driver.get("https://portal.postnord.com/shippingtoolpro/new-shipment/recipient/add")

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
