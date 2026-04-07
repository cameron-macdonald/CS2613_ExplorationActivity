# CS2613_ExplorationActivity
## 1. Which package/library did you select?
  I have selected SeleniumBase Python Package.
  ```python
    #To install package
    pip install seleniumbase
  ```
  ```python
    #To use the package
    from seleniumbase import Driver
    from selenium.webdriver.common.by import By
  ```

## 2. What is the package/library?
### • What purpose does it serve?
SeleniumBase is a high-level framework that is designed to make web interaction reliable, simple, and often automated. 
While the [original Selenium library][1] is like a raw engine, SeleniumBase is the more modern version built around it. 

**Its primary purposes are:**
  
  **Web Scraping:** Extracting data from dynamic websites (like [CapWages][5] or [ESPN][6] used in my project) where content is rendered via JavaScript and cannot be captured by simple tools like http requests.
  
  **Automated Testing:** Verifying that web applications work correctly by simulating user clicks, form entries, navigation and more.
  
  **Bot Detection Evasion:** Its "UC mode" (Undetected-Chromedriver) mode modifies some of the browser’s properties to prevent websites from identifying the script as a bot, which is essential for many modern sites.

### • How do you use it?

DONTTTTTT SUBMIT THIS SECTION
DONTTTTTT SUBMIT THIS SECTION
DONTTTTTT SUBMIT THIS SECTION
You use it by initializing a Driver object. This object acts as your "proxy" in the browser. Y
ou give it commands to navigate to URLs, wait for specific elements to appear (to handle slow loading), and then locate data using various "selectors" (like XPATH or CSS selectors).

In my specific program:

Initialization: 
You use Driver(uc=True, headless=True). This tells the program to run in the background (headless) and to use "Undetected" mode so the NHL/ESPN sites don't block you.

Navigation: driver.get(url) moves the browser to the team page.

Synchronization: driver.wait_for_element("table") is a critical step; it prevents the script from crashing by ensuring the data has actually loaded before the script tries to read it.

Interaction: You use find_elements(By.TAG_NAME, "tr") to iterate through the rows of the hockey rosters.


DONTTTTTT SUBMIT THIS SECTION
DONTTTTTT SUBMIT THIS SECTION
DONTTTTTT SUBMIT THIS SECTION

## 3. What are the functionalities of the package/library?

**1. Undetected Mode (UC):**
Standard web automation often leaves clues that tell a server it is a script being ran and not an acutual human. 
SeleniumBase’s UC mode (uc=True) hides these clues, which is why my script can access websites without an "Access Denied" pop up.

  ```python
    #Example from line 73:
    driver = Driver(uc=True, headless=True)
  ```

**2. Headless Mode:**
By setting headless=True, the browser runs in the computer's memory without redering an actual window. 
This makes the script faster and also allows it to run on servers that don't have a monitor. 
In my case it allows me to run it in the background without a browser popping up preventing my workflow.

  ```python
    #Example from line 73:
    driver = Driver(uc=True, headless=True)
  ```

**3. Website Navigation**
This method directs the automated browser to load a specific URL.
It acts as the primary trigger code for the WebDriver to fire up and begin interacting with the site's DOM.

  ```python
    #Example from line 77:
    driver.get(f"https://capwages.com/teams/{config['capwages']}")
  ```

**4. Intelligent Waiting**
When loading up a website certain features like tables or stats are not loaded right away.
Unlike time.sleep(), which pauses for a fixed amount of time, SeleniumBase's wait_for_element function polls the page and only resumes execution right when the required data appears. 
This makes the script function much better by making it significantly faster then a typical wait and by also preventing a crash caused by trying to scrape a table that hasn't finished loading yet.

  ```python
    #Example from line 80:
    driver.wait_for_element("table")
  ```

**5. Element Find & Selection with By:**
The By class allows you to target very specific parts or sections of a webpage that you know you want to use.
This prevents developers from having to dig deep into the html of the site and parse out what they want.

XPATH: You can use the webistes XPATH for complex navigation like an embeded table.
  ```python
    #Example from line 84:
    forward_table = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div[1]/div[3]/div[1]/table')
  ```
Tag Name: Used for getting structural elements like rows from a table.
  ```python
    #Example from line 87:
    forward_rows = forward_table.find_elements(By.TAG_NAME, "tr")
  ```

## 4. When was it created?
  [Selenium][2] itself was originally released in 2004 by a developer named Jason Huggins.
  It was designed to do one basic thing: make a web browser move on its own. 
  Today this software is like the "engine" that everything else is built on.

  [SeleniumBase][3], the modern framework I am using for my activity, was created later by Michael Mintz in 2016. 
  While it was first released around 2016, it didn't become the powerful version we use today until about 2018.
  Today it is a robust framework that is still consistently maintained with updates to match new browser versions.

## 5. Why did you select this package/library?
  I selected SeleniumBase as I knew I wanted to completed a project involving web scraping. 
  When I originally started the project I tried the [Beautiful Soup Python library][4] as it was recommended for being simple to work with.
  However, Beautiful Soup could not get past the security and technical barriers of the websites I needed to use.  
  It turns out that traditional tools like Beautiful Soup fail on modern websites that rely on React or Vue.
  On these sites, the data (the HTML) doesn't actually exist until a browser runs the JavaScript. Because Beautiful Soup isn't a browser, it just sees a blank page.

  I switched to SeleniumBase because it has extra features that helps it act as a "data bridge."
  One of these features I used in my code was Undetected-Chromedriver (uc) mode.
    
  ```python
  # Initializing the driver with stealth (UC) and background (Headless) modes
  driver = Driver(uc=True, headless=True)
  ```
  The uc=True attribute enables Undetected-Chromedriver mode. It is a specialized feature in SeleniumBase designed to stop websites from realizing that your browser is being controlled by a robot.
  Many modern websites, like [CapWages][5] and [ESPN][6] that i used, try to block script connections or throw up a CAPTCHA.
  By using SeleniumBase and the UC mode I was able to scrape two separate domains that i was unable to using Beautiful Soup.
 
  So, I chose SeleniumBase because it can execute JavaScript and bypass bot detection, allowing me to access two data-heavy websites that simpler scraping tools could not access.

## 6. How did learning the package/library influence your learning of the language?

## 7. How was your overall experience with the package/library?

***When would you recommend this package/library to someone?***

  If they were looking to do any sort of web scraping beyond some simple parsing.
  I would reccomend to use the [Beautiful Soup Python library][4] 
  
***Would you continue using this package/library? Why or why not?***

  Yeah I would definitley continue using the SeleniumBase package in the future. 
  Throughout my time working on the project the package was able to help achieve everything I wanted it to and it never really gave me any issues.
  In fact come the future I would actually like to explore the package more in depth. 
  When reading trough the documentation and other online materials there was many additional features I saw that I did not get to explore.

## References

  1. Selenium Documentation: [https://pypi.org/project/selenium/][1]

  2. Selenium History:  [https://www.selenium.dev/history/#:~:text=The%20story%20starts%20in%202004,this%20was%20a%20day%20job.][2]

  3. SeleniumBase Documentation: [https://github.com/seleniumbase/SeleniumBase][3]

  4. Beautiful Soup Documentation: [https://beautiful-soup-4.readthedocs.io/en/][4]

  5. CapWages Team Salaries: [https://capwages.com/][5]

  6. ESPN NHL Statistics: [https://www.espn.com/nhl/stats][6]


  [1]: https://pypi.org/project/selenium/ 

  [2]: https://www.selenium.dev/history/#:~:text=The%20story%20starts%20in%202004,this%20was%20a%20day%20job.
  
  [3]: https://github.com/seleniumbase/SeleniumBase
  
  [4]: https://beautiful-soup-4.readthedocs.io/en/
  
  [5]: https://capwages.com/

  [6]: https://www.espn.com/nhl/stats
