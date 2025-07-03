import tkinter as tk
import random

rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissor]


def play(user_choice):
    result_text.set("")  
    computer_choice = random.randint(0, 2)

    user_display.set("You chose:\n" + game_images[user_choice])
    comp_display.set("Computer chose:\n" + game_images[computer_choice])

    if user_choice == computer_choice:
        result_text.set("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        result_text.set("You win!")
    elif user_choice == 1 and computer_choice == 0:
        result_text.set("You win!")
    elif user_choice == 2 and computer_choice == 1:
        result_text.set("You win!")
    else:
        result_text.set("You lose!")


window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("600x600")
window.config(bg="lightblue")


tk.Label(window, text="Choose Rock, Paper or Scissors", font=("Helvetica", 16), bg="lightblue").pack(pady=10)


user_display = tk.StringVar()
comp_display = tk.StringVar()
result_text = tk.StringVar()

tk.Label(window, textvariable=user_display, font=("Courier", 10), bg="lightyellow", relief="solid", width=40, height=10).pack(pady=5)
tk.Label(window, textvariable=comp_display, font=("Courier", 10), bg="lightyellow", relief="solid", width=40, height=10).pack(pady=5)
tk.Label(window, textvariable=result_text, font=("Helvetica", 14, "bold"), bg="lightblue", fg="darkgreen").pack(pady=10)


button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack()

tk.Button(button_frame, text="Rock", font=("Helvetica", 12), width=12, command=lambda: play(0)).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Paper", font=("Helvetica", 12), width=12, command=lambda: play(1)).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Scissors", font=("Helvetica", 12), width=12, command=lambda: play(2)).grid(row=0, column=2, padx=10, pady=10)


window.mainloop()
