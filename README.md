# The Impossible Chessboard Game

### Overview

In this project, we created a game version of the famous chessboard problem. This problem has a beautiful mathematical solution and it has a relation to the information theory. For an introduction to the problem see these two videos:

[The impossible chessboard puzzle](https://youtu.be/wTJI_WuZSwE?si=rGebZSKBCutLFXTd)

[The almost impossible chessboard puzzle](https://youtu.be/as7Gkm7Y7h4?si=uADsswiq5Y3Kmymo)

The solution that we used is explained completely in this repo:

[The Repo](https://github.com/CoryLR/impossible-chessboard-escape-puzzle?tab=readme-ov-file)

---

### The Game

we wanted to implement the concept behind the puzzle with a game. everytime you run the game, there will be a chessboard with some random-located Heads and Tails. there is a key inside one of the squares of the board. the users role here, is to find the key position with the algorithm that is explained in that repo we mentioned above. if the user clicks the true square there will be a winning message and the program will be closed. this is the same for losing. so the users are in the role of the second prisoner,who should guess the solution based on the agreed algorithm with the first prisoner.

---

### The Code

as we wanted this project to be more fun, we did the random Heads/Tails generation by C in the "main.c" file. The game is built with pygame in python in the "Game_Dev.py" file. the output of the C program goes into the "main.txt" file and the text is formatted such that the python file can read and use the data in it.

---

### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

### Contributors

- [Ermia](https://github.com/ErmiaAbbasi)
- [Alefittase](https://github.com/Alefittase)
