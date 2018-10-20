<template>
  <q-page class="flex items-center">
    <div class="menu row justify-cener text-center">
      <div class="menu--logo col-xs-12 text-center text-justify">
        <div class="row">
          <div class="col-xs-12 text-center">
            <img
              class="logo"
              src="~assets/quasar-logo-full.svg"
              alt="Logo"
            >
          </div>
          <div class="col-xs-12">
            <p class="app-name text-center">
              Our Name
            </p>
          </div>
        </div>
      </div>
      <div class="menu--options offset-xs-1 col-xs-10">
        <div class="row">
          <div class="menu--option col-xs-12">
            <q-input
              v-model="username"
              type="text"
              placeholder="Username"
            />
          </div>
          <div class="menu--option col-xs-12">
            <q-input
              v-model="password"
              type="password"
              placeholder="Password"
            />
          </div>
          <div class="menu--option col-xs-12">
            <q-btn
              color="primary"
              class="full-width"
              size="lg"
              label="Sign In"
              @click="signIn"
            />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const conditionsNamespace = createNamespacedHelpers('conditions')
const usersNamespace = createNamespacedHelpers('users')

export default {
  name: 'PageIndex',
  data () {
    return {
      nextURL: '/deliveries',
      username: '',
      password: ''
    }
  },
  computed: {
    ...usersNamespace.mapState([
      'token',
      'userData'
    ])
  },
  methods: {
    ...conditionsNamespace.mapActions([
      'setToolbarVisibility'
    ]),
    ...usersNamespace.mapActions([
      'login'
    ]),
    async signIn () {
      this.$q.loading.show()
      let isUserLogged = await this.login({
        username: this.username,
        password: this.password
      })
      if (isUserLogged === true) {
        this.$q.loading.hide()
        this.$router.push(this.nextURL)
      } else {
        this.$q.loading.hide()
        this.$q.notify({
          message: 'Invalid credentials provided'
        })
      }
    }
  },
  mounted () {
    this.setToolbarVisibility(false)
    if (this.token.length === 40 && this.userData !== {}) {
      this.$router.push(this.nextURL)
    }
  }
}
</script>

<style scope lang="stylus">
.q-if-label
  font-size 1.0em !important

.q-input-target
  font-size 1.5em

.logo
  height 70px

.app-name
  font-size 2.5em
  font-weight bold
  letter-spacing 1.4px

.menu--title
  font-size 2.5em
  font-weight 300
  line-height normal
  letter-spacing 1.8px

.menu--option
  margin 32px 0px
</style>
