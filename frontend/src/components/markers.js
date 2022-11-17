import { useState } from 'react'
import { Marker, Popup, useMapEvents } from 'react-leaflet'

const Markers = () => {
  const [markers, setMarkers] = useState([])

  useMapEvents({
    click: (event) => {
      const newMarker = [event.latlng.lat, event.latlng.lng]
      setMarkers([...markers, newMarker])
    }
  })

  return (
    <>
      {markers.map(marker =>
        <Marker key={marker} position={marker}>
          <Popup>
            lat: {marker[0]} lng: {marker[1]}
          </Popup>
        </Marker>
      )}
    </>
  )
}

export default Markers