devisioApp = angular.module 'devisioApp', [
  'ngRoute',
  'journal'
]

devisioApp.config [
  '$routeProvider', ($routeProvider) ->
    $routeProvider.when('/journal', {
      templateUrl: '/static/partials/journals/journal_list.html',
      controller: 'JournalListCtrl'
    }).when('/journal/:journalId', {
      templateUrl: '/static/partials/journals/journal_detail.html',
      controller: 'JournalDetailCtrl'
    }).otherwise({
      redirectTo: '/journal'
    })
]

journal = angular.module('journal', [])

journal.factory 'Journal', ['$resource', ($resource) ->
  return $resource('/crud/journal/', {'pk': '@pk'}, {})
]

journals = [
  {id: 1, title: 'Test1'},
  {id: 2, title: 'Test2'},
  {id: 3, title: 'Test3'},
  {id: 4, title: 'Test4'},
]


journal.controller('JournalListCtrl', ['$scope', ($scope) ->
  $scope.journals = journals
])

journal.controller('JournalDetailCtrl', ['$scope', '$routeParams', ($scope, $routeParams) ->
  $scope.journal = journals[$routeParams.journalId - 1]
])
