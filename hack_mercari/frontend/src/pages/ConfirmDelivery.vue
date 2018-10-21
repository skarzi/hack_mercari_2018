<template>
  <q-page padding>
    <div class="page--container">
      <div class="page--wrapper row">
        <div class="page--title col-xs-12 q-headline">
          New Delivery Request
        </div>
        <div class="page--address col-xs-12">
          <div class="info--label q-title">
            <q-icon
              name="place"
              color="primary"
            />
            Sender address
          </div>
          <div class="info--text q-subheading">
            {{ deliveryData.sender_preference.where.address }}
          </div>
        </div>
        <div
          class="page--address col-xs-12"
          v-if="deliveryData.recipient_preference"
        >
          <div class="info--label q-title">
            Recipient address
          </div>
          <div class="info--text q-subheading">
            <q-icon
              name="place"
              color="negative"
            />
            {{ deliveryData.recipient_preference.where.address }}
          </div>
        </div>
        <div class="page--map-contaner col-xs-12">
          <gmap-map
            id="map"
            :center="mapData.center"
            :zoom="10"
            :options="{disableDefaultUI:true}"
          >
            <gmap-marker
              v-for="marker in mapData.markers"
              :key="marker.address"
              :position="marker.position"
              :icon="marker.icon"
              :clickable="true"
              :draggable="false"
            >
            </gmap-marker>
          </gmap-map>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-xs-12">
        <q-btn
          label="Akceptuj"
          class="full-width fixed-bottom"
          :to="`/deliveries/${deliveryData.id}/status/`"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { isSuccessfull } from '../utils.js'

const conditionsNamespace = createNamespacedHelpers('conditions')
const usersNamespace = createNamespacedHelpers('users')

export default {
  name: 'ConfirmDelivery',
  data () {
    return {
      deliveryData: {}
    }
  },
  computed: {
    ...usersNamespace.mapState([
      'userData'
    ])
  },
  methods: {
    ...conditionsNamespace.mapActions([
      'setToolbarVisibility'
    ]),
    async getDeliveryByID (id) {
      this.$q.loading.show()
      let response = await this.$axios.get(`/deliveries/${id}/`)
      if (isSuccessfull(response)) {
        this.deliveryData = response.data
        this.deliveryData.sender_preference.where = JSON.parse(
          this.deliveryData.sender_preference.where
        )
        if (this.deliveryData.recipient_preference) {
          this.deliveryData.recipient_preference.where = JSON.parse(
            this.deliveryData.recipient_preference.where
          )
        }
      }
      this.$q.loading.hide()
    }
  },
  mounted () {
    this.setToolbarVisibility(false)
    if (!this.userData.is_courier) {
      this.$router.push('/')
    }
    this.deliveryData = this.getDeliveryByID(this.$route.params.id)
    if (this.deliveryData.status !== 'assigning') {
      console.log('Delivery taken by another courier!')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped lang="stylus">
@import '~variables'

.page--container
  padding 15px

.page--wrapper
  padding 10px
  background-color white

.page--title
  margin-top 10px

.info--label
  margin-top 15px

.info--text
  margin 5px 15px
  color $faded

#map
  padding-top 30px
  width 100%
  height 420px
</style>
