document.addEventListener('readystatechange', event => {
  if (event.target.readyState === 'complete') {
    document.querySelector('header').style.color = '#FF0000';
  }
});
