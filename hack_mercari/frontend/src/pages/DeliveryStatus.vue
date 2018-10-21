<template>
  <q-page
    padding
    class="flex items-center justify-center"
  >
    <div class="page--container" v-if="deliveryData">
      <div class="page--wrapper row">
        <div class="page--title col-xs-12 q-headline">
          Delivery #{{ deliveryData.id }} <br>
          <small class="text-light">{{ statusToMessageMapping[deliveryData.status] }}</small>
        </div>
        <hr class="q-hr">
        <div class="page--address col-xs-12">
          <div class="info--label q-title">
            Pickup
          </div>
          <div class="info--text q-subheading">
            <q-icon
              name="place"
              color="primary"
            />
            {{ deliveryData.sender_preference.where.address }}
          </div>
          <div class="info--text q-subheading">
            <q-icon
              name="alarm"
              color="primary"
            />
            {{ deliveryData.sender_preference.when_min.substring(0, 10) }}
            since {{ deliveryData.sender_preference.when_min.substring(11, 16) }}
            until {{ deliveryData.sender_preference.when_max.substring(11, 16) }}
          </div>
        </div>
        <div
          class="page--address col-xs-12"
          v-if="deliveryData.recipient_preference"
        >
          <div class="info--label q-title">
            Delivery
          </div>
          <div class="info--text q-subheading">
            <q-icon
              name="place"
              color="negative"
            />
            {{ deliveryData.recipient_preference.where.address }}
          </div>
          <div class="info--text q-subheading">
            <q-icon
              name="alarm"
              color="negative"
            />
            {{ deliveryData.recipient_preference.when_min.substring(0, 10) }}
            since {{ deliveryData.recipient_preference.when_min.substring(11, 16) }}
            until {{ deliveryData.recipient_preference.when_max.substring(11, 16) }}
          </div>
        </div>
        <div class="page--map-contaner col-xs-12 q-mt-md">
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
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { isSuccessfull } from '../utils.js'

const conditionsNamespace = createNamespacedHelpers('conditions')
const usersNamespace = createNamespacedHelpers('users')

export default {
  name: 'DeliveryStatus',
  data () {
    return {
      deliveryData: null,
      statusToMessageMapping: {
        waiting_for_preference: 'Waiting for recipient preference',
        assigning: 'Assigning to courier',
        waiting_for_courier: 'Waiting for courier to pick up',
        in_transit: `Package is on it's way!`,
        delivered: 'Package delivered.'
      }
    }
  },
  computed: {
    ...usersNamespace.mapState(['userData']),
    mapData () {
      console.error(require('assets/recipient_icon.png'))
      let data = {
        center: {
          lat: 52.232382,
          lng: 20.983926
        },
        markers: [
          {
            position: this.deliveryData.sender_preference.where.position,
            icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
          }
        ]
      }
      if (this.deliveryData.recipient_preference) {
        data.markers.push({
          position: this.deliveryData.recipient_preference.where.position,
          icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        })
      }
      console.log(data)
      return data
    },
    deliveryStatus () {
      return this.statusToMessageMapping[this.deliveryData.status]
    }
  },
  methods: {
    ...conditionsNamespace.mapActions(['setToolbarVisibility']),
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
        console.log(this.deliveryData)
      }
      this.$q.loading.hide()
    }
  },
  created () {
    this.setToolbarVisibility(true)
    this.deliveryData = this.getDeliveryByID(this.$route.params.id)
    // pusher
    const channel = this.$pusher.channel(this.userData.username)
    channel.bind('delivery-updated', () => {
      this.deliveryData = this.getDeliveryByID(this.$route.params.id)
    })
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
  color $faded

#map
  padding-top 30px
  width 100%
  height 420px
</style>
