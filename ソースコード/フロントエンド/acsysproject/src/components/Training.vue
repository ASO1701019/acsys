<template>
    <div class="container">
        <b-card no-body class="mt-3">
            <b-tabs card>
                <b-tab title="おすすめ" active>
                    <div class="row">
                        <div class="card mx-3 mx-auto" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title">2回で1200カロリー消費する脂肪燃焼 鬼ヒート:1200kcal FAT BURNING</h5>
                                <h6 class="card-subtitle mb-2 text-muted">みおの女子トレ部</h6>
                                <p class="card-text">動画時間20分15秒。20種類のエクササイズを組み合わせた運動です！とてもハードなので頑張っていきましょう。</p>
                                <button v-b-modal.modal-center1 class="btn btn-outline-success" @click="set1">挑戦してみる</button>
                            </div>
                        </div>
                        <div class="card mx-3 mx-auto" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title">【1日10分】時短で100kcal消費する『有酸素&筋トレ』</h5>
                                <h6 class="card-subtitle mb-2 text-muted">Keisuke Fitness</h6>
                                <p class="card-text">今回は10分で100kcal消費するメニューを紹介しました！</p>
                                <button v-b-modal.modal-center2 class="btn btn-outline-success" @click="set2">挑戦してみる</button>
                            </div>
                        </div>
                        <div class="card mx-3 mx-auto" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title">1回10分で500kcal消費する痩せ筋HIIT！自宅で簡単にカロリー消費する方法。【脂肪燃焼,FAT BURNING】</h5>
                                <h6 class="card-subtitle mb-2 text-muted">藤井筋トレチャンネル</h6>
                                <p class="card-text">動画時間17分。10分で500kcal消費できます！</p>
                                <button v-b-modal.modal-center3 class="btn btn-outline-success" @click="set3">挑戦してみる</button>
                            </div>
                        </div>
                    </div>
                </b-tab>
            </b-tabs>
        </b-card>

        <b-modal id="modal-center1" centered title="2回で1200カロリー消費する脂肪燃焼 鬼ヒート:1200kcal FAT BURNING">
            <b-embed
                    type="iframe"
                    aspect="16by9"
                    src="https://www.youtube.com/embed/ldz_t6UJt_I"
                    allowfullscreen></b-embed>

            <template v-slot:modal-footer="{cancel }">
                <b-button @click="cancel()">
                    Cancel
                </b-button>
                <b-button variant="success" @click="addTraining">
                    OK
                </b-button>
            </template>

        </b-modal>
        <b-modal id="modal-center2" centered title="【1日10分】時短で100kcal消費する『有酸素&筋トレ』">
            <b-embed
                    type="iframe"
                    aspect="16by9"
                    src="https://www.youtube.com/embed/Dj5EmkCK0gY"
                    allowfullscreen></b-embed>

            <template v-slot:modal-footer="{cancel }">
                <b-button @click="cancel()">
                    Cancel
                </b-button>
                <b-button variant="success" @click="addTraining">
                    OK
                </b-button>
            </template>
        </b-modal>
        <b-modal id="modal-center3" centered title="1回10分で500kcal消費する痩せ筋HIIT！自宅で簡単にカロリー消費する方法。【脂肪燃焼,FAT BURNING】">
            <b-embed
                    type="iframe"
                    aspect="16by9"
                    src="https://www.youtube.com/embed/ikmRh6WPVo0"
                    allowfullscreen></b-embed>
            <template v-slot:modal-footer="{cancel }">
                <b-button @click="cancel()">
                    Cancel
                </b-button>
                <b-button variant="success" @click="addTraining">
                    OK
                </b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
    export default {
        name: "Training",
        data(){
            return{
                title:"",
                calorie:"",
                day:"",
                addItem:[],
            }
        },methods:{
            set1(){
                this.title ="2回で1200カロリー消費する脂肪燃焼 鬼ヒート:1200kcal FAT BURNING"
                this.calorie = 1200
            },
            set2(){
                this.title ="【1日10分】時短で100kcal消費する『有酸素&筋トレ』"
                this.calorie = 100
            },
            set3(){
                this.title ="1回10分で500kcal消費する痩せ筋HIIT！自宅で簡単にカロリー消費する方法。【脂肪燃焼,FAT BURNING】"
                this.calorie = 100
            },
            addTraining:async function(){

                this.addItem.push({
                    add_date:Number(this.day),
                    motion_calorie: this.calorie,
                    motion_name: this.title,
                })

                const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/motion"

                this.trainingArray ={
                    'account_token':this.$store.state.accountToken,
                    'data':this.addItem
                }
                console.log(this.addItem)

                const json_data = JSON.stringify(this.trainingArray)
                await fetch(URL,{
                    mode:'cors',
                    method:'POST',
                    body:json_data,
                    headers:{'Content-type':'application'},
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data)
                        let check = data["isSuccess"]
                        if (check === true){
                            console.log("トレーニング登録:ok")
                            this.$router.replace("/savecalorie")
                        }else {
                            alert("エラーが発生しました。もう一度やり直してください")
                            console.log("トレーニング登録:ng")
                        }
                    })
                    .catch(function (error) {
                        console.log(error)
                        alert("エラーが発生しました。もう一度やり直してください")
                    })
            }
        },
        created() {
            let today = new Date()
            this.day = today.getFullYear() + ("0" + (today.getMonth() + 1)).slice(-2) +("0" +today.getDate()).slice(-2)
            console.log(this.day)
        }
    }
</script>