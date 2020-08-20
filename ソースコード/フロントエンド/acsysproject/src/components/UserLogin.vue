<template>
    <div id="#app" class="container">
        <section>
            <div class="text-success mt-5 mb-4 text-center h1 font-weight-bold">
                acsys にログイン
            </div>
            <div v-if="!ErrorMessage" class="text-center h3 text-danger">
                メールアドレスかパスワードが間違っています
            </div>
            <form>
                <div class="form-group mx-auto">
                    <label for="Mail"></label>
                    <input type="email" id="Mail" placeholder="メールアドレス" v-model="loginForm.LoginMailAddress" class="form-control col-lg-6 col-md-8 mx-auto">
                    <p class="text-danger text-center h5">
                        {{ loginValidation.loginMailResult }}
                    </p>
                </div>
                <div class="form-group">
                    <label for="Pass"></label>
                    <input type="Password" id="Pass" placeholder="パスワード" v-model="loginForm.LoginPassword" class="form-control col-lg-6 col-md-8 mt-1 mx-auto">
                    <p class="text-danger text-center h5">
                        {{ loginValidation.loginPassResult }}
                    </p>
                </div>
                <div class="col text-center">
                    <button v-on:click="checkFrom" class="btn btn-success btn-lg mx-auto col-lg-6 col-md-8 mt-4">ログイン</button>
                </div>
            </form>
            <div class="text-center mt-3" >
                <router-link to="/signup" class="h5 text-success">アカウントの新規作成</router-link>
            </div>
        </section>
    </div>
</template>

<script>

    export default {

        data(){
            return{
                loginForm:{
                    LoginMailAddress : "",
                    LoginPassword:"",
                },
                ErrorMessage:true,
                loginValidation:{
                    loginMailResult: "",
                    loginPassResult:"",
                },
                loginArray:[],
                loginResult:false,
            }
        },
        methods:{

            getLogin:async function (mail,pass) {

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
                        alert("エラーが発生しました。もう一度やり直してください")
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
                }else {
                    this.loginValidation.loginMailResult=""
                    LoginMail = true
                }

                //パスワードの入力フォームのバリデーション
                if (!this.loginForm.LoginPassword) {
                    this.loginValidation.loginPassResult="パスワードを入力してください"
                    console.log("パスワードの文字が入力されていない")
                }else {
                    this.loginValidation.loginPassResult=""
                    LoginPass = true
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