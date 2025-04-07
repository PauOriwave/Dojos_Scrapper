from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Diccionario para almacenar los datos
taekwondo_cef_data = {}

def configure_driver():
    chromium_options = Options()
    chromium_options.binary_location = r"c:\Users\paw_f\Desktop\chromium.exe"  # Navegador
    chromium_options.add_argument("--headless")  # Opcional: sin ventana
    chromium_options.add_argument("--ignore-certificate-errors")
    chromium_options.add_argument("--ignore-ssl-errors")
    chromium_options.add_argument("--window-size=1920,1080")

    # AQUÍ usas chromedriver, NO chromium
    driver = webdriver.Chrome(
        service=Service(r"c:\Users\paw_f\Desktop\chromedriver.exe"),
        options=chromium_options
    )
    return driver

def busqueda_horarios():
    global taekwondo_cef_data
    url = "http://barcelonacef.com/"

    # Configurar el driver
    driver = configure_driver()

    try:
        # Navegar a la URL
        driver.get(url)

        # Ejemplo: Extraer el título de la página
        title = driver.title
        taekwondo_cef_data['title'] = title

        # Extraer todos los elementos ul que contienen span
        ul_elements = driver.find_elements(By.CSS_SELECTOR, "ul")  # Encuentra todos los ul

        all_span_texts = []  # Lista para almacenar todos los textos de los spans

        for ul in ul_elements:
            spans = ul.find_elements(By.TAG_NAME, "span")  # Encuentra todos los span dentro de cada ul
            span_texts = [span.text for span in spans]  # Extrae el texto de cada span
            if span_texts:
                all_span_texts.append(span_texts)  # Añade la lista de textos a la lista general

        # Asignar todos los textos de spans al diccionario
        if all_span_texts:
            taekwondo_cef_data['ul_spans'] = all_span_texts

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar el navegador
        driver.quit()

    # Imprimir los datos extraídos
    print(taekwondo_cef_data)

# Llamar a la función
busqueda_horarios()