// Get the search input element from the page
const searchInput = document.getElementById("searchInput");

// Get all movie cards
const movieCards = document.querySelectorAll(".movie-card");


// Run this function whenever the user types something
searchInput.addEventListener("input", function () {

    // Convert the search text to lowercase
    // so that search is not case-sensitive
    const searchText = searchInput.value.toLowerCase();


    // Check every movie card
    movieCards.forEach(function (card) {

        // Get the movie title from the card
        const movieTitle = card
            .querySelector("h3")
            .textContent
            .toLowerCase();


        // Show matching movies
        if (movieTitle.includes(searchText)) {

            card.style.display = "block";

        } else {

            // Hide movies that don't match
            card.style.display = "none";
        }

    });

});