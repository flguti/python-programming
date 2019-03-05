# Create a variable called title_or_ratings, set to 1.
# You should be able to change this between 1, 2, and 3 to change what your program prints.
title_or_ratings = 3

# Create a variable `movie_title` and set it to "Back to the Future".
movie_title = "Back to the Future"

# Create a variable `movie rating` to hold the rating and set it to `8`.
movie_rating = 8

# Create a function, print_movie_title, that prints the movie title.
def print_movie_title():
    # Print the movie title.
    print(movie_title)

# Create a function, print_movie_rating, that prints the movie rating.
def print_movie_rating():
    # prints the movie rating.
    print(movie_rating)
  
# Create a function, print_single_movie_rating, that prints the string you had in lab 1.
def print_single_movie_rating():
    # Print the whole formatted string.
    print("The rating for", movie_title, "is", movie_rating)

# Create a function, print_all_ratings, that takes one argument movie_list.
# This prints "The movie <movie> has a great rating!"
def print_all_ratings(movie_list):
    # Print all great ratings for a movie list.
    for movie in movie_list:
        print("The movie", movie, "has a great rating!")

# Create one main function which will call everything else - subsituting function calls for the print statements.
def main():
    # Inside the main function, create a default_movie_list with "Back to the Future", "Blade", and "Spirited Away"
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]

    # Inside the main function, call the print_all_ratings function and pass it the default_movie_list as a parameter
    print_all_ratings(default_movie_list)

    # Inside the main function, put your print statement from the previous lab but subsitute function calls.
    # If title_or_ratings is 1, call print_movie_title
    if title_or_ratings == 1:
        print_movie_title()
    # If title_or_ratings is 2, call print_movie_rating().
    if title_or_ratings == 2:
        print_movie_rating()
    # If title_or_ratings is 3, call print_single_movie_rating()
    if title_or_ratings == 3:
        print_single_movie_rating()

# Start with this prompt for your `main` function
# It tells Python to go directly to the main function and run that
if __name__ == "__main__":
    main()