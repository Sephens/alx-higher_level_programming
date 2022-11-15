$.ajax({
  type: 'GET',
  url: 'https://swapi.co/api/people/5/?format=json',
  success: function (names) {
    $('#character').text(names.name);
  }
});
