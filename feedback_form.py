def gather_feedback():
    player_name = input("Enter your name: ")
    feedback = input("Share feedback: ")
    with open('feedback.txt', 'a') as f:
        f.write(f"Player: {player_name}\nFeedback: {feedback}\n\n")
