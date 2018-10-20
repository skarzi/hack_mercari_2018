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
        path: '/orders',
        component: () => import('pages/Orders.vue'),
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
