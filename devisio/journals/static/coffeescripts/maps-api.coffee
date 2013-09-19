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
      map: map,
      slug: slug
    })
    bounds.extend googleLocation

  addLocation journal['location'], journal['slug'] for journal in journals

  if journals.length > 1
    map.setCenter bounds.getCenter()
    map.fitBounds bounds
