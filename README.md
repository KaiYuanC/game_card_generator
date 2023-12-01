# Game Card Generator
A simple python script to generate a PDF of printable (not pretty) game cards

<img width="400" alt="image" src="https://github.com/KaiYuanC/game_card_generator/assets/32350356/0323e189-89a1-4d10-b165-4bcca7620761">


## Context
There is a boardgame called *The Crew* that I really enjoyed playing during a summer internship, so I decided to purchase it and spread it among more people.

What happened was, I got the wrong version. I got [The Crew: The Quest for Planet Nine](https://boardgamegeek.com/boardgame/284083/crew-quest-planet-nine) the older version.
I wanted [The Crew: Mission Deep Sea](https://boardgamegeek.com/boardgame/324856/crew-mission-deep-sea) which has more variations and simpler rules. 

Mission Deep Sea is out of stock on all non-sketchy sources near me unfortunately. Out of desperation, I decided to print my own cards from the [card prompts](https://www.scribd.com/document/594466041/the-crew-deep-sea-mission-cards) I found online. 

Small Disclaimer: This is not promoting creating fake cards but for creating your own game cards. (I just really wanted to play the game)

## Code
- Update the card context file, the front/back parsing, and card dimensions before running the code
- Note that the odd pages are the front of the cards and even pages are the back
- Run `python3 generate_cards.py` or equivalent, a PDF called cards.pdf should be generated
  
## Printing
- Make sure to print double sided
- Currently the card number has to be multiples of 4 or whatever you set or the double sided mechanism will not work, the cards on the last page will not be printed correctly

## Future Improvements
- Remove hardcoded values and use constants/configs
- Fix printing problem for cards not multiple of 4
- Investigate why font changes for `reportlab` is not working
- Consider using json instead of txt if needed
- back and front of the card should be different colors to facilitate shuffling
