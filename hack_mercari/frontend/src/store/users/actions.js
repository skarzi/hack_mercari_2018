import { apiAxios } from '../../plugins/axios.js'

function isSuccessfull (response) {
  return response.status >= 200 && response.status <= 200
}

async function _login (payload) {
  try {
    let response = await apiAxios.post('/auth/login/', payload)
    return response
  } catch (error) {
    return error
  }
}

export async function login (context, payload) {
  let response = await _login(payload)
  if (isSuccessfull(response)) {
    const {token, ...userData} = response.data
    context.commit('setToken', token)
    context.commit('setUserData', userData)
    return true
  }
  return false
}
