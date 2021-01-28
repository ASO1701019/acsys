<template>
    <div id="app" class="container">
        <!--タイトル-->
        <div class="text-success pt-5  mb-3 text-center h1 font-weight-bold">
            acsys に新規登録
        </div>
        <form>
            <!--見出し-->
            <h4 class="text-success border-bottom border-success mb-4 mt-5 col-md-10 mx-auto">ユーザー情報</h4>
            <!--名前-->
            <span class="form-group row mx-auto">
                <label for="Name" class="col-md-3  col-form-label text-right col-auto">名前</label>
                <input type="text" class="col-md-6 col-auto form-control" id="Name" v-model="form.account_name" v-bind:class="{'is-invalid':!nameResult}">
                <span class="invalid-feedback text-center">{{SignupValidation.SignupNameResult}}</span>
                <span class="form-text text-muted col-md-11 text-md-center">
                    英字やカタカナ、ひらがな、漢字が使用できます
                </span>
            </span>

            <!--生年月日-->
            <div class="row form-group mx-auto mt-4" id="BirthDay">
                <span id="BirthDayTitle" class="col-md-3 col-form-label text-right col-auto mb-1">
                    生年月日
                </span>
                <!--日付選択-->
                <datepicker
                        v-model=form.account_birthday
                        :format="DatePickerFormat"
                        :language="ja"
                        :highlighted="highlighted"
                        :disabled-dates="disabledDates"
                        class="mt-1 col-md-7">
                </datepicker>
            </div>

            <!--性別 -->
            <div class="row mt-4">
                <label id="GenderTitle" class="col-md-3  col-form-label text-right col-3">性別</label>
                <div class="form-check mt-2 ml-3 col-md-2 col-auto">
                    <input class="form-check-input" type="radio" name="Gender" id="male" value="男性" v-model="form.account_gender" checked="checked">
                    <label class="form-check-label" for="male">男性</label>
                </div>
                <div class="form-check mt-2 col-md-2 col-auto">
                    <input class="form-check-input" type="radio" name="Gender" id="female" value="女性" v-model="form.account_gender">
                    <label class="form-check-label" for="female">女性</label>
                </div>
            </div>

            <!--見出し-->
            <h4 class="text-success border-bottom border-success mt-5 col-md-10 mx-auto">アカウント情報</h4>

            <!--メールアドレス -->
            <div class="form-group row mx-auto mt-5">
                <label for="MailAddress" class="col-md-3  col-form-label text-right col-auto">メールアドレス</label><br>
                <input type="email" class="col-md-7 col-auto form-control " id="MailAddress" v-model="form.account_address" v-bind:class="{'is-invalid':!mailResult}">
                <div class="invalid-feedback text-center">{{SignupValidation.SignupAddressResult}}</div>
            </div>

            <!--パスワード -->
            <div class="form-group row mx-auto mt-4">
                <label for="Password" class="col-md-3  col-form-label text-right col-auto">パスワード</label><br>
                <input type="password" class="col-md-7 col-auto form-control " id="Password" v-model="form.account_pass" v-bind:class="{'is-invalid':!passResult}"><br>
                <div class="invalid-feedback text-center">{{SignupValidation.SignupPasswordResult}}</div>
                <span class="form-text text-muted col-md-11 text-md-center">
                    6～128字の半角英数字で入力してください。大文字と小文字は区別されます。
                </span>
            </div>

            <!--見出し-->
            <h4 class="text-success border-bottom border-success mt-5 col-md-10 mx-auto">身体情報</h4>

            <!--身長 -->
            <div class="form-group row mx-auto mt-5">
                <label for="Height" class="col-md-3  col-form-label text-right col-auto">身長</label><br>
                <input type="number" class="col-md-7 col-auto form-control " id="Height" v-model="form.account_height" v-bind:class="{'is-invalid':!heightResult}"><br>
                <div class="invalid-feedback text-center">{{SignupValidation.SignupHeightResult}}</div>
            </div>

            <!--体重 -->
            <div class="form-group row mx-auto mt-4">
                <label for="BodyWeight" class="col-md-3  col-form-label text-right col-auto">体重</label><br>
                <input type="number" class="col-md-7 col-auto form-control" id="BodyWeight" v-model="form.account_weight" v-bind:class="{'is-invalid':!weightResult}"><br>
                <div class="invalid-feedback text-center">{{SignupValidation.SignupWeightResult}}</div>
            </div>

            <!--身体活動レベル -->
            <div id="ActiveLevel" class="form-group mt-4 mx-auto row">
                <label for="ActiveLevel" class="col-md-3  col-form-label text-right col-auto">身体活動レベル</label>
                <select name=”ActiveLevel” v-model="form.account_level"  class="col-md-7 col-auto form-control" v-bind:class="{'is-invalid':!levelResult}">
                    <option disabled value="">選択してください</option>
                    <option value=1>レベルⅠ</option>
                    <option value=2>レベルⅡ</option>
                    <option value=3>レベルⅢ</option>
                </select>
                <div class="invalid-feedback text-center">{{SignupValidation.SignupLevelResult}}</div>
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
                    <input class="form-check-input" type="radio" name="Purpose" id="down" value="減量" v-model="form.account_purpose" checked="checked">
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
    </div>
</template>

<script>
    import Datepicker from "vuejs-datepicker";
    import {ja} from 'vuejs-datepicker/dist/locale'

    const URL = 'https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users'
    export default {
        name: "test",
        components:{ Datepicker },
        data: function () {
            return {
                form: {
                    account_name: '',
                    account_height: '',
                    account_weight: '',
                    account_birthday: new Date(1990,0),
                    account_gender: '男性',
                    account_level: '',
                    account_address: '',
                    account_pass: '',
                    account_purpose:'減量',
                },
                post_data: [],
                errors:[],
                signupResult:false,
                //エラー枠表示
                nameResult:true,
                mailResult:true,
                passResult:true,
                heightResult:true,
                weightResult:true,
                levelResult:true,
                result:"",
                //カレンダー入力に使用
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
                //バリデーションエラー名
                SignupValidation: {
                    SignupNameResult: "",
                    SignupBirthdayResult: "",
                    SignupBirthdayYearResult: "",
                    SignupBirthdayMonthResult: "",
                    SignupBirthdayDayResult: "",
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
            //Topへスクロール
            scrollTop: function(){
                window.scrollTo({
                    top: 0,
                    behavior: "instant"
                })
            },
            //----------------------------データ保存---------------------------------------
            Data_post:async function (array) {

                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)

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
                    account_birthday: this.form.account_birthday.getFullYear() + ("0" + (this.form.account_birthday.getMonth() + 1)).slice(-2) +("0" + this.form.account_birthday.getDate()).slice(-2),
                    account_gender: array.account_gender,
                    account_level: array.account_level,
                    account_address: array.account_address,
                    account_pass: array.account_pass,
                    account_token:newToken,
                    account_purpos:array.account_purpose,
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
                            console.log('新期登録ng')
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                    })
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
                if (this.signupResult){
                    return newToken
                }else{
                    return 0
                }
            },
            //------------------------------------------------------------------------------

            //-----------------------------バリデーション-------------------------------------
            checkForm:async function (event) {
                this.errors.splice(-this.errors.length)
                let re1 = /^[A-Za-z0-9][A-Za-z0-9_.-]*@[A-Za-z0-9_.-]+\.[A-Za-z0-9]+$/
                let re3 = /^[A-Za-z0-9]+$/

                // 氏名の入力フォームのバリデーション
                if (!this.form.account_name) {
                    this.SignupValidation.SignupNameResult = "名前を入力してください"
                    console.log("名前未入力")
                    this.errors.push(this.SignupValidation.SignupNameResult)
                    this.nameResult = false
                }
                else if (!this.form.account_name.match(/^[a-zA-Zぁ-んァ-ヶー一-龠]+$/)) {
                    this.SignupValidation.SignupNameResult = "名前に使用できない文字が含まれています"
                    console.log("使用できない文字が含まれている")
                    this.errors.push(this.SignupValidation.SignupNameResult)
                    this.nameResult = false
                }
                else if (this.form.account_name.length >= 20) {
                    this.SignupValidation.SignupNameResult = "20文字以下で入力してください"
                    console.log("名前:文字数オーバー")
                    this.errors.push(this.SignupValidation.SignupNameResult)
                    this.nameResult = false
                } else {
                    this.nameResult  = true
                    this.SignupValidation.SignupNameResult = ""
                }

                //生年月日のバリデーション必要なし
                //性別のバリデーション必要なし

                // メールアドレスの入力フォームのバリデーション
                if (!this.form.account_address) {
                    this.SignupValidation.SignupAddressResult = "メールアドレスを入力してください"
                    console.log("メールアドレスを未入力")
                    this.mailResult = false
                }
                else if (!re1.test(this.form.account_address)){
                    this.SignupValidation.SignupAddressResult = "メールアドレスの形式で入力してください"
                    console.log("メールアドレスの形式ではない")
                    this.mailResult = false
                }
                else if (this.form.account_address.length >= 200) {
                    this.SignupValidation.SignupAddressResult = "200文字以下で入力してください"
                    console.log("メールアドレス文字数オーバー")
                    this.mailResult = false
                }
                else {
                    this.mailResult = true
                    this.SignupValidation.SignupAddressResult = ""
                }

                // パスワードの入力フォームのバリデーション
                if (!this.form.account_pass) {
                    this.SignupValidation.SignupPasswordResult = "パスワードを入力してください"
                    console.log("パスワード未入力")
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    this.passResult = false
                }
                else if (!re3.test(this.form.account_pass)) {
                    console.log("パスワードに使用できない文字が含まれています")
                    this.SignupValidation.SignupPasswordResult = "パスワードに使用できない文字が含まれています"
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    this.passResult = false
                }
                else if (this.form.account_pass.length < 6) {
                    this.SignupValidation.SignupPasswordResult = "6文字以上で入力してください"
                    console.log("パスワードが短すぎる")
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    this.passResult = false
                }
                else if (this.form.account_pass.length > 128) {
                    this.SignupValidation.SignupPasswordResult = "128文字以下で入力してください"
                    console.log("パスワードが長すぎる")
                    this.errors.push(this.SignupValidation.SignupPasswordResult)
                    this.passResult = false
                } else {
                    this.passResult = true
                    this.SignupValidation.SignupPasswordResult = ""
                }

                // 体重の入力フォームのバリデーション
                if (!this.form.account_weight) {
                    this.SignupValidation.SignupWeightResult = "体重を入力してください"
                    console.log("体重未入力")
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    this.weightResult = false
                }
                else if (this.form.account_weight < 15) {
                    this.SignupValidation.SignupWeightResult = "15kg以上で入力してください"
                    console.log("体重:規定値より小さい")
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    this.weightResult = false
                }
                else if (this.form.account_weight > 300) {
                    this.SignupValidation.SignupWeightResult = "300kg以下で入力してください"
                    console.log("体重:規定値より大きい")
                    this.errors.push(this.SignupValidation.SignupWeightResult)
                    this.weightResult = false
                }
                else {
                    this.weightResult = true
                    this.SignupValidation.SignupWeightResult = ""
                }

                // 身長の入力フォームのバリデーション
                if (!this.form.account_height) {
                    this.SignupValidation.SignupHeightResult = "身長を入力してください"
                    console.log("身長未入力")
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    this.heightResult = false
                }
                else if (this.form.account_height < 80) {
                    this.SignupValidation.SignupHeightResult = "80cm以上で入力してください"
                    console.log("身長：規定値より小さい")
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    this.heightResult = false
                }
                else if (this.form.account_height > 300) {
                    this.SignupValidation.SignupHeightResult = "300cm以下で入力してください"
                    console.log("身長：規定値より大きい")
                    this.errors.push(this.SignupValidation.SignupHeightResult)
                    this.heightResult = false
                }
                else {
                    this.heightResult = true
                    this.SignupValidation.SignupHeightResult = ""
                }

                // 身体活動レベルの入力フォームのバリデーション
                if (!this.form.account_level) {
                    this.SignupValidation.SignupLevelResult = "レベルを入力してください"
                    console.log(this.SignupValidation.SignupLevelResult)
                    this.errors.push(this.SignupValidation.SignupLevelResult)
                    this.levelResult = false
                }else {
                    this.SignupValidation.SignupLevelResult = ""
                    this.levelResult = true
                }

                //目的のバリデーション必要なし

                //バリデーションをクリアした時にsign-up
                console.log(this.errors)
                if (this.errors.length===0) {
                    const check = await this.Data_post(this.form)
                    if (check !== 0){
                        //登録時
                        this.$store.commit('tokenUpdate',check)
                        await this.$router.replace("/savecalorie")
                    }else {
                        //エラーが発生した場合
                        alert("新規登録に失敗しました。もう一度やり直してください")
                    }
                }else {
                    this.scrollTop()
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