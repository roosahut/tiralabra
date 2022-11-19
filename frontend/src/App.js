import { useState, useEffect } from 'react'
import { MapContainer, TileLayer, Polyline, useMapEvents, Marker, Popup } from 'react-leaflet'
import findRoute from './services/routes'


const App = () => {
  const [route, setRoute] = useState([])
  const [markers, setMarkers] = useState([])

  const Markers = () => {
    useMapEvents({
      click: (event) => {
        if (markers.length === 1) {
          const newMarker = [event.latlng.lat, event.latlng.lng]
          setMarkers([...markers, newMarker])
          const pointsObject = {
            start: markers[0],
            end: newMarker
          }
          findRoute(pointsObject)
            .then(returnedRoute => {
              setRoute(returnedRoute)
            })
        } else if (markers.length === 2) {
          const newMarker = [event.latlng.lat, event.latlng.lng]
          setMarkers([newMarker])
          setRoute([])
        } else if (markers.length === 0) {
          const newMarker = [event.latlng.lat, event.latlng.lng]
          setMarkers([...markers, newMarker])
        }
      }
    })
  }

  const redOptions = { color: 'red' }

  return (
    <MapContainer center={[60.184136, 24.949670]} zoom={12} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Polyline pathOptions={redOptions} positions={route} />
      <Markers />
      {markers.map(marker =>
        <Marker key={marker} position={marker}>
          <Popup>
            lat: {marker[0]} lng: {marker[1]}
          </Popup>
        </Marker>
      )}
    </MapContainer>
  )
}

export default App
