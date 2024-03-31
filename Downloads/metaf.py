import requests
import pyperclip
import time

def get_metar_info(airport_code):
    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{airport_code.upper()}.TXT"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve METAR information for {airport_code}: {e}")
        return "Failed to retrieve METAR information."

def main():
    print("Welcome to METAR Info!")
    while True:
        airport_code = input("Please enter the airport code (e.g., CYUL, CYYZ) or type 'QUIT' to exit: ")
        if airport_code.upper() == 'QUIT':
            quit_option = input("Are you sure you want to quit? (Y/N): ")
            if quit_option.upper() == 'Y':
                print("Exiting program. Thank you!")
                break
            else:
                continue

        metar_info = get_metar_info(airport_code)
        if not metar_info.startswith("Failed"):
            print("METAR information for", airport_code.upper() + ":")
            print(metar_info)
            
            # Ask if the user wants to copy METAR information to clipboard
            copy_option = input("Do you want to copy the METAR information to the clipboard? (Y/N): ")
            if copy_option.upper() == 'Y':
                pyperclip.copy(metar_info)
                print("METAR information copied to clipboard!")

        # Ask if the user wants to quit the program
        print("Press 'Y' to quit or 'N' to input another airport code.")
        quit_option = input("Do you want to quit? (Y/N): ")
        if quit_option.upper() == 'Y':
            print("Exiting program. Thank you!")
            break

if __name__ == "__main__":
    main()
