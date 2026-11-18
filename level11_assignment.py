# Level #11 Assignment - Video Game Catalog Manager
# IS 303 - Hilton
# Riley Kotter
#
# Reads video_games_raw.csv, lets the user inspect and update one game's
# status, flags recommended games, and saves the result to a new CSV file.
# The original CSV file is never overwritten.

import pandas as pd

# Read the CSV file into a DataFrame
dfGames = pd.read_csv("video_games_raw.csv")

print("VIDEO GAME CATALOG MANAGER")
print()

# Ask the user for a row number to inspect
iRow = int(input("Enter a row number to inspect: "))

# Use .iloc[] to access the selected row by position
selectedGame = dfGames.iloc[iRow]

print()
print("Selected Game:")
print(f"Title: {selectedGame['Title']}")
print(f"Platform: {selectedGame['Platform']}")
print(f"Genre: {selectedGame['Genre']}")
print(f"Rating: {selectedGame['Rating']}")
print(f"Current Status: {selectedGame['Status']}")
print()

# Ask for a new status and use .at[] to change that one value
sNewStatus = input("Enter a new status: ")
dfGames.at[iRow, "Status"] = sNewStatus

# Add the Recommended column, defaulting every game to No
dfGames["Recommended"] = "No"

# Use .loc[] to change multiple rows: rating at least 8 and price $40 or less
dfGames.loc[(dfGames["Rating"] >= 8) & (dfGames["Price"] <= 40), "Recommended"] = "Yes"

# Use .query() to filter and display the recommended games
dfRecommended = dfGames.query("Recommended == 'Yes'")

print()
print("Recommended Games:")
print(dfRecommended[["Title", "Platform", "Price", "Rating"]])
print()

# Save the updated data to a new file so the original stays unchanged
dfGames.to_csv("video_games_cleaned.csv", index=False)

print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv.")
