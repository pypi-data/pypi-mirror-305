import asyncio
import random
import os
import logging
import sys
import pickle

from logging import info

from selenium_driverless import webdriver


# Инициализация браузера.
async def init_browser(proxy = None, headless = True, maximize_window = False):
    try:
        options = webdriver.ChromeOptions()
        if proxy:
            options.single_proxy = f'http://{proxy}/'
        options.startup_url = 'https://google.com/'
        options.headless = headless

        browser = await webdriver.Chrome(options = options)
        if maximize_window:
            await browser.maximize_window()
        await asyncio.sleep(2)
        info(f'Один из браузеров инициализирован с прокси: {proxy}.')

        return browser
    except Exception as error:
        info(f'Ошибка при инициализации браузера: {error}')


# Переход по ссылке.
async def go_to_url(browser, url):
    try:
        try:
            await browser.get(url, timeout=150)
        except:
            try:
                await browser.get(url, timeout=250)
            except:
                await browser.get(url, timeout=300)
        info(f'Браузер перешёл на {url}.')
        await asyncio.sleep(random.randint(3, 5))
    except Exception as error:
        info(f'Ошибка при переходе на {url}: {error}.')


# Настройка логов.
async def init_logging(to_console = True, filename = f'{os.path.dirname(__file__)}/logs.log'):
    if to_console and not filename:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO, filename=filename)
        if to_console:
            logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


# Аутентификация в аккаунт.
async def auth(browser, url, path_to_cookies):
    try:
        await go_to_url(browser, url)
        await asyncio.sleep(0.5 + random.random())

        try:
            for cookie in pickle.load(open(path_to_cookies, 'rb')):
                await browser.add_cookie(cookie)
        except:
            for cookie in pickle.load(open(path_to_cookies, 'rb')):
                await browser.add_cookie(cookie)
        
        await asyncio.sleep(0.5 + random.random())
        await go_to_url(browser, url)
        info('Браузер авторизовался.')
    except Exception as error:
        info(f'Ошибка при попытке авторизации: {error}')
        info('Завершение работы программы...')
        quit()


# Сохранение файлов cookie.
async def save_cookie(browser, path, close_browser = False):
    try:
        await asyncio.sleep(random.randint(3, 5))
        with open(path, 'wb') as file:
            pickle.dump(await browser.get_cookies(), file)
        info(f'Сохранены куки браузера.') 
        if close_browser:
            try:
                await browser.quit()
                info('Работа браузера завершена.')
            except:
                ...
    except Exception as error:
        info(f'Ошибка при попытке сохранить cookie: {error}')