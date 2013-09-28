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

    this.displayPhoto(@pos)
    this.registerListeners()

  addPhoto: (photo) ->
    photo.ratio = photo.width / photo.height
    @photos.push photo

  displayPhoto: () ->
    photo = @photos[@pos % @photos.length]
    @photoContainer.attr 'src', photo.src
    this.resizePhoto()

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

  resizePhoto: () ->
    windowWidth = $(window).width()
    windowHeight = $(window).height()

    photo = @photos[@pos]

    width = height = -120

    if windowWidth / photo.width > windowHeight / photo.height
      width += windowHeight * photo.ratio
      height += windowHeight
    else
      width += windowWidth
      height += windowWidth / photo.ratio

    @photoContainer.css({
      width: width + 'px',
      height: height + 'px',
    })

  registerListeners: () ->
    $(window).bind 'resize', (evt) =>
      this.resizePhoto()
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
