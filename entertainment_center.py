import media
import fresh_tomatoes

# This Python file contains instances of Favorite Movies
# used for popular the website

lord_of_rings = media.Movie("Lord of The Rings",
                            "The story of a boy and his friend trying to " +
                            "destroy a powerful ring",
                            "https://upload.wikimedia.org/wikipedia/pt/8/" +
                            "87/Ringstrilogyposter.jpg",
                            "https://www.youtube.com/watch?v=IUerKBZHnBs",
                            "2001",
                            "All you have to decide is what to do with the " +
                            "time that is given to you.")

harry_potter = media.Movie("Harry Potter",
                           "A young man going to study at Hogwarts",
                           "https://upload.wikimedia.org/wikipedia/pt/3/3a/" +
                           "Harry_Potter_and_the_Deathly_Hallows_-_Part_2.jpg",
                           "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                           "2001",
                           "Fear of a name increases fear of the thing " +
                           "itself.")


definitely_maybe = media.Movie("Definitely Maybe",
                               "Will tell his daughter about how meet " +
                               "her mother",
                               "https://upload.wikimedia.org/wikipedia/" +
                               "pt/a/a0/Definitely_Maybe_poster.jpg",
                               "https://www.youtube.com/watch?v=0oK4VOUmOkc",
                               "2008",
                               "I kept the book, because it was the only " +
                               "thing that I had left of you.")

me_before_you = media.Movie("Me Before You",
                            "Louisa Clark and Will Turner Love Story",
                            "https://upload.wikimedia.org/wikipedia/en/" +
                            "f/fd/Me_Before_You_%28film%29.jpg",
                            "https://www.youtube.com/watch?v=Eh993__rOxA",
                            "2016",
                            "Sometimes , Clark, you are pretty much the " +
                            "only thing that makes me want to get up in " +
                            "the morning")

beauty_and_beast = media.Movie("Beauty and The Beast",
                               "A girl starts to live an enchanted " +
                               "castle with a Beast",
                               "https://upload.wikimedia.org/wikipedia/" +
                               "pt/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                               "https://www.youtube.com/watch?v=OvW_L8sTu5E",
                               "2017",
                               "Think of the one thing that you have always " +
                               "wanted. Now find it in your mind is eye and " +
                               "feel it in your heart.")

star_wars = media.Movie("Star Wars - The Last Jedi",
                        "Rey tries to convince Luke to train her",
                        "https://upload.wikimedia.org/wikipedia/pt/0/0e/" +
                        "Star_Wars_The_Last_Jedi.png",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY",
                        "2017",
                        "I need someone to show me my place in all of this.")

# Instances used for create the website
movies = [lord_of_rings, harry_potter, definitely_maybe, me_before_you,
          beauty_and_beast, star_wars]
fresh_tomatoes.open_movies_page(movies)

