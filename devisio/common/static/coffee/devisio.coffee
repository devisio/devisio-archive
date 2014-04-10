# devisio app
devisioApp = angular.module 'devisioApp', [
  'ngRoute',
  'ngSanitize',
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
    $routeProvider.when('/stream/', {
      templateUrl: '/static/partials/photos/photo_stream.html',
    }).when('/journal/', {
      templateUrl: '/static/partials/journals/journal_list.html',
      controller: 'JournalListCtrl'
    }).when('/journal/:journalId', {
      templateUrl: '/static/partials/journals/journal_detail.html',
      controller: 'JournalDetailCtrl'
    }).when('/archive/', {
      templateUrl: '/static/partials/photos/photo_archive.html',
    }).when('/about/', {
      templateUrl: '/static/partials/devisio/devisio_about.html',
    }).otherwise({
      redirectTo: '/journal'
    })
]

# ga
devisioApp.run ($rootScope, $location) ->
  ga("create", "UA-39701200-2", 'devisio.net')
  $rootScope.$on '$routeChangeSuccess', () ->
    ga('send', 'pageview', $location.path())

devisioApp.filter('nl2p', () ->
  return (text) ->
    text = String(text).trim()
    return '<p>' + text.replace(/[\r\n]+/, '</p><p>') + '</p>'
)

devisioApp.directive 'ngJournalFullscreen', () ->
  (scope, element, attrs) ->
    resize = () ->
      angular.element(element).css 'height', document.body.getBoundingClientRect().height - 64 + 'px'
    resize()
    window.addEventListener 'resize', () ->
      resize()

journal = angular.module('journal', ['restangular'])

journal.controller('JournalListCtrl', ($scope, Restangular) ->
  Restangular.all('journal').getList().then (journals) ->
    $scope.journals = journals
)

journal.controller('JournalDetailCtrl', ($scope, $routeParams, Restangular) ->
  Restangular.one('journal', $routeParams.journalId).get().then (journal) ->
    $scope.journal = journal
)
