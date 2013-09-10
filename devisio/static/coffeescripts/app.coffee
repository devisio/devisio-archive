$ = jQuery

class AlbumManager
  constructor: () ->
    @albums = new Array(0)
    this.registerAlbum $(link) for link in $('a[data-album-id]')

  registerAlbum: (link) ->
    @albums.push(new Album(link))


class Album
  constructor: (@link) ->
    @link.bind 'click', (evt) =>
      evt.preventDefault()
      response = $.ajax(this.getURL(), {'async': false}).responseText
      json = JSON.parse(response)
      @gallery = new document.Gallery(json)
      @gallery.show()

  getURL: () ->
    '/albums/'+@link.attr('data-album-id')+'/'


document.albums = new AlbumManager()

jQuery(document).on 'pjax:end', () ->
  document.albums = new AlbumManager()
