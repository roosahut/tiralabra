import axios from 'axios'

const findRoute = async (params) => {
  const response = await axios.post('http://localhost:8000/api/route', params)
  return response.data.route
}

export default findRoute