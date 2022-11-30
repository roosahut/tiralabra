import axios from 'axios'

const findRoute = async (params) => {
  const response = await axios.post('/api/route', params)
  return response.data
}

export default findRoute