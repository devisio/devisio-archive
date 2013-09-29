$ = jQuery

class PhotoViewer
  constructor: (data) ->
    @photos = new Array(0)
    json = JSON.parse(data)

    @fullscreen = false

    this.addPhoto photo for photo in json

    @photoContainer = $('#photoviewer > .gallery > img')

    @pos = 0
    if window.location.hash
      @pos = parseInt window.location.hash.substring(1)
      if isNaN(@pos)
        @pos = 0
        this.updatePositionURL()
      else
        this._translatePosition()
        this.updatePositionURL()

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
    window.location.hash = @pos

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

    if @fullscreen
      width = height = -2 * 20
    else
      width = height = -120

    if windowWidth / photo.width > windowHeight / photo.height
      width += windowHeight * photo.ratio
      height += windowHeight
    else
      width += windowWidth
      height += windowWidth / photo.ratio

    @photoContainer.css({
      #width: width + 'px',
      height: height + 'px',
    })

    if @fullscreen
      deltaHeight = windowHeight - height
    else
      deltaHeight = 0

    $('#photoviewer .photo').css('margin-top': (deltaHeight / 2)+'px')

  closeFullscreen: () ->
    $('#photoviewer').removeClass('fullscreen')
    @fullscreen = false
    this.resizePhoto()

  toggleFullscreen: () ->
    $('#photoviewer').toggleClass('fullscreen')
    @fullscreen = !@fullscreen
    this.resizePhoto()

  registerListeners: () ->
    $(window).bind 'resize', (evt) =>
      this.resizePhoto()
    $(document).bind 'keyup', (evt) =>
      switch evt.keyCode
        when 27 then this.closeFullscreen()
        when 37 then this.prevPhoto()
        when 39 then this.nextPhoto()
    $('#photoviewer .photo').bind 'click', (evt) =>
      this.nextPhoto()
    $('#photoviewer a.next').bind 'click', (evt) =>
      evt.preventDefault()
      this.nextPhoto()
    $('#photoviewer a.prev').bind 'click', (evt) =>
      evt.preventDefault()
      this.prevPhoto()
    $('#photoviewer a.fullscreen').bind 'click', (evt) =>
      evt.preventDefault()
      this.toggleFullscreen()



document.PhotoViewer = PhotoViewer
