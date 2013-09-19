@initializeMaps = () ->
  google.maps.visualRefresh = true

  map = new google.maps.Map(document.getElementById("map-canvas"), {
    disableDefaultUI: true,
    mapTypeControl: true,
    mapTypeControlOptions: {
      style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
    },
    draggable: false,
    scrollwheel: false,
    disableDoubleClickZoom: true,
    zoom: 5,
    center: new google.maps.LatLng(journals[0]['location'][0], journals[0]['location'][1]),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  })

  bounds = new google.maps.LatLngBounds()

  addLocation = (location, slug) ->
    googleLocation = new google.maps.LatLng(location[0], location[1])
    marker = new google.maps.Marker({
      position: googleLocation
      #icon: 'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash4/211080_255490747861760_412573813_q.jpg',
      map: map,
      title: 'Click to view details',
      slug: slug
    })

    google.maps.event.addListener marker, 'click', (evt) ->
      document.getElementById('map-canvas').style.height = '200px'
      google.maps.event.trigger(map, "resize")
      map.setZoom 10
      map.setCenter marker.getPosition()

    bounds.extend googleLocation

  addLocation journal['location'], journal['slug'] for journal in journals

  resetMap = () ->
    map.setCenter bounds.getCenter()
    map.fitBounds bounds

  if journals.length > 1
    resetMap()
