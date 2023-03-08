import requests
import os
import time
import webbrowser
def open_telegram():
    webbrowser.open("https://t.me/msbtehelp")
print("\033]8;;https://t.me/msbtehelp\a" + "Join telegram" + "\033]8;;\a")
print("\033[2m" + """Created by - idiotboxai""" + "\033[0m")
print("\033[38;5;208m" + """
 ███▄ ▄███▓  ██████  ▄▄▄▄   ▄▄▄█████▓▓█████           
▓██▒▀█▀ ██▒▒██    ▒ ▓█████▄ ▓  ██▒ ▓▒▓█   ▀           
▓██    ▓██░░ ▓██▄   ▒██▒ ▄██▒ ▓██░ ▒░▒███             
▒██    ▒██   ▒   ██▒▒██░█▀  ░ ▓██▓ ░ ▒▓█  ▄           
▒██▒   ░██▒▒██████▒▒░▓█  ▀█▓  ▒██▒ ░ ░▒████▒          
░ ▒░   ░  ░▒ ▒▓▒ ▒ ░░▒▓███▀▒  ▒ ░░   ░░ ▒░ ░          
░  ░      ░░ ░▒  ░ ░▒░▒   ░     ░     ░ ░  ░          
░      ░   ░  ░  ░   ░    ░   ░         ░             
       ░         ░   ░                  ░  ░          
                          ░                           
 ███▄    █  ▄▄▄      ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
 ██ ▀█   █ ▒████▄    ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▓██  ▀█ ██▒▒██  ▀█▄  ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
▓██▒  ▐▌██▒░██▄▄▄▄██ ░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
▒██░   ▓██░ ▓█   ▓██▒  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░ ▒░   ▒ ▒  ▒▒   ▓▒█░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░  ▒   ▒▒ ░    ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
   ░   ░ ░   ░   ▒     ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
         ░       ░  ░          ░      ░ ░           ░ 
                                           
""" + "\033[0m")
time.sleep(3)
# Other code goes here
#good
# Prompt user for subject code and year
subject_code = input("Enter subject code: ").upper()
print("Choose year from the following:")
print("QPS22 - Summer 2022")
print("QPW19 - Winter 2019")
print("QPS19 - Summer 2019")
print("QPW18 - Winter 2018")
print("QPS18 - Summer 2018")
print("QPW17 - Winter 2017")
print("QPS17 - Summer 2017")

year = input("Enter year (e.g. QPW19): ").upper()

year_dict = {
    'QPS22': 'Summer 2022',
    'QPW19': 'Winter 2019',
    'QPS19': 'Summer 2019',
    'QPW18': 'Winter 2018',
    'QPS18': 'Summer 2018',
    'QPW17': 'Winter 2017',
    'QPS17': 'Summer 2017'
}

if year not in year_dict.keys():
    print("Invalid year.")
else:

    paper_code = year[-2:]
    url = f"https://msbte.org.in/portal/msbte_files/questionpaper_search/{year}/{subject_code}.pdf"

    # Check if URL exists and download PDF if it does
    if requests.get(url).status_code == 200:
        # Create directory if it doesn't exist
        directory = f"{subject_code}_{year_dict[year]}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Check if file already exists
        file_path = os.path.join(directory, f"{subject_code}_{paper_code}.pdf")
        if os.path.exists(file_path):
            print(f"{file_path} already exists.")
        else:
            # Download PDF
            response = requests.get(url)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded {subject_code}_{paper_code}.pdf")
    else:
        print("Paper not found.")

