import Vue from 'vue'
import Router from 'vue-router'
import VueAnalytics from 'vue-analytics'

// components
import StartTop from "../components/StartTop"
import UserLogin from '../components/UserLogin'
import UserSignUp from '../components/UserSignUp'
import SaveCalorie from '../components/SaveCalorie'
import ConsumptionCalorieRegistration from "../components/ConsumptionCalorieRegistration"
import IntakeCalorieRegistration from "../components/IntakeCalorieRegistration"
import Calender from "../components/Calendar"
import Training from "../components/Training"
import Statistics from "../components/Statistics"
import UserChange from "../components/UserChange"
import PasswordChange from "../components/PasswordChange"
import FormJudge from "../components/FormJudge"
import NotFound from "../components/NotFound";
import CalorieShare from "../components/CalorieShare";
import UpdateInformation from "../components/UpdateInformation";
import RePassword from "../components/RePassword";
import CountTraining from "../components/CountTraining";

// store
import Store from '../store'

Vue.use(Router)


const router = new Router({
    //#を外すためhistory
    mode: 'history',
    routes: [
        {
            //Topページ
            //ログイン前にあるサイトはmetaを追加する
            path: '/',
            name: 'StartTop',
            component: StartTop,
            meta: {
                isPublic: true
            }
        },
        {
            //ログイン
            path: '/login',
            name: 'login',
            component: UserLogin,
            meta: {
                isPublic: true
            }
        },
        {
            //新規登録
            path: '/signup',
            name: 'signup',
            component: UserSignUp,
            meta: {
                isPublic: true
            }
        },
        {
            //カロリー貯金
            path: '/savecalorie',
            component: SaveCalorie,
            name:'savecalorie',
        },
        {
            //消費カロリー入力
            path: '/consumptioncalorie',
            component: ConsumptionCalorieRegistration,
        },
        {
            //摂取カロリー入力
            path: '/intakecalorie',
            component: IntakeCalorieRegistration,
            name: 'intakecalorie',
        },
        {
            //投稿
            path: '/calorieshare',
            component: CalorieShare,
            name: 'calorieshare',
        },
        {
            //カレンダー
            path: "/calendar",
            component: Calender,
            name: 'calendar',
        },
        {
            //トレーニング
            path: "/training",
            name: "training",
            component: Training,
        },
        {
            //フォーム判定
            path: "/formjudge",
            name: "formjudge",
            component: FormJudge,
        },
        {
            //統計
            path: "/statistics",
            name: "statistics",
            component: Statistics,
        },
        {
            //ユーザー情報変更
            path: "/userchange",
            name: "userchange",
            component: UserChange,
        },
        {
            //パスワード再設定
            path: "/passwordchange",
            name: "passwordchange",
            component: PasswordChange,
        },
        {
            //更新情報
            path: '/updateinformation',
            name: 'updateinformation',
            component: UpdateInformation,
            meta: {
                isPublic: true
            }
        },
        {
            //投稿
            path: '/tweet',
            name: 'tweet',
            component: CalorieShare,
        },
        {
            //回数記録
            path: '/counttraining',
            name: 'counttraining',
            component: CountTraining,
        },
        {
            //パスワード再発行
            path: '/repassword',
            name: 'repassword',
            component: RePassword,
            meta: {
                isPublic: true
            }
        },
        {
            //NotFound
            path: "/*",
            name: 'notfound',
            component: NotFound,
        },
    ]
})

//Googleアナリティクスの設定
Vue.use(VueAnalytics, {
    id: 'UA-178757623-1',
    router
})

// metaかトークンがないとログインに遷移する
router.beforeEach((to, from, next) => {
    if (to.matched.some(page => page.meta.isPublic) || Store.state.accountToken) {
        next()
    } else {
        next('/login')
    }
})

export default router
