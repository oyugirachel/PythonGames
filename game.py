score=0;
print("Guess the Country")
guess1=input("Which is the smallest country in Asia?")
def check_guess(guess,answer):
  global score
  if guess == answer:
     print('Correct answer')
  score = score + 1
 
check_guess(guess1,"Maldives")

guess2 = input('What is the name of the president of kenya?')
check_guess(guess2, 'Uhuru Kenyatta')
guess3 = input('Who is answering the questions?')
check_guess(guess3, 'Me')
guess4 = input('Which one of these is an animal?\n \
A) Goldfish\n B) Shark\n C) Hyena\n D) Jerry\n \
Type A, B, C, or D ')
check_guess(guess4, 'C')
print('Your score is ' + str(score))
