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
SeleniumBase is a high-level framework that is designed for web interaction using python.
While the [original Selenium library][1] is like a raw engine, SeleniumBase is the more modern version built around it. 
This version is known for being reliable, simple, and often automated.

**Its primary purposes are:**
  
  **Web Scraping:** Extracting data from dynamic websites like [CapWages][5] or [ESPN][6] used in my project.
  For many modern websites the content is rendered via JavaScript and cannot be captured by simple tools like http requests.
  
  **Automated Testing:** Verifying that web applications work and are running correctly. 
  The framework has great features allowing the developer to simulate user clicks, form entries, navigation and more.
  
  **Script Detection Evasion:** Its "UC mode" (Undetected-Chromedriver) mode modifies some of the browser’s properties to prevent websites from identifying the script as a bot.
  This is essential if you want to scrape many modern sites.

### • How do you use it?

SeleniumBase is designed to be a ready to use package. 
You use it by initializing a Driver object, which acts as a programmable interface for a web browser. 
Instead of manually clicking, scrolling, etc. you write Python commands to that Driver for it to execute.

The typical workflow involves four main steps:

1. Initialization: You configure the browser with the settings you want, such as enabling UC Mode to bypass detection or Headless Mode to run the script without a visible window.

2. Navigation: You direct the driver object to a specific URL using the .get() method.

3. Synchronization: Since modern websites load content dynamically, you use smart waits like a wait_for_element(). This ensures the page is fully ready before the script attempts to interact with it.

4. Interaction & Extraction: This is key functionality, using selectors like CSS or XPATH to locate specific data or buttons you want to interact with.
   Once you find what you want, you can extract text, click links, or scrape entire tables into Python data structures.

A Basic Implementation Example:
  ```python
    from seleniumbase import Driver
    
    # 1. Initialize the driver with stealth settings
    driver = Driver(uc=True, headless=True)
    
    try:
        # 2. Navigate to the target site
        driver.get("https://capwages.com/teams/columbus_blue_jackets")
    
        # 3. Wait for the JavaScript-heavy table to actually render
        driver.wait_for_element("table", timeout=10)
    
        # 4. Extract data (Example: printing the page title)
        print(f"Successfully accessed: {driver.get_title()}")
    
    finally:
        driver.quit()
  ```

## 3. What are the functionalities of the package/library?

**1. Undetected Mode (UC):**
Standard web automation often leaves clues that tell a server it is a script being run and not an actual human. 
SeleniumBase’s UC mode (uc=True) hides these clues, which is why my script can access websites without an "Access Denied" pop up.

  ```python
    #Example from line 73:
    driver = Driver(uc=True, headless=True)
  ```

**2. Headless Mode:**
By setting headless=True, the browser runs in the computer's memory without rendering an actual window. 
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
This makes the script function much better by making it significantly faster than a typical wait and by also preventing a crash caused by trying to scrape a table that hasn't finished loading yet.

  ```python
    #Example from line 80:
    driver.wait_for_element("table")
  ```

**5. Element Find & Selection with By:**
The By class allows you to target very specific parts or sections of a webpage that you know you want to use.
This prevents developers from having to dig deep into the html of the site and parse out what they want.

XPATH: You can use the website's XPATH for complex navigation like an embeded table.
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
  I selected SeleniumBase as I knew I wanted to complete a project involving web scraping. 
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

  
  |Feature | Beautiful Soup | SeleniumBase|
  | -------- | -------- | -------- |
  | JS Rendering  | No  | Yes   |
  | Bot Evasion   | Limited   | High (UC Mode)  |
  | Speed   | Fast (Static)   | Moderate (Dynamic)   |
   
  So, I chose SeleniumBase for a few reasons. First I had no problem with slower speeds, my program could function well no matter the delay. Second, it can execute JavaScript allowing me to access two data-heavy   websites that simpler scraping tools could not. Finally, because of its bot evasion I was able access the websites with no detection.

## 6. How did learning the package/library influence your learning of the language?
  For me, this package really helped me learn data structures and Object-Oriented Programming (OOP). 
  For a lot of my previous work in python it mainly involved string and variable manipulation but nothing further.
  While I knew OOP from Java I hadnt done much OOP in pyhton, so using the Driver object in SeleniumBase helped me learn it in pyhton. Just like java an object has specific methods like _.get()_, _.find_element()_, and _.quit()_.
  
   As well learning this package for my project required me to learn how to use Dictionaries.
   While I had heard of dictionaries before this was really my first time implementing them myself.
   Scraping the rosters from [CapWages][5] and [ESPN][6] required more than just simple lists to map player names to their stats and salaries.
   I had to learn to work with Key and Value pairs so that the driver would access the proper links to the right teams for both websites.
 
  ```python
     #Example Dictionary from lines 15-48
     team_link_map = {
        "CBJ": {"capwages": "columbus_blue_jackets", "espn": "cbj/columbus-blue-jackets"},
        "DET": {"capwages": "detroit_red_wings", "espn": "det/detroit-red-wings"},
        ...
        "TBL": {"capwages": "tampa_bay_lightning", "espn": "tb/tampa-bay-lightning"},
        "VGK": {"capwages": "vegas_golden_knights", "espn": "vgs/vegas-golden-knights"},
    }
  ```
    
## 7. How was your overall experience with the package/library?

  My overall experience with [SeleniumBase][3] was really great!
  I found it quite simple to install and also very easy to start learning.
  While I did not dive into every feature available, the ones I did look into were fairly straightforward and had lots of examples online for reference.
  The package was able to help me achieve everything I wanted to throughout my time working on the project.
  As well, it never really gave me any bugs or issues I could not solve.

***When would you recommend this package/library to someone?***
  I would recommend SeleniumBase to someone if they were looking to do any sort of complex web work. 
  If someone mentioned wanting to do some web testing, automation or scraping then SeleniumBase would be great for them.
  However, if they were just interested in doing some parsing of simple websites I would recommend them to use the 
  [Beautiful Soup Python library][4] as its a more lightweight library for parsing static HTML, 
  whereas SeleniumBase is better suited for dynamic, JavaScript-heavy websites.

***Would you continue using this package/library? Why or why not?***
  Yeah I would definitely continue using the SeleniumBase package in the future. 
  In fact come the future I would actually like to explore the package more in depth myself. 
  When reading through the documentation and other online materials there were many additional features I saw that I did not get to explore.
  Specifically I did not utilize any of the the testing features like simulating clicking or form submissions as my project just utilized data scraping.
  
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
