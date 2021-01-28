<template>
    <div class="container">
        <div class="text-success mt-5 mb-3 text-center h1 font-weight-bold">
            パスワード変更
        </div>
        <form>
            <!--パスワード -->
            <div class="form-group row mx-auto mt-5">
                <label for="OldPass" class="col-md-3  col-form-label text-right col-auto">現在のパスワード</label><br>
                <input type="password" class="col-md-7 col-auto form-control " id="OldPass" v-model="form.account_old_pass" v-bind:class="{'is-invalid':!oldPassBoolean}"><br>
                <div class="invalid-feedback text-center">{{OldPasswordResult}}</div>
            </div>
            <!--新しいパスワード -->
            <div class="form-group row mx-auto mt-4">
                <label for="NewPass" class="col-md-3  col-form-label text-right col-auto">新しいパスワード</label><br>
                <input type="password" class="col-md-7 col-auto form-control " id="NewPass" v-model="form.account_new_pass" v-bind:class="{'is-invalid':!newPassBoolean}"><br>
                <div class="invalid-feedback text-center">{{NewPasswordResult}}</div>
                <span class="form-text text-muted col-md-11 text-md-center">
                    6～128字の半角英数字で入力してください。大文字と小文字は区別されます。
                </span>
            </div>
            <!--新しいパスワード確認 -->
            <div class="form-group row mx-auto mt-4">
                <label for="ConNewPass" class="col-md-3  col-form-label text-right col-auto">パスワード確認</label><br>
                <input type="password" class="col-md-7 col-auto form-control " id="ConNewPass" v-model="form.account_con_new_pass" v-bind:class="{'is-invalid':!conNewPassBoolean}"><br>
                <div class="invalid-feedback text-center">{{ConNewPasswordResult}}</div>
                <span class="form-text text-muted col-md-11 text-md-center">
                    新しいパスワードで入力したものを、もう一度入力してください。
                </span>
            </div>
        </form>
        <div class="row mt-5 md-5">
            <button id="password_decision" class="btn btn-success col-8 mx-auto" @click="checkHandler(form,$event)">決定</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "PasswordChange",
        data: function () {
            return{
                form: {
                    account_pass: "",
                    account_old_pass: "",
                    account_new_pass: "",
                    account_con_new_pass: "",
                },
                //バリデーション結果
                OldPasswordResult: "",
                NewPasswordResult: "",
                ConNewPasswordResult: "",
                oldPassBoolean:true,
                newPassBoolean:true,
                conNewPassBoolean:true,
            }
        },methods: {
            checkHandler: function (form, event) {
                this.checkForm(event);
            },
            //-----------------------------バリデーション-------------------------------------
            checkForm: async function(event) {
                let re3 = /^[A-Za-z0-9]+$/

                // 現在パスワードの入力フォームのバリデーション
                if (!this.form.account_old_pass) {
                    this.OldPasswordResult = "パスワードを入力してください"
                    console.log("現在のパスワード未入力")
                    this.oldPassBoolean = false
                }
                else if (this.form.account_old_pass.length < 6) {
                    this.OldPasswordResult = "6文字以上で入力してください"
                    console.log("現在のパスワードが短すぎる")
                    this.oldPassBoolean = false
                }
                else if (this.form.account_old_pass.length > 128) {
                    this.OldPasswordResult = "128文字以下で入力してください"
                    console.log("現在のパスワードが長すぎる")
                    this.oldPassBoolean = false
                } else {
                    this.oldPassBoolean = true
                    this.OldPasswordResult = ""
                }
                // 新パスワードの入力フォームのバリデーション
                if (!this.form.account_new_pass) {
                    this.NewPasswordResult = "新しいパスワードを入力してください"
                    console.log("新パスワード未入力")
                    this.newPassBoolean = false
                }
                else if (!re3.test(this.form.account_new_pass)) {
                    console.log("新パスワードに使用できない文字が含まれています")
                    this.NewPasswordResult = "パスワードに使用できない文字が含まれています"
                    this.newPassBoolean = false
                }
                else if(this.form.account_old_pass === this.form.account_new_pass){
                    this.NewPasswordResult = "前のパスワードと別のパスワードを入力してください"
                    this.newPassBoolean = false
                }
                else if (this.form.account_new_pass.length < 6) {
                    this.NewPasswordResult = "6文字以上で入力してください"
                    console.log("新パスワードが短すぎる")
                    this.newPassBoolean = false
                }
                else if (this.form.account_new_pass.length > 128) {
                    this.NewPasswordResult = "128文字以下で入力してください"
                    console.log("新パスワードが長すぎる")
                    this.newPassBoolean = false
                } else {
                    this.newPassBoolean = true
                    this.NewPasswordResult = ""
                }

                // 新しいパスワード確認のバリデーション
                if(!this.form.account_con_new_pass){
                    this.ConNewPasswordResult = "もう一度入力してください"
                    this.conNewPassBoolean= false
                }
                else if(this.form.account_new_pass !== this.form.account_con_new_pass){
                    this.ConNewPasswordResult = "新しいパスワードとパスワード確認が一致しません"
                    this.conNewPassBoolean = false
                    this.newPassBoolean = false
                }else{
                    this.conNewPassBoolean = true
                    this.ConNewPasswordResult = ""
                }

                // バリデーションをクリアした時にパスワード更新
                if(this.oldPassBoolean === true && this.newPassBoolean === true && this.conNewPassBoolean === true){

                    //ローディングアニメーションを起動
                    this.$store.commit("setLoading", true)

                    // APIと通信
                    const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/pass/change"
                    const post_data={
                        account_token:this.$store.state.accountToken,
                        current_pass:this.form.account_old_pass,
                        new_pass:this.form.account_new_pass,
                    }
                    const json_data = JSON.stringify(post_data)
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
                            //ローディングアニメーションを終了
                            this.$store.commit("setLoading", false)
                            if(flg_data){
                                console.log('パスワード変更ok')
                                //topへ
                                this.$router.replace("/savecalorie")
                            }else {
                                console.log('パスワード変更ng')
                                //パスワードが違う
                                alert("入力されたパスワードが間違っています")
                            }
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                }
                event.preventDefault();
            },
        }
    }
</script>