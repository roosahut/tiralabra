import { useState, useEffect, useRef } from 'react'
import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet'
import getRoute from './services/routes'

const App = () => {
  const [route, setRoute] = useState([])

  useEffect(() => {
    getRoute().then(array => {
      setRoute(array.route)
    })
  })

  const redOptions = { color: 'red' }

  return (
    <MapContainer center={[60.184136, 24.949670]} zoom={12} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[60.184136, 24.949670]}>
        <Popup>
          Kallion kirkko
        </Popup>
      </Marker>
      <Marker position={[60.186760, 24.978402]}>
        <Popup>
          REDI
        </Popup>
      </Marker>
      <Polyline pathOptions={redOptions} positions={route} />
    </MapContainer>
  );
}

export default App
