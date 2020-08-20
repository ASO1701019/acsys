import Vue from 'vue'
import Router from 'vue-router'

// components
import StartTop from "../components/SrartTop"
import UserLogin from '../components/UserLogin'
import UserSignUp from '../components/UserSignUp'
import UserGuide from "../components/UserGuide"
import SaveCalorie from '../components/SaveCalorie'
import ConsumptionCalorieRegistration from "../components/ConsumptionCalorieRegistration"
import IntakeCalorieRegistration from "../components/IntakeCalorieRegistration"
import Calender from  "../components/Calendar"
import Training from "../components/Training"
import Statistics from "../components/Statistics"
import UserChange from "../components/UserChange"

// store
import Store from '../store/index'

Vue.use(Router)

const router = new Router({

    routes: [
        {
            path: '/',
            name: 'StartTop',
            component: StartTop,
            meta: {
                isPublic: true
            }
        },
        {
            path: '/login',
            name: 'login',
            component: UserLogin,
            meta: {
                isPublic: true
            }
        },
        {
            path: '/signup',
            name: 'signup',
            component: UserSignUp,
            meta: {
                isPublic: true
            }
        },
        {
            path: '/userguide',
            name: 'userguide',
            component: UserGuide,
            meta: {
                isPublic: true
            }
        },
        {
            path: '/savecalorie',
            component: SaveCalorie,
        },
        {
            path: '/consumptioncalorie',
            component: ConsumptionCalorieRegistration,
        },
        {
            path: '/intakecalorie',
            component: IntakeCalorieRegistration
        },
        {
            path: "/calendar",
            component: Calender
        },
        {
            path: "/training",
            name: "training",
            component: Training,
        },
        {
            path: "/statistics",
            name: "statistics",
            component: Statistics,
        },
        {
            path: "/userchange",
            name: "userchange",
            component: UserChange,
        }
    ]
})


router.beforeEach((to, from, next) => {
    if (to.matched.some(page => page.meta.isPublic) || Store.state.accountToken) {
        next()
    } else {
        next('/login')
    }
})

export default router