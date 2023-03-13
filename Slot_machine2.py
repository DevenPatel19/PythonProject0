import random
import tkinter as tk

# Define the symbols and their payouts
symbols = ["cherry", "lemon", "orange", "plum", "bell", "bar", "7"]
payouts = {"cherry": 2, "lemon": 3, "orange": 4, "plum": 5, "bell": 6, "bar": 7, "7": 10}

# Define the initial balance and bet amount
balance = 10
bet = 1


# Define the function to spin the reels
def spin():
    global balance
    global bet

    # Subtract the bet amount from the balance
    balance -= bet

    # Generate three random symbols
    symbols1 = random.choice(symbols)
    symbols2 = random.choice(symbols)
    symbols3 = random.choice(symbols)

    # Update the symbols in the GUI
    label1.config(text=symbols1)
    label2.config(text=symbols2)
    label3.config(text=symbols3)

    # Determine the payout based on the symbols
    if symbols1 == symbols2 == symbols3:
        payout = payouts[symbols1] * bet
        result_label.config(text="Jackpot! You won " + str(payout))
    elif symbols1 == symbols2 or symbols2 == symbols3 or symbols1 == symbols3:
        payout = payouts[symbols2] * bet
        result_label.config(text="Two of a kind! You won " + str(payout))
    else:
        result_label.config(text="Sorry, try again!")
        payout = 0

    # Add the payout to the balance
    balance += payout
    balance_label.config(text="Balance: " + str(balance))


# Define the main window and widgets
root = tk.Tk()
root.title("Slot Machine")

balance_label = tk.Label(root, text="Balance: " + str(balance))
balance_label.pack()

label1 = tk.Label(root, text="")
label1.pack(side="left", padx=10)

label2 = tk.Label(root, text="")
label2.pack(side="left", padx=10)

label3 = tk.Label(root, text="")
label3.pack(side="left", padx=10)

spin_button = tk.Button(root, text="Spin", command=spin)
spin_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
