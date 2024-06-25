from selenium.webdriver.common.by import By


class Locators:
    LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    EMAIL_FOR_AUTHORIZATION = (By.XPATH, ".//label[text() = 'Email']/parent::div/input")  # Инпут с email для авторизации
    PASSWORD_FOR_AUTHORIZATION = (By.XPATH, ".//input[@name = 'Пароль']")  # Инпут с паролем для авторизации
    AUTH_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти" в форме авторизации
    CHECK_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ" для проверки авторизации
    LOGIN_LINK = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти" в формах регистрации и восстанавления пароля
    REGISTRATION_LINK = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")  # Ссылка "Зарегистироваться"
    NAME = (By.XPATH, ".//label[text() = 'Имя']/parent::div/input")  # Инпут для ввода имени в форме регистрации
    EMAIL_FOR_REGISTRATION = (By.XPATH, "//label[text() = 'Email']/parent::div/input")  # Инпут с email для регистрации
    PASSWORD_FOR_REGISTRATION = (By.XPATH, ".//input[@name = 'Пароль']")  # Инпут с паролем для регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']/parent::a")  # Ссылка для перехода в личный кабинет
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"
    LOGIN_TEXT = (By.XPATH, ".//h2[text() = 'Вход']")  # Заголовок в форме авторизации
    CHANGE_PERSONAL_INFORMATION = (By.XPATH, ".//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")  # Параграф об изменении персональных данных
    COLLECT_BURGER = (By.XPATH, ".//h1[text() = 'Соберите бургер']")  # Заголовок "Соберите бургер"
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']")  # Ссылка для восстановления пароля
    INVALID_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # Текст, появляющийся при вводе некорректного пароля
    LOGO_LINK = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")  # Ссылка логотипа Stellar Burger
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text() = 'Конструктор']/parent::a")  # Ссылка для перехода в раздел "Конструктор"
    CONSTRUCTOR_SAUCES = (By.XPATH, ".//span[text() = 'Соусы']/parent::div")  # Раздел "Соусы" в конструкторе
    CONSTRUCTOR_FILLINGS = (By.XPATH, ".//span[text() = 'Начинки']/parent::div")  # Раздел "Начинки" в конструкторе
    CONSTRUCTOR_BUNS = (By.XPATH, ".//span[text() = 'Булки']/parent::div")  # Раздел "Булки" в конструкторе
