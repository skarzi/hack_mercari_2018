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
              @click="login"
            />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const { mapActions } = createNamespacedHelpers('conditions')

export default {
  name: 'PageIndex',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    ...mapActions(['setToolbarVisibility']),
    login () {
      console.log(this.username, this.password)
    }
  },
  mounted () {
    this.setToolbarVisibility(false)
  }
}
</script>

<style scope lang="stylus">
.q-if-label
  font-size 1.2em !important

.q-input-target
  font-size 1.7em

.logo
  height 70px

.app-name
  font-size 2.5em
  font-weight bold
  letter-spacing 1.4px

.menu--title
  font-size 3em
  font-weight 300
  line-height normal
  letter-spacing 1.8px

.menu--option
  margin 32px 0px
</style>
