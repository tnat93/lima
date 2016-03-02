(function () {
  'use strict';

  angular
    .module('lima.maps.controllers')
    .controller('searchCtrl', searchCtrl);

  searchCtrl.$inject = ['$scope', 'Search', '$http', '$location'];

  function searchCtrl($scope, Search, $http, $location) {
    $scope.search = Search;
    $scope.blab = "";

  }

})();
