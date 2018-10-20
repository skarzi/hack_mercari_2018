<template>
  <q-page padding>
    <q-list
      highlight
      multiline
      no-border
      class="list--self"
    >
      <q-list-header>
        Available Couriers:
      </q-list-header>
      <q-item
        v-for="courier in getAvailableCouriers(1, 2)"
        :key="courier.id"
        :to="`couriers/${courier.id}`"
      >
        <q-item-side :avatar="courier.avatarURL"/>
        <q-item-main>
          <q-item-tile label>
            <p class="courier--name">
              {{ courier.name }}
            </p>
          </q-item-tile>
          <q-item-tile sublabel>
            Near you around:
            <span class="arrival-time">
              {{ courier.arrivalTime }}
            </span>
          </q-item-tile>
        </q-item-main>
        <q-item-side>
          <p class="score">
            <q-icon
              name="star"
              color="orange"
            />
            {{ courier.score }} / 5
          </p>
        </q-item-side>
      </q-item>
    </q-list>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

const conditionsNamespace = createNamespacedHelpers('conditions')

export default {
  name: 'AvailableCouriers',
  data () {
    return {
    }
  },
  methods: {
    ...conditionsNamespace.mapActions(['setToolbarVisibility']),
    getAvailableCouriers (senderData, recipientData) {
      return [
        {
          id: 12,
          avatarURL: 'https://static2.srcdn.com/wordpress/wp-content/uploads/2016/12/jar-jar-binks-star-wars-gungan-face-smile.jpg',
          name: 'Jar Jar Binks',
          arrivalTime: '15:35',
          score: 4.7
        },
        {
          id: 13,
          avatarURL: 'https://static2.srcdn.com/wordpress/wp-content/uploads/2016/12/jar-jar-binks-star-wars-gungan-face-smile.jpg',
          name: 'Jar Jar Binks 2',
          arrivalTime: '15:35',
          score: 4.7
        },
        {
          id: 14,
          avatarURL: 'https://static2.srcdn.com/wordpress/wp-content/uploads/2016/12/jar-jar-binks-star-wars-gungan-face-smile.jpg',
          name: 'Jar Jar Binks 2',
          arrivalTime: '15:35',
          score: 4.7
        },
        {
          id: 15,
          avatarURL: 'https://static2.srcdn.com/wordpress/wp-content/uploads/2016/12/jar-jar-binks-star-wars-gungan-face-smile.jpg',
          name: 'Jar Jar Binks 2',
          arrivalTime: '15:35',
          score: 4.7
        },
        {
          id: 16,
          avatarURL: 'https://static3.srcdn.com/wordpress/wp-content/uploads/2016/12/jar-jar-binks-star-wars-gungan-face-smile.jpg',
          name: 'Jar Jar Binks 2',
          arrivalTime: '15:35',
          score: 4.7
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
</style>
