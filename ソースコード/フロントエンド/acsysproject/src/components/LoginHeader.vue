<template>
    <div >
        <b-navbar toggleable="lg" variant="dark" type="dark">
            <a class="navbar-brand " href='/#/savecalorie'>
                <img src="../../public/favicon.png" width="35" height="35" class="d-inline-block align-top" alt="penguin">
                acsys</a>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                        <b-nav-item href="/#/calendar">カレンダー</b-nav-item>
                        <b-nav-item href="/#/statistics">統計</b-nav-item>
                        <b-nav-item href="/#/training">トレーニング</b-nav-item>
                </b-navbar-nav>

                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                        <template v-slot:button-content>
                            <em>{{userName}}</em>
<!--                            Apiで名前の取得-->
                        </template>
                        <b-dropdown-item href="/#/userchange">登録情報の変更</b-dropdown-item>
                        <b-dropdown-item @click="openModal">ログアウト</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>

            </b-collapse>
        </b-navbar>


        <div class="example-modal-window">
            <!-- コンポーネント MyModal -->
            <MyModal @close="closeModal" v-if="modal">
                <!-- default スロットコンテンツ -->
                <h3><span class="text-danger">ログアウト</span>しますか？</h3>
                <!-- /default -->
                <!-- footer スロットコンテンツ -->
                <template slot="footer">
                    <button class="btn btn-outline-dark" @click="closeModal">キャンセル</button>
                    <button class="btn btn-outline-danger" @click="logout">ログアウト</button>
                </template>
                <!-- /footer -->
            </MyModal>
        </div>
    </div>
</template>

<script>

    import MyModal from './MyModal'

    export default {
        components: { MyModal },
        data() {
            return {
                modal: false,
                //通信に関数
                dataGet:[],
                userToken:this.$store.state.accountToken,
                userInfBox:[],
            }
        },
        async created() {
            const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/information"
            this.dataGet={
                account_token:this.userToken
            }
            const json_data = JSON.stringify(this.dataGet)
            await fetch(URL,{
                mode:'cors',
                method:'POST',
                body:json_data,
                headers:{'Content-type':'application'},
            })
                .then(response => response.json())
                .then(data => {
                    // console.log(data)
                    const flg_data = data['isSuccess']
                    if(flg_data){
                        console.log('ユーザー情報取得:ok')
                        this.userInfBox={
                            name:data['account_name'],
                            birthday:data['account_birthday'],
                            gender:data['account_gender'],
                            height:data['account_height'],
                            weight:data['account_weight'],
                            activlevel:data['account_level'],
                            startday:data['regist_date']
                        }
                        this.$store.commit('accountUpdate',this.userInfBox)
                    }else {
                        console.log('ユーザー情報取得:ng')
                    }
                })
                .catch(function (error) {
                    console.log(error)
                    alert("エラーが発生しました。もう一度やり直してください")
                })
        },
        methods:{
            openModal(){
                this.modal = true
            },
            closeModal() {
                this.modal = false
            },
            logout(){
                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/logout"
                this.dataGet={
                    account_token:this.userToken
                }
                const json_data = JSON.stringify(this.dataGet)
                fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        // console.log(data)
                        const flg_data = data['isSuccess']
                        if(flg_data){
                            console.log('ログアウト:ok')
                            this.$store.commit("tokenDelete")
                            this.$router.replace("/")
                        }else {
                            console.log('ログアウト:ng')
                            alert("エラーが発生しました。もう一度やり直してください")
                        }
                    })
            },
        },
        computed:{
            userName:function () {
                return this.$store.state.accountName
            }
        },
        watch:{

        }
    }
</script>
