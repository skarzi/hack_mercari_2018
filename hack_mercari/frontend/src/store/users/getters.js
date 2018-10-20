export function isAuthenticated (state) {
  return state.token !== '' && state.userData !== {}
}
