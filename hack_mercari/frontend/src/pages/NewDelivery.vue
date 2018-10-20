<template>
  <q-page padding>
    <div class="form row text-center justify-center">
      <div class="form--option offset-xs-1 col-xs-10">
        <q-input
          v-model="recipientName"
          type="text"
          placeholder="Recipient"
        />
      </div>
      <div class="form--option offset-xs-1 col-xs-10">
        <q-input
          v-model="pickupAddress"
          type="text"
          placeholder="Pickup address"
        />
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
          v-model="pickupDateTime"
          type="datetime"
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
      pickupDateTime: new Date(),
      pickupAddress: '',
      description: ''
    }
  },
  methods: {
    ...conditionsNamespace.mapActions(['setToolbarVisibility']),
    async makeDelivery () {
      const payload = {
        recipient: this.recipientName,
        description: this.description,
        sender_preference: {
          when: this.pickupDateTime.toJSON(),
          where: this.pickupAddress
        }
      }
      try {
        let response = await this.$axios.post('/deliveries/', payload)
        return response
      } catch (error) {
        return error
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
  font-size 1.0em !important

.q-input-target
  font-size 1.5em

.form--option
  margin 22px 0px
</style>
