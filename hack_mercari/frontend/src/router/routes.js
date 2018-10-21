const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/Index.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(false))
        }
      },
      {
        path: '/couriers',
        component: () => import('pages/AvailableCouriers.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      },
      {
        path: '/deliveries',
        component: () => import('pages/Deliveries.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      },
      {
        path: '/courier-deliveries',
        component: () => import('pages/CourierDeliveries.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      },
      {
        path: '/new-delivery',
        component: () => import('pages/NewDelivery.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      },
      {
        path: '/deliveries/:id/recipient-preference/',
        component: () => import('pages/RecipientPreference.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      },
      {
        path: '/deliveries/:id/status/',
        component: () => import('pages/DeliveryStatus.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      },
      {
        path: '/courier-delivery/:id/',
        component: () => import('pages/CourierDelivery.vue'),
        beforeEnter (to, from, next) {
          next(vm => vm.setToolbarVisibility(true))
        }
      }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
