<template>
  <q-page padding>
    <div class="form row text-center justify-center">
      <div class="form--option offset-xs-1 col-xs-10">
        <p class="q-display-1">
          New Delivery
        </p>
      </div>
      <div class="form--option offset-xs-1 col-xs-10">
        <q-input
          v-model="recipientName"
          type="text"
          placeholder="Recipient"
        />
      </div>
      <div class="form--option offset-xs-1 col-xs-10">
        <div
          class="q-if row no-wrap relative-position q-input q-if-standard q-if-has-content text-primary"
        >
          <gmap-autocomplete
            class="q-input q-input-target"
            @place_changed="setPickupAddress"
          >
          </gmap-autocomplete>
        </div>
      </div>
      <div class="form--option offset-xs-1 col-xs-10">
        <q-input
          v-model="description"
          type="textarea"
          rows="1"
          placeholder="Description"
        />
      </div>
      <div class="form--option offset-xs-1 col-xs-10">
        <q-datetime
          v-model="pickupDateTime.start"
          type="datetime"
          :default-value="new Date()"
          placeholder="Pickup Date & time"
        />
      </div>
      <div class="form--option offset-xs-1 col-xs-10">
        <q-btn
          color="primary"
          class="full-width"
          size="lg"
          label="Make Delivery"
          @click="makeDelivery"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const conditionsNamespace = createNamespacedHelpers('conditions')

export default {
  name: 'NewDelivery',
  data () {
    return {
      recipientName: '',
      pickupDateTime: {},
      pickupLocation: '',
      description: ''
    }
  },
  methods: {
    ...conditionsNamespace.mapActions(['setToolbarVisibility']),
    setPickupAddress (pickupLocation) {
      console.log(pickupLocation)
      this.pickupLocation = JSON.stringify({
        address: pickupLocation.formatted_address,
        position: {
          lat: pickupLocation.geometry.location.lat(),
          lng: pickupLocation.geometry.location.lng()
        }
      })
      console.log(this.pickupLocation)
    },
    async makeDelivery () {
      this.$q.loading.show()
      if (!this.pickupDateTime.start) {
        this.pickupDateTime.start = new Date()
      }
      const payload = {
        recipient: this.recipientName,
        description: this.description,
        sender_preference: {
          when: this.pickupDateTime.start.toJSON(),
          where: this.pickupLocation
        }
      }
      try {
        await this.$axios.post('/deliveries/', payload)
        this.$q.loading.hide()
        this.$router.push('/deliveries/')
      } catch (error) {
        this.$q.loading.hide()
        this.$q.notify({
          message: 'Invalid delivery data provided'
        })
      }
    }
  },
  mounted () {
    this.setToolbarVisibility(true)
  }
}
</script>

<style scoped lang="stylus">
.q-if-label
  font-size 1.3em !important

.pac-container
  width 100%

.q-input-target
  font-size 1.3em !important

.form--option
  margin 22px 0px
</style>
