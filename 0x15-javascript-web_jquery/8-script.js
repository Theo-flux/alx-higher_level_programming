$('document').ready(() => {
    $.ajax(
        {
            url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
            success: (res) => {
                res.results.map((data, index) => {
                    $('UL#list_movies').append(`<li>${data.title}</li>`)
                })
            }
        }
    );
});