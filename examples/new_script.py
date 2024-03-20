import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurar logging
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class SimpleGoogleTester:
    def __init__(self, url: str, headless: bool = True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)
        logging.info("Google ha sido abierto en el navegador headless.")

    def close(self):
        if self.driver:
            self.driver.quit()
            logging.info("El navegador se ha cerrado correctamente.")

if __name__ == "__main__":
    tester = SimpleGoogleTester("https://www.google.com", headless=True)
    tester.close()
