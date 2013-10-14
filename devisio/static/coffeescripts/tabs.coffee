$(document).ready (evt) ->
  initializeTabs()

  $('#pjax-container').on 'pjax:end', (evt) ->
    initializeTabs()


registerTabs = (tabs) ->
  container = $(tabs)

  if container.children('.tab.active').length <= 0
    container.children().first().addClass 'active'

  $('.tab-link').on 'click', (evt) ->
    evt.preventDefault()
    targetId = $(evt.target).attr('href').substring(1)

    console.log $(evt.target).parent('.tabs').trigger 'change'

    targetElement = $('.tabs > .tab[data-tab=' + targetId + ']')
    $(element).removeClass('active') for element in $(targetElement.parents('.tabs')[0]).children()
    targetElement.addClass 'active'

initializeTabs = () ->
  registerTabs tab for tab in $('.tabs')
