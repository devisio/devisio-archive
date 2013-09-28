$ = jQuery

class PhotoViewer
  constructor: (data) ->
    @photos = new Array(0)
    json = JSON.parse(data)

    this.addPhoto photo for photo in json

    @photoContainer = $('#photoviewer > .gallery > img')

    if window.location.hash
      @pos = window.location.hash.substring(1)
    else
      @pos = 0
    this.updatePositionURL()

    this.displayPhoto(@pos)
    this.registerListeners()

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

  updatePositionURL: () ->
    window.location.hash = '#' + @pos

  nextPhoto: () ->
    @pos++
    this._translatePosition()
    this.displayPhoto()
    this.updatePositionURL()

  prevPhoto: () ->
    @pos--
    this._translatePosition()
    this.displayPhoto()
    this.updatePositionURL()


  registerListeners: () ->
    $(document).bind 'keyup', (evt) =>
      switch evt.keyCode
        when 37 then this.prevPhoto()
        when 39 then this.nextPhoto()
    $('#photoviewer a.next').bind 'click', (evt) =>
      evt.preventDefault()
      this.nextPhoto()
    $('#photoviewer a.prev').bind 'click', (evt) =>
      evt.preventDefault()
      this.prevPhoto()



document.PhotoViewer = PhotoViewer
