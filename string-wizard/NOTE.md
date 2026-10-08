# Notes For Python String Wizard Module
This is specific module, handles the challenges those manage strings and manipulating them (e.g. getting an URL subdomains and clean them.).

---

## Word Guessing
> Came from my college challenges of programming courses which professors gave us as homeword or an instant challenge to solve.

This is kind of **Wordle** game which let you guessing words thise match to the actual generated word by program. User guesses is limited (e.g. cannot guess more than 5 times) base on what we defined, also the letters.
#### Output
```
<user-guess-1>: <corrected-letters [int]> <corrected-indexes [int]>

e.g. abcde: 4 2 -> means 4 correct letters compared to the generated word and 2 of those corrected letters are in the right place/index.
```
