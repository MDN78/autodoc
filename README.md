# Проект по тестированию сервиса поиска и подбора автозпчастей, интернет магазин "Автодок"

----
> AUTODOC.RU – ведущий продавец автозапчастей в России с 1998 года. Является одним из лидеров по продажам автомобильных
> товаров от ведущих мировых производителей.  
> [Сайт AUTODOC.RU](https://www.autodoc.ru/)

![](https://github.com/MDN78/qa_guru_python_10_15/blob/master/assets/autodoc_main_page.PNG)
----

## Список проверок, реализованных в автотестах:

### UI автотесты:

- [x] Проверка формы авторизации на сайте
- [x] Авторизация пользователя на сайте (в процессе доработки)
- [x] Авторизация незарегестрированнного пользователя
- [x] Проверка загрузки главной страницы сайта
- [x] Поиск автозапчасти по номеру
- [x] Поиск каталога по VIN номеру автомобиля

----

### Проект реализован с использованием:

<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="https://github.com/MDN78/MDN78/blob/main/assets/selene.png"></code>
<code><img width="5%" title="selenium" src="https://github.com/MDN78/MDN78/blob/main/assets/selenium.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="selenoid" src="https://github.com/MDN78/MDN78/blob/main/assets/selenoid.png"></code>
<code><img width="5%" title="jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="github" src="https://github.com/MDN78/MDN78/blob/main/assets/github.png"></code>  
<code><img width="5%" title="telegram" src="assets/tg.png"></code>   
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  


> Для полноценного прохождения всех тестов должен быть или тестовый аккаунт на сайте ***Автодок*** или реальный, данные
> которого нужно будет указывать в файле
`.env`
>
Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`
Библиотека модульного тестирования: `PyTest`  
`Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер
пользователя не требуется.  
`Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)  
Фреймворк `Allure Report` собирает графический отчет о прохождении тестов  
После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант `Allure Report`

----

### <img width="3%" title="pc" src="assets/pc.jpg"> Локальный запуск

Необходимо создать файл `.env` и заполнить его актуальными тестовыми параметрами.  
Пример заполнения файла указан в файле `.env.example`

1) Скачать проект и открыть в IDE
2) Для локального запуска необходимо выполнить команду в терминале:

```commandline
pytest
```

3) Выполнить запрос на формирование отчета  
   note: команда для Windows

```commandline
allure serve
```

Результат: откроется страница с отчетом Allure Report

----

### <img width="3%" title="Jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"> Удаленный запуск автотестов выполняется на сервере Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_MDN782007_autodoc_test_project/">Ссылка на проект в
> Jenkins</a>

----

### Параметры сборки:

`ENVIRONMENT` - определение среды сборки, по умолчанию `PROD`  
`BROWSER NAME` - выбор браузера  
`BROWSER VERSION` - выбор версии браузера. По умолчанию выбран браузер Chrome, версия 100  
`COMMENT` - комментарий для получателя уведомления в Телеграмм

Версии браузеров, используемые в данной сборке в `Jenkins` и `Selenoid`:

| Chrome | Firefox |
|--------|---------|
| 100.0  | 98.0    |
| 99.0   | 97.0    |

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_MDN782007_autodoc_test_project/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать браузер
4. Выбрать версию браузера
4. Указать комментарий для уведомления в Телеграмм
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![image](assets/jenkins_main_page.PNG)

----

### <img width="3%" title="Allure report" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"> Allure отчет

![image](assets/allure_report.PNG)
Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты и log - файлы

![image](assets/allure_report_suits.PNG)

### <img width="3%" title="Allure testops" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"> Allure TestOps отчет

![image](assets/allure_testops_report.PNG)   

### <img width="3%" title="Allure report" src="https://github.com/MDN78/MDN78/blob/main/assets/selenoid.png"> Видео прохождения теста:

Видеозапись каждого теста генерируется с помощью `Selenoid` после успешного запуска контейнера c тестами в `Docker`.

![image](assets/test_example.gif)

### <img width="3%" title="Allure report" src="assets/tg.png"> Получение уведомлений о прохождении тестов в Telegram

После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.  

![image](assets/telegramm_report.PNG)  






