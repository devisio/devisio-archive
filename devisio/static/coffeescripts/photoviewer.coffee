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

  displayPhoto: () ->
    photo = @photos[@pos % @photos.length]
    @photoContainer.attr 'src', photo.src
    @photoContainer.css 'width', photo.width
    @photoContainer.css 'height', photo.height

  _translatePosition: () ->
   @pos = @pos % @photos.length
   if @pos < 0
     @pos = @photos.length

  nextPhoto: () ->
    @pos++
    this._translatePosition()
    this.displayPhoto()

  prevPhoto: () ->
    @pos--
    this._translatePosition()
    this.displayPhoto()


  registerListeners: () ->
    $('#photoviewer a.next').bind 'click', (evt) =>
      evt.preventDefault()
      this.nextPhoto()
    $('#photoviewer a.prev').bind 'click', (evt) =>
      evt.preventDefault()
      this.prevPhoto()



document.PhotoViewer = PhotoViewer
