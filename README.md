## AI-Word-Search-Solver
A Python-based word search puzzle application where an AI solver finds and highlights words in a randomly generated 15x15 grid. Built entirely using Python's built-in libraries.

---

#### Features

1. 9 themed puzzles across different categories
2. Randomly generated 15x15 word search grid
3. AI solver that finds words in all 8 directions
4. Animated cell-by-cell highlighting with unique colors per word
5. Strikethrough effect on found words
6. Clean and intuitive GUI with smooth screen transitions
7. Back navigation between screens  

---

#### How it Works

Generator:  

1. Creates an empty 15x15 grid
2. For each word, randomly picks a starting cell and direction
3. Checks if the word fits without conflicting with existing letters from other words
4. Retries up to 1000 times if placement fails
5. Fills remaining empty cells with random letters  

Solver:

1. Iterates over every cell in the grid
2. For each cell matching the first letter of the target word, searches all 8 directions
3. Uses recursion to walk letter by letter in the chosen direction
4. Returns the word's starting position and direction when found  

GUI:

1. Built with tkinter
2. Three screens: Welcome, Puzzle Gallery, and Puzzle
3. Each puzzle cell is a Label widget arranged in a grid
4. Solver results are used to animate highlighting across found word cells
5. Word list updates with strikethrough as words are found  

---

#### Screens

| Screen | Description |
|---|---|
| Welcome | App title and button to open the puzzle gallery |
| Puzzle Gallery | 3x3 grid of 9 themed puzzle buttons |
| Puzzle | Generated grid, word list, entry box, and solve button |  

---  

#### Puzzles Included

| Puzzle | Theme |
|---|---|
| Biscuits | Types of biscuits and snacks |
| New Year | New Year celebrations |
| Car Companies | Automobile brands |
| Olympics | Olympic games and sports |
| All American | American culture |
| Scotland | Scottish culture and landmarks |
| Science and Medicine | Medical and scientific terms |
| Parts of Circle | Geometry terms |
| Drum Kit | Musical instruments and percussion |  

---

#### Concepts Used

| Concept | Where |
|---|---|
| 2D Lists | Grid representation |
| Direction Vectors | 8-directional word placement and search |
| Bounds Checking | Prevents index errors during placement and search |
| Limited Backtracking | Retries word placement up to 1000 times |
| Randomisation | Random position, direction, and fill letters |
| Collision Detection | Detects letter conflicts during placement |
| Linear Search | Searches every cell in all 8 directions |
| Result Tracking | Stores found word locations for GUI highlighting |  

---

#### Limitations

 1. **Short words** (3 letters or fewer) may be found accidentally in random fill letters rather than where they were placed
2. **Words with spaces or hyphens** are not supported — only single unbroken words work correctly
3. **Rarely**, a word may not be placed if the grid becomes too crowded after 1000 failed attempts
4. **Grid is not fixed** — the same puzzle generates a different layout every time it is loaded

---

#### Future Improvements
 
1. Custom puzzle creator where users can enter their own word lists
2. Support for multi-word phrases by skipping spaces during search  

---

#### Inspiration

This project was inspired by the *Dreamland Super Word Search* book series, which features 15x15 word search grids across themed categories.