<template>
  <q-page padding>
    <q-list
      highlight
      multiline
      no-border
      class="list--self"
    >
      <q-list-header>
        Your Deliveries
      </q-list-header>
      <q-item
        v-for="order in deliveries"
        :key="order.id"
        :to="`/deliveries/${order.id}/status/`"
      >
        <q-item-main>
          <q-item-tile label>
            <p class="courier--name">
              Order <b>#{{ order.id }}</b>
            </p>
          </q-item-tile>
          <q-item-tile class="date__details" sublabel>
            Forwarded to the courier:
            <span class="arrival-time">
              {{ order.sender_preference.when }}
            </span>
          </q-item-tile>
          <q-item-tile class="date__details" sublabel>
            <div v-if="order.recipient_preference">
              Estimated delivery date:
              <span class="arrival-time">
                {{ order.recipient_preference.when }}
              </span>
            </div>
            <div v-else>
              Waiting for recipient response.
            </div>
          </q-item-tile>
          <q-item-separator/>
          <q-item-tile
            class="order--description"
            v-if="order.description"
            sublabel
          >
            {{ order.description }}
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
      deliveries: []
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
      if (this.userData.is_courier) {
        path = '/assignments/'
      }
      if (this.isAuthenticated) {
        this.$q.loading.show({
        })
        let response = await this.$axios.get(path)
        this.deliveries = response.data.reverse()
        this.$q.loading.hide()
      }
    }
  },
  mounted () {
    this.setToolbarVisibility(true)
    this.getOrdersFromAPI()
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
  font-weight bold

.courier--name
  font-size 1.5em !important

.order--description
  color $light

.date__details
  color $tertiary

.FAB
  right 20px
  bottom 25px
</style>
