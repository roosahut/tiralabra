import axios from 'axios'

const getRoute = async () => {
  const request = axios.get('http://localhost:8000/api/route')
  return request.then(response => response.data)
}

export default getRoute