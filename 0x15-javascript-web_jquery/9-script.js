$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (lang) {
    $('#hello').text(lang.hello);
  }
});
