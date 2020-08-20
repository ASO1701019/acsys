<template>
    <div class="container">
        <div class="row">
            <h1 class="col-auto pt-4 pb-2">消費カロリー入力</h1>
        </div>
        <v-date-picker
                :input-props="{ class: 'formats.input', name: 'event_dates', placeholder:'日付を入力' }"
                :mode="mode"
                :formats="formats"
                v-model="selectedDate"></v-date-picker>
        <!--リスト-->
        <table class="table table-hover mt-1 table-sm col-auto">
            <thead>
            <tr class="table-danger">
                <th class="addDate">日付</th>
                <th class="training">トレーニング</th>
                <th class="calorie">カロリー</th>
                <th class="delete">削除</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in addItem" v-bind:key="item.id">
                <td>{{ item.add_date }}</td>
                <td>{{ item.motion_name }}</td>
                <td>{{ item.motion_calorie }}kcal</td>
                <td class="deleteButton">
                    <!-- 削除ボタン-->
                    <button v-on:click="removeItem(item)" class="btn btn-outline-danger btn-sm">ー</button>
                </td>
            </tr>
            <td v-if="!addItem.length">リストは空です</td>
            </tbody>
        </table>
        <div class="row">
            <h4 class="col-xs-6 col-auto pt-1 pb-2">消費カロリー合計：{{sumCalories}}kcal</h4>
        </div>
        <div class="row">
            <button @click="openInputModal" class="btn btn-outline-info col-lg-2 col-auto">入力して追加する</button>
            <button @click="openSelectModal" class="btn btn-outline-primary col-lg-2 col-auto ml-3">選択して追加する</button>
            <button class="btn btn-outline-success col-lg-2 col-3 ml-auto" @click="enterInformation">決定</button>
        </div>

        <div class="example-modal-window">
            <!-- コンポーネント MyModal -->
            <inputMyModal @close="closeInputModal" v-if="inputModal">
                <!-- default スロットコンテンツ -->
                <div class="h3 pb-0">トレーニングとカロリーを入力してください</div>
                <div class="form-group">
                    <label for="training"></label>
                    <input type="text" placeholder="トレーニング" v-model="inputTraining" id="training" class="form-control">
                    <span class="text-danger">{{inputTrainingResult}}</span>
                    <label for="calorie"></label>
                    <input type="number" placeholder="カロリー" v-model="inputCalorie" id="calorie" class="form-control">
                    <span class="text-danger">{{inputCalorieResult}}</span>
                </div>
                <!-- /default -->
                <!-- footer スロットコンテンツ -->
                <template slot="footer">
                    <button @click="closeInputModal" class="btn btn-outline-secondary">キャンセル</button>
                    <button @click="addInputData" class="btn btn-outline-success">追加</button>
                </template>
                <!-- /footer -->
            </inputMyModal>
        </div>

        <div class="example-modal-window">
            <!-- コンポーネント MyModal -->
            <inputMyModal @close="closeSelectModal" v-if="selectModal">
                <!-- default スロットコンテンツ -->
                <h4 class="px-lg-5 mx-5">分類を選択してください</h4>
                <table class="table table-hover table-sm ">
                    <thead>
                    <tr class="table-info">
                        <th class="genre">分類</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in genreBox" v-bind:key="item.id">
                        <td @click="getTraining(item)">{{ item.genre_name }}</td>
                    </tr>
                    </tbody>
                </table>
                <!-- /default -->
                <!-- footer スロットコンテンツ -->
                <template slot="footer">
                    <button @click="closeSelectModal" class="btn btn-outline-secondary">キャンセル</button>
                </template>
                <!-- /footer -->
            </inputMyModal>
        </div>

        <div class="example-modal-window">
            <!-- コンポーネント MyModal -->
            <inputMyModal @close="closeTrainingSelectModal" v-if="selectTrainingModal">
                <!-- default スロットコンテンツ -->
                <h4 class="px-lg-5 mx-5">トレーニングを選択してください</h4>
                <table class="table table-hover table-sm ">
                    <thead>
                    <tr class="table-info">
                        <th class="food">トレーニング</th>
                        <th class="calorie">カロリー</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in trainingBox" v-bind:key="item.id">
                        <td @click="addSelectData(item.motion_name,item.motion_carolies)">{{ item.motion_name }}</td>
                        <td @click="addSelectData(item.motion_name,item.motion_carolies)">{{item.motion_carolies}}</td>
                    </tr>
                    </tbody>
                </table>
                <!-- /default -->
                <!-- footer スロットコンテンツ -->
                <template slot="footer">
                    <button @click="closeTrainingSelectModal" class="btn btn-outline-secondary">キャンセル</button>
                </template>
                <!-- /footer -->
            </inputMyModal>
        </div>

    </div>
</template>

<script>
    import inputMyModal from "./MyModal";

    export default {
        name: "ConsumptionCalorieRegistration",
        components: { inputMyModal },
        data(){
            return{
                //モーダル
                inputModal:false,
                selectModal:false,
                selectTrainingModal:false,
                //入力のデータ
                inputTraining:"",
                inputCalorie:"",
                //エラー名入れ
                inputTrainingResult:"",
                inputCalorieResult:"",
                //リスト用
                addItem:[],
                trainingArray:[],
                //日付選択
                mode: 'single',
                formats: {
                    input: ['YYYY-MM-DD'],
                },
                selectedDate: new Date(),
                //分類
                genreBox:[],
                trainingBox:[],
            }
        },
        methods:{
            //リストの削除
            removeItem:function (item) {
                const index = this.addItem.indexOf(item);
                this.addItem.splice(index, 1)
            },
            //直接入力のモーダルを閉じる
            closeInputModal() {
                this.inputModal = false
                this.inputTrainingResult = ""
                this.inputCalorieResult = ""
            },
            //直接入力のモーダルを開く
            openInputModal(){
                this.inputModal = true
            },
            //直接入力のモーダルを開く
            openSelectModal(){
                this.selectModal = true
            },
            //直接入力のモーダルを閉じる
            closeSelectModal() {
                this.selectModal = false
            },
            //直接入力のモーダルを開く
            openTrainingSelectModal(){
                this.selectTrainingModal = true
            },
            //直接入力のモーダルを閉じる
            closeTrainingSelectModal() {
                this.selectTrainingModal = false
            },
            addInputData(){
                //バリデーション
                let inputTrainingCheck = false
                let inputCalorieCheck = false
                if (!this.inputTraining){
                    this.inputTrainingResult="トレーニングを入力してください"
                    inputTrainingCheck = false
                }else if (this.inputTraining.length>75){
                    this.inputTrainingResult="文字数が多すぎます"
                    inputTrainingCheck = false
                }else {
                    this.inputTrainingResult=""
                    inputTrainingCheck = true
                }
                if (!this.inputCalorie){
                    this.inputCalorieResult="カロリーを入力してください"
                    inputCalorieCheck = false
                }else if(Number(this.inputCalorie) < 0){
                    this.inputCalorieResult="プラスで入力してください"
                    inputCalorieCheck = false
                }else if (this.inputCalorie.length > 7){
                    this.inputCalorieResult="桁数が多すぎます"
                    inputCalorieCheck = false
                }else {
                    this.inputCalorieResult=""
                    inputCalorieCheck = true
                }
                let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                if (inputTrainingCheck === true && inputCalorieCheck ===true) {
                    //追加処理
                    this.addItem.push({
                        motion_name: this.inputTraining,
                        motion_calorie: this.inputCalorie,
                        add_date:Number(time),
                    })
                    this.inputTraining = ""
                    this.inputCalorie = ""
                    this.inputModal = false
                }
            },
            addSelectData(training,calorie){
                let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                this.addItem.push({
                    add_date:Number(time),
                    motion_calorie: calorie,
                    motion_name: training,
                })
                this.closeTrainingSelectModal()
            },
            //データ送信
            enterInformation:async function(){

                if (this.addItem.length===0){
                    alert("一つ以上入力してください")
                    return
                }

                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/motion"

                this.trainingArray ={
                    'account_token':this.$store.state.accountToken,
                    'data':this.addItem
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
                        console.log(data)
                        let check = data["isSuccess"]
                        if (check === true){
                            console.log("消費カロリー登録:ok")
                            this.$router.replace("/savecalorie")
                        }else {
                            alert("エラーが発生しました。もう一度やり直してください")
                            console.log("消費カロリー登録:ng")
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                    })

            },
            getTraining:async function(item){
                this.selectModal = false
                this.openTrainingSelectModal()
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/motion"
                let getTrainingItem ={
                    'genre_ID':item.genre_ID
                }
                const json_data = JSON.stringify(getTrainingItem)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("トレーニング取得:ok")
                        this.trainingBox = data
                    })
                    .catch(function (error) {
                        console.log(error)
                        console.log("トレーニング取得:ng")
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
            },
        },
        computed:{
            //カロリー合計計算
            sumCalories(){
                return this.addItem.reduce(function(sum, item) {
                    return Number(sum) + Number(item.motion_calorie)
                }, 0)
            }
        },
        async created() {
            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/motion"

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
        }
    }
</script>

<style scoped>

</style>