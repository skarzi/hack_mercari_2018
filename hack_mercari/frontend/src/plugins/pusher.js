import pusher from 'vue-pusher'

export default ({ app, router, Vue }) => {
  Vue.use(pusher, {
    api_key: '730d620608cd6e422461',
    options: {
      cluster: 'eu',
      encrypted: true
    }
  })
}
