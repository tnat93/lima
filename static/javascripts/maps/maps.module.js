(function () {
  'use strict';

  angular
    .module('lima.maps', [
      'lima.maps.controllers',
      'lima.maps.services'
    ]);

    angular
      .module('lima.maps.controllers', ['uiGmapgoogle-maps']);

    angular
      .module('lima.maps.services', []);
})();
