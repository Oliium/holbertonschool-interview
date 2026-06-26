#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], (e, res, charBody) => {
      if (e) {
        console.error(e);
        return;
      }
      console.log(JSON.parse(charBody).name);
      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
