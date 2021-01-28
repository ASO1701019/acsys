<template>
    <div class="container">
        <div class="text-success pt-5 mb-4 text-center h1 font-weight-bold">
            パスワード再発行
        </div>
        <form>
        <!--メールアドレスの入力-->
            <div class="form-group row mx-auto mt-5">
                <label for="Mail" class="col-md-3  col-form-label text-right col-auto">メールアドレス</label><br>
                <input type="email" class="col-md-7 col-auto form-control " id="Mail" v-model="sendMail" v-bind:class="{'is-invalid':!sendMailResult}">
                <div class="invalid-feedback text-center">{{mailValidation}}</div>
            </div>
        </form>
        <!--決定ボタン-->
        <div class="col text-center">
            <button v-on:click="checkMail" class="btn btn-success btn-lg mx-auto col-lg-6 col-md-8 mt-4">送信</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "RePassword",
        data(){
            return{
                sendMail:"",
                sendMailResult:true,
                mailValidation:"",
                sendArray:[],
                dataBox:[],
            }
        },
        methods:{
            checkMail:async function () {
                let re1 = /^[A-Za-z0-9][A-Za-z0-9_.-]*@[A-Za-z0-9_.-]+\.[A-Za-z0-9]+$/
                // メールアドレスの入力フォームのバリデーション
                if (!this.sendMail) {
                    this.mailValidation = "メールアドレスを入力してください"
                    console.log("メールアドレスを未入力")
                    this.sendMailResult = false
                }
                else if (!re1.test(this.sendMail)){
                    this.mailValidation = "メールアドレスの形式で入力してください"
                    console.log("メールアドレスの形式ではない")
                    this.sendMailResult = false
                }
                else if (this.sendMail.length >= 200) {
                    this.mailValidation = "200文字以下で入力してください"
                    console.log("メールアドレス文字数オーバー")
                    this.sendMailResult = false
                }
                else {
                    this.sendMailResult = true
                    this.mailValidation = ""
                }
                if (this.sendMailResult === true){
                    //ローディングアニメーションを起動
                    this.$store.commit("setLoading", true)
                    // ここでAPIに送信
                    const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/pass/forget"
                    this.sendArray={
                        to_address:this.sendMail,
                    }
                    const json_data = JSON.stringify(this.sendArray)
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
                            this.dataBox = data
                            console.log("送信成功")
                            alert("メールの送信完了しました！メールボックスを確認してください。")
                        })
                        .catch(function (error) {
                            alert("エラーが発生しました。もう一度やり直してください")
                            console.log(error)
                        })
                    //ローディングアニメーションを終了
                    this.$store.commit("setLoading", false)
                }
            }
        }
    }
</script>

<style scoped>

</style>