# Create a variable called search_or_ratings, set to "1".
# You should be able to change this between "1", "2", and "3" to change what your program prints.
search_or_ratings = 1

# Create a variable `movie_title` and set it to `"Back to the Future"`.
movie_title = "Back to the Future"

# Create a variable `movie rating` to hold the rating and set it to `8`.
movie_rating = 8

def list_search_results(movie_titles):
    # Loop through the list of titles and print them (indented with four spaces).
    for title in movie_titles:
        print("    " + title)

def print_movie_title():
    # Print the movie title.
    print(movie_title)

def print_movie_rating():
    # Print the movie rating.
    print(movie_rating)

def print_single_movie_rating():
    # Print the whole formatted string.
    print("The rating for", movie_title, "is", movie_rating)

def print_all_ratings(movie_list):
    # Print all great ratings for a movie list.
    for movie in movie_list:
        print("The movie", movie, "has a great rating!")


# Create one main function that will call everything else.
def main():

    # A hard-coded movie list with which to test.
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]

    # Let's test: Call a print_all_ratings() function and pass it the default_movie_list as a parameter.
    print_all_ratings(default_movie_list)

    if search_or_ratings == 1:
        # If search_or_ratings is "1", call list_search_results().
        list_search_results(default_movie_list)
    elif search_or_ratings == 2:
        # If search_or_ratings is "2", call print_movie_rating().
        print_movie_rating()
    else:
        # If search_or_ratings is "3", call print_single_movie_rating().
        print_single_movie_rating()

# This line tells Python to run main() when it first opens.
if __name__ == "__main__":
    main()