<template>
    <div id='app' class="container">
        <v-date-picker
                :mode="mode"
                v-model="selectedDate"
                is-inline
                is-expanded
        ></v-date-picker>
        <div v-if="!spiner">
            <button class="btn btn-primary" type="button" disabled>
                <span class="spinner-border" role="status" aria-hidden="true"></span> Loading...</button>
        </div>
        <div v-if="spiner">
            <table class="table table-sm col-auto mt-3">
                <thead>
                <tr class="table-info">
                    <th class="food">食品</th>
                    <th class="calorie">カロリー</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in intaked" v-bind:key="item.id">
                    <td>{{ item.food_name }}</td>
                    <td>{{ item.food_calorie }}kcal</td>
                </tr>
                <td v-if="!intaked.length">何も登録されていません</td>
                </tbody>
            </table>
            <h4 class="col-xs-6 col-auto pb-2">摂取カロリー合計：{{sumFoodCalories}}kcal</h4>
            <table class="table table-hover table-sm col-auto">
                <thead>
                <tr class="table-danger">
                    <th class="training">トレーニング</th>
                    <th class="calorie">カロリー</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in burned" v-bind:key="item.id">
                    <td>{{ item.motion_name }}</td>
                    <td>{{ item.motion_calorie }}kcal</td>
                </tr>
                <td v-if="!burned.length">何も登録されていません</td>
                </tbody>
            </table>
            <h4 class="col-xs-6 col-auto pt-1 pb-2">消費カロリー合計：{{sumTrainingCalories}}kcal</h4>
        </div>
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
                spiner:false
            }
        }, async created() {
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