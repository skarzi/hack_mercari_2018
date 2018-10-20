import { apiAxios } from '../../plugins/axios.js'

export function setUserData (state, userData) {
  state.userData = userData
}

export function setToken (state, token) {
  state.token = token
  const authToken = `Token ${token}`
  apiAxios.defaults.headers.common['Authorization'] = authToken
}
