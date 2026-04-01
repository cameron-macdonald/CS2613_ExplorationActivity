# CS2613_ExplorationActivity
## 1. Which package/library did you select?

## 2. What is the package/library?
### • What purpose does it serve?
### • How do you use it?
### • This section should be the largest and go into lots of detail. Not everything here must be utilized in your sample program.

## 3. What are the functionalities of the package/library?
### • Snippets of code and examples of output should be given here.

## 4. When was it created?
  Selenium itself was originally released in 2004 by a developer named Jason Huggins [1].
  It was designed to do one basic thing: make a web browser move on its own. 
  Today this software is like the "engine" that everything else is built on.

  SeleniumBase, the modern framework I am using for my activity, was created later by Michael Mintz in 2016. 
  While it was first released around 2016, it didn't become the powerful version we use today until about 2018.
  Today it is a robust framework that is still consistently maintained with updates to match new browser versions [2].

## 5. Why did you select this package/library?
  I selected SeleniumBase as I knew I wanted to completed a project involving web scraping. 
  When I originally started the project I tried the Beautiful Soup Python library as it was recommended for being simple to work with [3].
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
  Many modern websites, like CapWages[4] and ESPN[5] that i used, try to block script connections or throw up a CAPTCHA.
  By using SeleniumBase and the UC mode I was able to scrape two separate domains that i was unable to using Beautiful Soup.
 
  So, I chose SeleniumBase because it can execute JavaScript and bypass bot detection, allowing me to access two data-heavy websites that simpler scraping tools could not access.

## 6. How did learning the package/library influence your learning of the language?

## 7. How was your overall experience with the package/library?
### • When would you recommend this package/library to someone?
### • Would you continue using this package/library? Why or why not?

## References
  [1] Selenium History:  https://www.selenium.dev/history/#:~:text=The%20story%20starts%20in%202004,this%20was%20a%20day%20job.
  
  [2] SeleniumBase Documentation: https://github.com/seleniumbase/SeleniumBase
  
  [3] Beautiful Soup Documentation: https://beautiful-soup-4.readthedocs.io/en/
  
  [4] CapWages Team Salaries: https://capwages.com/

  [5] ESPN NHL Statistics: https://www.espn.com/nhl/stats/
