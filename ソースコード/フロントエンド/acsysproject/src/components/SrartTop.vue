<template>
    <div id="#app">
        <div class="jumbotron-extend">
            <div class="container-fluid jumbotron-container">
                <h1>カロリーを管理してみませんか？</h1>
                <p><a class="btn btn-outline-warning btn-lg" href="/#/signup" role="button">新規登録はこちら</a></p>
            </div>
        </div>
    </div>
</template>

<style scoped>

    .jumbotron-extend {
        position: relative;
        height: 91.3vh;
        min-height: 300px;
        background: url(../assets/StartTopImage.jpg) no-repeat center center;
        background-size: cover;
        color: white;
    }

    .jumbotron-container {
        position: relative;
        top: 50%;
        transform: translateY(-50%);
    }

    #StartUp{
        position: relative;
        top: 10px;
    }

</style>