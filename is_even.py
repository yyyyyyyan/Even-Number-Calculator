from bs4 import BeautifulSoup                                   # HTML parsing library
import requests                                                 # HTTP requests library
import locale                                                   # Standard locale library

# Amazing resource I've found. You can change if you find a better one:
SUPER_MAGIC_LINK = "https://www.chilimath.com/lessons/introductory-algebra/list-of-even-numbers/"

def get_even_numbers_list():                                    # Define function to get even numbers list
    r = requests.get(SUPER_MAGIC_LINK)                          # Execute a GET request to the resource I've found
    soup = BeautifulSoup(r.content, "lxml")                     # Create an object to parse the HTML
    all_even_numbers = []                                       # Create a list to store even numbers
    locale.setlocale(locale.LC_NUMERIC, ("en_US", "UTF-8"))     # Make sure locale is set to MURICAH
    for sub in soup.select('h2 + p > strong:nth-child(1)'):     # Even numbers are in this cool CSS selector
        sub_int = [locale.atoi(n) for n in sub.text.split()]    # We need locale 'cos nearly 0.2% of the numbers use ","
        all_even_numbers.extend(sub_int)                        # Add this section of even numbers to the complete list 
    return all_even_numbers                                     # Return even numbers list


def is_even(number):                                            # Define function to determine if number is even
    if number > 1000:                                           # Check if number is higher than 1,000
        raise ValueError("This number is too high!")              # Raise an exception if it is; our resource is limited
    all_even_numbers = get_even_numbers_list()                  # Calculate list every time, in case it changes
    if number in all_even_numbers:                              # Check if number is in the list of even numbers
        return True                                               # Return True if it is (it's even!!!)
    return False                                                  # Return False if it's not (it's odd :( )
