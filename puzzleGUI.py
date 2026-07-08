import time
import tkinter as tk
import tkinter.font as tkFont
from puzzleGenerator import generatePuzzleGrid
from puzzleSolver import solvePuzzleGrid

# Color palette
BG           = "#accbe1"  
BUTTON       = "#7c98b3"  
BUTTON_HOVER = "#2F4153"  
BORDER       = "#072230"   
CELL_BG      = "#7c98b3"   
CELL_FG      = "#2F4153"   
TEXT_FG      = "#072230"  
BTN_TEXT     = "#2F4153"  
BTN_HOVER_TEXT = "#7c98b3"
HIGHLIGHT_COLORS = [
    ("#f7c948", "#072230"),   # yellow
    ("#f4845f", "#072230"),   # orange
    ("#f26ca7", "#072230"),   # pink
    ("#c77dff", "#072230"),   # purple
    ("#74b3ce", "#072230"),   # sky blue
    ("#52b788", "#072230"),   # mint green
    ("#f94144", "#fbfff1"),   # red
    ("#90e0ef", "#072230"),   # light cyan
    ("#b7e4c7", "#072230"),   # pale green
    ("#ffd6ff", "#072230"),   # lavender
]

currentGrid = []

highlightIndex = 0

def typeWriter(text, delay=0.03):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()

def openGallery():
    welcomeFrame.pack_forget()
    galleryFrame.pack(fill=tk.BOTH, expand=True)

def backToWelcome():
    galleryFrame.pack_forget()
    welcomeFrame.pack(fill=tk.BOTH, expand=True)

def backToGallery():
    puzzleFrame.pack_forget()
    galleryFrame.pack(fill=tk.BOTH, expand=True)

def onHover(e):
    e.widget.config(bg=BUTTON_HOVER, fg=BTN_HOVER_TEXT)

def onLeave(e):
    e.widget.config(bg=BUTTON, fg=BTN_TEXT)

def loadPuzzle(puzzle):
    typeWriter(f"Loading {puzzle}...")
    global currentGrid, highlightIndex
    highlightIndex = 0
    words = PUZZLES[puzzle]
    currentGrid = generatePuzzleGrid(words)
    galleryFrame.pack_forget()
    puzzleFrame.pack(fill=tk.BOTH, expand=True)
    
    for widget in topFrame.winfo_children():
        widget.destroy()  
    
    lblPuzzleName = tk.Label(
        topFrame,
        text=puzzle,
        font=("Courier", 20, "bold"),
        bg=BG,
        fg=TEXT_FG,
    )
    lblPuzzleName.pack(pady=(10,0))
    
    displayGrid(currentGrid)
    displayWords(words)

def createBackButton(frame, command):
    btnBack = tk.Button(
        frame,
        text="← Back",
        bg=BUTTON,
        fg=BTN_TEXT,
        font=("Courier", 11, "bold"),
        relief="raised",
        cursor="hand2",
        command=command
    )
    btnBack.place(x=10, y=10)
    btnBack.bind("<Enter>", onHover)
    btnBack.bind("<Leave>", onLeave)
    return btnBack

cellLabels = []

def displayGrid(grid):
    global cellLabels
    cellLabels = []
    
    for widget in rightFrame.winfo_children():
        widget.destroy()  

    for r in range(15):
        row = []
        for c in range(15):
            cellFrame = tk.Frame(
                leftFrame,
                bg=BORDER,
                padx=1,
                pady=1
            )
            cellFrame.grid(row=r, column=c, padx=0, pady=0)

            lbl = tk.Label(
                cellFrame,
                text=grid[r][c],
                font=("Courier", 14, "bold"),
                width=2,
                height=1,
                relief="flat",
                bg=CELL_BG,
                fg=CELL_FG,
            )
            lbl.pack()
            row.append(lbl)
        cellLabels.append(row)
        
def displayWords(words):
     global wordLabels
     wordLabels = {}
     for widget in rightFrame.winfo_children():
        widget.destroy()  
     wordsFrame = tk.Frame(rightFrame, bg=BG)
     wordsFrame.pack(anchor="center", pady=(40, 5))
     
     for index, word in enumerate(words):
        row = index // 2    
        col = index % 2     

        lbl = tk.Label(
            wordsFrame,
            text=f"• {word}",
            font=("Courier", 14, "bold"),
            bg=BG,
            fg=TEXT_FG,
            anchor="w",
            width=14            
        )
        lbl.grid(row=row, column=col, padx=5, pady=2, sticky="w")
        wordLabels[word] = lbl
     
     separator = tk.Frame(rightFrame, bg=BUTTON_HOVER, height=2)
     separator.pack(fill="x", padx=20, pady=10)
     
     lblEntry = tk.Label(
        rightFrame,
        text="Enter a word:",
        font=("Courier", 14),
        bg=BG,
        fg=TEXT_FG
    )
     
     lblEntry.pack()
     
     wordEntry = tk.Entry(
        rightFrame,
        font=("Courier", 14),
        bg=BUTTON,
        fg=BTN_TEXT,
        insertbackground=BTN_TEXT,
        relief="flat",
        justify="center"
    )
     
     wordEntry.pack(pady=5, ipady=5, fill="x", padx=20)
     
     btnSolve = tk.Button(
        rightFrame,
        text="SOLVE",
        font=("Courier", 14, "bold"),
        bg=BUTTON,
        fg=BTN_TEXT,
        relief="raised",
        cursor="hand2",
        height=2,
        command=lambda: solveWord(wordEntry.get(), words)
    )
     
     btnSolve.pack(pady=10, fill="x", padx=20)
     btnSolve.bind("<Enter>", onHover)
     btnSolve.bind("<Leave>", onLeave)

def solveWord(word, words):
    global highlightIndex
    word = word.strip().upper()
    if word not in words:
        typeWriter("Word is not in the word list.")
        return
    result = solvePuzzleGrid(currentGrid, [word])
    if not result:
        typeWriter(f"{word} not found.")
        return
    foundWord, row, col, dr, dc = result[0]
    
    bgColor, fgColor = HIGHLIGHT_COLORS[highlightIndex % len(HIGHLIGHT_COLORS)]
    highlightIndex += 1   
    
    highlightWord(word, row, col, dr, dc, bgColor, fgColor)
    existingFont = tkFont.Font(font=wordLabels[word]["font"])
    existingFont.configure(overstrike=1)
    wordLabels[word].config(font=existingFont, fg=BUTTON_HOVER)
    typeWriter(f"{word} found!")
     
def highlightWord(word, row, col, dr, dc, bgColor, fgColor, letter=0):
    if letter == len(word):
        return
    currentRow = row + (letter * dr)
    currentColumn = col + (letter * dc)
    cellLabels[currentRow][currentColumn].config(bg=bgColor, fg=fgColor)
    window.after(100, lambda: highlightWord(word, row, col, dr, dc, bgColor, fgColor, letter+1))
     
PUZZLES = {
    "Biscuits" : ["CHEESE", "COFFEE", "COOKIES", "CRACKERS", "CREAM", "ENERGEN", "FINGERS", "GLUCOSE", "RITZ", "SALTY", "SAVORY", "SNACKS", "SWEET", "WAFER"],
    "New Year" : ["BALLOONS", "BEGINNING", "CAKE", "DANCE", "DINNER", "DRINKS", "ENJOYMENT", "FIREWORKS", "HATS", "JANUARY", "MIDNIGHT", "NEW", "PARADE", "PARTIES", "RESOLUTIONS", "TOGETHER", "TRADITION"],
    "Car Companies" : ["AUDI", "BMW", "CHRYSLER", "FIAT", "FORD", "HONDA", "HYUNDAI", "IMPALA", "LINCOLN", "MAHINDRA", "MAYBACH", "MERCEDES", "MITSUBISHI", "NISSAN", "PORSCHE", "TOYOTA", "VOLVO"],
    "Olympics" : ["ARCHERY", "BASKETBALL", "BRONZE", "CEREMONY", "COUNTRY", "DIVING", "GAMES", "GOLD", "GYMNASTICS", "HOCKEY", "HONOR", "MEDALS", "RESPECT", "SILVER", "SWIMMING", "TORCH", "VOLLEYBALL"],
    "All American" : ["AVOCET", "BEAVER", "BITTERN", "BREAKFAST", "BURGERS", "COCKROACHES", "FLAG", "FOOTBALL", "FOOTLONGS", "LOBSTER", "MINK", "SALAMI", "SNAKE", "TWINS", "YANKEES"],
    "Scotland" : ["AYE", "BAIM", "BRAE", "BRUCE", "BRUN", "DRAM", "DRINK", "EDINBURGH", "HIGHLAND", "HILLSIDE", "KELPY", "LAKE", "LOCH", "MOORS", "ROBROY", "SMALL", "STREAM", "WALLACE", "WEF"],
    "Science and Medicine" : ["AIDS", "ANALGESICS", "ANTIBIOTICS", "ECG", "ECOSYSTEM", "EEG", "EFFECT", "GREENHOUSE", "HORMONES", "MEDICINES", "NARCOTICS", "PACEMAKER", "POLYGRAPH", "SEDATIVES", "TRANQUILIZERS", "VACCINES"],
    "Parts of Circle" : ["ARC", "CHORD", "CIRCUMFERENCE", "DIAMETER", "LOOP", "ORBIT", "RADIUS", "RING", "ROTATE", "ROUND", "SECTOR", "SET", "TANGENT", "TURN", "WHEEL"],
    "Drum Kit" : ["BASS", "BELL", "BIWA", "CYMBAL", "DRUM", "FLUTE", "HARP", "LYRE", "MARACA", "MBIRA", "PIPE", "REGAL", "SANSA", "STAND"]
}


window = tk.Tk()
window.title("AI Word Search Solver")
window.configure(bg=BG)

width = 900
height = 600

screenWidth  = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
x = (screenWidth  // 2) - (width  // 2)
y = (screenHeight // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")


welcomeFrame = tk.Frame(window, bg=BG)
galleryFrame = tk.Frame(window, bg=BG)
puzzleFrame  = tk.Frame(window, bg=BG)
topFrame = tk.Frame(puzzleFrame, bg=BG)
topFrame.pack(side=tk.TOP, fill=tk.X, pady=10)
leftFrame    = tk.Frame(puzzleFrame, bg=BORDER, padx=1, pady=1)
rightFrame   = tk.Frame(puzzleFrame, bg=BG)

welcomeFrame.pack(fill=tk.BOTH, expand=True)


lblTitle = tk.Label(
    welcomeFrame,
    text="Welcome to the AI Word Search Solver!",
    font=("Courier", 20, "bold"),
    bg=BG,
    fg=TEXT_FG
)
lblTitle.pack(pady=60)

btnStart = tk.Button(
    welcomeFrame,
    text="Open Puzzle Gallery",
    width=20,
    height=2,
    relief="raised",
    bg=BUTTON,
    fg=BTN_TEXT,
    font=("Courier", 12, "bold"),
    cursor="hand2",
    command=openGallery
)

btnStart.pack(pady=120)
btnStart.bind("<Enter>", onHover)
btnStart.bind("<Leave>", onLeave)


lblGalleryTitle = tk.Label(
    galleryFrame,
    text="Puzzle Gallery",
    font=("Courier", 20, "bold"),
    bg=BG,
    fg=TEXT_FG
)
lblGalleryTitle.pack(pady=50)

gridFrame = tk.Frame(galleryFrame, bg=BG)
gridFrame.pack(pady=30)

for index, puzzle in enumerate(PUZZLES):
    row = index // 3
    col = index % 3

    btnPuzzle = tk.Button(
        gridFrame,
        text=puzzle,
        width=25,
        height=3,
        bg=BUTTON,
        fg=BTN_TEXT,
        font=("Courier", 12, "bold"),
        relief="raised",
        cursor="hand2",
        command=lambda p=puzzle: loadPuzzle(p)
    )
    btnPuzzle.grid(row=row, column=col, padx=10, pady=10)
    btnPuzzle.bind("<Enter>", onHover)
    btnPuzzle.bind("<Leave>", onLeave)

createBackButton(galleryFrame, backToWelcome)

leftFrame.pack(side=tk.LEFT, padx=20, pady=20)
rightFrame.pack(side=tk.RIGHT, padx=20, pady=20, expand=True, fill=tk.BOTH)
createBackButton(puzzleFrame, backToGallery)

window.mainloop()