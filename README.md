# random-pairup-norepeat
I wrote this little snippet a while ago for a club I started. The purpose of the script is to randomly match up people in pairs (2 in a group).

## Features
1. No-repeat - Each member will never be matched with the same partner more than once.
2. Late-comers - Additional members not in the original textfile can be added to the working memory in-between rounds.
3. Odd numbers - When the total number of members is odd, the unlucky extra person will be revealed at each round.

## Disclaimer
I didn't put much thought into this one, I made it quick and dirty. For that reason, it's probably not very efficient nor pretty. Code contributions are welcome :)

## Usage
Either run the Python script or download the compiled release. The program was coded and tested with Python 3.8.1.

1. Create a members.txt textfile in the same directory. Populate it based on the sample given in this repository.
2. That's pretty much it, just run the .py file or the compiled executable and you're good to go. Further instructions will be printed in the console.
