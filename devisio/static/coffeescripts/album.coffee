$ = jQuery

class Gallery
  html: '''
    <div class="gallery">
      <a class="close">&times;</a>
      <img src="" alt="" />
      <a class="prev">‹</a>
      <a class="next">›</a>
    </div>
    <div class="gallery-background"></div>'''
  margin: 20

  constructor: (@images) ->
    @count = @images.length
    @pos = 0
    this._calculateRatio id for obj, id in @images
    this._preloadImage(@pos)

  _calculateRatio: (id) ->
    image = @images[id]
    image['ratio'] = image['width'] / image['height']

  preloadNextAndPrev: () ->
    this._preloadImage(this._getPrev(@pos))
    this._preloadImage(this._getNext(@pos))

  _preloadImage: (id) ->
    if @images[id]['preload'] is undefined
      img = new Image()
      $(img).attr({src: @images[id].src}).bind 'load', (evt) =>
        @images[id]['image'] = evt.target
        @images[id]['preload'] = true

  show: ->
    $('body').append(@html)
    $('.gallery-background').css 'opacity', '1'
    this.registerListeners()
    this.updateImage()

  updateImage: ->
    $('.gallery > img').attr('src', @images[@pos].src)
    this.updatePosition()
    this.preloadNextAndPrev()

  registerListeners: ->
    $('.gallery > a.close').bind 'click', (evt) =>
      this.close()
    $(document).bind 'keyup', (evt) =>
      if evt.keyCode is 27
        this.close()
    $(window).bind 'resize', (evt) =>
      this.updatePosition()
    $('.gallery > a.next').bind 'click', (evt) =>
      evt.preventDefault()
      this.next()
    $('.gallery > a.prev').bind 'click', (evt) =>
      evt.preventDefault()
      this.prev()
    $('.gallery > img').bind 'click', (evt) =>
      evt.preventDefault()
      this.next()

  updatePosition: ->
    image = @images[@pos]

    windowWidth = $(window).width()
    windowHeight = $(window).height()

    #console.log 'updatePosition', windowWidth, windowHeight, image['width'], image['height']

    width = -2 * @margin
    height = -2 * @margin

    if windowWidth / image['width'] > windowHeight / image['height']
      width += windowHeight * image.ratio
      height += windowHeight
    else
      width += windowWidth
      height += windowWidth / image['ratio']

    deltaWidth = windowWidth - width
    deltaHeight = windowHeight - height

    $('.gallery').css({
      top: (deltaHeight / 2)+'px',
      left: (deltaWidth / 2)+'px',
    })

    $('.gallery > img').css({
      width: width+'px',
      height: height+'px',
    })

  close: ->
    $('.gallery').remove()
    $('.gallery-background').remove()

  _getNext: (from) ->
    if from < @count - 1
      return from + 1
    else
      return 0

  _getPrev: (from) ->
    if from > 0
      return from - 1
    else
      return @count - 1

  next: ->
    @pos = this._getNext(@pos)
    this.updateImage()

  prev: ->
    @pos = this._getPrev(@pos)
    this.updateImage()


document.Gallery = Gallery
