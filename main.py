import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager


LOGIN = "demo-tt1@inet-yar.ru"  # Для удобства проверки не стал убирать переменные в .env файл
PASSWORD = "rNCV14la"


def main():
    """Основная функция."""
    with webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager().install())
    ) as driver:

        result_text = ""
        driver.get("https://proxy6.net/")
        time.sleep(2)
        driver.find_element(
            By.CLASS_NAME, "icon-login"
        ).click()  # Нажатие кнопки войти
        time.sleep(2)

        email_input = driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys(LOGIN)  # Вводим логин в форму

        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(PASSWORD)  # Вводим парроль в форму
        time.sleep(30)  # Пункт с reCAPTCHA
        password_input.send_keys(Keys.ENTER)

        time.sleep(10)
        for elem in driver.find_elements(
            By.XPATH, ".//ul[@class = 'list-dotted user_list_dotted']"
        ):  # Получаем таблицу прокси
            elem_text = elem.text.split()

            if len(elem_text[1]) > 10:  # Формируем текст для вывода в консоль
                result_text += f"{elem_text[1]} - "
            else:
                result_text += f"{elem_text[1]} {elem_text[2]}\n"

        print(result_text[:-1])  # Печатаем результат.


if __name__ == "__main__":
    main()
