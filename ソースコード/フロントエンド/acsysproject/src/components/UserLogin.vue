<template>
    <div id="#app" class="container">
        <section>
            <div class="text-success pt-5 mb-4 text-center h1 font-weight-bold">
                acsys にログイン
            </div>
            <!--メールアドレスかパスワード間違っていた時のエラー表示-->
            <div v-if="!ErrorMessage" class="text-center h4 text-danger">
                メールアドレスかパスワードが間違っています
            </div>
            <form>
                <!--メールアドレスの入力-->
                <div class="form-group row mx-auto mt-5">
                    <label for="Mail" class="col-md-3  col-form-label text-right col-auto">メールアドレス</label><br>
                    <input type="email" class="col-md-7 col-auto form-control " id="Mail" v-model="loginForm.LoginMailAddress" v-bind:class="{'is-invalid':!mailResult}">
                    <div class="invalid-feedback text-center">{{loginValidation.loginMailResult }}</div>
                </div>

                <div class="form-group row mx-auto mt-4">
                    <label for="Pass" class="col-md-3  col-form-label text-right col-auto">パスワード</label><br>
                    <input type="password" class="col-md-7 col-auto form-control " id="Pass" v-model="loginForm.LoginPassword" v-bind:class="{'is-invalid':!passResult}"><br>
                    <div class="invalid-feedback text-center">{{loginValidation.loginPassResult}}</div>
                </div>

                <!--ログインボタン-->
                <div class="col text-center">
                    <button v-on:click="checkFrom" class="btn btn-success btn-lg mx-auto col-lg-6 col-md-8 mt-4">ログイン</button>
                </div>
            </form>

            <!--新規登録リンク-->
            <div class="text-center mt-3" >
                <router-link to="/signup" class="h5 text-success">アカウントの新規作成</router-link>
            </div>

            <!--パスワード再発行リンク-->
            <div class="text-center mt-3" >
                <router-link to="/repassword" class="h5 text-success">パスワードを<br>忘れてしまった方はこちら</router-link>
            </div>

        </section>
    </div>
</template>

<script>

    export default {

        data(){
            return{
                //入力用の値
                loginForm:{
                    LoginMailAddress : "",
                    LoginPassword:"",
                },
                //エラー表示用の値
                ErrorMessage:true,
                loginValidation:{
                    loginMailResult: "",
                    loginPassResult:"",
                },
                //通信時使用
                loginArray:[],
                loginResult:false,
                //フォームに使用
                mailResult:true,
                passResult:true,
            }
        },
        methods:{
            getLogin:async function (mail,pass) {

                //ローディングアニメーションを起動
                this.$store.commit("setLoading", true)

                //トークン生成
                // 生成する文字列の長さ
                const l = 32;
                // 生成する文字列に含める文字セット
                const c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
                const cl = c.length;
                let newToken = "";
                for(let i=0; i<l; i++){
                    newToken += c[Math.floor(Math.random()*cl)];
                }

                // ここでAPIに送信
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/login"
                this.loginArray={
                    account_address:mail,
                    account_pass:pass,
                    account_token:newToken,
                }
                const json_data = JSON.stringify(this.loginArray)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(function (response) {
                        return response.json()
                    })
                    .then(data => {
                        const flg_data = data['isSuccess']
                        if(flg_data){
                            console.log('ログインok')
                            this.loginResult = true
                        }else {
                            console.log('ログインng')
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                    })
                //ローディングアニメーションを終了
                this.$store.commit("setLoading", false)
                if (this.loginResult){
                    return newToken
                }else{
                    return 0
                }
            },

            login:async function () {
                //バリデーション
                if (this.loginValidEmail(this.loginForm.LoginMailAddress) && this.loginValidPass(this.loginForm.LoginPassword)){
                    const check = await this.getLogin(this.loginForm.LoginMailAddress, this.loginForm.LoginPassword);
                    if (check !== 0){
                        //ユーザーが存在時
                        this.$store.commit('tokenUpdate',check)
                        await this.$router.replace("/savecalorie")
                    }else {
                        //エラーや存在しなかった場合
                        console.log("アカウントが存在しないもしくわエラー")
                        this.ErrorMessage = false
                    }
                }else {
                    // バリデーションにはじかれた場合
                    this.ErrorMessage = false
                }
            },

            checkFrom: function(event){
                let LoginMail = false
                let LoginPass = false

                //メールアドレスの入力フォームのバリデーション
                if (!this.loginForm.LoginMailAddress) {
                    this.loginValidation.loginMailResult="メールアドレスを入力してください"
                    console.log("メールアドレスの文字が入力されていない")
                    this.mailResult = false
                }else {
                    this.loginValidation.loginMailResult=""
                    LoginMail = true
                    this.mailResult = true
                }

                //パスワードの入力フォームのバリデーション
                if (!this.loginForm.LoginPassword) {
                    this.loginValidation.loginPassResult="パスワードを入力してください"
                    console.log("パスワードの文字が入力されていない")
                    this.passResult = false
                }else {
                    this.loginValidation.loginPassResult=""
                    LoginPass = true
                    this.passResult = true
                }

                //両方trueの時に実行。loginを呼び出す
                if(LoginMail === true && LoginPass === true){
                    this.loginValidation.loginMailResult=""
                    this.loginValidation.loginPassResult=""
                    this.login()
                }
                event.preventDefault()
            },

            //メールアドレスの厳格なバリデーション
            loginValidEmail: function (email) {
                let ValidateEmail = true
                let re = /^[A-Za-z0-9][A-Za-z0-9_.-]*@[A-Za-z0-9_.-]+\.[A-Za-z0-9]+$/
                if (!re.test(email)){
                    ValidateEmail = false
                    console.log("メールアドレスに使用できない文字が含まれているもしくわ形式が違う")
                }
                if (email.length >= 200){
                    ValidateEmail = false
                    console.log("メールアドレスの文字数オーバー")
                }
                return ValidateEmail
            },

            //パスワードの厳格なバリデーション
            loginValidPass: function (pass) {
                let ValidatePassword = true
                let re = /^[A-Za-z0-9]+$/
                if (!re.test(pass)){
                    ValidatePassword = false
                    console.log("パスワードに使用できない文字が含まれています")
                }
                if (pass.length >= 128 || pass.length <= 5){
                    ValidatePassword = false;
                    console.log("パスワードの文字数が足りないもしくわ多い")
                }
                return ValidatePassword
            },
        },
        created: function () {
            //すでにトークンがある場合
            if (this.$store.state.accountToken) {
                this.$router.replace("/savecalorie")
            }
        },
    }</script>