import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({

    state: {
        //ユーザー情報
        accountToken:'',
        accountName:'ユーザー',
        accountBirthDay:'',
        accountGender:'',
        accountHeight:'',
        accountWeight:'',
        accountActiveLevel:'',
        accountStartDay:'',
        accountPurpose:'',
        //Twitter投稿用カロリー情報
        intakeCalorie:'',
        consumptionCalorie:'',
        calorie:'',
        //ローディングアニメーション
        loading: false,
        //日付指定登録
        date:'',
        //判定必須情報
        motion1:'', //選択トレーニング内容
        motion2:'', //選択トレーニングc平均メッツ値
        judge_count:'', //判定カウント値
        judge_rate:'', //トレーニング精度
        add_date:'',//判定した日付

    },

    mutations:{
        //トークン登録又は更新
        tokenUpdate(state,newToken){
            state.accountToken = newToken
        },
        //ユーザー情報の削除
        tokenDelete(state){
            state.accountToken = ""
            state.accountName = "ユーザー"
            state.accountBirthDay = ""
            state.accountGender = ""
            state.accountHeight = ""
            state.accountWeight = ""
            state.accountActiveLevel = ""
            state.calorie = ""
            state.intakeCalorie = ""
            state.consumptionCalorie = ""
            state.accountPurpose = ""
        },
        //ユーザー取得又は更新
        accountUpdate(state,data){
            state.accountName = data.name
            state.accountBirthDay = data.birthday
            state.accountGender = data.gender
            state.accountHeight = data.height
            state.accountWeight = data.weight
            state.accountActiveLevel = data.activlevel
            state.accountStartDay = data.startday
            state.accountPurpose = data.purpose
        },
        //カロリー情報の取得
        calorieAdd(state,data){
            state.calorie = data.userCalorie
            state.intakeCalorie = data.userIntakeCalorie
            state.consumptionCalorie = data.userConsumptionCalorie
        },
        //ローディングアニメーション
        setLoading(state, payload) {
            state.loading = payload
        },
        //日付指定
        setDate(state,dateInput){
            state.date = dateInput
        },
        //判定情報のセット
        // setMenu(state, val) {
        //     state.motion1= val
        //     state.motion2= val
        // },
        //トレーニングフォーム判定の情報取得
        judgeADD(state,data){
          state.motion_name = data.motion_name
          state.motion_calorie = data.motion_calorie
          state.judge_rate = data.judge_rate
          state.judge_count = data.judge_count
          //判定した日付
          state.add_date = data.add_date
        }
    },

    plugins: [createPersistedState({
        key: 'acsys',
        storage: window.sessionStorage
    })]
})