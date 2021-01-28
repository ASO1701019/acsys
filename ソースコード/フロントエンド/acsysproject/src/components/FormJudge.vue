<template>
  <!-- PoseNetモデルの読み込み -->
  <div id="app" class="container">
    <h1>デモ</h1>
    <p id='status'></p>
    <div class="container">
      <div class="dash-unit">

        <h2 class="a-spacing-none">回数</h2>
        <div class="count">
          <div id="disp_count">{{ count_value }}</div>
        </div>

        <h3>選択トレーニング</h3>
        <div id="training">
<!--          <Training v-on:select-category="this.selectCategory"/>-->
        </div>

        <div class="reset">
          <button id="btn_reset" @click="reset();">リセット</button>
          <div class="judge">
            <button class="btn btn-outline-success" @click="this.Data_post">終了</button>
          </div>
        </div>
        <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
        <video ref="video" id="video" width="500" height="500" autoplay></video>
      </div>
    </div>
  </div>

</template>

<script>
export default {
}
</script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/posenet"></script>

<script>
import p5 from 'p5'
import ml5 from 'ml5'
// import Training from '@/components/Training';

export default {

  data: function () {
    const post_data = {
      judge_ID: '',
      burned_ID: '',
      judge_rate: '',
      count_disp: document.getElementById("dips_count"),
    }
    return {
      video: {},
      posenet: '',
      poses: [],
      count_value: 0,
      should_count: true,
      count_disp: document.getElementById("dips_count"),
      reset_btn: document.getElementById("btn_reset"),
      keypoint: '',
      canvas: {},
    }
  },

  mounted() {
    //Webカメラ
    this.video = this.$refs.video
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        this.video.srcObject = stream
        this.video.play()
      })
    }

    //poseNetのセットアップ処理
    console.log("挙動確認")
    // this.video = p5.createCapture();
    this.posenet = ml5.poseNet(this.video,this.modelReady());
    let val=[];
    const ref = this;
    this.posenet.on('pose', function (results) {
      val = this.poses = results;
      ref.draw(val)
    })
  },
  methods: {
    selectCategory(value){
      },
    //canvasにVIDEOの内容を描画
    capture () {
      this.canvas = this.$refs.canvas
      this.canvas.getContext('2d').drawImage(this.video, 0, 0, 500, 500)
    },

    //poseNetのモデルが読み取られたか確認するメソッド
    modelReady: function () {
      console.log('モデルの読取に成功しました')
    },

    //回数をカウントするメソッド
    count: function () {
      this.count_value += 1;
      console.log(this.count_value);
      this.count_disp.innerHTML = this.count_value;
    },

    draw: function (poses) {
      this.poses = poses;
      console.log('描画を開始')
      if (this.poses.length > 0) {
        let pose = this.poses[0].pose;
        this.keypoint = pose.keypoints[0];
        for (let i = 0; i < this.poses.length; i++) {
          // poseが持つ情報を出力
          console.log('poseが持つ情報を出力します')
          let pose = this.poses[i].pose
          //本当は0.6以上だが挙動確認のため低い値に設定
          if (pose.score >= 0.3) {
            console.log("ok");
            //ユーザーが判定ラインより下にいった時
            //本当は250以上だが挙動確認のため低い値に設定
            if (pose.nose.y >= 220.0 && this.should_count) {
              console.log('カウントします')
              console.log(pose.nose.y);
              this.count_value += 1;
              this.should_count = false;
            } else if (pose.nose.y <= 240.0) {
              // 姿勢が元に戻った判定
              this.should_count = true;
            }
            if (this.count_value === 10) {
              document.getElementById('disp_count').style.color = "#FF0000";
            }
          }
        }
        this.drawSkeleton();
        this.drawKeypoints();
      }
      else {
        console.log('pose情報が見当たりません')
      }
    },

    drawKeypoints: function () {
      console.log('drawKeypoints起動')
      for (let i = 0; i < this.poses.length; i++) {
        let pose = this.poses[i].pose;
        for (let j = 0; j < pose.length; j++) {
          this.keypoint = pose.keypoints[j];
          if (this.keypoint > 0.2) {
            // シェイプの塗りに使用するカラーを設定
            this.keypoint.fill(color(0, 0, 255));
            // 線とシェイプの枠線の描画に使用するカラーを設定
            this.keypoint.stroke(20);
            this.keypoint.ellipse(this.keypoint.position.x, this.keypoint.position.y, 10, 10);
          }
        }
      }
    },

    drawSkeleton: function () {
      console.log('drawSkeleton起動')
      for (let i = 0; i < this.poses.length; i++) {
        let skeleton = this.poses[i].skeleton;
        for (let j = 0; j < skeleton.length; j++) {
          let partA = skeleton[j][0];
          let partB = skeleton[j][1];

          //骨格の線を引く
          this.canvas = this.$refs.canvas
          let ctx = this.canvas.getContext("2d");
          ctx.strokeStyle = "green";
        }
      }
    },

    //回数の値をリセットするメソッド
    reset: function () {
      console.log("リセットしました")
      this.count_value = 0;
    },
    //-------------------------データ保存処理--------------------------------------
    Data_post:async function (array) {
      const URL = "https://fat3lak1i2.execute-api.us-east-1.amazonaws.com/acsys/users/schedule/motion/judge"
      this.post_data = {
        // judgeRate: Number(this.$store.state.judge_rate), //判定結果（カウント値）
        add_date:Number(this.$store.state.add_date),
        motion_calorie: this.$store.state.motion_calorie,
        motion_name: this.$store.state.motion_name,
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
              this.$store.commit('judgeADD',check)
              this.$router.replace("/savecalorie")
            }else {
              console.log('form_judge:NG')
            }
          })
          .catch(function (error) {
            console.log(error)
          })
    }
  }
}

</script>
