import * as VueGoogleMaps from 'vue2-google-maps'

export default ({ app, router, Vue }) => {
  Vue.use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyBedu1neLBefpIqB8K2vKOkaW-lgBM_kJs',
      libraries: 'places' // for autocomplete plugin
    }
  })
}
