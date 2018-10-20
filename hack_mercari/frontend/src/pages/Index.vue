<template>
  <q-page class="flex">
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
      <div class="menu--title col-xs-12 text-center">
        Select your role
      </div>
      <div class="menu--options col-xs-12">
        <div class="menu--option col-xs-12">
          <q-btn
            class="full-width"
            color="primary"
            label="Courier"
            size="lg"
            to=""
          />
        </div>
        <div class="menu--option col-xs-12">
          <q-btn
            class="full-width"
            color="primary"
            label="Sender"
            size="lg"
            to=""
          />
        </div>
        <div class="menu--option col-xs-12">
          <q-btn
            class="full-width"
            color="primary"
            size="lg"
            label="Recipient"
            to=""
          />
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
  methods: {
    ...mapActions(['setToolbarVisibility'])
  },
  mounted () {
    this.setToolbarVisibility(false)
  }
}
</script>

<style scope lang="stylus">
.menu
  margin 80px 20px

.menu--logo
  margin-top 20px

.logo
  height 70px

.app-name
  font-size 2.5em
  font-weight bold
  letter-spacing 1.4px
  margin-top 20px

.menu--title
  margin-top 50px
  font-size 3em
  font-weight 300
  line-height normal
  letter-spacing 1.8px

.menu--option
  margin 32px 0px
</style>
