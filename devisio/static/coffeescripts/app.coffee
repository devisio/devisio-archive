$ = jQuery

class AlbumManager
  constructor: () ->
    @albums = new Array(0)
    this.registerAlbum album for album in $('div.album')

  registerAlbum: (album) ->
    @albums.push(new Album(album))


class Album
  constructor: (@album) ->
    @link = $(@album).children('a[data-album-id]')
    @link.bind 'click', (evt) =>
      evt.preventDefault()
      response = $.ajax(this.getURL(), {'async': false}).responseText
      json = JSON.parse(response)
      @gallery = new document.Gallery(json)
      @gallery.show()

  getURL: () ->
    '/albums/'+@link.attr('data-album-id')+'/'


document.albums = new AlbumManager()
