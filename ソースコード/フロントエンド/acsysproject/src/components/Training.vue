<template>
    <div class="container">
        <span class="row ml-2 mt-4">
            <span v-for="tItem in genreBox" v-bind:key="tItem.genre_ID">
                <button @click="getTraining(tItem)" class="btn btn btn-outline-info">{{tItem.genre_name}}</button>
            </span>
        </span>
        <b-card no-body class="col-auto">
            <div class="h5 mt-2">
                選択トレーニング：{{titleName}}
            </div>
            <div class="row">
                <span v-for="trainingItem in trainingBox" v-bind:key="trainingItem.url_ID" class="mx-auto col-md-4 mb-2">
                    <div class="card" >
                        <div class="card-body">
                            <h5 class="card-title">{{trainingItem.url_title}}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{trainingItem.url_subtitle}}</h6>
                            <p class="card-text">消費カロリー：{{trainingItem.url_calorie}}</p>
                            <button @click="openTrainingModal(trainingItem)" class="btn btn-outline-success" >挑戦してみる</button>
                        </div>
                    </div>
                </span>
            </div>
        </b-card>
        <!--モーダル-->
        <b-modal ref="trainingModal" :title=selectBox.url_title hide-footer>
            <div class="form-group mt-auto">
                <b-embed
                        type="iframe"
                        aspect="16by9"
                        :src="this.selectBox.url"
                        allowfullscreen></b-embed>
                <!--ボタン-->
                <div class="mt-4 row float-right">
                    <button @click="closTrainingModal" class="btn btn-outline-secondary mr-3">キャンセル</button>
                    <button @click="addTraining" class="btn btn-outline-success mr-3">完了</button>
                </div>
            </div>
        </b-modal>
    </div>
</template>

<script>
    export default {
        name: "Training",
        data(){
            return{
                day:"",
                addIntakeItem:[],
                //分類
                genreBox:[],
                trainingGetBox:[],
                trainingBox:[],
                selectBox:[],
                titleName:"",
            }
        },methods:{
            //分類取得
            getTraining:async function(trainigItem){
                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)
                this.trainingGetBox.splice(-this.trainingGetBox.length)
                this.trainingGetBox.push({
                    genre_ID:trainigItem.genre_ID
                })
                this.titleName = trainigItem.genre_name
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/trainingurl"

                const json_data = JSON.stringify(this.trainingGetBox)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        this.trainingBox = data
                        console.log("トレーニング取得:ok")
                    })
                    .catch(function (error) {
                        console.log(error)
                        console.log("トレーニング取得:ng")
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
            },
            //トレーニングのモーダルを開く
            openTrainingModal(selectItem){
                this.$refs['trainingModal'].show()
                this.selectBox = selectItem
                console.log(this.selectBox)
            },
            //トレーニングのモーダルを閉じる
            closTrainingModal() {
                this.$refs['trainingModal'].hide()
            },
            addTraining:async function(){
                this.closTrainingModal()
                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)

                this.addIntakeItem.push({
                    add_date:Number(this.day),
                    motion_calorie: this.selectBox.url_calorie,
                    motion_name: this.selectBox.url_title,
                })

                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/motion"

                this.trainingArray ={
                    'account_token':this.$store.state.accountToken,
                    'data':this.addIntakeItem
                }

                const json_data = JSON.stringify(this.trainingArray)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        let check = data["isSuccess"]
                        //ローディングアニメーションを終了
                        this.$store.commit("setLoading", false)
                        if (check === true){
                            console.log("トレーニング登録:ok")
                            this.$router.replace("/savecalorie")
                        }else {
                            alert("エラーが発生しました。もう一度やり直してください")
                            console.log("トレーニング登録:ng")
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
            }
        },
        async created() {
            //ローディングアニメーションを起動
            this.$store.commit("setLoading", true)
            let today = new Date()
            this.day = today.getFullYear() + ("0" + (today.getMonth() + 1)).slice(-2) +("0" +today.getDate()).slice(-2)
            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/trainingurl"
            await fetch(URL,{
                mode:'cors',
                method:'Get',
                headers:{'Content-type':'application'},
            })
                .then(response => response.json())
                .then(data => {
                    console.log("トレーニング分類取得:ok")
                    this.genreBox = data
                })
                .catch(function (error) {
                    console.log(error)
                    console.log("トレーニング分類取得:ng")
                    alert("エラーが発生しました。もう一度やり直してください")
                })
            this.trainingGetBox.push({
                genre_ID:3
            })
            this.titleName = "背筋"
            const URL2 = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/trainingurl"

            const json_data = JSON.stringify(this.trainingGetBox)
            await fetch(URL2,{
                mode:'cors',
                method:'POST',
                body:json_data,
                headers:{'Content-type':'application'},
            })
                .then(response => response.json())
                .then(data => {
                    this.trainingBox = data
                    console.log("トレーニング取得:ok")
                })
                .catch(function (error) {
                    console.log(error)
                    console.log("トレーニング取得:ng")
                    alert("エラーが発生しました。もう一度やり直してください")
                })
            //ローディングアニメーションを終了
            this.$store.commit("setLoading", false)
        }
    }
</script>