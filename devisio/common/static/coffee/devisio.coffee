devisioApp = angular.module 'devisioApp', [
  'ngRoute',
  'journal'
]

devisioApp.config((RestangularProvider) ->
  RestangularProvider.setBaseUrl("/api/v1")
  RestangularProvider.setResponseExtractor((response, operation, what, url) ->
    if (operation is "getList")
      newResponse = response.objects
      newResponse.metadata = response.meta
    else
      newResponse = response
    return newResponse
  )
  RestangularProvider.setRequestSuffix('/?')
)

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

journal = angular.module('journal', ['restangular'])

journal.controller('JournalListCtrl', ($scope, Restangular) ->
  Restangular.all('journal').getList().then (journals) ->
    $scope.journals = journals
)

journal.controller('JournalDetailCtrl', ($scope, $routeParams, Restangular) ->
  Restangular.one('journal', $routeParams.journalId).get().then (journal) ->
    $scope.journal = journal
)
