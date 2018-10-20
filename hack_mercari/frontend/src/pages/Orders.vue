<template>
  <q-page padding>
    <q-list
      highlight
      multiline
      no-border
      class="list--self"
    >
      <q-list-header>
        Current Orders
      </q-list-header>
      <q-item
        v-for="order in getOrders(1)"
        :key="order.id"
        :to="`order/${order.id}`"
      >
        <q-item-main>
          <q-item-tile label>
            <p class="courier--name">
              Order #{{ order.id }}
            </p>
          </q-item-tile>
          <q-item-tile sublabel>
            Forwarded to the courier:
            <span class="arrival-time">
              {{ order.forwardedDate }}
            </span>
          </q-item-tile>
          <q-item-tile sublabel>
            Estimated delivery date:
            <span class="arrival-time">
              {{ order.estimatedDeliveryDate }}
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
      to="/new-order"
    />
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const conditionsNamespace = createNamespacedHelpers('conditions')

export default {
  name: 'Orders',
  methods: {
    ...conditionsNamespace.mapActions(['setToolbarVisibility']),
    getOrders (userID) {
      return [
        {
          id: 1,
          forwardedDate: '14:34 20.10.2018',
          estimatedDeliveryDate: '16:34 20.10.2018'
        },
        {
          id: 2,
          forwardedDate: '14:34 20.10.2018',
          estimatedDeliveryDate: '16:34 20.10.2018'
        },
        {
          id: 3,
          forwardedDate: '14:34 20.10.2018',
          estimatedDeliveryDate: '16:34 20.10.2018'
        },
        {
          id: 5,
          forwardedDate: '14:34 20.10.2018',
          estimatedDeliveryDate: '16:34 20.10.2018'
        },
        {
          id: 6,
          forwardedDate: '14:34 20.10.2018',
          estimatedDeliveryDate: '16:34 20.10.2018'
        },
        {
          id: 7,
          forwardedDate: '14:34 20.10.2018',
          estimatedDeliveryDate: '16:34 20.10.2018'
        }
      ]
    }
  },
  mounted () {
    this.setToolbarVisibility(true)
  }
}
</script>

<style scoped lang="stylus">
.list--self
  margin-top 10px
  margin-left 20px
  margin-right 20px

.q-list-header
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
  font-weight bold

.courier--name
  font-size 1.5em !important

.FAB
  right 20px
  bottom 25px
</style>
