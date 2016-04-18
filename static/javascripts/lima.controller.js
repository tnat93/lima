(function () {
  'use strict';

  angular
    .module('lima')
    .controller('limaCtrl', limaCtrl);

  limaCtrl.$inject = ['$scope', '$pusher', 'Search', 'tweetData'];

  function limaCtrl($scope, $pusher, Search, tweetData) {
    $scope.search = Search;
    var client = new Pusher('b87e84a0194862d39bdd');
    var pusher = $pusher(client)
    pusher.subscribe('lima');
    pusher.bind('tweet_stream',
      function(data) {
        console.log(data);
        tweetData.getSentiment(data.data);
      });
    $scope.blab = "";
  }
})();
