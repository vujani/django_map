ymaps.ready(init);
function init(){
    var myMap = new ymaps.Map("map", {
        center: [48.475544, 135.068398],
        zoom: 13,
        behaviors: ['default', 'scrollZoom'],
        controls: ['default']
    }, {
    balloonMaxWidth: 200,
    floatIndex: 10
    }),
    objectManager = new ymaps.ObjectManager({
        // Чтобы метки начали кластеризоваться, выставляем опцию.
        clusterize: true,
        // ObjectManager принимает те же опции, что и кластеризатор.
        gridSize: 32,
        clusterDisableClickZoom: true
        });
    myMap.controls.remove('trafficControl');
    myMap.controls.remove('geolocationControl');
    myMap.controls.remove('searchControl');
    myMap.controls.remove('fullscreenControl');

    var myButton = new ymaps.control.Button({
        data: {
            'content': '<b>Нажмите на карту, чтобы добавить метку</b>'
        },
        options: {
            selectOnClick: false,
            maxWidth: 300
        }});
    myMap.controls.add(myButton, {
        float: "left",
    });

    // внешний вид балуна Да/ Нет
    BalloonContentLayout = ymaps.templateLayoutFactory.createClass(
    '<div style="width: 200px; background: #fff; text-align: center; border-radius: 15px; border: 2px solid #696969;">' +
    '<h5 class="modal-title" id="exampleModalLabel">Добавить метку?</h5>' +
    '<div style="display: flex; justify-content: space-between; padding: 1em">' +
    '<button id="btnyes" type="button" class="btn btn-primary" data-dismiss="modal">Да</button>' +
    '<button id="btnno" type="button" class="btn btn-secondary">Нет</button></div>' +
    '</div></div>', {

        build: function() {
            BalloonContentLayout.superclass.build.call(this);
            $('#btnyes').bind('click', this.ButtonYes);
            $('#btnno').bind('click', this.ButtonNo);
            },

        clear: function() {
            $('#btnyes').unbind('click', this.ButtonYes);
            $('#btnno').unbind('click', this.ButtonNo);
            BalloonContentLayout.superclass.clear.call(this);
        },

        ButtonNo: function() {
          myMap.balloon.close();
        },

        ButtonYes: function() {
          myMap.balloon.close();
          var sidebar = document.getElementById('sidebar')
            sidebar.style.visibility = 'visible'
        }
      });


    // Обработка события, возникающего при щелчке
    // левой кнопкой мыши в любой точке карты.
    // При возникновении такого события откроем балун.
    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords');
            myMap.balloon.open(coords, {
                name: "single balloon"
                }, {
                layout: BalloonContentLayout
            });
        }
        else {
            myMap.balloon.close();
        }
    });


    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    myMap.geoObjects.add(objectManager);

    $.ajax({
        url: "static/tags/tags.json"
    }).done(function(data) {
        objectManager.add(data);
    });

}
