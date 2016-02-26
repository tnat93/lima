(function() {
  'use strict';

  angular
    .module('lima.routes')
    .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
      $routeProvider.when('/',{
        controller: 'searchCtrl',
        // controllerAs: 'vm',
        templateUrl: '/static/templates/search.html'
      }).when('/maps',{
        templateUrl: '/static/templates/map.html'
      }).otherwise('/');
    }
})();
