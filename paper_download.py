import requests
import os
import threading
from tqdm import tqdm
import sys

# Function to print the banner
def print_banner():
    banner = """
\033]8;;https://t.me/msbtehelp\aJoin telegram\033]8;;\a
\033[2mCreated by - idiotboxai\033[0m
\033[38;5;208m
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

\033[0m
    """
    print(banner)

# Function to download a paper
def download_paper(paper_type, subject_code, year_code):
    # Construct the URL based on the paper type and user input
    if paper_type == "question":
        url = f"https://msbte.org.in/portal/msbte_files/questionpaper_search/{year_code}/{subject_code}.pdf"
        file_name = f"{subject_code}_question_paper_{year_code}.pdf"
    elif paper_type == "answer":
        url = f"https://msbte.org.in/portal/msbte_files/ModalAns/{year_code}/{subject_code}.pdf"
        file_name = f"{subject_code}_answer_paper_{year_code}.pdf"
    else:
        print("Invalid paper type entered")
        return

    # Create directory for subject code if it does not exist
    if not os.path.exists(subject_code):
        os.mkdir(subject_code)

    # Create directory for paper type inside the subject code folder if it does not exist
    paper_folder_path = os.path.join(subject_code, paper_type)
    if not os.path.exists(paper_folder_path):
        os.mkdir(paper_folder_path)

    # Check if the PDF file already exists in the folder
    if os.path.exists(os.path.join(paper_folder_path, file_name)):
        print(f"{paper_type} paper ({year_code}) already downloaded.")
        return

    # Function to check if the URL is a valid PDF
    def is_valid_pdf():
        try:
            response = requests.head(url)
            content_length = response.headers.get('content-length')
            return content_length and int(content_length) >= 1024
        except Exception as e:
            return False

    if not is_valid_pdf():
        print(f"Invalid {paper_type} paper ({year_code}). Skipping download.")
        return

    # Function to download the file and update the progress bar
    def download_with_progress():
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=file_size, unit='iB', unit_scale=True, unit_divisor=1024, ncols=100, ascii=True, bar_format="{l_bar}{bar:50}{r_bar}")
        with open(os.path.join(paper_folder_path, file_name), 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                progress_bar.update(len(data))
        progress_bar.close()
        print(f"Download complete for {paper_type} paper ({year_code})!")

    # Create a thread for each download
    download_thread = threading.Thread(target=download_with_progress)
    download_thread.start()

def main():
    # Print the banner
    print_banner()

    subject_code = input("Enter the subject code: ")

    # Define available year codes for question papers
    question_year_codes = ["QPW23", "QPS23", "QPW21", "QPW22", "QPS22", "QPW19", "QPS19", "QPW18", "QPS18", "QPW17", "QPS17"]

    # Create threads for downloading question papers
    question_threads = []
    for year_code in question_year_codes:
        thread = threading.Thread(target=download_paper, args=("question", subject_code, year_code))
        question_threads.append(thread)
        thread.start()

    # Define available year codes for answer papers
    answer_year_codes = ["S23", "W23", "W21", "S21", "W22", "S22", "S20", "W20", "W19", "S19", "W18", "S18", "W17", "S17"]

    # Create threads for downloading answer papers
    answer_threads = []
    for year_code in answer_year_codes:
        thread = threading.Thread(target=download_paper, args=("answer", subject_code, year_code))
        answer_threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in question_threads + answer_threads:
        thread.join()

if __name__ == "__main__":
    main()
