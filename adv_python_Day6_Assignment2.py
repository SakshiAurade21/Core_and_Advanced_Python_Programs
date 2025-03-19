class MovieLibrary:
    # Class Attribute: List of all available movies in the library
    available_movies = ["Inception", "Titanic", "Interstellar", "Avengers", "The Matrix"]

    def __init__(self, member_name):
        """Initialize a library member with a name and an empty borrowed movies list."""
        self.member_name = member_name
        self.borrowed_movies = []  # Stores movies borrowed by the member

    def borrow_movie(self, movie):
        """Allows a member to borrow a movie if available."""
        if movie in MovieLibrary.available_movies:
            self.borrowed_movies.append(movie)  # Add movie to borrowed list
            MovieLibrary.available_movies.remove(movie)  # Remove from library
            print(f"{self.member_name} borrowed '{movie}'")
        else:
            print(f"'{movie}' is not available.")

    def return_movie(self, movie):
        """Allows a member to return a borrowed movie."""
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)  # Remove from member's list
            MovieLibrary.available_movies.append(movie)  # Add back to library
            print(f"{self.member_name} returned '{movie}'")
        else:
            print(f"{self.member_name} does not have '{movie}' to return.")

    def view_borrowed_movies(self):
        """Displays the list of movies borrowed by the member."""
        if self.borrowed_movies:
            print(f"{self.member_name} has borrowed: {', '.join(self.borrowed_movies)}")
        else:
            print(f"{self.member_name} has not borrowed any movies.")


# Example Usage
# Viewing available movies before borrowing
print("Available Movies:", MovieLibrary.available_movies)

# Creating members
member1 = MovieLibrary("Alice")
member2 = MovieLibrary("Bob")

# Borrowing movies
member1.borrow_movie("Inception")
member2.borrow_movie("Titanic")

# Viewing borrowed movies
member1.view_borrowed_movies()
member2.view_borrowed_movies()

# Viewing available movies after borrowing
print("Available Movies:", MovieLibrary.available_movies)

# Returning movies
member1.return_movie("Inception")
member2.return_movie("Titanic")

# Viewing borrowed movies after returning
member1.view_borrowed_movies()
member2.view_borrowed_movies()

# Viewing available movies after returning
print("Available Movies:", MovieLibrary.available_movies)

'''
Output:
Available Movies: ['Inception', 'Titanic', 'Interstellar', 'Avengers', 'The Matrix']
Alice borrowed 'Inception'
Bob borrowed 'Titanic'
Alice has borrowed: Inception
Bob has borrowed: Titanic
Available Movies: ['Interstellar', 'Avengers', 'The Matrix']
Alice returned 'Inception'
Bob returned 'Titanic'
Alice has not borrowed any movies.
Bob has not borrowed any movies.
Available Movies: ['Interstellar', 'Avengers', 'The Matrix', 'Inception', 'Titanic']
'''
