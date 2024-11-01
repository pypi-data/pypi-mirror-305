# sufsd (Standart Utils For Selenium_driverless)

## What is this?

When parsing different sites, you almost always have to copy+paste some functions; this module was created to make such code easier. It includes the most commonly used functions when parsing. In the future it will be very actively replenished.



## Dependencies



- Python >= 3.8
- Google-Chrome installed (Chromium not tested)



## Usage

```python
import asyncio
import os
import base64

from sufsd import init_browser
from sufsd import auth
from sufsd import init_logging
from selenium_driverless import webdriver


LINK = https://github.com/
PATH_TO_DIR = os.path.dirname(__file__)

async def main():
    await init_logging(to_console=True, filename= f'{PATH_TO_DIR}/logs.log')
    try:
        browser = await init_browser(
            proxy = 'user:password@ip:port',
            headless=False,
            maximize_window = True)
        
        await auth(browser, LINK, f'{PATH_TO_DIR}/cookies')
        
        logging.info(f'Title page: {await browser.title}.')
        
        bytes_for_pdf = await browser.print_page()
        
        with open(f'{PATH_TO_DIR}/github.pdf', 'wb') as file:
            file.write(base64.b64decode(pdf))
        
        logging.info('Created file github.pdf.')
        
    except Exception as error:
        logging.info(f'ERROR: {error}')
    
    finally:
        await browser.quit()
        logging.ingo('The browser was closed.')


if __name__ == '__main__':
    asyncio.run(main())
```



## Utils implemented so far

`init_browser(proxy = None, headless = True, maximize_window = False) #async`

Browser initialization, taking into account human delays, keeping logs.

#####     **Parameters:**    

- proxy (`str`)  -  proxy in the format `ip:port` or `user@password:ip:port`

- headless (`bool`)  -  headless on/off.

- maximize_window (`bool`)  -  maximize_window on/off

#####     **Return type:**   `class selenium_driverless.webdriver.Chrome`

------

`go_to_url(browser, url) #async`

Сonfidently go to the link (it is impossible not to get to the site due to any lags/proxy speed limits), taking into account human delays, keeping logs.

​    **Parameters:**    

- browser (`Chrome`)  -  browser selenium_driverless.webdriver.Chrome.

- url (`str`)  -  link to site.


​    **Return type:**    `None`

------

`init_logging(to_console = True, filename = f'{os.path.dirname(__file__)}logs.log') #async`

enabling logs.

​    **Parameters:**   

- ##### to_console (`bool`)  -  on/off logging to console.

- filename (`str | bool`)  -  on/off logging to filename. filename=False to off logging to file.


​    **Return type:**  `None`

------

`auth(browser, url, path_to_cookies) #async`

The browser goes to the url and re-enters the site with cookies from path_to_cookies, keeping logs.

​    **Parameters:**    

- ##### browser (`Chrome`)  -  browser selenium_driverless.webdriver.Chrome.

- url (`str`)  -  link to site.

- path_to_cookies (`str`)  -  path to file with cookies.

​    **Return type:**    `None`

------

`save_cookie(browser, path, close_browser = False) #async`

Saves the browser cookie to a file located at path if close_browser then closes the browser, keeping logs.

​    **Parameters:**    

- browser (`Chrome`)  -  browser selenium_driverless.webdriver.Chrome.

- path (`str`)  - path to file.


- close_browser (`bool`)  -  if True then closes the browser.


​    **Return type:**    `None`



## Author

Developer: https://t.me/VHdpcj