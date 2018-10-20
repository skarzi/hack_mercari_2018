import axios from 'axios'

const apiAxios = axios.create({
  baseURL: 'http://172.16.230.173:8000/api'
})

export default ({ Vue }) => {
  Vue.prototype.$axios = apiAxios
}
export {
  apiAxios
}
