import { useState } from 'react'
import { MapContainer, TileLayer, Polyline, useMapEvents, Marker, Popup } from 'react-leaflet'
import findRoute from './services/routes'


const App = () => {
  const [fringe, setFringe] = useState([])
  const [dijkstra, setDijkstra] = useState([])
  const [markers, setMarkers] = useState([])
  const [algorithm, setAlgorithm] = useState('dijkstra')
  const [info, setInfo] = useState([0, 0, 0, 0])

  const redOptions = { color: 'red' }
  const blueOptions = { color: 'blue' }

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
            .then(returnedRoutes => {
              if (algorithm === 'dijkstra') {
                setDijkstra(returnedRoutes.dijkstra.route)
                setInfo([returnedRoutes.dijkstra.cost, returnedRoutes.dijkstra.time])
              } else if (algorithm === 'fringe') {
                setFringe(returnedRoutes.fringe.route)
                setInfo([returnedRoutes.fringe.cost, returnedRoutes.fringe.time])
              } else {
                setFringe(returnedRoutes.fringe.route)
                setDijkstra(returnedRoutes.dijkstra.route)
                setInfo([returnedRoutes.dijkstra.cost, returnedRoutes.dijkstra.time, returnedRoutes.fringe.cost, returnedRoutes.fringe.time])
              }
            })
        } else if (markers.length === 2) {
          const newMarker = [event.latlng.lat, event.latlng.lng]
          setMarkers([newMarker])
          setFringe([])
          setDijkstra([])
          setInfo([0, 0, 0, 0])
        } else if (markers.length === 0) {
          const newMarker = [event.latlng.lat, event.latlng.lng]
          setMarkers([...markers, newMarker])
        }
      }
    })
  }

  return (
    <div>
      <div id='panel'>
        <h2>Comparison between Dijkstra and Fringe Search in Helsinki</h2>
        <p>Choose what algorithm to use
          <select id="algo" name="algo" onChange={({ target }) => setAlgorithm(target.value)}>
            <option value="dijkstra">Dijkstra</option>
            <option value="fringe">Fringe search</option>
            <option value="both">Both</option>
          </select>
        </p>
        <p>Then to select the start and goal points click twice anywhere in Helsinki and the program will count the route with the algorithm chosen below</p>
        <p>Please note that you might have to wait a bit</p>
        {algorithm === 'both' ?
          <div>
            <p>Dijkstra cost: {info[0]} m  time: {info[1]} s</p>
            Fringe search cost: {info[2]} m  time: {info[3]} s
          </div> :
          <div>
            cost: {info[0]} m  time: {info[1]} s
          </div>
        }
      </div>
      <MapContainer center={[60.184136, 24.949670]} zoom={12}>
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Polyline pathOptions={redOptions} positions={dijkstra} />
        <Polyline pathOptions={blueOptions} positions={fringe} />
        <Markers />
        {markers.map(marker =>
          <Marker key={marker} position={marker}>
            <Popup>
              lat: {marker[0]} lng: {marker[1]}
            </Popup>
          </Marker>
        )}
      </MapContainer>
    </div>
  )
}

export default App
