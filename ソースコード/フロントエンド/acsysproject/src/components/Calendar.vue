<template>
    <div id='app' class="container">
        <div v-if="!this.$store.state.loading">
            <v-date-picker
                    :mode="mode"
                    v-model="selectedDate"
                    is-inline
                    is-expanded
                    :max-date="new Date()"
                    :attributes='attrs'
            ></v-date-picker>
            <div v-if="!spiner">
                <button class="btn btn-primary mt-3" type="button" disabled>
                    <span class="spinner-border" role="status" aria-hidden="true"></span><span class="ml-2 h4">Loading...</span></button>
            </div>
            <div v-if="spiner">
                <table class="table table-sm table-hover col-auto mt-3">
                    <thead>
                    <tr class="table-info">
                        <th class="food">食品</th>
                        <th class="calorie">カロリー</th>
                        <th class="delete">削除</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in intaked" v-bind:key="item.id">
                        <td>{{ item.food_name }}</td>
                        <td>{{ item.food_calorie }}kcal</td>
                        <td class="deleteButton">
                            <!-- 削除ボタン-->
                            <button v-on:click="showdeleteModal(item)" class="btn btn-outline-danger btn-sm">ー</button>
                        </td>
                    </tr>
                    <td v-if="!intaked.length">何も登録されていません</td>
                    </tbody>
                </table>
                <div class="row pb-3">
                    <h4 class="col-sm-7 col-auto mt-1">摂取カロリー合計：{{sumFoodCalories}}kcal</h4>
                    <a @click="intakeDate()" class="btn col-sm-5 btn-outline-info float-left" role="button">摂取カロリー登録</a>
                </div>
                <table class="table table-sm table-hover col-auto">
                    <thead>
                    <tr class="table-danger">
                        <th class="training">トレーニング</th>
                        <th class="calorie">カロリー</th>
                        <th class="delete">削除</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in burned" v-bind:key="item.id">
                        <td>{{ item.motion_name }}</td>
                        <td>{{ item.motion_calorie }}kcal</td>
                        <td class="deleteButton">
                            <!-- 削除ボタン-->
                            <button v-on:click="showdeleteConModal(item)" class="btn btn-outline-danger btn-sm">ー</button>
                        </td>
                    </tr>
                    <td v-if="!burned.length">何も登録されていません</td>
                    </tbody>
                </table>
                <div class="row pb-3">
                    <h4 class="col-sm-7 col-auto mt-1">消費カロリー合計：{{sumTrainingCalories}}kcal</h4>
                    <a @click="consumptionDate()" class="btn col-sm-5  btn-outline-danger float-left" role="button">消費カロリー登録</a>
                </div>
            </div>
        </div>
        <!--摂取削除確認モーダル-->
        <b-modal ref="deleteModal" title="削除確認" class="text-danger" centered hide-footer>
            <div class="form-group mt-auto">
                <div class="h6">
                    {{this.delete.food_name}}を<span class="text-danger">削除</span>しますか？
                </div>
                <div class="mt-4 row float-right">
                    <button @click="hidedeleteModal" class="btn btn-outline-secondary mr-3">キャンセル</button>
                    <button @click="removeIntakeItem" class="btn btn-outline-danger mr-3">削除</button>
                </div>
            </div>
        </b-modal>
        <!--消費削除確認モーダル-->
        <b-modal ref="deleteConModal" title="削除確認" class="text-danger" centered hide-footer>
            <div class="form-group mt-auto">
                <div class="h6">
                    {{this.delete.motion_name}}を<span class="text-danger">削除</span>しますか？
                </div>
                <div class="mt-4 row float-right">
                    <button @click="hidedeleteConModal" class="btn btn-outline-secondary mr-3">キャンセル</button>
                    <button @click="removeConItem" class="btn btn-outline-danger mr-3">削除</button>
                </div>
            </div>
        </b-modal>
    </div>
</template>

<script>
    import Vue from 'vue'
    import VCalendar from 'v-calendar'
    Vue.use(VCalendar)

    export  default {
        data() {
            return {
                mode: 'single',
                selectedDate: new Date(),
                selectDay: "",
                dataGet:"",
                burned:[],
                intaked:[],
                spiner:true,
                delete:[],
                attrs: [
                    {
                        key: 'today',
                        dot: true,
                        dates: new Date(),
                    },
                ],
            }
        },
        methods:{
          //摂取日付指定呼び出し
            intakeDate(){
                this.$store.commit("setDate", this.selectedDate)
                this.$router.replace("/intakecalorie")
            },
            consumptionDate(){
                this.$store.commit("setDate", this.selectedDate)
                this.$router.replace("/consumptioncalorie")
            },
            //モーダル呼び出し
            //直接入力のモーダルを開く
            showdeleteModal(item) {
                this.delete = item
                this.$refs['deleteModal'].show()
            },
            //直接入力のモーダルを閉じる
            hidedeleteModal() {
                this.$refs['deleteModal'].hide()
            },
            //直接入力のモーダルを開く
            showdeleteConModal(item) {
                this.delete = item
                this.$refs['deleteConModal'].show()
            },
            //直接入力のモーダルを閉じる
            hidedeleteConModal() {
                this.$refs['deleteConModal'].hide()
            },
            //摂取リストの削除
            removeIntakeItem:async function () {
                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)
                //モーダルを閉じる
                this.hidedeleteModal()
                //削除処理
                //通信
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/food/delete"
                this.dataGet={
                    intaked_ID:this.delete.intaked_ID
                }
                const json_data = JSON.stringify(this.dataGet)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        const flg_data = data["isSuccess"]
                        if (flg_data){
                            console.log("摂取カロリー削除:ok")
                        }else {
                            console.log("摂取カロリー削除:ng")
                            alert("削除に失敗しました。。もう一度やり直してください")
                            return 0
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                        return 0
                    })
                //リストから削除
                const index = this.intaked.indexOf(this.delete);
                this.intaked.splice(index, 1)
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
            },
            removeConItem:async function () {
                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)
                //モーダルを閉じる
                this.hidedeleteConModal()
                //削除処理
                //通信
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/motion/delete"
                this.dataGet={
                    burned_ID:this.delete.burned_ID
                }
                const json_data = JSON.stringify(this.dataGet)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        const flg_data = data["isSuccess"]
                        if (flg_data){
                            console.log("消費カロリー削除:ok")
                        }else {
                            console.log("消費カロリー削除:ng")
                            alert("削除に失敗しました。。もう一度やり直してください")
                            return 0
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                        return 0
                    })
                //リストから削除
                const index = this.burned.indexOf(this.delete);
                this.burned.splice(index, 1)
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
            },
        },
        async created() {
            //ローディングアニメーションを起動
            this.$store.commit("setLoading", true)
            const selectYear = this.selectedDate.getFullYear()
            const selectMonth = ("0" + (this.selectedDate.getMonth() + 1)).slice(-2)
            const selectDay = ("0" + this.selectedDate.getDate()).slice(-2)
            this.selectDay = "" + selectYear + selectMonth + selectDay

            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule"
            this.dataGet={
                account_token:this.$store.state.accountToken,
                add_date:Number(this.selectDay)
            }
            const json_data = JSON.stringify(this.dataGet)
            await fetch(URL,{
                mode:'cors',
                method:'POST',
                body:json_data,
                headers:{'Content-type':'application'},
            })
                .then(response => response.json())
                .then(data => {
                    console.log("カレンダー情報取得:ok")
                    this.intaked.splice(0,this.intaked.length)
                    this.burned.splice(0,this.burned.length)
                    this.intaked = data["intaked"]
                    this.burned = data["burned"]
                })
                .catch(function (error) {
                    console.log(error)
                    alert("エラーが発生しました。もう一度やり直してください")
                })
            //ローディングアニメーションを終了
            this.$store.commit("setLoading", false)
        }, watch: {
            selectedDate: async function () {
                this.spiner = false
                const selectYear = this.selectedDate.getFullYear()
                const selectMonth = ("0" + (this.selectedDate.getMonth() + 1)).slice(-2)
                const selectDay = ("0" + this.selectedDate.getDate()).slice(-2)
                this.selectDay = "" + selectYear + selectMonth + selectDay

                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule"
                this.dataGet={
                    account_token:this.$store.state.accountToken,
                    add_date:Number(this.selectDay)
                }
                const json_data = JSON.stringify(this.dataGet)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("カレンダー情報取得:ok")
                        this.intaked.splice(0,this.intaked.length)
                        this.burned.splice(0,this.burned.length)
                        this.intaked = data["intaked"]
                        this.burned = data["burned"]
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
                this.spiner = true
            }
        },
        computed: {
            sumFoodCalories() {
                return this.intaked.reduce(function (sum, item) {
                    return Number(sum) + Number(item.food_calorie)
                }, 0)
            },
            sumTrainingCalories() {
                return this.burned.reduce(function (sum, item) {
                    return Number(sum) + Number(item.motion_calorie)
                }, 0)
            },
        }
    }
</script>