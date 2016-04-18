(function () {
  'use strict';

  angular
    .module('lima.maps.controllers')
    .controller('LayerHeatmapCtrl', LayerHeatmapCtrl);

  LayerHeatmapCtrl.$inject = ['$scope', '$interval', '$timeout', 'tweetData', 'Search', 'uiGmapGoogleMapApi'];

  function LayerHeatmapCtrl($scope, $interval, $timeout, tweetData, Search, uiGmapGoogleMapApi) {
    var vm = this;
    uiGmapGoogleMapApi.then(function(maps){
      var local_layer, heatLayer;
      $interval(function() {
        MockHeatLayer();
      }, 100);

      $scope.map = {
        center: {
          latitude: 37.09024,
          longitude: -95.712891
        }, zoom: 4
      };
    });

    function MockHeatLayer() {
      console.log('ah');
      var pointArray = tweetData.getPoints();
      setCircles(pointArray[0], pointArray[1], pointArray[2], pointArray[3]);
    };

        function getColor(sent) {
          var hue = 60 * (sent + 1);
          return 'hsl(' + hue + ', 100%, 50%)';
        }

        function setCircles(sf, atx, chi, nyc) {
          $scope.circles = [
                { //San Francisco
                  id: 1,
                  center: {
                      latitude: 37.7833,
                      longitude: -122.4167
                  },
                  radius: 100000,
                  stroke: {
                      color: getColor(sf),
                      weight: 2,
                      opacity: 1
                  },
                  fill: {
                      color: getColor(sf),
                      opacity: 0.5
                  }
                },
                { //Chicago
                  id: 2,
                  center: {
                      latitude: 41.8369,
                      longitude: -87.6847
                  },
                  radius: 100000,
                  stroke: {
                      color: getColor(chi),
                      weight: 2,
                      opacity: 1
                  },
                  fill: {
                      color: getColor(chi),
                      opacity: 0.5
                  }
                },
                { //NYC
                  id: 3,
                  center: {
                      latitude: 40.1727,
                      longitude: -74.0059
                  },
                  radius: 100000,
                  stroke: {
                      color: getColor(nyc),
                      weight: 2,
                      opacity: 1
                  },
                  fill: {
                      color: getColor(nyc),
                      opacity: 0.5
                  }
                },
                { //Austin
                    id: 4,
                    center: {
                        latitude: 30.25,
                        longitude: -97.75
                    },
                    radius: 100000,
                    stroke: {
                        color: getColor(atx),
                        weight: 2,
                        opacity: 1
                    },
                    fill: {
                        color: getColor(atx),
                        opacity: 0.5
                    }
                  }
              ];
      }
  }
})();
