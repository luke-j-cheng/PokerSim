<h1>🎲 Poker Simulator 🎲</h1>
<b>
  My friends and I have gotten really into Texas Hold'em Poker recently
  <br/> One of the things we like to do while we wait for everyone to arrive is play our favorite hands with no betting, leaving the winner all up to chance
  <br/> This Poker Simulator aims to replicate that
</b> 
<h2> 🎰 How it Works 🎰</h2>
<b>
  1. The user chooses the amount of players that are in the game. Each player is dealt 2 unique cards
  <br/> 2. The code shows the community cards
  <br/> 3. The winner is calculated and shown, and the user can choose to keep playing or quit
</b>

<h2> Code </h2>
<h3> 🃏 Card Class 🃏</h3>

![Card Class](https://github.com/user-attachments/assets/c4b9e723-2bba-4e62-b899-b7fdfc47d530)
<br/>I made a card parent class and child classes for each card value in a 52 card deck
<br/> The class has 3 attributes: 
<br/>    - The card's name
<br/>    - The card's value 
<br/>    - The card's suit
<br/> Each child class has a set value for the name and value
<br/> I used a loop to create a card of every value in a certain suit, and repeated this for all 4 suits
<br/> Each individual card is added to the list of all cards

![Screenshot 2024-09-04 110952](https://github.com/user-attachments/assets/552d0337-e23e-49aa-9c72-c8027b4c6b19)

<h3> Hand Class </h3>

![Screenshot 2024-09-04 143526](https://github.com/user-attachments/assets/e397e03d-ba83-4c03-9c80-589db47efedf)

The Hand parent class consists of attributes: 
<br/> - Name: Title of the hand
<br/> - Score: The hand's score (used to calculate the best hand)
<br/> - High: A list of the hand's highcards (used for ties)
<br/> - Highnum: How many highcards are in the hand
<br/>Each child class of Hand is a different way that someone could win a hand
<br/> The child classes have fixed values for their score and highnum attribute

<h3> Nutsearch Function </h3>


