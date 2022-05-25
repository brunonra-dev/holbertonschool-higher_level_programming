fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Request failed');
    }
    return response.json();
  })
  .then(data => {
    const movies = data.results;
    for (const movie in movies) {
      $('UL#list_movies').append(`<li>${movies[movie].title}</li>`);
    }
    console.log();
  })
  .catch(error => console.log(error));
