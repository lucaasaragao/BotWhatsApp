from selenium import webdriver
import time

class WhatsAppBotRegiao:
    def __init__(self):
        self.post = ["Segunda via", "10246287446", "935998216"]
        self.bots = ["Gisa Sergipe"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def postMenssage(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for bot in self.bots:
            bot = self.driver.find_element_by_xpath(f"//span[@title='{bot}']")
            time.sleep(3)
            bot.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse') #pode mudar de acordo com a versão do chromeDrive
            time.sleep(3)
            chat_box.click()
            #Aqui vou pegar mensagem por mensagem
            for _msg in self.post:
                _msg = chat_box.send_keys(_msg)
                buttom_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)
                buttom_send.click()
                time.sleep(8)


runTester = WhatsAppBotRegiao()
runTester.postMenssage()