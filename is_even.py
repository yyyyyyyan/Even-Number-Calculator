from bs4 import BeautifulSoup                                   # HTML parsing library
import requests                                                 # HTTP requests library
import locale                                                   # Standard locale library

# Amazing resource I've found. You can change if you find a better one:
SUPER_MAGIC_LINK = "https://www.chilimath.com/lessons/introductory-algebra/list-of-even-numbers/"

def get_even_numbers_list():                                    # Define function to get even numbers list
    all_even_numbers = []                                       # Create a list to store even numbers

    # 0 - 1000
    r = requests.get(SUPER_MAGIC_LINK)                          # Execute a GET request to the resource I've found
    soup = BeautifulSoup(r.content, "lxml")                     # Create an object to parse the HTML
    locale.setlocale(locale.LC_NUMERIC, ("en_US", "UTF-8"))     # Make sure locale is set to MURICAH
    for sub in soup.select('h2 + p > strong:nth-child(1)'):     # Even numbers are in this cool CSS selector
        sub_int = [locale.atoi(n) for n in sub.text.split()]    # We need locale 'cos nearly 0.2% of the numbers use ","
        all_even_numbers.extend(sub_int)                        # Add this section of even numbers to the complete list 

    # 1000 - 1100
    EVEN_SUPERER_MAGICER_LINK = "https://sandeepbarouli.com/counting-chart-numbers-1000-to-1100/"                      # A repository with the numbers we need, so we can iterate over them
    numbers_between_one_thousand_and_one_thousand_and_one_hundred = []                                                 # List to store the even numbers

    r = requests.get(EVEN_SUPERER_MAGICER_LINK)                                                                        # GET request to get the page's content
    soup = BeautifulSoup(r.text, 'html.parser')                                                                        # Object to parse the HTML
    for paragraph in soup.find_all('p'):                                                                               # Iterating through all paragraphs from the site
        if 'One Thousand' in paragraph.text:                                                                           # There are paragraphs that DO NOT contain numbers !! We have to check
            number_alone = paragraph.text.split('–')[0]                                                                # THIS IS NOT A HYPHEN (-) I DON'T KNOW WHY
            number_alone_without_space = number_alone[0:-1]                                                            # After removing the unwanted part, we just need to remove the space at the end

            if int(number_alone_without_space) != 1000:                                                                # Lastly but not leastly, we have to exclude 1000 because the solution above
                numbers_between_one_thousand_and_one_thousand_and_one_hundred.append(int(number_alone_without_space))  # already has it. Easy peezy.

    for number in numbers_between_one_thousand_and_one_thousand_and_one_hundred:                                       # I don't know the math behind it, but I ran through all the numbers
        not_even = False                                                                                               # from 1000 to 1100 and I spotted a pattern (maybe a coincidence idk)
                                                                                                                       # all the odd numbers end with either a 1, 3, 5, 7 or a 9. So all we
        if str(number)[-1:] == '1':                                                                                    # have to do is pick the ones that don't and voila we have even numbers.
            not_even = True                                                                                            # Haven't got the time to check if this logic still works for more numbers,
        elif str(number)[-1:] == '3':                                                                                  # so if anyone is insterested in investing in this approach, give it a try...
            not_even = True                                                                                            # But you'll have to find another website to get more numbers from.
        elif str(number)[-1:] == '5':
            not_even = True
        elif str(number)[-1:] == '7':
            not_even = True
        elif str(number)[-1:] == '9':
            not_even = True

        if not not_even:                                                                                          
            all_even_numbers.append(number)                                                                       

    return all_even_numbers                                     # Return even numbers list

def is_even(number):                                            # Define function to determine if number is even
    if number > 1100:                                           # Check if number is higher than 1,100
        raise ValueError("This number is too high!")            # Raise an exception if it is; our resource is limited
    all_even_numbers = get_even_numbers_list()                  # Calculate list every time, in case it changes
    if number in all_even_numbers:                              # Check if number is in the list of even numbers
        return True                                             # Return True if it is (it's even!!!)
    return False                                                # Return False if it's not (it's odd :( )
