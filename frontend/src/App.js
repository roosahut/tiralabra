import { useState, useEffect } from 'react'
import { MapContainer, TileLayer, Polyline } from 'react-leaflet'
import getRoute from './services/routes'
import Markers from './components/markers'

const App = () => {
  const [route, setRoute] = useState([])

  useEffect(() => {
    getRoute().then(array => {
      setRoute(array.route)
    })
  }, [])

  const redOptions = { color: 'red' }

  return (
    <MapContainer center={[60.184136, 24.949670]} zoom={12} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Polyline pathOptions={redOptions} positions={route} />
      <Markers />
    </MapContainer>
  )
}

export default App
