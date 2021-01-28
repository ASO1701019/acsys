<template>
    <div id="twitter_share" class="container">
        <div class="text-success mt-4 mb-4 text-center h2 font-weight-bold">
            Twitterにシェア
        </div>
        <form>
            <div>
                <span class="form-group row mx-auto">
                    <label for="detail" class="col-sm-3  col-form-label text-right col-auto" >SNSで共有する内容</label>
                    <textarea class="col-sm-9 col-auto form-control ml-xs-5 " id="detail" rows="5" maxlength="280" v-model="TweetDetail"></textarea>
                </span>
            </div>
            <div class="form-group col text-center">
                <button class="btn btn-success btn-lg mx-auto col-md-offset-3 mt-4 " @click="twitterShare">ツイッターでシェアする</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "Share",
        data() {
            return {
                // HashTag: "",
                TweetDetail: "今までの貯金:" + this.$store.state.calorie+"kcal\n" + "今日の記録\n摂取カロリー:" + + this.$store.state.intakeCalorie
                    +"kcal\n消費カロリー:" + this.$store.state.consumptionCalorie + "kcal\n",
                HashTag: "",
            }
        },methods:{
            twitterShare(){
                this.TweetDetail = this.TweetDetail.replace(/\r?\n/g,"%0a")
                console.log(this.TweetDetail)
                //シェアするためのtwitterの画面を設定（textareaに記載された内容付きで）
                let shareURL = 'https://twitter.com/intent/tweet?text=' + this.TweetDetail + "%20%23acsys" ;
                //シェア用の画面へ移行
                window.open(shareURL,null,'left=350,top=200,width=700,height=550')
                // location.href = shareURL
                // this.$router.replace("/savecalorie")
            },
        }
    }
</script>
