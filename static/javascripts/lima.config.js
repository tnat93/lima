(function () {
  'use strict';

  angular
    .module('lima.config')
    .config(config);

  config.$inject = ['$locationProvider', 'uiGmapGoogleMapApiProvider'];

  function config($locationProvider, uiGmapGoogleMapApiProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
    uiGmapGoogleMapApiProvider.configure({
      v: '3.20',
      libraries: 'weather,geometry,visualization'
    });
  }
})();
