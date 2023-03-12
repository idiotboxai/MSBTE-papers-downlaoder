import requests
import os
import time
import webbrowser
from tqdm import tqdm
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
def download_paper(paper_type):
    subject_code = input("What is the subject code? ")
    print("Choose year from the following:")
    print("QPS22 - Summer 2022 enter 1")
    print("QPW19 - Winter 2019 enter 2")
    print("QPS19 - Summer 2019 enter 3")
    print("QPW18 - Winter 2018 enter 4")
    print("QPS18 - Summer 2018 enter 5")
    print("QPW17 - Winter 2017 enter 6")
    print("QPS17 - Summer 2017 enter 7")
    year = input("Enter the year code: ")

    # convert year code to format used in URL
    if year == "1":
        year_code = "QPS22"
    elif year == "2":
        year_code = "QPW19"
    elif year == "3":
        year_code = "QPS19"
    elif year == "4":
        year_code = "QPW18"
    elif year == "5":
        year_code = "QPS18"
    elif year == "6":
        year_code = "QPW17"
    elif year == "7":
        year_code = "QPS17"
    else:
        print("Invalid year code entered")
        return

    # construct the URL based on the paper type and user input
    if paper_type == "question":
        url = f"https://msbte.org.in/portal/msbte_files/questionpaper_search/{year_code}/{subject_code}.pdf"
        file_name = f"{subject_code}_question_paper.pdf"
    elif paper_type == "answer":
        url = f"https://msbte.org.in/portal/msbte_files/ModalAns/{year_code}/{subject_code}.pdf"
        file_name = f"{subject_code}_answer_paper.pdf"
    else:
        print("Invalid paper type entered")
        return

    # create directory if it does not exist
    if not os.path.exists(subject_code):
        os.mkdir(subject_code)

    # check if a directory with subject code already exists
    else:
        # if it does, create another directory with year code
        os.mkdir(os.path.join(subject_code, year_code))
        subject_code = os.path.join(subject_code, year_code)

    # download the file and save it to the directory
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=file_size, unit='iB', unit_scale=True)
    with open(os.path.join(subject_code, file_name), 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()

    print("Download complete!")

# prompt user for paper type
paper_type = input("Which paper do you want to download? Enter 1 for question paper and 2 for answer paper: ")

# call download_paper function based on user input
if paper_type == "1":
    download_paper("question")
elif paper_type == "2":
    download_paper("answer")
else:
    print("Invalid input, please enter 1 or 2")
