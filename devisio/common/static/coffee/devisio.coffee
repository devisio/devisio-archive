devisioApp = angular.module 'devisioApp', [
  'ngRoute',
  'journal'
]

devisioApp.config [
  '$routeProvider', ($routeProvider) ->
    $routeProvider.when('/journal', {
      templateUrl: '/static/partials/journals/journal_list.html',
      controller: 'JournalListCtrl'
    }).when('/journal/:journalSlug', {
      templateUrl: '/static/partials/journals/journal_detail.html',
      controller: 'JournalDetailCtrl'
    }).otherwise({
      redirectTo: '/journal'
    })
]

journal = angular.module('journal', ['ngResource'])

journal.factory('Journal', ['$resource', ($resource) ->
  return $resource('/crud/journals/', {'slug': '@slug'}, {})
])

journal.controller('JournalListCtrl', ['$scope', 'Journal', ($scope, Journal) ->
  $scope.journals = Journal.query()
])

journal.controller('JournalDetailCtrl', ['$scope', '$routeParams', 'Journal', ($scope, $routeParams, Journal) ->
  $scope.journal = Journal.get({slug: $routeParams.journalSlug})
])
