

<template>
    <div id="app" class="container">
        <div class="text-success mt-5 mb-3 text-center h1 font-weight-bold">
            登録内容を変更
        </div>
        <form>
<!--            <h4 class="text-success border-bottom border-success mt-4 mb-4 col-11 text-left mx-auto">アカウント情報</h4>-->

<!--            &lt;!&ndash;メールアドレス &ndash;&gt;-->
<!--            <div class="form-group row mx-auto mt-5">-->
<!--                <label for="MailAddress" class="col-lg-3 col-auto col-form-label text-right col-auto">メールアドレス</label><br>-->
<!--                <input type="email" class="col-sm-7 col-auto form-control ml-xs-5 " id="MailAddress" v-model="form.account_address">-->
<!--            </div>-->
<!--            <p class="text-danger text-center h5 col-9">-->
<!--                {{ ChangeValidation.ChangeAddressResult }}-->
<!--            </p>-->

<!--            &lt;!&ndash;パスワード &ndash;&gt;-->
<!--            <div class="form-group row mx-auto mt-5">-->
<!--                <label for="Password" class="col-sm-3  col-form-label text-right col-auto">パスワード</label><br>-->
<!--                <input type="password" class="col-sm-7 col-auto form-control ml-xs-5 " id="Password" v-model="form.account_pass"><br>-->
<!--            </div>-->
<!--            <p class="text-danger text-center h5 col-9">-->
<!--                {{ ChangeValidation.ChangePasswordResult }}-->
<!--            </p>-->

            <h4 class="text-success border-bottom border-success mt-5 mb-5 col-11 text-left mx-auto">身体情報</h4>

            <!--身長 -->
            <div class="form-group row mx-auto mt-5">
                <label for="Height"  class="col-sm-3  col-form-label text-right col-auto">身長</label><br>
                <input type="text" class="col-sm-7 col-auto form-control ml-xs-5 " id="Height" v-model="form.account_height">
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ ChangeValidation.ChangeHeightResult }}
            </p>

            <!--体重 -->
            <div class="form-group row mx-auto mt-5">
                <label for="BodyWeight" class="col-sm-3  col-form-label text-right col-auto">体重</label><br>
                <input type="text" class="col-sm-7 col-auto form-control ml-xs-5 " id="BodyWeight" v-model="form.account_weight">
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ ChangeValidation.ChangeWeightResult }}
            </p>

            <!--身体活動レベル -->
            <div id="ActiveLevel" class="form-group mt-5 mx-auto">
                <div class="row">
                    <label class="col-lg-3 col-auto col-form-label text-right col-auto" for="ActiveLevel">身体活動レベル</label>
                    <select name=”ActiveLevel” v-model="form.account_level"  class="form-control col-sm-7">
                        <option value=1 selected="selected" >レベルⅠ</option>
                        <option value=2>レベルⅡ</option>
                        <option value=3>レベルⅢ</option>
                    </select>
                </div>

                <p class="text-danger text-center h5 col-9">
                    {{ ChangeValidation.ChangeLevelResult }}
                </p>

                <div>
                    <table class="table col-11  mx-auto mt-2">
                        <tr>
                            <td></td>
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
            </div>
        </form>
        <div class="row mt-3 mb-5">
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
            }
            return {
                form: {
                    account_height: this.$store.state.accountHeight,
                    account_weight: this.$store.state.accountWeight,
                    account_level: this.$store.state.accountActiveLevel,
                },
                post_data: post_data,
                input_data: [],
                output_data: [],
                errors:[],
                ErrorMessage: true,
                ChangeResult:false,

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


                this.post_data = {
                    account_height: Number(array.account_height),
                    account_weight: Number(array.account_weight),
                    account_level: array.account_level,
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
                return this.ChangeResult
            },
            //------------------------------------------------------------------------------


            //-----------------------------バリデーション-------------------------------------


            checkForm:async function (event) {
                let SignWeight
                let SignHeight
                let SignLevel
                let re2 = /^[0-9]+$/




                // 体重の入力フォームのバリデーション
                if ("" === this.form.account_weight) {
                    this.ChangeValidation.ChangeWeightResult = "体重を入力してください"
                    console.log(this.ChangeValidation.ChangeWeightResult)
                    this.errors.push(this.ChangeValidation.ChangeWeightResult)
                    SignWeight = false
                }
                else if (!re2.test(this.form.account_weight)) {
                    this.ChangeValidation.ChangeWeightResult = "数値以外の値、もしくは全角が含まれています"
                    console.log(this.ChangeValidation.ChangeWeightResult)
                    this.errors.push(this.ChangeValidation.ChangeWeightResult)
                    SignWeight = false
                }
                else if (this.form.account_weight < 15) {
                    this.ChangeValidation.ChangeWeightResult = "軽すぎです"
                    console.log(this.ChangeValidation.ChangeWeightResult)
                    this.errors.push(this.ChangeValidation.ChangeWeightResult)
                    SignWeight = false
                }
                else if (this.form.account_weight > 300) {
                    this.ChangeValidation.ChangeWeightResult = "重すぎです"
                    console.log(this.ChangeValidation.ChangeWeightResult)
                    this.errors.push(this.ChangeValidation.ChangeWeightResult)
                    SignWeight = false
                }
                else {
                    SignWeight = true
                }

                // 身長の入力フォームのバリデーション
                if ("" === this.form.account_height) {
                    this.ChangeValidation.ChangeHeightResult = "身長を入力してください"
                    console.log(this.ChangeValidation.ChangeHeightResult)
                    this.errors.push(this.ChangeValidation.ChangeHeightResult)
                    SignHeight = false
                }
                else if (!re2.test(this.form.account_height)) {
                    this.ChangeValidation.ChangeHeightResult = "数値以外の値、もしくは全角が含まれています"
                    console.log(this.ChangeValidation.ChangeHeightResult)
                    this.errors.push(this.ChangeValidation.ChangeHeightResult)
                    SignHeight = false
                }
                else if (this.form.account_height < 80) {
                    this.ChangeValidation.ChangeHeightResult = "低すぎです"
                    console.log(this.ChangeValidation.ChangeHeightResult)
                    this.errors.push(this.ChangeValidation.ChangeHeightResult)
                    SignHeight = false
                }
                else if (this.form.account_height > 300) {
                    this.ChangeValidation.ChangeHeightResult = "高すぎです"
                    console.log(this.ChangeValidation.ChangeHeightResult)
                    this.errors.push(this.ChangeValidation.ChangeHeightResult)
                    SignHeight = false
                }
                else {
                    SignHeight = true
                }

                // 身体レベルの入力フォームのバリデーション
                if (!this.form.account_level) {
                    this.ChangeValidation.ChangeLevelResult = "レベルを入力してください"
                    console.log(this.ChangeValidation.ChangeLevelResult)
                    this.errors.push(this.ChangeValidation.ChangeLevelResult)
                    SignLevel = false
                }else {
                    this.ChangeValidation.ChangeLevelResult = ""
                    SignLevel = true
                }

                //バリデーションをクリアした時に登録情報変更
                if (SignWeight === true && SignHeight === true && SignLevel === true) {
                    const check = await this.Data_post(this.form)
                    console.log(check)
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
        }
    }
</script>
