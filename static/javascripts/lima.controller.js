(function () {
  'use strict';

  angular
    .module('lima')
    .controller('limaCtrl', limaCtrl);

  limaCtrl.$inject = ['$scope', 'Search'];

  function limaCtrl($scope, Search) {
    $scope.search = Search;
    // $scope.blab = "";
  }
})();
