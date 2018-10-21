<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header>
      <q-toolbar
        color="primary"
        :inverted="$q.theme === 'ios'"
        v-if="toolbarVisibility"
      >
        <q-btn
          flat
          dense
          round
          aria-label="Menu"
          @click="goBack()"
        >
          <q-icon name="keyboard_arrow_left" />
        </q-btn>
        Go back
        <q-toolbar-title>
        </q-toolbar-title>
        <img class="logo" src="~assets/logo.png" alt="Logo">
      </q-toolbar>
    </q-layout-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { openURL } from 'quasar'
import { createNamespacedHelpers } from 'vuex'

const { mapState, mapActions } = createNamespacedHelpers('conditions')

export default {
  name: 'MyLayout',
  data () {
    return {
      leftDrawerOpen: this.$q.platform.is.desktop
    }
  },
  computed: {
    ...mapState([
      'toolbarVisibility'
    ])
  },
  methods: {
    openURL,
    ...mapActions([
      'setToolbarVisibility'
    ]),
    goBack () {
      this.$router.go(-1)
    }
  },
  mounted () {
    this.setToolbarVisibility(false)
  }
}
</script>

<style scoped lang="stylus">
.logo
  height 40px
</style>
