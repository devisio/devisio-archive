$(document).ready (evt) ->
  if $('.tabs').children('.tab.active').length <= 0
    $('.tabs').children().first().addClass 'active'
  $('.tab-link').on 'click', (evt) ->
    targetId = $(evt.target).attr('href').substring(1)

    targetElement = $('.tabs > .tab[data-tab=' + targetId + ']')
    $(element).removeClass('active') for element in $(targetElement.parents('.tabs')[0]).children()
    targetElement.addClass 'active'
