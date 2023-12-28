import requests
import time



display_design = '''
       ****************************************************

          ===============================================
                  Welcome to AdminSeeker v1.0.0           *
          =============================================== *
                                                          *
                        A          S                      *
                       / \       =====//                  *
                      / _ \ ____ #                        *
                     / ___ \∆∆∆∆ #====                    *
                    /_/   \_\        #                    *
                                //===#                    *
          =============================================== *
                         Ready to Seek Admins!            *
          =============================================== *

      *****************************************************

                            MadeBy: BarCode
'''

print(display_design)
time.sleep(1)
print("NOTE: Do not put '/' at the end of Target url! ")
time.sleep(1)
print("Find Admin Panel!")
time.sleep(1)
print("Enjoy!")
time.sleep(1)
print("Loading...")
time.sleep(2)
# Wordlist
with open('wordlist.txt', 'r') as wordlist_file:
    wordlist = wordlist_file.read().splitlines()

# Target URL here
target_url = input("Input Target URL: ")

#robots.txt
robots = target_url + '/robots.txt'
response = requests.get(robots)
print("Check out here if you notice some valuable information!")
print('--------------------')
print(response)
print('--------------------')
if response.status_code == 404:
        print("Sorry! robots.txt not found. ")
else:
        pass


# Loop to test wordlist
for word in wordlist:
    # Append the word to the target URL
    url = target_url + '/' + word

    # Send a GET request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code == 200:
        print(f'Admin panel found at: [✓]{url}')
        break
    else:
        print(f'Admin panel not found at:[×]{url}')
