from handlers import points_data
from interface import text_format


def send():
    # Sends sorted scores.
    sorted_scores = points_data.retrieve_scores()

    text_format.send_separator_message("SCORES DATA")
    print("Listed from your highest to lowest score")
    print("PLAYER <--> KEEPER")

    # Prints out in format PLAYER SCORE <-> KEEPER SCORE.
    for i in range(len(sorted_scores)):
        print((sorted_scores[i][0] + " <-> " + sorted_scores[i][1]).center(18))
    return
