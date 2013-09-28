$ = jQuery

class PhotoViewer

  constructor: (data) ->
    @photos = new Array(0)
    json = JSON.parse(data)

    this.addPhoto photo for photo in json

    @photoContainer = $('#photoviewer > .gallery > img')

    this.displayPhoto(0)

  addPhoto: (photo) ->
    photo.ratio = photo.width / photo.height
    @photos.push photo

  displayPhoto: (id) ->
    photo = @photos[id % @photos.length]
    @photoContainer.attr 'src', photo.src
    @photoContainer.css 'width', photo.width
    @photoContainer.css 'height', photo.height



document.PhotoViewer = PhotoViewer
