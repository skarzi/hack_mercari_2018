<template>
  <q-page padding>
    <q-list
      highlight
      multiline
      no-border
      class="list--self q-mx-md q-mt-xs"
    >
      <q-list-header>
        Your Deliveries
      </q-list-header>
      <q-item
        v-for="delivery in deliveries"
        :key="delivery.id"
        :to="`/deliveries/${delivery.id}/` + ((delivery.recipient === userData.username && !delivery.recipient_preference) ? 'recipient-preference/' : 'status/')"
        class="q-px-md"
      >
        <q-item-main>
          <q-item-tile label>
            <p class="courier--name q-mb-xs">
              Delivery <b>#{{ delivery.id }}</b>
            </p>
          </q-item-tile>
          <q-item-tile
            class="delivery--description"
            v-if="delivery.description"
            sublabel
          >
            {{ delivery.description }}
          </q-item-tile>
          <q-item-separator/>
          <q-item-tile class="date__details" sublabel>
            <strong>Status:</strong>
            <span class="arrival-time">
              {{ statusToMessageMapping[delivery.status] }}
            </span>
          </q-item-tile>
        </q-item-main>
      </q-item>
    </q-list>
    <q-btn
      round
      class="FAB fixed"
      size="lg"
      color="warning"
      icon="add"
      to="/new-delivery"
    />
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const conditionsNamespace = createNamespacedHelpers('conditions')
const usersNamespace = createNamespacedHelpers('users')

export default {
  name: 'Deliveries',
  data () {
    return {
      deliveries: [],
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
    ...usersNamespace.mapGetters(['isAuthenticated'])
  },
  methods: {
    ...conditionsNamespace.mapActions(['setToolbarVisibility']),
    async getOrdersFromAPI () {
      let path = '/deliveries/'
      if (this.isAuthenticated) {
        this.$q.loading.show({
        })
        let response = await this.$axios.get(path)
        this.deliveries = response.data.reverse()
        this.$q.loading.hide()
      }
    }
  },
  created () {
    this.setToolbarVisibility(true)
    this.getOrdersFromAPI()
    // pusher
    const channel = this.$pusher.channel(this.userData.username)
    channel.bind('delivery-updated', () => {
      // refresh deliveries
      this.getOrdersFromAPI()
    })
  }
}
</script>

<style scoped lang="stylus">
@import '~variables'

.q-list-header
  line-height initial !important
  font-size 2em

.q-item
  margin-top 15px
  background-color white

.q-item-sublabel
  font-size 1.2em

.score
  font-size 1.2em
  font-weight bold

.arrival-time
  white-space nowrap
  font-weight 100

.courier--name
  font-size 1.5em !important

.delivery--description
  color $light

.date__details
  color $tertiary

.FAB
  right 20px
  bottom 25px
</style>
