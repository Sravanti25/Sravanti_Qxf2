"""This program is fill the payment details for the shopping items"""

import time
from selenium import webdriver

class PaymentPage:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
#Navigate to weather Shopper sunscreen page

    def goToURL(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
        time.sleep(4)

#click Add button for all the creams

    def clickAddButton(self):
        list_of_add_buttons = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::button")
        for each_val in list_of_add_buttons:
            each_val.click()
        time.sleep(3)
    
#Click on Cart button to check all creams have been added

    def goToCart(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Cart ')]").click()
        time.sleep(2)

#Do the payment
    def doPayment(self):
        self.driver.find_element_by_xpath("//button/span[contains(text(),'Pay with Card')]").click()
        time.sleep(1)
        #Switch to frame to be able to access the Payment pop-up window
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@name,'stripe_checkout_app')]")
        self.driver.switch_to_frame(iframe)
        time.sleep(2)
        #Enter all the details and click on Pay button
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("sravanti.t30@gmail.com")
        self.driver.find_element_by_xpath("//div[@class='Textbox-inputRow']/descendant::input[@placeholder='Card number']").send_keys("4000007020000003")
        self.driver.find_element_by_xpath("//div[@class='Textbox-inputRow']/descendant::input[@placeholder='MM / YY']").send_keys("0821")
        self.driver.find_element_by_xpath("//div[@class='Textbox-inputRow']/descendant::input[@placeholder='CVC']").send_keys("123")
        self.driver.find_element_by_xpath("//div[@class='Textbox-inputRow']/descendant::input[@placeholder='ZIP Code']").send_keys("560072")
        self.driver.find_element_by_xpath("//a[@class='Checkbox']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='Textbox-inputRow']/descendant::input[@inputmode='tel']").send_keys("123456789")
        self.driver.find_element_by_xpath("//div[@class='Section-button']/button").click()

        time.sleep(3)

        #Switch back from frame to main window
        self.driver.switch_to_default_content()

        time.sleep(4)

#Check whether Payment is successful
    def checkPaymentStatus(self):
        message = self.driver.find_element_by_xpath("//body/descendant::h2").text
        print(message)

        if(message == 'PAYMENT SUCCESS'):
            print("The Payment was successful")
        elif(message == 'PAYMENT FAILED'):
            print("The Payment was not successful")
        else:
            print("Error message")
             
        time.sleep(1)

#Close the browser
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    mois_obj = PaymentPage()
    mois_obj.setUp()
    mois_obj.goToURL()
    mois_obj.clickAddButton()
    mois_obj.goToCart()
    mois_obj.doPayment()
    mois_obj.checkPaymentStatus()
    mois_obj.tearDown()
   

    