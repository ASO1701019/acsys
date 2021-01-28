<template>
    <div class="container">
        <div class="pt-4 h2">今日で{{timeDay}}日目！</div>
        <div class="row pt-2 pb-2">
            <button @click="downYear" class="btn btn-outline-danger btn-sm" v-if="this.check2">-1</button>
            <h4 class="pt-1 px-2">{{year}}年</h4>
            <button @click="upYear" class="btn btn-outline-success btn-sm" v-if="this.check">+1</button>
        </div>
        <div class="row">
            <table class="table table-sm col-lg-5 col-auto" >
                <thead>
                <tr class="table-success">
                    <th class="month">月</th>
                    <th class="food">摂取カロリー</th>
                    <th class="training">消費カロリー</th>
                    <th class="training">貯金</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in 12" v-bind:key="item">
                    <td>{{ item }}月</td>
                    <td>{{intaked[item-1]}}</td>
                    <td>{{burned[item-1]}}</td>
                    <td>{{calorieBox[item-1]}}</td>
                </tr>
                <td v-if="!burned.length">リストは空です</td>
                </tbody>
            </table>
            <StatisticsChart class="col-lg-7" :chart-data="dataCollection" :options="dataOptions"></StatisticsChart>
            </div>
    </div>
</template>

<script>
    import StatisticsChart from "./SaveCalorieChart";
    export default {
        name: "Statistics",
        data(){
            return{
                dayBox:[],
                timeDay:"",
                year:"",
                dataGet:[],
                burned:[],
                intaked:[],
                calorieBox:[],
                dataCollection: null,
                dataOptions:null,
                spiner:false,
                toyear:new Date(),
                check:false,
                check2:true,
                collorBox:[],
            }
        },
        components: {
            StatisticsChart
        }
        ,async created() {
            //日付の差分取得
            getDay = new Date()
            const getTodayTime = getDay.getTime()
            this.year=getDay.getFullYear()
            const startDay = String(this.$store.state.accountStartDay)
            this.dayBox=startDay.split("")
            const year = this.dayBox[0] + this.dayBox[1] + this.dayBox[2] + this.dayBox[3]
            const month = this.dayBox[4] + this.dayBox[5]
            const day = this.dayBox[6] + this.dayBox[7]
            let getDay = new Date(year,month-1,day)
            const getTime = getDay.getTime()
            this.timeDay = Math.floor((getTodayTime-getTime) / (1000 * 60 * 60 * 24))
        },
        mounted () {
            this.fillData()
        },
        methods: {
            fillData() {
                this.dataCollection = {
                    labels: ['1月', '2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'],
                    datasets: [
                        {
                            backgroundColor: [this.collorBox[0],this.collorBox[1],this.collorBox[2],this.collorBox[3],this.collorBox[4],
                                this.collorBox[5],this.collorBox[6],this.collorBox[7],this.collorBox[8],this.collorBox[9],this.collorBox[10],
                                this.collorBox[11],],
                            data: [this.calorieBox[0], this.calorieBox[1],this.calorieBox[2],this.calorieBox[3],this.calorieBox[4],
                                this.calorieBox[5],this.calorieBox[6],this.calorieBox[7],this.calorieBox[8],this.calorieBox[9],
                                this.calorieBox[10],this.calorieBox[11]]
                        },
                    ],
                }
                this.dataOptions = {
                    title: {
                        //見出し
                        display: true,
                        text: this.year+"年のカロリー貯金",
                        padding: 1,
                        fontSize: 20
                    },

                    scales: {
                        yAxes: [
                            //y軸
                            {
                                ticks: {
                                    //軸のメモリ
                                    beginAtZero: true //0から始まる
                                },
                                gridLines: {
                                    //y軸の網線
                                    display: true //表示するか否か
                                },
                                scaleLabel: {
                                    //表示されるy軸の名称について
                                    display: true, //表示するか否か
                                    labelString: "kcal",
                                    fontSize: 20
                                }
                            }
                        ],
                        xAxes: [
                            //x軸
                            {
                                ticks: {
                                    autoSkip: false, //横幅が狭くなったときに表示を間引くか否か
                                    maxRotation: 90, //下のと合わせて表示される角度を決める
                                    minRoation: 90, //横幅を最小にしたときに縦に表示される
                                    fontSize: 18
                                },
                                gridLines: {
                                    //x軸の網線
                                    display: false
                                },
                            }
                        ]
                    },
                    legend: {
                        //凡例
                        display: false,
                    },
                    responsive: true,
                    maintainAspectRatio: false, //元のcanvasのサイズを保つか否か
                    spanGaps: false, //値が抜け落ちていた時、埋めるか否か
                    tooltips: {
                        mode: "point",
                        intersect: false //modeがpointのときは違いは、なし？
                    },
                }
            },
            upYear(){
                this.year+=1
                if (Number(this.year) === Number(this.toyear.getFullYear())){
                    this.check = false
                }
                if (Number(this.year) >= 2020){
                    this.check2 = true
                }
            },
            downYear(){
                this.year-=1
                if (Number(this.year) <= Number(this.toyear.getFullYear())){
                    this.check = true
                }
                if (Number(this.year) === 2020){
                    this.check2 = false
                }
            }
        },
        watch:{
            year:async function () {
                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)
                //通信
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/statistics"
                this.dataGet={
                    account_token:this.$store.state.accountToken,
                    year:this.year
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
                            console.log("カロリー統計取得:ok")
                            this.intaked = data["intaked"]
                            this.burned = data["burned"]
                            if (this.$store.state.accountPurpose==="減量"){
                                for (let i = 0; i < 12; i++) {
                                    this.calorieBox[i] =  this.burned[i] - this.intaked[i]
                                }
                            }else {
                                for (let i = 0; i < 12; i++) {
                                    this.calorieBox[i] =  this.intaked[i] - this.burned[i]
                                }
                            }
                            for (let i = 0; i < 12; i++) {
                                if (this.calorieBox[i] >= 0){
                                    this.collorBox[i] = "mediumspringgreen"
                                }else{
                                    this.collorBox[i] = "crimson"
                                }
                            }
                            this.fillData()
                        }else {
                            console.log("カロリー統計取得:ng")
                            alert("エラーが発生しました。もう一度やり直してください")
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
            },
        }
    }
</script>