import time
import tkinter as tk
from puzzleGenerator import generatePuzzleGrid
from puzzleSolver import solvePuzzleGrid

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
    e.widget.config(bg="#c73652")

def onLeave(e):
    e.widget.config(bg="#e94560")
    
def loadPuzzle(puzzle):
     typeWriter(f"Loading {puzzle}...")
     words = PUZZLES[puzzle]
     grid = generatePuzzleGrid(words)
     galleryFrame.pack_forget()
     puzzleFrame.pack(fill=tk.BOTH, expand=True)
     displayGrid(grid)
     
def createBackButton(frame, command):
    btnBack = tk.Button(
        frame,
        text="← Back",
        bg="#e94560",
        fg="#ffffff",
        font=("Courier", 11, "bold"),
        relief="flat",
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
     
     for r in range(15):
          r= []
          for c in range(15):
               lbl = tk.Label(
                    leftFrame,
                    text=grid[r][c],
                    font=("Courier", 14, "bold"),
                    width=2,
                    height=1,
                    relief="flat",
                    bg="#0f3460", 
                    fg="#ffffff",
               )
               lbl.grid(row=r, column=c, padx=2, pady=2)
               row.append(lbl)
          cellLabels.append(row)
    
PUZZLES = {
     "Biscuits" : ["CHEESE", "COFFEE", "COOKIES", "CRACKERS", "CREAM", "ENERGEN", "FINGERS", "GLUCOSE", "RITZ", "SALTY", "SAVORY", "SNACKS", "SWEET", "WAFER"],
     "New Year" : ["BALLOONS", "BEGINNING", "CAKE", "DANCE", "DINNER", "DRINKS", "ENJOYMENT", "FIREWORKS", "HATS", "JANUARY", "MIDNIGHT", "NEW", "PARADE", "PARTIES", "RESOLUTIONS", "TOGETHER", "TRADITION"],
     "Car Companies" : ["AUDI", "BMW", "CHRYSLER", "FIAT", "FORD", "HONDA", "HYUNDAI", "IMPALA", "LINCOLN", "MAHINDRA", "MAYBACH", "MERCEDES", "MITSUBISHI", "NISSAN", "PORSCHE", "TOYOTA", "VOLVO"],
     "Olympics" : ["ARCHERY", "BASKETBALL", "BRONZE", "CEREMONY", "COUNTRY", "DIVING", "GAMES", "GOLD", "GYMNASTICS", "HOCKEY", "HONOR", "MEDALS", "RESPECT", "SILVER", "SWIMMING", "TORCH", "VOLLEYBALL"],
     "All American": ["AVOCET", "BEAVER", "BITTERN", "BREAKFAST", "BURGERS", "COCKROACHES", "FLAG", "FOOTBALL", "FOOTLONGS", "LOBSTER", "MINK", "SALAMI", "SNAKE", "TWINS", "YANKEES"],
     "Scotland" : ["AYE", "BAIM", "BRAE", "BRUCE", "BRUN", "DRAM", "DRINK", "EDINBURGH", "HIGHLAND", "HILLSIDE", "KELPY", "LAKE", "LOCH", "MOORS", "ROBROY", "SMALL", "STREAM", "WALLACE", "WEF"],
     "Science and Medicine" : ["AIDS", "ANALGESICS", "ANTIBIOTICS", "ECG", "ECOSYSTEM", "EEG", "EFFECT", "GREENHOUSE", "HORMONES", "MEDICINES", "NARCOTICS", "PACEMAKER", "POLYGRAPH", "SEDATIVES", "TRANQUILIZERS", "VACCINES"],
     "Parts of Circle" : ["ARC", "CHORD", "CIRCUMFERENCE", "DIAMETER", "LOOP", "ORBIT", "RADIUS", "RING", "ROTATE", "ROUND", "SECTOR", "SET", "TANGENT", "TURN", "WHEEL"],
     "Drum Kit" : ["BASS", "BELL", "BIWA", "CYMBAL", "DRUM", "FLUTE", "HARP", "LYRE", "MARACA", "MBIRA", "PIPE", "REGAL", "SANSA", "STAND"]
     }

window = tk.Tk()
window.configure(bg="#0f3460")

#setting the size of the window
width = 900
height = 600

#getting the screen dimensions
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

#calculating centre position
x = (screenWidth // 2) - (width // 2)
y = (screenHeight // 2) - (height // 2)


window.geometry(f"{width}x{height}+{x}+{y}")

welcomeFrame = tk.Frame(window, bg="#0f3460")
galleryFrame = tk.Frame(window, bg="#0f3460")
puzzleFrame =  tk.Frame(window, bg="#0f3460")

leftFrame = tk.Frame(puzzleFrame, bg="#0f3460")
rightFrame = tk.Frame(puzzleFrame, bg="#0f3460")


welcomeFrame.pack(fill=tk.BOTH, expand=True)

lblTitle = tk.Label(
     welcomeFrame,
     text="Welcome to the AI Word Search Solver!",
     font=("Courier", 20, "bold"),
     bg="#0f3460",
     fg="#ffffff"
)

lblTitle.pack(pady=60)

btnStart = tk.Button(
     welcomeFrame,
     text="Open Puzzle Gallery",
     width=20,
     height=2,
     relief = "raised",
     bg = "#e94560",
     fg="#ffffff",
     font=("Courier", 12, "bold"),
     cursor="hand2",
     
     borderwidth=0,
     command=openGallery
)



btnStart.pack(pady=120)

btnStart.bind("<Enter>", onHover)
btnStart.bind("<Leave>", onLeave)

lblTitle2 = tk.Label(
     galleryFrame,
     text="Puzzle Gallery",
     font=("Courier", 20, "bold"),
     bg="#0f3460",
     fg="#ffffff"
)

lblTitle2.pack(pady=50)

gridFrame = tk.Frame(
     galleryFrame,
     bg="#0f3460"
)

gridFrame.pack(pady=30)

for index, puzzle in enumerate(PUZZLES):
     row = index // 3
     col = index % 3
     
     btnPuzzle = tk.Button(
          gridFrame,
          text=puzzle,
          width=25,
          height=3,
          bg="#e94560",
          fg="#ffffff",
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
rightFrame.pack(side=tk.RIGHT, padx=20, pady=20)



window.mainloop()