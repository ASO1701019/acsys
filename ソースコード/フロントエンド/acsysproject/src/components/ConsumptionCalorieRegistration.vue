<template>
    <div class="container">
        <div class="row">
            <h1 class="col-auto pt-4 pb-2">消費カロリー入力</h1>
        </div>
        <!--日付選択-->
        <datepicker
            v-model=selectedDate
            :format="DatePickerFormat"
            :language="ja"
            :highlighted="highlighted"
            :disabled-dates="disabledDates">
        </datepicker>
        <!--リスト-->
        <table class="table table-hover mt-1 table-sm col-auto">
            <thead>
                <tr class="table-danger">
                    <th class="addDate">日付</th>
                    <th class="training">運動</th>
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
                <!--リストが空だった時-->
                <td v-if="!addItem.length">リストは空です</td>
            </tbody>
        </table>
        <!--合計-->
        <div class="row">
            <h4 class="col-xs-6 col-auto pt-1 pb-2">消費カロリー合計：{{sumCalories}}kcal</h4>
        </div>
        <div class="row">
            <button @click="showInputModal" class="btn btn-outline-info col-md-3 mx-3 mb-3">入力して追加する</button>
            <button @click="openSelectModal" class="btn btn-outline-primary col-md-3 mx-3 mb-3">選択して追加する</button>
            <button @click="addDayCalorie" class="btn btn-outline-danger col-md-3 mx-3 mb-3">一日の消費カロリー追加</button>
        </div>
        <button @click="enterInformation" class="btn btn-outline-success col-md-3 mt-3 float-right">決定</button>

        <!--入力モーダル-->
        <b-modal ref="trainingInputModal" title="運動とカロリーを入力してください" centered hide-footer>
            <div class="form-group mt-auto">
                <!--トレーニング入力-->
                <input type="text" placeholder="運動" v-model="inputTraining" class="form-control" v-bind:class="{'is-invalid':!inputTrainingError}">
                <span class="invalid-feedback text-center">{{inputTrainingResult}}</span>
                <!--カロリー入力-->
                <input type="number" placeholder="カロリー" v-model="inputCalorie" class="form-control mt-3" v-bind:class="{'is-invalid':!inputCalorieError}">
                <span class="invalid-feedback text-center">{{inputCalorieResult}}</span>
                <!--ボタン-->
                <div class="mt-4 row float-right">
                    <button @click="hideInputModal" class="btn btn-outline-secondary mr-3">キャンセル</button>
                    <button @click="addInputData" class="btn btn-outline-success mr-3">追加</button>
                </div>
            </div>
        </b-modal>

        <!--選択第一モーダル-->
        <b-modal ref="selectTrainingModal" title="分類を選択してください" centered hide-footer scrollable >
            <div v-if="!selectSpiner">
                <button class="btn btn-primary" type="button" disabled>
                    <span class="spinner-border mr-1" role="status" aria-hidden="true"></span> Loading...</button>
            </div>
            <div v-if="selectSpiner">
                <div v-if="errorMesage">
                    {{errorMesage}}
                </div>
                <div v-if="!errorMesage">
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
                </div>
            </div>
            <button @click="closeSelectModal" class="btn btn-outline-secondary float-right ">キャンセル</button>
        </b-modal>

        <!--選択第二モーダル-->
        <b-modal ref="selectActionModal" title="運動を選択してください" centered hide-footer scrollable size="lg">
            <div v-if="!trainingSpiner">
                <button class="btn btn-primary" type="button" disabled>
                    <span class="spinner-border mr-1" role="status" aria-hidden="true"></span> Loading...</button>
            </div>
            <div v-if="trainingSpiner">
                <input type="text" placeholder="索引" v-model="keyword" class="form-control mb-2">
                <table class="table table-hover table-sm">
                    <thead>
                    <tr class="table-info">
                        <th class="training" scope="col">トレーニング</th>
                        <th class="calorie" scope="col">メッツ</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in filteredTraining" v-bind:key="item.id">
                        <td @click="addSelectData(item.motion_name,item.motion_calorie)">{{ item.motion_name }}</td>
                        <td @click="addSelectData(item.motion_name,item.motion_calorie)">{{item.motion_calorie}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <button @click="closeTrainingSelectModal" class="btn btn-outline-secondary float-right ">キャンセル</button>
            <button @click="backTrainingSelectModal" class="btn btn-outline-primary float-right mr-2">戻る</button>
        </b-modal>

        <!--選択第三モーダル-->
        <b-modal ref="inputActionModal" title="時間(分)を入力してください" centered hide-footer>
            <div class="form-group mt-auto">
                <!--トレーニング入力-->
                <input type="text" placeholder="運動" readonly v-model="selectTraining" class="form-control" >
                <!--カロリー入力-->
                <input type="number" placeholder="カロリー" readonly  v-model="selectCalorie" class="form-control mt-3" >
                <!--時間入力-->
                <input type="number" placeholder="時間(分)"  v-model="selectMinutes" class="form-control mt-3" v-bind:class="{'is-invalid':!selectMinutesErrer}">
                <span class="invalid-feedback text-center">{{selectMinutesResult}}</span>
                <!--ボタン-->
                <div class="mt-4 row float-right">
                    <button @click="inputTrainingHideSelectModal" class="btn btn-outline-secondary mr-3">キャンセル</button>
                    <button @click="backTrainingOpenSelectModal" class="btn btn-outline-primary float-right mr-3">戻る</button>
                    <button @click="addInputSelectData" class="btn btn-outline-success mr-3">追加</button>
                </div>
            </div>
        </b-modal>

    </div>
</template>

<script>
    import Datepicker from "vuejs-datepicker";
    import {ja} from 'vuejs-datepicker/dist/locale'

    export default {
        name: "ConsumptionCalorieRegistration",
        components: { Datepicker },
        data(){
            return{
                //直接入力のデータ
                inputTraining:"",
                inputCalorie:"",
                //直接エラー名入れ
                inputTrainingResult:"",
                inputCalorieResult:"",
                //直接入力欄エラー判定
                inputTrainingError:true,
                inputCalorieError:true,
                //選択入力計算用変数
                selectTraining:"",
                selectCalorie:"",
                selectMinutes:"",
                //選択入力エラー
                selectMinutesResult:"",
                selectMinutesErrer:true,
                //リスト用
                addItem:[],
                trainingArray:[],
                //日付選択
                selectedDate: new Date(),
                //日付形式
                DatePickerFormat: 'yyyy-MM-dd',
                //土日を強調表示
                highlighted: {
                    days: [6, 0],
                },
                //日本語設定
                ja:ja,
                //日付制約
                disabledDates: {
                    from: new Date(),
                },
                //分類
                genreBox:[],
                trainingBox:[],
                //スピナー
                selectSpiner:false,
                trainingSpiner:false,
                errorMesage:"",
                keyword:"",
            }
        },
        methods:{
            //リストの削除
            removeItem:function (item) {
                const index = this.addItem.indexOf(item);
                this.addItem.splice(index, 1)
            },
            //直接入力のモーダルを開く
            showInputModal() {
                if(!this.selectedDate){
                    alert("日付呼び出しに失敗しました。もう一度やり直してください")
                }
                else {
                    this.$refs['trainingInputModal'].show()
                }
            },
            //直接入力のモーダルを閉じる
            hideInputModal() {
                this.$refs['trainingInputModal'].hide()
                this.inputTrainingResult=""
                this.inputCalorieResult=""
                this.inputTrainingError = true
                this.inputCalorieError = true
            },
            //分類選択入力のモーダルを開く
            openSelectModal(){
                this.$refs['selectTrainingModal'].show()
            },
            //分類選択入力のモーダルを閉じる
            closeSelectModal() {
                this.$refs['selectTrainingModal'].hide()
            },
            //運動選択入力のモーダルを開く
            openTrainingSelectModal(){
                this.$refs['selectActionModal'].show()
            },
            //運動選択のモーダルを閉じる
            closeTrainingSelectModal() {
                this.$refs['selectActionModal'].hide()
                this.keyword = ""
            },
            //分類選択に戻る
            backTrainingSelectModal(){
                this.$refs['selectActionModal'].hide()
                this.$refs['selectTrainingModal'].show()
            },
            //選択入力モーダル
            inputTrainingOpenSelectModal(){
                this.$refs['inputActionModal'].show()
            },
            inputTrainingHideSelectModal() {
                this.$refs['inputActionModal'].hide()
                this.selectTraining = ""
                this.selectCalorie=""
                this.selectMinutes=""
                this.selectMinutesResult = ""
                this.selectMinutesErrer = true
            },
            backTrainingOpenSelectModal(){
                this.$refs['inputActionModal'].hide()
                this.selectTraining = ""
                this.selectCalorie=""
                this.selectMinutes=""
                this.selectMinutesResult = ""
                this.selectMinutesErrer = true
                this.$refs['selectActionModal'].show()
            },
            addInputData(){
                //バリデーション
                //トレーニングが空だった時
                if (!this.inputTraining){
                    this.inputTrainingResult="トレーニングを入力してください"
                    this.inputTrainingError = false
                }
                //文字数が多い時
                else if (this.inputTraining.length>75){
                    this.inputTrainingResult="文字数が多すぎます"
                    this.inputTrainingError = false
                }
                //正常
                else {
                    this.inputTrainingResult=""
                    this.inputTrainingError = true
                }
                //カロリーが空だったとき
                if (!this.inputCalorie){
                    this.inputCalorieResult="カロリーを入力してください"
                    this.inputCalorieError = false
                }
                //値が負数だったとき
                else if(Number(this.inputCalorie) < 0){
                    this.inputCalorieResult="プラスで入力してください"
                    this.inputCalorieError = false
                }
                //桁数が多いとき
                else if (this.inputCalorie.length > 7){
                    this.inputCalorieResult="桁数が多すぎます"
                    this.inputCalorieError = false
                }
                //値が正常
                else {
                    this.inputCalorieResult=""
                    this.inputCalorieError = true
                }
                //日付加工
                let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                //リストに登録
                if (this.inputTrainingError === true && this.inputCalorieError === true) {
                    //追加処理
                    this.addItem.push({
                        motion_name: this.inputTraining,
                        motion_calorie: this.inputCalorie,
                        add_date:Number(time),
                    })
                    this.inputTraining = ""
                    this.inputCalorie = ""
                    this.hideInputModal()
                }
            },
            //データ選択時変数に追加しモーダルを開く
            addSelectData(training,calorie){
                this.closeTrainingSelectModal()
                this.selectTraining = training
                this.selectCalorie = Number(calorie)
                this.inputTrainingOpenSelectModal()
            },
            //選択データ入力
            addInputSelectData(){
                //バリデーション
                //時間が空だったとき
                if (!this.selectMinutes){
                    this.selectMinutesResult="時間を入力してください"
                    this.selectMinutesErrer = false
                }
                //値が負数だったとき
                else if(Number(this.selectMinutes) < 0){
                    this.selectMinutesResult="プラスで入力してください"
                    this.selectMinutesErrer = false
                }
                //桁数が多いとき
                else if (this.selectMinutes.length > 5){
                    this.selectMinutesResult="桁数が多すぎます"
                    this.selectMinutesErrer = false
                }
                //値が正常
                else {
                    this.selectMinutesResult=""
                    this.selectMinutesErrer = true
                }
                if (this.selectMinutesErrer === true){
                    // 日付を求める
                    let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                    // 計算
                    let min = Math.round(this.selectMinutes/60*100)/100
                    let calorieResult = Math.round(this.selectCalorie * this.$store.state.accountWeight  * min * 1.05)
                    //リストに登録
                    this.addItem.push({
                        add_date:Number(time),
                        motion_calorie: calorieResult,
                        motion_name: this.selectTraining,
                    })
                    // モーダルを閉じる
                    this.inputTrainingHideSelectModal()
                }
            },
            //一日の消費カロリー追加
            addDayCalorie(){
                //すでに入力されているかチェック
                let check = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                for (let item of this.addItem){
                    if (Number(item.add_date) === Number(check)){
                        if (item.motion_name === "一日の消費カロリー"){
                            alert("同じ日付に2回目の登録は出来ません")
                            return
                        }
                    }
                }
                //初期値の登録
                let genderFirstNum = 0
                let genderSecondNum = 0
                let genderThirdNum = 0
                let genderForceNum = 0
                if (this.$store.state.accountGender === "男性"){
                    genderFirstNum = 13.397
                    genderSecondNum =4.799
                    genderThirdNum = 5.677
                    genderForceNum = 88.362
                }else {
                    genderFirstNum = 9.247
                    genderSecondNum = 3.098
                    genderThirdNum = 4.33
                    genderForceNum = 447.593
                }
                // 年齢を求める
                let age = this.$store.state.accountBirthDay.toString()
                let ageYear = Number(age.slice(0, 4))
                let ageMonth = Number(age.slice(4, 6))
                let ageDay = Number(age.slice(6, 8))
                let today = new Date()
                let todayYear = today.getFullYear()
                let todayMonth = today.getMonth()+1
                let todayDay = today.getDate()
                age = todayYear - ageYear
                if (ageMonth > todayMonth){
                    --age
                }else if (ageMonth === todayMonth){
                    if (ageDay >= todayDay){
                        --age
                    }
                }
                //身体レベル
                let boddyLevel = 0
                if (this.$store.state.accountActiveLevel === "1"){
                    boddyLevel = 1.2
                }else if (this.$store.state.accountActiveLevel === "2"){
                    boddyLevel = 1.55
                }else {
                    boddyLevel = 1.9
                }
                //基礎代謝を求める
                let sumCalorie = genderFirstNum * this.$store.state.accountWeight + genderSecondNum * this.$store.state.accountHeight - genderThirdNum * age + genderForceNum
                sumCalorie = Math.round(sumCalorie * 1000) /1000
                sumCalorie = Math.round(sumCalorie * boddyLevel)
                // 日付を求める
                let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                //リストに登録
                this.addItem.push({
                    add_date:Number(time),
                    motion_calorie: sumCalorie,
                    motion_name: "一日の消費カロリー",
                })
            },
            //データ送信
            enterInformation:async function(){

                if (this.addItem.length===0){
                    alert("一つ以上入力してください")
                    return
                }

                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)

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
                        let check = data["isSuccess"]
                        //ローディングアニメーションを終了
                        this.$store.commit("setLoading", false)
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
            //トレーニングの中身取得
            getTraining:async function(item){
                this.closeSelectModal()
                this.openTrainingSelectModal()
                this.trainingSpiner = false
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
                this.trainingSpiner = true
            },
        },
        computed:{
            //カロリー合計計算
            sumCalories(){
                return this.addItem.reduce(function(sum, item) {
                    return Number(sum) + Number(item.motion_calorie)
                }, 0)
            },
            filteredTraining: function() {
                let trainingBox = []
                for(let i in this.trainingBox) {
                    let training = this.trainingBox[i];
                    if(training.motion_name.indexOf(this.keyword) !== -1) {
                        trainingBox.push(training);
                    }
                }
                return trainingBox;
            }
        },
        async created() {
            //トレーニング分類取得
            this.selectSpiner = false
            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/motion"

            if (this.$store.state.date){
                this.selectedDate = this.$store.state.date
                this.$store.commit("setDate", null)
            }

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
                    this.errorMesage = "分類の取得に失敗しました。もう一度ページを読み込みなおしてください。"
                })
            this.selectSpiner = true
        }
    }
</script>