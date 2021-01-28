<template>
    <div id="#app">
        <div class="jumbotron jumbotron-fluid bg-dark">
            <div class="container text-center">
                <h1 class="display-1 font-weight-lighter" style="font-family: Helvetica,'Yu Gothic UI',serif">acsys</h1>
                <h3 class= "font-weight-lighter" style="font-family: Helvetica,'Yu Gothic UI',serif">-簡単にカロリー貯金-</h3>
                <hr class="my-4" style="background-color: white">
                <div class="row">
                    <div class="col text-right">
                        <p><a class="btn btn-success btn-lg" href="/login" role="button">ログイン</a></p>
                    </div>
                    <div class="col text-left">
                        <p><a class="btn btn-info btn-lg" href="/signup" role="button">無料登録</a></p>
                    </div>
                </div><!-- /.row -->
            </div><!-- /.container -->
        </div><!-- /.jumbotron -->

        <div class="container marketing">
            <h2 class="text-center pt-4">カロリー管理を簡単に</h2>
            <div class="row pt-5">
                <div class="col-lg-4">
                    <div class="text-center mb-1">
                        <svg width="64" height="64" viewBox="0 0 16 16" class="bi bi-display" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5.75 13.5c.167-.333.25-.833.25-1.5h4c0 .667.083 1.167.25 1.5H11a.5.5 0 0 1 0 1H5a.5.5 0 0 1 0-1h.75z"/>
                            <path fill-rule="evenodd" d="M13.991 3H2c-.325 0-.502.078-.602.145a.758.758 0 0 0-.254.302A1.46 1.46 0 0 0 1 4.01V10c0 .325.078.502.145.602.07.105.17.188.302.254a1.464 1.464 0 0 0 .538.143L2.01 11H14c.325 0 .502-.078.602-.145a.758.758 0 0 0 .254-.302 1.464 1.464 0 0 0 .143-.538L15 9.99V4c0-.325-.078-.502-.145-.602a.757.757 0 0 0-.302-.254A1.46 1.46 0 0 0 13.99 3zM14 2H2C0 2 0 4 0 4v6c0 2 2 2 2 2h12c2 0 2-2 2-2V4c0-2-2-2-2-2z"/>
                        </svg>
                    </div><!-- /.text-center -->
                    <h5 class="pb-2 pt-1 font-weight-bold">場所やデバイスを問わず</h5>
                    <p>Webアプリのため、どこでも利用出来ます。</p>
                </div><!-- /.col-lg-4 -->
                <div class="col-lg-4">
                    <div class="text-center mb-1">
                        <svg width="64" height="64" viewBox="0 0 16 16" class="bi bi-bar-chart-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <rect width="4" height="5" x="1" y="10" rx="1"/>
                            <rect width="4" height="9" x="6" y="6" rx="1"/>
                            <rect width="4" height="14" x="11" y="1" rx="1"/>
                        </svg>
                    </div><!-- /.text-center -->
                    <h5 class="pb-2 pt-1 font-weight-bold">直感的にカロリー管理</h5>
                    <p>グラフで日や月のカロリー情報を表示しているため、現在の状況をすぐ理解できます。</p>
                </div><!-- /.col-lg-4 -->
                <div class="col-lg-4">
                    <div class="text-center mb-1">
                        <svg width="64" height="64" viewBox="0 0 16 16" class="bi bi-bicycle" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M4 4.5a.5.5 0 0 1 .5-.5H6a.5.5 0 0 1 0 1v.5h4.14l.386-1.158A.5.5 0 0 1 11 4h1a.5.5 0 0 1 0 1h-.64l-.311.935.807 1.29a3 3 0 1 1-.848.53l-.508-.812-2.076 3.322A.5.5 0 0 1 8 10.5H5.959a3 3 0 1 1-1.815-3.274L5 5.856V5h-.5a.5.5 0 0 1-.5-.5zm1.5 2.443l-.508.814c.5.444.85 1.054.967 1.743h1.139L5.5 6.943zM8 9.057L9.598 6.5H6.402L8 9.057zM4.937 9.5a1.997 1.997 0 0 0-.487-.877l-.548.877h1.035zM3.603 8.092A2 2 0 1 0 4.937 10.5H3a.5.5 0 0 1-.424-.765l1.027-1.643zm7.947.53a2 2 0 1 0 .848-.53l1.026 1.643a.5.5 0 1 1-.848.53L11.55 8.623z"/>
                        </svg>
                    </div><!-- /.text-center -->
                    <h5 class="pb-2 pt-1 font-weight-bold">おすすめトレーニング</h5>
                    <p>色々なトレーニングを紹介しています。トレーニングを達成すると自動的に登録されます。</p>
                </div><!-- /.col-lg-4 -->
            </div><!-- /.row -->

            <div class="row">
                <div class="col-lg-4">
                    <div class="text-center mb-1">
                        <img src="../assets/Twitter_Logo_Blue.png" class="img-fluid" alt="Responsive image" width="76" height="76">
                    </div><!-- /.text-center -->
                    <h5 class="pb-2 pt-1 font-weight-bold"> Twitterに簡単共有</h5>
                    <p>今までの貯金、今日のカロリーが自動で入力されるため簡単にツイートできます。</p>
                </div><!-- /.col-lg-4 -->
                <div class="col-lg-4">
                    <div class="text-center mb-1">
                        <svg width="64" height="64" viewBox="0 0 16 16" class="bi bi-emoji-smile" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                            <path fill-rule="evenodd" d="M4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683z"/>
                            <path d="M7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5z"/>
                        </svg>
                    </div><!-- /.text-center -->
                    <h5 class="pb-2 pt-1 font-weight-bold"> 完全フリー</h5>
                    <p>卒業制作なので広告なし、利用無料です。</p>
                </div><!-- /.col-lg-4 -->
            </div><!-- /.row -->

            <hr class="featurette-divider  mt-5 pb-5">

            <div class="row featurette">
                <div class="col-md-6">
                    <h2 class="featurette-heading">シンプルなデザイン<span class="text-muted"><br> 直感的に操作できる。</span></h2>
                    <p class="lead">画像に表示されているのは、カロリー貯金画面です。視覚的にわかりやすいようにグラフやカレンダーを使用しています。スマートフォンでも同じように扱えます。</p>
                </div>
                <div class="col-md-6">
                    <img src="../assets/topPage.png" class="img-fluid" alt="Responsive image">
                </div>
            </div><!-- /.row featurette -->
            <hr class="featurette-divider  mt-5">
        </div><!-- /.container -->
        <footer class="container">
            <div class="text-center">
                <div class="sosyal">
                    <a href="https://twitter.com/acsys_calorie" class="twitter">acsys公式Twitter</a>
                </div>
            </div>
            <p>2020 麻生ビジネス専門学校情報工学科2班<br>
                お問い合わせ:1701017@st.asojuku.ac.jp</p>
            <p class="float-right"><button class="btn btn-outline-success" @click="scrollTop()">トップに戻る</button></p>
        </footer><!-- /.footer -->
    </div>
</template>

<script>
    export default {
        name: "StartTop",
        methods:{
            scrollTop: function(){
                window.scrollTo({
                    top: 0,
                    behavior: "instant"
                })
            },
        }
    }
</script>

<style scoped>
    .jumbotron {
        background-image: url("../assets/3275593_m.jpg");
        background-size: cover;
        background-position: center 60%;
        color: #ffffff;
    }
    .sosyal {
        margin: 50px auto;
    }
    .twitter {
        background-color: #008DDE;
        box-shadow: 0 4px 0 #0078BD;

        display: inline;
        position: relative;
        font-family: Arial;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        color: white;
        border-radius: 5px;
        padding: 14px 80px;
    }
    .twitter:active {
        top: 2px;
        box-shadow: 0 2px 0 #0078BD;
    }
    .twitter:hover {
        background-color: #1397D8;
    }
</style>