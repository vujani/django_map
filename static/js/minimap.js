var myMap;
ymaps.ready(init);

var x_coord = $("#xcord").val();
var y_coord = $("#ycord").val();



function init () {

    myMap = new ymaps.Map('minimap', {
        center: [x_coord, y_coord],
        zoom: 14
    });

    myMap.controls.remove('trafficControl');
    myMap.controls.remove('geolocationControl');
    myMap.controls.remove('searchControl');
    myMap.controls.remove('fullscreenControl');

}