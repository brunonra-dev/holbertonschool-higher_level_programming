fetch('https://fourtonfish.com/hellosalut/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error('Request failed');
    }
    return response.json();
  })
  .then(data => {
    console.log(data.hello);
    $('DIV#hello').text(data.hello);
  })
  .catch(error => console.log(error));
