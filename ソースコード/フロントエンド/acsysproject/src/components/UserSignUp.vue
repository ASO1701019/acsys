<template>
    <div id="app" class="container">
        <div class="text-success mt-5 mb-3 text-center h1 font-weight-bold">
            acsys に新規登録
        </div>
        <form>
            <div>
                <h4 class="text-success border-bottom border-success mb-5 col-11 text-left mx-auto">ユーザー情報</h4>
                <span class="form-group row mx-auto">
                    <label for="Name" class="col-sm-3  col-form-label text-right col-auto" >名前</label>
                    <input type="text" class="col-sm-7 col-auto form-control ml-xs-5 " id="Name" v-model="form.account_name">
                </span>
                <p class="text-danger text-center h5 col-9">
                    {{ SignupValidation.SignupNameResult }}
                </p>
            </div>

            <div class="row form-group mx-auto mt-5" id="BirthDay">
                <span id="BirthDayTitle" class="col-3 col-form-label text-right">
                    生年月日
                </span>
                <!--年 -->
                <input type="text" id="Year" v-model="form.account_year" class="col-2 form-control">
                <label for="Year" class="col-1 col-form-label">年</label>
                <!--月 -->
                <input type="text" id="Month" v-model="form.account_month" class="col-2 form-control">
                <label for="Month" class="col-1 col-form-label">月</label>
                <!--日 -->
                <input type="text" id="Day" v-model="form.account_day" class="col-2 form-control">
                <label for="Day" class="col-1 col-form-label">日</label>
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ SignupValidation.SignupBirthdayResult }}
            </p>

            <!--性別 -->
            <div class="Category_Gender row mt-5">
                <label id="GenderTitle" class="col-3 col-form-label text-right">性別</label>
                <div class="form-check mt-2 ml-3 col-2">
                    <input class="form-check-input" type="radio" name="Gender" id="male" value="男性" v-model="form.account_gender" checked="checked">
                    <label class="form-check-label" for="male">男性</label>
                </div>
                <div class="form-check mt-2 col-2">
                    <input class="form-check-input" type="radio" name="Gender" id="female" value="女性" v-model="form.account_gender">
                    <label class="form-check-label" for="female">女性</label>
                </div>
            </div>
            <h4 class="text-success border-bottom border-success mt-4 mb-4 col-11 text-left mx-auto">アカウント情報</h4>

            <!--メールアドレス -->
            <div class="form-group row mx-auto mt-5">
                <label for="MailAddress" class="col-lg-3 col-auto col-form-label text-right col-auto">メールアドレス</label><br>
                <input type="email" class="col-sm-7 col-auto form-control ml-xs-5 " id="MailAddress" v-model="form.account_address">
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ SignupValidation.SignupAddressResult }}
            </p>

            <!--パスワード -->
            <div class="form-group row mx-auto mt-5">
                <label for="Password" class="col-sm-3  col-form-label text-right col-auto">パスワード</label><br>
                <input type="password" class="col-sm-7 col-auto form-control ml-xs-5 " id="Password" v-model="form.account_pass"><br>
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ SignupValidation.SignupPasswordResult }}
            </p>

            <h4 class="text-success border-bottom border-success mt-5 mb-5 col-11 text-left mx-auto">身体情報</h4>

            <!--身長 -->
            <div class="form-group row mx-auto mt-5">
                <label for="Height"  class="col-sm-3  col-form-label text-right col-auto">身長</label><br>
                <input type="text" class="col-sm-7 col-auto form-control ml-xs-5 " id="Height" v-model="form.account_height">
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ SignupValidation.SignupHeightResult }}
            </p>

            <!--体重 -->
            <div class="form-group row mx-auto mt-5">
                <label for="BodyWeight" class="col-sm-3  col-form-label text-right col-auto">体重</label><br>
                <input type="text" class="col-sm-7 col-auto form-control ml-xs-5 " id="BodyWeight" v-model="form.account_weight">
            </div>
            <p class="text-danger text-center h5 col-9">
                {{ SignupValidation.SignupWeightResult }}
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
                    {{ SignupValidation.SignupLevelResult }}
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
    const URL = 'https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users'
    export default {
        name: "test",
        data: function () {
            const post_data = {
                account_name: '',
                account_height: '',
                account_weight: '',
                account_birthday: '',
                account_gender: '',
                account_level: '',
                account_address: '',
                account_pass: '',
            }
            return {
                form: {
                    account_name: '',
                    account_height: '',
                    account_weight: '',
                    account_year: '',
                    account_month: '',
                    account_day: '',
                    account_birthday: '',
                    account_gender: '男性',
                    account_level: '',
                    account_address: '',
                    account_pass: '',
                },
                post_data: post_data,
                input_data: [],
                output_data: [],
                errors:[],
                ErrorMessage: true,
                signupResult:false,

                SignupValidation: {
                    SignupNameResult: "",
                    SignupBirthdayResult: "",
                    SignupAddressResult: "",
                    SignupPasswordResult: "",
                    SignupHeightResult: "",
                    SignupWeightResult: "",
                    SignupLevelResult: "",
                }
            }
        },
        methods: {
            checkHandler: function (array, event) {
                this.checkForm(event);
            },
            //----------------------------データ保存---------------------------------------
            Data_post:async function (array) {

                // 生成する文字列の長さ
                const l = 32;
                // 生成する文字列に含める文字セット
                const c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
                const cl = c.length;
                let newToken = "";
                for(let i=0; i<l; i++){
                    newToken += c[Math.floor(Math.random()*cl)];
                }

                this.post_data = {
                    account_name: array.account_name,
                    account_height: Number(array.account_height),
                    account_weight: Number(array.account_weight),
                    account_birthday: Number(array.account_year + '' + ('00' + array.account_month).slice(-2) + '' + ('00' + array.account_day).slice(-2)),
                    account_gender: array.account_gender,
                    account_level: array.account_level,
                    account_address: array.account_address,
                    account_pass: array.account_pass,
                    account_token:newToken,

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
                            console.log('新期登録ok')
                            this.signupResult = true
                        }else {
                            console.log('新期登録ok')
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                    })
                if (this.signupResult){
                    return newToken
                }else{
                    return 0
                }
            },
            //------------------------------------------------------------------------------


            //-----------------------------バリデーション-------------------------------------


            checkForm:async function (event) {
                let SignMail
                let SignPass
                let SignName
                let SignBirthDay
                let SignWeight
                let SignHeight
                let SignLevel
                let re1 = /^[A-Za-z0-9][A-Za-z0-9_.-]*@[A-Za-z0-9_.-]+\.[A-Za-z0-9]+$/
                let re2 = /^[0-9]+$/
                let re3 = /^[A-Za-z0-9]+$/

                // メールアドレスの入力フォームのバリデーション
                if (!this.form.account_address) {
                    this.SignupValidation.SignupAddressResult = "メールアドレスを入力してください"
                    console.log(this.SignupValidation.SignupAddressResult)
                    SignMail = false
                }
                else if (!re1.test(this.form.account_address) && this.form.account_address !== undefined) {
                    this.SignupValidation.SignupAddressResult = "メールアドレスの形式で入力してください"
                    console.log(this.SignupValidation.SignupAddressResult)
                    SignMail = false
                }
                else if (this.form.account_address.length >= 200) {
                    this.SignupValidation.SignupAddressResult = "メールアドレスの文字数オーバー"
                    console.log(this.SignupValidation.SignupAddressResult)
                    SignMail = false
                }
                else {
                    SignMail = true
                    this.SignupValidation.SignupAddressResult = ""
                }


                // パスワードの入力フォームのバリデーション
                if (!this.form.account_pass) {
                    this.SignupValidation.SignupPasswordResult = "パスワードを入力してください"
                    console.log(this.SignupValidation.SignupPasswordResult)
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    SignPass = false
                }
                else if (!re3.test(this.form.account_pass)) {
                    console.log("パスワードに使用できない文字、もしくは全角が含まれています")
                    this.SignupValidation.SignupPasswordResult = "パスワードに使用できない文字、もしくは全角が含まれています"
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    SignPass = false
                }
                else if (this.form.account_pass.length < 6) {
                    this.SignupValidation.SignupPasswordResult = "パスワードの文字数が少ないです"
                    console.log(this.SignupValidation.SignupPasswordResult)
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    SignPass = false
                }
                else if (this.form.account_pass.length > 128) {
                    this.SignupValidation.SignupPasswordResult = "パスワードの文字数オーバー"
                    console.log(this.SignupValidation.SignupPasswordResult)
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    SignPass = false
                } else {
                    SignPass = true
                    this.SignupValidation.SignupPasswordResult = ""
                }

                // 氏名の入力フォームのバリデーション
                if (!this.form.account_name) {
                    this.SignupValidation.SignupNameResult = "氏名を入力してください"
                    console.log(this.SignupValidation.SignupNameResult)
                    this.errors.push(this.SignupValidation.SignupNameResult)
                    SignName = false
                }
                else if (re2.test(this.form.account_name)) {
                    this.SignupValidation.SignupNameResult = "名前に使用できない文字が含まれています"
                    console.log(this.SignupValidation.SignupNameResult)
                    this.errors.push(this.SignupValidation.SignupNameResult)
                    SignName = false
                }
                else if (this.form.account_name.length >= 20) {
                    this.SignupValidation.SignupNameResult = "名前の文字数オーバー"
                    console.log(this.SignupValidation.SignupNameResult)
                    this.errors.push(this.SignupValidation.SignupNameResult)
                    SignName = false
                } else {
                    SignName = true
                    this.SignupValidation.SignupNameResult = ""
                }


                // 生年月日の入力フォームのバリデーション
                if (!this.form.account_year || !this.form.account_year || !this.form.account_year) {
                    this.SignupValidation.SignupBirthdayResult = "生年月日を入力してください"
                    console.log(this.SignupValidation.SignupBirthdayResult)
                    this.errors.push(this.SignupValidation.SignupBirthdayResult)
                    SignBirthDay = false
                }
                else if (!re2.test(this.form.account_year) || !re2.test(this.form.account_month) || !re2.test(this.form.account_day)) {
                    this.SignupValidation.SignupBirthdayResult = "数値以外の値、もしくは全角が含まれています"
                    console.log(this.SignupValidation.SignupBirthdayResult)
                    this.errors.push(this.SignupValidation.SignupBirthdayResult)
                    SignBirthDay = false
                }
                else if (this.form.account_year.length > 4) {
                    this.SignupValidation.SignupBirthdayResult = "年：文字数オーバー"
                    console.log(this.SignupValidation.SignupBirthdayResult)
                    this.errors.push(this.SignupValidation.SignupBirthdayResult)
                    SignBirthDay = false
                }
                else if (this.form.account_month.length > 2) {
                    this.SignupValidation.SignupBirthdayResult = "月：文字数オーバー"
                    console.log(this.SignupValidation.SignupBirthdayResult)
                    this.errors.push(this.SignupValidation.SignupBirthdayResult)
                    SignBirthDay = false
                }
                else if (this.form.account_day.length > 2) {
                    this.SignupValidation.SignupBirthdayResult = "日：文字数オーバー"
                    console.log(this.SignupValidation.SignupBirthdayResult)
                    this.errors.push(this.SignupValidation.SignupBirthdayResult)
                    SignBirthDay = false
                } else {
                    SignBirthDay = true
                    this.SignupValidation.SignupBirthdayResult = ""
                }


                // 体重の入力フォームのバリデーション
                if (!this.form.account_weight) {
                    this.SignupValidation.SignupWeightResult = "体重を入力してください"
                    console.log(this.SignupValidation.SignupWeightResult)
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    SignWeight = false
                }
                else if (!re2.test(this.form.account_weight)) {
                    this.SignupValidation.SignupWeightResult = "数値以外の値、もしくは全角が含まれています"
                    console.log(this.SignupValidation.SignupWeightResult)
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    SignWeight = false
                }
                else if (this.form.account_weight < 15) {
                    this.SignupValidation.SignupWeightResult = "軽すぎです"
                    console.log(this.SignupValidation.SignupWeightResult)
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    SignWeight = false
                }
                else if (this.form.account_weight > 300) {
                    this.SignupValidation.SignupWeightResult = "重すぎです"
                    console.log(this.SignupValidation.SignupWeightResult)
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    SignWeight = false
                }
                else {
                    SignWeight = true
                }

                // 身長の入力フォームのバリデーション
                if (!this.form.account_height) {
                    this.SignupValidation.SignupHeightResult = "身長を入力してください"
                    console.log(this.SignupValidation.SignupHeightResult)
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    SignHeight = false
                }
                else if (!re2.test(this.form.account_height)) {
                    this.SignupValidation.SignupHeightResult = "数値以外の値、もしくは全角が含まれています"
                    console.log(this.SignupValidation.SignupHeightResult)
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    SignHeight = false
                }
                else if (this.form.account_height < 80) {
                    this.SignupValidation.SignupHeightResult = "低すぎです"
                    console.log(this.SignupValidation.SignupHeightResult)
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    SignHeight = false
                }
                else if (this.form.account_height > 300) {
                    this.SignupValidation.SignupHeightResult = "高すぎです"
                    console.log(this.SignupValidation.SignupHeightResult)
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    SignHeight = false
                }
                else {
                    SignHeight = true
                }

                // 氏名の入力フォームのバリデーション
                if (!this.form.account_level) {
                    this.SignupValidation.SignupLevelResult = "レベルを入力してください"
                    console.log(this.SignupValidation.SignupLevelResult)
                    this.errors.push(this.SignupValidation.SignupLevelResult)
                    SignLevel = false
                }else {
                    this.SignupValidation.SignupLevelResult = ""
                    SignLevel = true
                }

                //バリデーションをクリアした時にsign-up
                if (SignMail === true && SignPass === true && SignName === true
                    && SignBirthDay === true && SignWeight === true && SignHeight === true && SignLevel === true) {
                    const check = await this.Data_post(this.form)
                    if (check !== 0){
                        //登録時
                        this.$store.commit('tokenUpdate',check)
                        await this.$router.replace("/savecalorie")
                    }else {
                        //エラーや存在しなかった場合
                        console.log("アカウントが存在しないもしくわエラー")
                        alert("エラーが発生しました。もう一度やり直してください")
                    }
                }
                event.preventDefault();
            },
        },created() {
            //すでにトークンがある場合
            if (this.$store.state.accountToken) {
                this.$router.replace("/savecalorie")
            }
        }
    }
</script>