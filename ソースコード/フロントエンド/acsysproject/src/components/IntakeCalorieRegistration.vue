<template>
    <div class="container">
        <div class="row">
            <h1 class="col-auto pt-4 pb-2">摂取カロリー入力</h1>
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
                <tr class="table-info">
                    <th class="addDate">日付</th>
                    <th class="food">食品</th>
                    <th class="calorie">カロリー</th>
                    <th class="delete">削除</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in addItem" v-bind:key="item.id">
                    <td>{{ item.add_date }}</td>
                    <td>{{ item.food_name }}</td>
                    <td>{{ item.food_calorie }}kcal</td>
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
            <h4 class="col-xs-6 col-auto pt-1 pb-2">摂取カロリー合計：{{sumCalories}}kcal</h4>
        </div>
        <div class="row">
            <button @click="showInputModal" class="btn btn-outline-info col-md-3 col-auto mr-3 ml-3">入力して追加する</button>
            <button @click="openSelectModal" class="btn btn-outline-primary col-md-3 col-auto">選択して追加する</button>
        </div>
        <button @click="enterInformation" class="btn btn-outline-success col-md-3 mt-3 float-right">決定</button>

        <!--入力モーダル-->
        <b-modal ref="inputModal" title="食べ物とカロリーを入力してください" centered hide-footer>
            <div class="form-group mt-auto">
                <!--食べ物入力-->
                <input type="text" placeholder="食べ物" v-model="inputFood" class="form-control" v-bind:class="{'is-invalid':!inputFoodError}">
                <span class="invalid-feedback text-center">{{inputFoodResult}}</span>
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
        <b-modal ref="selectModal" title="分類を選択してください" centered hide-footer scrollable >
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
                            <td @click="getFood(item)">{{ item.genre_name }}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <button @click="closeSelectModal" class="btn btn-outline-secondary float-right ">キャンセル</button>
        </b-modal>

        <!--選択第二モーダル-->
        <b-modal ref="selectFoodModal" title="食べ物を選択してください" centered hide-footer scrollable>
            <div v-if="!foodSpiner">
                <button class="btn btn-primary" type="button" disabled>
                    <span class="spinner-border mr-1" role="status" aria-hidden="true"></span> Loading...</button>
            </div>
            <div v-if="foodSpiner">
                <input type="text" placeholder="索引" v-model="keyword" class="form-control mb-2">
                <table class="table table-hover table-sm ">
                    <thead>
                    <tr class="table-info">
                        <th class="food">食品</th>
                        <th class="calorie">カロリー</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in filteredFood" v-bind:key="item.id">
                        <td @click="addSelectData(item.food_name,item.food_calorie)">{{ item.food_name }}</td>
                        <td @click="addSelectData(item.food_name,item.food_calorie)">{{item.food_calorie}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <button @click="closeFoodSelectModal" class="btn btn-outline-secondary float-right ">キャンセル</button>
            <button @click="backFoodSelectModal" class="btn btn-outline-primary float-right mr-2">戻る</button>
        </b-modal>
    </div>
</template>

<script>
    import Datepicker from "vuejs-datepicker";
    import {ja} from 'vuejs-datepicker/dist/locale'

    export default {
        name: "IntakeCalorieRegistration",
        components: {Datepicker},
        data(){
            return{
                //直接入力のデータ
                inputFood:"",
                inputCalorie:"",
                //直接入力エラー名入れ
                inputFoodResult:"",
                inputCalorieResult:"",
                //入力欄エラー判定
                inputFoodError:true,
                inputCalorieError:true,
                //リスト用
                addItem: [],
                //通信用
                foodArray:[],
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
                foodBox:[],
                //スピナー
                foodSpiner:false,
                selectSpiner:false,
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
                    this.$refs['inputModal'].show()
                }
            },
            //直接入力のモーダルを閉じる
            hideInputModal() {
                this.$refs['inputModal'].hide()
                this.inputFoodResult=""
                this.inputCalorieResult=""
                this.inputFoodError = true
                this.inputCalorieError = true
            },
            //分類選択入力のモーダルを開く
            openSelectModal(){
                this.$refs['selectModal'].show()
            },
            //分類選択入力のモーダルを閉じる
            closeSelectModal() {
                this.$refs['selectModal'].hide()
            },
            //食べ物選択入力のモーダルを開く
            openFoodSelectModal(){
                this.$refs['selectFoodModal'].show()
            },
            //食べ物選択入力のモーダルを閉じる
            closeFoodSelectModal() {
                this.$refs['selectFoodModal'].hide()
                this.keyword = ""
            },
            //選択へ戻るモーダル
            backFoodSelectModal() {
                this.$refs['selectFoodModal'].hide()
                this.$refs['selectModal'].show()
            },
            addInputData(){
                //バリデーションチェック
                //食べ物が空だった時
                if (!this.inputFood){
                    this.inputFoodResult="食べ物を入力してください"
                    this.inputFoodError = false
                }
                //食べ物の文字数が多いとき
                else if (this.inputFood.length>75){
                    this.inputFoodResult="文字数が多すぎます"
                    this.inputFoodError = false
                }
                //食べ物入力が正常
                else{
                    this.inputFoodResult=""
                    this.inputFoodError = true
                }
                //カロリーが空だったとき
                if (!this.inputCalorie){
                    this.inputCalorieResult="カロリーを入力してください"
                    this.inputCalorieError = false
                }
                //カロリーの値が負数だったとき
                else if(Number(this.inputCalorie) < 0){
                    this.inputCalorieResult="プラスで入力してください"
                    this.inputCalorieError = false
                }
                //カロリー桁数が多い
                else if (this.inputCalorie.length > 7){
                    this.inputCalorieResult="桁数が多すぎます"
                    this.inputCalorieError = false
                }
                //カロリーの入力が正常
                else {
                    this.inputCalorieResult=""
                    this.inputCalorieError = true
                }

                //日付加工
                let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                //リストに追加
                if (this.inputFoodError === true && this.inputCalorieError === true){
                    //追加処理
                    this.addItem.push({
                        add_date:Number(time),
                        food_calorie: this.inputCalorie,
                        food_name: this.inputFood,
                    })
                    this.inputFood = ""
                    this.inputCalorie = ""
                    this.hideInputModal()
                }
            },
            //食べ物の取得
            getFood:async function(item){
                this.closeSelectModal()
                this.openFoodSelectModal()
                this.foodSpiner = false
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/food"

                let getFoodItem ={
                    'genre_ID':item.genre_ID
                }
                const json_data = JSON.stringify(getFoodItem)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("食べ物取得:ok")
                        this.foodBox = data
                    })
                    .catch(function (error) {
                        console.log(error)
                        console.log("食べ物取得:ng")
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
                this.foodSpiner = true
            },
            //リストに追加
            addSelectData(food,calorie){
                let time = this.selectedDate.getFullYear() + ("0" + (this.selectedDate.getMonth() + 1)).slice(-2) +("0" + this.selectedDate.getDate()).slice(-2)
                this.addItem.push({
                    add_date:Number(time),
                    food_calorie: calorie,
                    food_name: food,
                })
                this.closeFoodSelectModal()
            },
            //データ送信
            enterInformation:async function(){

                if (this.addItem.length===0){
                    alert("1つ以上リストに入力してください")
                    return
                }

                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)

                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/food"

                this.foodArray ={
                    'account_token':this.$store.state.accountToken,
                    'data':this.addItem
                }

                const json_data = JSON.stringify(this.foodArray)
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
                            console.log("摂取カロリー登録:ok")
                            this.$router.replace("/savecalorie")
                        }else {
                            alert("登録に失敗しました。もう一度やり直してください")
                            console.log("摂取カロリー登録:ng")
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
            }
        },computed:{
            //カロリー合計計算
            sumCalories(){
                return this.addItem.reduce(function(sum, item) {
                    return Number(sum) + Number(item.food_calorie)
                }, 0)
            },
            filteredFood: function() {
                let foodBox = []
                for(let i in this.foodBox) {
                    let food = this.foodBox[i];
                    if(food.food_name.indexOf(this.keyword) !== -1) {
                        foodBox.push(food);
                    }
                }
                return foodBox;
            }
        },
        async created() {
            //食べ物の分類リスト取得
            this.selectSpiner = false
            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/calorie/food"

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
                    console.log("食べ物分類取得:ok")
                    this.genreBox = data
                })
                .catch(function (error) {
                    console.log(error)
                    console.log("食べ物分類取得:ng")
                    this.errorMesage = "分類の取得に失敗しました。もう一度ページを読み込みなおしてください。"
                })
            this.selectSpiner = true
        }
    }
</script>