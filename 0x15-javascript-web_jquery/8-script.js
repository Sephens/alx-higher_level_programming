$.ajax({
    type: 'GET',
    url: "https://swapi.co/api/films/?format=json",
    success: function (movies) {
      movies.results.forEach(function(item) {
        $('#list_movies').append('<li>' + item.title + '</li>')
});
}
});
