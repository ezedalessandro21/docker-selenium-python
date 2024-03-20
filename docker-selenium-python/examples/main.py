from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SimpleGoogleTester:
    def __init__(self, url: str, headless: bool = True):
        # Configurar las opciones de Chrome
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Inicializar el WebDriver con las opciones definidas
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)

    def close(self):
        # Cerrar el navegador
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    # Crear una instancia de SimpleGoogleTester y abrir Google
    tester = SimpleGoogleTester("https://www.google.com", headless=True)
    print("Google ha sido abierto en el navegador headless.")
    # Cerrar el navegador
    tester.close()
    print("El navegador se ha cerrado correctamente.")
