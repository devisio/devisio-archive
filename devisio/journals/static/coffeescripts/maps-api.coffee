@initializeMaps = () ->
  google.maps.visualRefresh = true

  map = new google.maps.Map(document.getElementById("map-canvas"), {
    disableDefaultUI: true,
    draggable: false,
    zoom: 5,
    center: new google.maps.LatLng(locations[0][0], locations[0][1]),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  })

  bounds = new google.maps.LatLngBounds()

  addLocation = (location) ->
    googleLocation = new google.maps.LatLng(location[0], location[1])
    marker = new google.maps.Marker({
      position: googleLocation
      map: map
    })
    bounds.extend googleLocation

  addLocation location for location in locations

  if locations.length > 1
    map.setCenter bounds.getCenter()
    map.fitBounds bounds
