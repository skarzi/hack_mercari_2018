<template>
  <q-page padding>
    <q-list
      highlight
      multiline
      no-border
      class="list--self"
    >
      <q-list-header>
        Possible deliveries
      </q-list-header>
      <q-item
        v-for="delivery in assignments"
        :key="delivery.id"
        :to="`/courier-delivery/${delivery.id}`"
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
    <q-list
      highlight
      multiline
      no-border
      class="list--self"
    >
      <q-list-header>
        Accepted Deliveries
      </q-list-header>
      <q-item
        v-for="delivery in deliveries"
        :key="delivery.id"
        :to="`/courier-delivery/${delivery.id}/`"
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
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const conditionsNamespace = createNamespacedHelpers('conditions')
const usersNamespace = createNamespacedHelpers('users')

export default {
  name: 'CourierDeliveries',
  data () {
    return {
      deliveries: [],
      assignments: [],
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
    async getAssignmentsFromAPI () {
      let path = '/assignments/'
      if (this.isAuthenticated) {
        this.$q.loading.show({
        })
        let response = await this.$axios.get(path)
        this.assignments = response.data.reverse()
        this.$q.loading.hide()
      }
    },
    async getDeliveriesFromAPI () {
      let path = '/deliveries/'
      if (this.isAuthenticated) {
        this.$q.loading.show({
        })
        let response = await this.$axios.get(path)
        this.deliveries = response.data.reverse()
        this.$q.loading.hide()
      }
    }
    // acceptDelivery (id) {
    //   this.$swal({
    //     title: 'Do you want to accept'
    //   })
    // }

  },
  created () {
    this.setToolbarVisibility(true)
    this.getAssignmentsFromAPI()
    this.getDeliveriesFromAPI()
    // pusher
    const channel = this.$pusher.channel(this.userData.username)
    channel.bind('delivery-updated', () => {
      // refresh deliveries
      this.getAssignmentsFromAPI()
      this.getDeliveriesFromAPI()
    })
    channel.bind('new-assignment', () => {
      // refresh deliveries
      this.getAssignmentsFromAPI()
      this.getDeliveriesFromAPI()
    })
  }
}
</script>

<style scoped lang="stylus">
@import '~variables'

.list--self
  margin-top 10px
  margin-left 20px
  margin-right 20px

.q-list-header
  line-height initial !important
  font-size 2em

.q-item
  margin-top 15px
  padding-top 15px !important
  padding-bottom 15px !important
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
