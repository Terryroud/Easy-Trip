var options = {
    valueNames: [ 'name', 'rate', 'desc' ],
};

// var values = [{
//     id: '1',
//     name: 'Кремль',
//     rate: '7/10',
//     desc: 'Крепость в центре Москвы и древнейшая её часть, главный общественно-политический и историко-художественный комплекс города, официальная резиденция Президента Российской Федерации.'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'

// },
// {
//     name: 'Martina Elm',
//     id: '2',
//     rate: '6/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '2',
//     rate: '9/10',
//     desc: 'dasfasdf'
// },
// {
//     name: 'Jonas Arnklint',
//     id: '3',
//     rate: '9/10',
//     desc: 'dasfasdf'
// }];


// var filteredValues = values.filter(function(item) {
//     return parseInt(item.id) > 1; // Фильтруем по id > 3
// });



var userList = new List('serlist', options);


const butfilt = document.querySelector(".filt")
const filters = document.querySelector(".filters")
const svgbf = document.querySelector(".svgbf")


butfilt.addEventListener("click", () => {


    if (filters.style.height === "120px") {
        svgbf.style.transform = "rotate(0deg)"
        filters.style.height = "0px";
    }
    else if (filters.style.height === "0px") {
        svgbf.style.transform = "rotate(180deg)"
        filters.style.height = "120px";
    }

})