import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from plyer import notification  # pip install plyer

# Function to fetch IPL scores


def fetch_ipl_score():
    url = "https://www.cricbuzz.com/"
    page = requests.get(url)

    if page.status_code != 200:
        print("Failed to retrieve the page.")
        return

    soup = BeautifulSoup(page.text, "html.parser")

    # Find team names and scores
    teams = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
    scores = soup.find_all(class_="cb-ovr-flo")

    # Check if teams and scores are found
    if len(teams) < 2:
        print("Unable to find team names.")
        return

    if len(scores) < 11:  # Check if there are enough scores found
        print("Unable to find scores.")
        return

    # Get team names and scores
    team1 = teams[0].get_text()
    team2 = teams[1].get_text()
    team1_score = scores[8].get_text()
    team2_score = scores[10].get_text()

    # Print scores
    print(f"{team1} : {team1_score}")
    print(f"{team2} : {team2_score}")

    # Send notification
    notification.notify(
        title="IPL SCORE:",
        message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
        timeout=15
    )


# Call the function
fetch_ipl_score()
