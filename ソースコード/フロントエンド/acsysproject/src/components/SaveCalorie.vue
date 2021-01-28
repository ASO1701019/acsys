<template>
    <div class="container">
        <h3 class="pt-5 pb-4">現在の貯金は<span class="h1">{{totalCalorie}}</span>kcal</h3>
        <div class="row mx-auto">
            <ul class="col-md-6 col-auto list-group">
                <li class="list-group-item list-group-item-primary lead">今日の貯金:{{todayCalorie}}kcal</li>
                <li class="list-group-item list-group-item-info lead">摂取カロリー：{{todayPlusCalorie}}kcal</li>
                <li class="list-group-item list-group-item-danger lead">消費カロリー：{{todayMinusCalorie}}kcal</li>
                <!--コメント-->
                <li class="list-group-item  mb-4 lead">{{comment}}</li>
                <!--カロリー登録ボタン-->
                <a class="btn btn-outline-info btn-lg mb-4 " href="/intakecalorie" role="button">摂取カロリー登録</a>
                <a class="btn btn-outline-danger btn-lg mb-4" href="/consumptioncalorie" role="button">消費カロリー登録</a>
            </ul><!-- /.ul -->
            <div class="chart-small col-md-6 col-auto">
                <!--グラフ-->
                <SaveCalorieChart :chart-data="dataCollection" :options="dataOptions"></SaveCalorieChart>
            </div><!-- /.div -->
        </div><!-- /.row -->
    </div><!-- /.container -->
</template>

<script>
    //グラフ
    import SaveCalorieChart from "./SaveCalorieChart";

    export default {
        name: "save_calorie",
        components:{
            SaveCalorieChart
        },
        data(){
            return{
                //カロリー関係
                totalCalorie:0,
                //当日
                todayPlusCalorie:0,
                todayMinusCalorie:0,
                todayCalorie:0,
                //昨日
                yestardayIntaked:0,
                yestardayBurned:0,
                yestardayCalorie:0,
                //一昨日
                backYestardayIntaked:0,
                backYestardayBurned:0,
                backYestardayCalorie:0,
                //コメント類
                comment:"",
                //グラフの関数
                dataCollection: null,
                dataOptions:null,
                todayCollor:"",
                yestardayCollor:"",
                backYestardayCollor:"",
            }
        },
        async created() {
            //ローディングアニメーションを起動
            this.$store.commit("setLoading", true)
            //ユーザー情報取得
            const GURL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/information"
            let data={
                account_token:this.$store.state.accountToken
            }
            const json_dataP = JSON.stringify(data)
            await fetch(GURL,{
                mode:'cors',
                method:'POST',
                body:json_dataP,
                headers:{'Content-type':'application'},
            })
                .then(response => response.json())
                .then(data => {
                    const flg_data = data['isSuccess']
                    if(flg_data){
                        console.log('ユーザー情報取得:ok')
                        //ストアにユーザー情報を保存する処理
                        this.userInfBox={
                            name:data['account_name'],
                            birthday:data['account_birthday'],
                            gender:data['account_gender'],
                            height:data['account_height'],
                            weight:data['account_weight'],
                            activlevel:data['account_level'],
                            startday:data['regist_date'],
                            purpose:data['account_purpose'],
                        }
                        this.$store.commit('accountUpdate',this.userInfBox)
                    }else {
                        console.log('ユーザー情報取得:ng')
                    }
                })
                .catch(function (error) {
                    console.log(error)
                })

            //カロリーデータ取得
            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/calorie"
            let dataGet={
                account_token:this.$store.state.accountToken
            }
            const json_data = JSON.stringify(dataGet)
            await fetch(URL,{
                mode:'cors',
                method:'POST',
                body:json_data,
                headers:{'Content-type':'application'},
            })
                .then(response => response.json())
                .then(data => {
                    console.log("ユーザーカロリー取得:ok")
                    this.totalCalorie =data["difference_calorie"]
                    this.todayPlusCalorie = data["today_intaked"]
                    this.todayMinusCalorie  = data["today_burned"]
                    this.yestardayBurned =  data["yestarday_burned"]
                    this.yestardayIntaked = data["yestarday_intaked"]
                    this.backYestardayBurned = data["before_yestarday_burned"]
                    this.backYestardayIntaked =  data["before_yestarday_intaked"]
                    //Twitter用のカロリーを登録
                    let calorieInf={
                        userCalorie : this.totalCalorie,
                        userIntakeCalorie : this.todayPlusCalorie,
                        userConsumptionCalorie : this.todayMinusCalorie
                    }
                    this.$store.commit('calorieAdd',calorieInf)
                })
                .catch(function (error) {
                    console.log("エラー発生" + error)
                    alert("エラーが発生しました。再読み込みをしてください。もし治らなければ報告してくださると助かります")
                })

            //貯金を求める
            if (this.$store.state.accountPurpose === "増量"){
                this.totalCalorie = -(this.totalCalorie)
                this.todayCalorie =  this.todayPlusCalorie - this.todayMinusCalorie
                this.yestardayCalorie = this.yestardayIntaked - this.yestardayBurned
                this.backYestardayCalorie = this.backYestardayIntaked - this.backYestardayBurned
            }else {
                this.todayCalorie = this.todayMinusCalorie - this.todayPlusCalorie
                this.yestardayCalorie = this.yestardayBurned - this.yestardayIntaked
                this.backYestardayCalorie = this.backYestardayBurned - this.backYestardayIntaked
            }
            //コメント
            let kcalKg = Math.round(this.totalCalorie / 7305 *100)/100
            if (this.$store.state.accountPurpose === "増量"){
                if (kcalKg<0){
                    this.comment += "体重が"+ -(kcalKg) +"kg減りました。体重が減少傾向にあります。毎日摂取カロリーを増やしたり、運動を少し減らしたりしてみましょう！"
                }
                else if (kcalKg===0){
                    this.comment = "体重に変化はありません"
                }
                else if (2>=kcalKg&&kcalKg>0){
                    this.comment += "体重が"+ kcalKg +"kg増えました。体重が増え始めましたね！無理せずこのまま継続していきましょう。"
                }else if (5>kcalKg&&kcalKg>2){
                    this.comment += "体重が"+ kcalKg +"kg増えました。いいですね！この調子でいきましょう！"
                }else {
                    this.comment += "体重が"+ kcalKg +"kg増えました。増量おめでとうございます！増量のし過ぎは体調にも影響があるので、体と相談しながらやりましょう！"
                }
            }
            else {
                if (kcalKg<0){
                    this.comment += "体重が"+ -(kcalKg) +"kg増えました。体重が増加傾向にあります。毎日摂取カロリーを減らしたり、運動を少し増やしたりしてみましょう！"
                }
                else if (kcalKg===0){
                    this.comment = "体重に変化はありません"
                }
                else if (2>=kcalKg&&kcalKg>0){
                    this.comment += "体重が"+ kcalKg +"kg減りました。体重が減り始めましたね！無理せずこのまま継続していきましょう。"
                }else if (5>kcalKg&&kcalKg>2){
                    this.comment += "体重が"+ kcalKg +"kg減りました。いいですね！この調子でいきましょう！"
                }else {
                    this.comment += "体重が"+ kcalKg +"kg減りました。減量おめでとうございます！減量のし過ぎは体調にも影響があるので、体と相談しながらやりましょう！"
                }
            }

            //グラフカラー選定
            if (this.todayCalorie >= 0){
                this.todayCollor = "mediumspringgreen"
            }else {
                this.todayCollor = "crimson"
            }
            if (this.yestardayCalorie >= 0){
                this.yestardayCollor = "mediumspringgreen"
            }else {
                this.yestardayCollor = "crimson"
            }
            if (this.backYestardayCalorie >= 0){
                this.backYestardayCollor = "mediumspringgreen"
            }else {
                this.backYestardayCollor = "crimson"
            }
            //グラフ描画
            this.fillData()

            this.$store.commit("setLoading", false)
        },
        mounted () {
            this.fillData()
        },
        methods: {
            //グラフ
            fillData () {
                this.dataCollection = {
                    labels: ['2日前', '1日前','今日'],
                    datasets: [
                        {
                            backgroundColor: [ this.backYestardayCollor,this.yestardayCollor,this.todayCollor],
                            data: [this.backYestardayCalorie,this.yestardayCalorie,this.todayCalorie]
                        },
                    ],
                }
                this.dataOptions = {
                    title:{
                        //見出し
                        display: true,
                        text: "最近の貯金",
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
                                    fontSize:18
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
        },
    }
</script>