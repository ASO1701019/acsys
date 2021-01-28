

<template>
    <div id="app" class="container">
        <div class="text-success mt-5 mb-3 text-center h1 font-weight-bold">
            登録内容を変更
        </div>
        <form>
            <!--見出し-->
            <h4 class="text-success border-bottom border-success mt-5 col-md-10 mx-auto">身体情報</h4>
            <!--身長 -->
            <div class="form-group row mx-auto mt-4">
                <label for="Height" class="col-md-3  col-form-label text-right col-auto">身長</label><br>
                <input type="number" class="col-md-7 col-auto form-control " id="Height" v-model="form.account_height" v-bind:class="{'is-invalid':!heightBoolean}"><br>
                <div class="invalid-feedback text-center">{{ChangeValidation.ChangeHeightResult}}</div>
            </div>
            <!--体重 -->
            <div class="form-group row mx-auto mt-4">
                <label for="BodyWeight" class="col-md-3  col-form-label text-right col-auto">体重</label><br>
                <input type="number" class="col-md-7 col-auto form-control" id="BodyWeight" v-model="form.account_weight" v-bind:class="{'is-invalid':!weightBoolean}"><br>
                <div class="invalid-feedback text-center">{{ChangeValidation.ChangeWeightResult}}</div>
            </div>
            <!--身体活動レベル -->
            <div id="ActiveLevel" class="form-group mt-4 mx-auto row">
                <label for="ActiveLevel" class="col-md-3  col-form-label text-right col-auto">身体活動レベル</label>
                <select name=”ActiveLevel” v-model="form.account_level"  class="col-md-7 col-auto form-control">
                    <option disabled value="">選択してください</option>
                    <option value=1>レベルⅠ</option>
                    <option value=2>レベルⅡ</option>
                    <option value=3>レベルⅢ</option>
                </select>
            </div>
            <div>
                <table class="table col-md-10 mx-auto mt-3">
                    <tr>
                        <td class="text-nowrap">概要</td>
                        <td>身体活動レベルとは、1日あたりの総エネルギー消費量を1日あたりの基礎代謝量で割った指標です。</td>
                    </tr>
                    <tr>
                        <td class="text-nowrap">レベルⅠ</td>
                        <td>生活の大部分が座位で、静的な活動が中心の場合</td>
                    </tr>
                    <tr>
                        <td class="text-nowrap">レベルⅡ</td>
                        <td>座位中心の仕事だが、職場内での移動や立位での作業・接客等、あるいは通勤・買物・家事、軽いスポーツ等のいずれかを含む場合</td>
                    </tr>
                    <tr>
                        <td class="text-nowrap">レベルⅢ</td>
                        <td>移動や立位の多い仕事への従事者。あるいは、スポーツなど余暇における活発な運動習慣をもっている場合</td>
                    </tr>
                </table>
            </div>
            <!--見出し-->
            <h4 class="text-success border-bottom border-success mt-5 col-md-10 mx-auto">利用目的</h4>
            <!--利用目的-->
            <div class="row mt-4">
                <label id="PurposeTitle" class="col-md-3  col-form-label text-right col-3">目的</label>
                <div class="form-check mt-2 ml-3 col-md-2 col-auto">
                    <input class="form-check-input" type="radio" name="Purpose" id="down" value="減量" v-model="form.account_purpose">
                    <label class="form-check-label" for="down">減量</label>
                </div>
                <div class="form-check mt-2 col-md-2 col-auto">
                    <input class="form-check-input" type="radio" name="Purpose" id="up" value="増量" v-model="form.account_purpose">
                    <label class="form-check-label" for="up">増量</label>
                </div>
            </div>
        </form>
        <div class="row mt-5 mb-5">
            <button id="post_btn" class="btn btn-success col-8 mx-auto"  @click="checkHandler(form,$event)">決定</button>
        </div>
        <div>
        </div>
    </div>
</template>

<script>
    const URL = 'https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/update'
    export default {
        name: "UserChange",
        data: function () {
            const post_data = {
                account_height: '',
                account_weight: '',
                account_level: '',
                account_purpose: "0",
            }
            return {
                form: {
                    account_height: this.$store.state.accountHeight,
                    account_weight: this.$store.state.accountWeight,
                    account_level: this.$store.state.accountActiveLevel,
                    account_purpose:this.$store.state.accountPurpose,
                },
                post_data: post_data,
                ChangeResult:false,
                heightBoolean:true,
                weightBoolean:true,
                ChangeValidation: {
                    ChangeHeightResult: "",
                    ChangeWeightResult: "",
                    ChangeLevelResult: "",
                }
            }
        },
        methods: {
            checkHandler: function (array, event) {
                this.checkForm(event);
            },
            //----------------------------データ保存---------------------------------------
            Data_post:async function (array) {
                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)
                this.post_data = {
                    account_height: Number(array.account_height),
                    account_weight: Number(array.account_weight),
                    account_level: array.account_level,
                    account_purpose:array.account_purpose,
                    account_token:this.$store.state.accountToken,
                }
                const json_data = JSON.stringify(this.post_data)
                await fetch(URL, {
                    mode: 'cors',
                    method: 'POST',
                    body: json_data,
                    headers: {'Content-type': 'application'},
                })
                    .then(function (response) {
                        return response.json()
                    })
                    .then(data => {
                        const flg_data = data['isSuccess']
                        if(flg_data){
                            console.log('登録情報変更ok')
                            this.ChangeResult = true
                        }else {
                            console.log('登録情報変更ng')
                            this.ChangeResult = false
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                    })
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
                return this.ChangeResult
            },
            //------------------------------------------------------------------------------
            //-----------------------------バリデーション-------------------------------------
            checkForm:async function (event) {
                // 身長の入力フォームのバリデーション
                if (!this.form.account_height) {
                    this.ChangeValidation.ChangeHeightResult = "身長を入力してください"
                    console.log("身長未入力")
                    this.heightBoolean = false
                }
                else if (this.form.account_height < 80) {
                    this.ChangeValidation.ChangeHeightResult = "80cm以上で入力してください"
                    console.log("身長：規定値より小さい")
                    this.heightBoolean = false
                }
                else if (this.form.account_height > 300) {
                    this.ChangeValidation.ChangeHeightResult = "300cm以下で入力してください"
                    console.log("身長：規定値より大きい")
                    this.heightBoolean = false
                }
                else {
                    this.heightBoolean = true
                    this.ChangeValidation.ChangeHeightResult = ""
                }
                // 体重の入力フォームのバリデーション
                if (!this.form.account_weight) {
                    this.ChangeValidation.ChangeWeightResult = "体重を入力してください"
                    console.log("体重未入力")
                    this.weightBoolean = false
                }
                else if (this.form.account_weight < 15) {
                    this.ChangeValidation.ChangeWeightResult = "15kg以上で入力してください"
                    console.log("体重:規定値より小さい")
                    this.weightBoolean = false
                }
                else if (this.form.account_weight > 300) {
                    this.ChangeValidation.ChangeWeightResult = "300kg以下で入力してください"
                    console.log("体重:規定値より大きい")
                    this.weightBoolean = false
                }
                else {
                    this.weightBoolean = true
                    this.ChangeValidation.ChangeWeightResult = ""
                }
                //身体レベルの入力フォームのバリデーションは必要なし
                // バリデーションをクリアした時に登録情報変更
                if (this.weightBoolean === true && this.heightBoolean === true) {
                    const check = await this.Data_post(this.form)
                    if (check){
                        //登録時
                        await this.$router.replace("/savecalorie")
                    }else {
                        //エラーや存在しなかった場合
                        console.log("アカウントが存在しないもしくはエラー")
                        alert("エラーが発生しました。もう一度やり直してください")
                    }
                }
                event.preventDefault();
            },
        },
    }
</script>
