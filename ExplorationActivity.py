from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time
import re

#=================================================================================
#===================================SETUP MAPS====================================
#=================================================================================
stat_map = {
    "G": 2,
    "A": 3,
    "P": 4
}

team_link_map = {
    "ANA": {"capwages": "anaheim_ducks", "espn": "ana/anaheim-ducks"},
    "BOS": {"capwages": "boston_bruins", "espn": "bos/boston-bruins"},
    "BUF": {"capwages": "buffalo_sabres", "espn": "buf/buffalo-sabres"},
    "CAR": {"capwages": "carolina_hurricanes", "espn": "car/carolina-hurricanes"},
    "CBJ": {"capwages": "columbus_blue_jackets", "espn": "cbj/columbus-blue-jackets"},
    "CGY": {"capwages": "calgary_flames", "espn": "cgy/calgary-flames"},
    "CHI": {"capwages": "chicago_blackhawks", "espn": "chi/chicago-blackhawks"},
    "COL": {"capwages": "colorado_avalanche", "espn": "col/colorado-avalanche"},
    "DAL": {"capwages": "dallas_stars", "espn": "dal/dallas-stars"},
    "DET": {"capwages": "detroit_red_wings", "espn": "det/detroit-red-wings"},
    "EDM": {"capwages": "edmonton_oilers", "espn": "edm/edmonton-oilers"},
    "FLA": {"capwages": "florida_panthers", "espn": "fla/florida-panthers"},
    "LAK": {"capwages": "los_angeles_kings", "espn": "lak/los-angeles-kings"},
    "MIN": {"capwages": "minnesota_wild", "espn": "min/minnesota-wild"},
    "MTL": {"capwages": "montreal_canadiens", "espn": "mtl/montreal-canadiens"},
    "NJD": {"capwages": "new_jersey_devils", "espn": "njd/new-jersey-devils"},
    "NSH": {"capwages": "nashville_predators", "espn": "nsh/nashville-predators"},
    "NYI": {"capwages": "new_york_islanders", "espn": "nyi/new-york-islanders"},
    "NYR": {"capwages": "new_york_rangers", "espn": "nyr/new-york-rangers"},
    "OTT": {"capwages": "ottawa_senators", "espn": "ott/ottawa-senators"},
    "PHI": {"capwages": "philadelphia_flyers", "espn": "phi/philadelphia-flyers"},
    "PIT": {"capwages": "pittsburgh_penguins", "espn": "pit/pittsburgh-penguins"},
    "SJS": {"capwages": "san_jose_sharks", "espn": "sj/san-jose-sharks"},
    "SEA": {"capwages": "seattle_kraken", "espn": "sea/seattle-kraken"},
    "STL": {"capwages": "st_louis_blues", "espn": "stl/st-louis-blues"},
    "TBL": {"capwages": "tampa_bay_lightning", "espn": "tb/tampa-bay-lightning"},
    "TOR": {"capwages": "toronto_maple_leafs", "espn": "tor/toronto-maple-leafs"},
    "UTA": {"capwages": "utah_hockey_club", "espn": "uta/utah-hockey-club"},
    "VAN": {"capwages": "vancouver_canucks", "espn": "van/vancouver-canucks"},
    "VGK": {"capwages": "vegas_golden_knights", "espn": "vgs/vegas-golden-knights"},
    "WPG": {"capwages": "winnipeg_jets", "espn": "wpg/winnipeg-jets"},
    "WSH": {"capwages": "washington_capitals", "espn": "wsh/washington-capitals"}
}

#=================================================================================
#============================Get USER INPUT Info====================================
#=================================================================================
print('\n---- Welcome to the Under Valued Hockey Player Finder----')
print('=====================================================\n')
print('---- Please Input How You Would Like To Evaluate The Players ----\n')
print('\tP (Points)\n\tG (Goals)\n\tA (Assists)\n')
evaluation_choice = input()
i = stat_map.get(evaluation_choice)


print('---- Please Input Which Team You Would Like to Evaluate ----\n')
print('\tANA (Anaheim Ducks)\n\tBOS (Boston Bruins)\n\tBUF (Buffalo Sabres)\n\tCAR (Carolina Hurricanes)\n\tCBJ (Columbus Blue Jackets)\n\tCGY (Calgary Flames)\n\tCHI (Chicago Blackhawks)\n\tCOL (Colorado Avalanche)\n\tDAL (Dallas Stars)\n\tDET (Detroit Red Wings)\n\tEDM (Edmonton Oilers)\n\tFLA (Florida Panthers)\n\tLAK (Los Angeles Kings)\n\tMIN (Minnesota Wild)\n\tMTL (Montreal Canadiens)\n\tNJD (New Jersey Devils)\n\tNSH (Nashville Predators)\n\tNYI (New York Islanders)\n\tNYR (New York Rangers)\n\tOTT (Ottawa Senators)\n\tPHI (Philadelphia Flyers)\n\tPIT (Pittsburgh Penguins)\n\tSJS (San Jose Sharks)\n\tSEA (Seattle Kraken)\n\tSTL (St. Louis Blues)\n\tTBL (Tampa Bay Lightning)\n\tTOR (Toronto Maple Leafs)\n\tUTA (Utah Hockey Club)\n\tVAN (Vancouver Canucks)\n\tVGK (Vegas Golden Knights)\n\tWPG (Winnipeg Jets)\n\tWSH (Washington Capitals)')
team_choice = input()
config = team_link_map[team_choice]

print("Please wait ...")

#=================================================================================
#============================Get Contract Info====================================
#=================================================================================
driver = Driver(uc=True, headless=True)

try:

    driver.get(f"https://capwages.com/teams/{config['capwages']}")

    # Wait for the table to exist
    driver.wait_for_element("table")

    # Get Tables i want
    defense_table = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div[1]/div[3]/div[2]/table')              
    forward_table = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div[1]/div[3]/div[1]/table')


    forward_rows = forward_table.find_elements(By.TAG_NAME, "tr")
    defense_rows = defense_table.find_elements(By.TAG_NAME, "tr")

    forward_roster_list = []
    defense_roster_list = []
    full_roster_list = {}

    for row in forward_rows:
        # Get all columns
        cells = row.find_elements(By.TAG_NAME, "td")

        #skip blank cells
        if not cells:
            continue
        
        #format name
        raw_name = cells[0].text.strip()
        clean_name = re.sub(r'".*?"', '', raw_name).strip()
        row_data = [clean_name] + [cell.text.strip() for cell in cells[1:]]
        
        # Only add rows with data 
        if row_data:
            forward_roster_list.append(row_data)


    for row in defense_rows:
        # Get all columna
        cells = row.find_elements(By.TAG_NAME, "td")
        
        #skip blank cells
        if not cells:
            continue
        
        #format name
        raw_name = cells[0].text.strip()
        clean_name = re.sub(r'".*?"', '', raw_name).strip()
        row_data = [clean_name] + [cell.text.strip() for cell in cells[1:]]
        
        # Only add rows with data
        if row_data:
            defense_roster_list.append(row_data)

    # add defense with forards
    merged_roster_contracts = forward_roster_list + defense_roster_list
    
    #format money to int
    for row in merged_roster_contracts:
        salary_str = row[9]  # e.g., '$1,825,000'
        
        # Convert to number (handling potential empty strings with a guard)
        if salary_str and '$' in salary_str:
            row[9] = int(salary_str.replace('$', '').replace(',', ''))
    
#=================================================================================
#============================Get Stats Info====================================
#=================================================================================

    driver.get(f"https://www.espn.com/nhl/team/stats/_/name/{config['espn']}")

    # Wait for the table to exist
    driver.wait_for_element("table")

    # Get Tables i want
    #ESPN uses two tables (name, stats)
    player_name_table = driver.find_element(By.XPATH, '//*[@id="fittPageContainer"]/div[2]/div/div[5]/div/div/section/div/div[6]/div[2]/table')
    stat_table = driver.find_element(By.XPATH, '//*[@id="fittPageContainer"]/div[2]/div/div[5]/div/div/section/div/div[6]/div[2]/div/div[2]/table[1]')

    stat_rows = stat_table.find_elements(By.TAG_NAME, "tr")
    name_rows = player_name_table.find_elements(By.TAG_NAME, "tr")

    player_stat_list = []
    player_name_list = []

    for row in stat_rows:
        # Get all columns
        cells = row.find_elements(By.TAG_NAME, "td")
        
        row_data = [cell.text.strip() for cell in cells]
        
        # Only add rows with data 
        if row_data:
            player_stat_list.append(row_data)

    #do name table
    for row in name_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = []
        #format their names to match other table
        for cell in cells:
            parts = cell.text.split()
            if len(parts) >= 2:
                formatted_name = f"{parts[1]}, {parts[0]}"
                row_data.append(formatted_name)
            else:
                row_data.append(cell.text.strip())

        if row_data and row_data[0]:
            player_name_list.append(row_data)

    #Add the stats to their name
    merged_roster = []

    for name_data, stat_data in zip(player_name_list, player_stat_list):
        full_row = name_data + stat_data
        merged_roster.append(full_row)


#=================================================================================
#============================Do the Fun stuff now====================================
#=================================================================================
    print(f"\n---- Evaluating {team_choice} Players Based on {evaluation_choice} ----\n")

    final_roster = [m + [f[9]] for m in merged_roster for f in merged_roster_contracts if m[0] == f[0]]

    # Sorting logic to keep 0-stat players at the bottom
    sorted_words = sorted(
        final_roster, 
        key=lambda s: s[14] / int(s[i]) if int(s[i]) > 0 else float('inf')
    )

    for player in sorted_words:
        stat_value = int(player[i])
        salary = player[14]
        

        if stat_value > 0:
            value_score = int(salary / stat_value)
            print(f"{player[0]:<25} | Value for {evaluation_choice}: ${value_score:,} per {evaluation_choice}")
        else:
            print(f"{player[0]:<25} | Value for {evaluation_choice}: N/A (0 {evaluation_choice} recorded)")

finally:
    driver.quit()


    