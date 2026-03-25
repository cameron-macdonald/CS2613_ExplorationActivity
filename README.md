# CS2613_ExplorationActivity

### 1. Which package/library does the sample program demonstrate?

My program demonstrates the use of the Selenium package.
    
    from seleniumbase import Driver
    from selenium.webdriver.common.by import By

### 2. How does someone run your program?

    Someone would run my program by running the ExplorationActivity.py file in the terminal

    python ExplorationActivity.py

### 3. What purpose does your program serve?



### 4. What would be some sample input/output?
The first output you should see just after running ExplorationAcitivity.py:

    ---- Welcome To The Under Valued Hockey Player Finder ----
    =================================================================
    ---- Please Input How You Would Like To Evaluate The Players ----

        P (Points)
        G (Goals)
        A (Assists)

From here you would input either _P_ _G_ or _A_ to select how youd like to evalute the players

    Sample Ex: G

Upon selecting your choice you should see the following output:

    ---- Please Input Which Team You Would Like to Evaluate ----

        ANA (Anaheim Ducks)
        BOS (Boston Bruins)
        BUF (Buffalo Sabres)
        CAR (Carolina Hurricanes)
        CBJ (Columbus Blue Jackets)
        CGY (Calgary Flames)
        CHI (Chicago Blackhawks)
        COL (Colorado Avalanche)
        DAL (Dallas Stars)
        DET (Detroit Red Wings)
        EDM (Edmonton Oilers)
        FLA (Florida Panthers)
        LAK (Los Angeles Kings)
        MIN (Minnesota Wild)
        MTL (Montreal Canadiens)
        NJD (New Jersey Devils)
        NSH (Nashville Predators)
        NYI (New York Islanders)
        NYR (New York Rangers)
        OTT (Ottawa Senators)
        PHI (Philadelphia Flyers)
        PIT (Pittsburgh Penguins)
        SJS (San Jose Sharks)
        SEA (Seattle Kraken)
        STL (St. Louis Blues)
        TBL (Tampa Bay Lightning)
        TOR (Toronto Maple Leafs)
        UTA (Utah Hockey Club)
        VAN (Vancouver Canucks)
        VGK (Vegas Golden Knights)
        WPG (Winnipeg Jets)
        WSH (Washington Capitals)

From here you would input the abbriviation of the team above you would like to evalute

    Sample Ex: MTL

The program will then prompt you to wait:
    
    Please wait ...

After about 10-20 seconds you should see a resulting table like the following:
| Rank | Player | Value for P (per P) |
|-----:|:-------|--------------------:|
| 1 | Hutson, Lane | $13,768 |
| 2 | Demidov, Ivan | $17,422 |
| 3 | Kapanen, Oliver | $26,428 |
| 4 | Bolduc, Zack | $33,205 |
| 5 | Texier, Alexandre | $52,631 |
| 6 | Suzuki, Nick | $91,569 |
| 7 | Caufield, Cole | $103,289 |
| 8 | Slafkovsky, Juraj | $120,634 |
| 9 | Evans, Jake | $135,714 |
| 10 | Struble, Jayden | $141,250 |
| 11 | Newhook, Alex | $145,000 |
| 12 | Matheson, Mike | $147,727 |
| 13 | Carrier, Alexandre | $170,454 |
| 14 | Dobson, Noah | $206,521 |
| 15 | Veleno, Joe | $225,000 |
| 16 | Dach, Kirby | $240,178 |
| 17 | Anderson, Josh | $250,000 |
| 18 | Gallagher, Brendan | $295,454 |
| 19 | Danault, Phillip | $500,000 |
| 20 | Guhle, Kaiden | $555,000 |
| 21 | Xhekaj, Arber | $650,000 |
| 22 | Laine, Patrik | $8,700,000 |
