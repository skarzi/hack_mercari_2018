import * as VueGoogleMaps from 'vue2-google-maps'

export default ({ app, router, Vue }) => {
  Vue.use(VueGoogleMaps, {
    load: {
      key: 'YOUR_API_TOKEN',
      libraries: 'places' // for autocomplete plugin
    }
  })
}
