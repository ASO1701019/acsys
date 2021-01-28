<template>
    <div class="container">
        <!-- 姿勢判定機能リンク -->
        <div class="text-success pt-5  mb-3 text-center h1 font-weight-bold">
            回数カウント(デモ版)
        </div>
        <div class="text-success pt-5  mb-3 text-center text-danger h5 font-weight-bold">
            （注意）デモ版と書いてある通り、まだ完成してないです。そのためおかしい動作があります。<br>
            又カメラを使用するため、動作が重たいです。
        </div>
        <div class="row mt-5">
            <label class="col-lg-3 col-auto col-form-label" >トレーニング名</label>
            <select v-bind:key="form.id" name=”TrainingDetail” v-model="form.training_detail"  class="form-control col-sm-7 text-left">
                <option value=1 selected="selected" >スクワット</option>
                <option value=2>腕立て伏せ</option>
                <option value=3>腹筋</option>
            </select>
        </div>

        <div class="row mt-5 mb-5">
            <button id="send_btn" class="btn btn-success col-7 mx-auto"  @click="new SendData(form.id)">決定</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CountTraining",
        data(){
            return{
                selectedCategory:'',
                categories:[
                    {id:1,name:'スクワット'},
                    {id:2,name:'腕立て伏せ'},
                    {id:3,name:'腹筋'},
                ],
                form: {
                    training_detail: '',
                },
            }
        },
        methods:{
            SendData(EventId){
                let EventLink = {name:'formjudge',EventLink:EventId}
                this.$router.push(EventLink).catch(() => {})
            },
        },
    }
</script>

<style scoped>

</style>