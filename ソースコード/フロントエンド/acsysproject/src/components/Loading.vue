<template>
    <div class="loading" v-show="$store.state.loading">
        <div class="overlay" :style="overlayPosition">
            <div class="spinner-border text-light" role="status">
                <span class="sr-only">Loading...</span>
            </div>
            <div class="message-box mt-4 ml-3 h5">
                <p>通信中...</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                overlayPosition: {
                    top: "0"
                }
            };
        },
        watch: {
            "$store.state.loading": function(newVal) {
                // スクロールされていても表示領域いっぱいに
                // オーバレイが表示されるように高さを調整する
                if (newVal) {
                    this.overlayPosition.top = window.pageYOffset + "px";
                }
            }
        }
    };
</script>

<style>
    .overlay {
        background-color: rgba(0, 0, 0, 0.75);
        /* 画面いっぱいに広げる */
        position: absolute;
        height: 100vh;
        width: 100vw;
        left: 0;
        top: 0;
        /* 子要素を上下左右に中央寄せ */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .message-box {
        color: #fff;
        animation-name: blink;
        animation-duration: 600ms;
        animation-timing-function: ease-in-out;
        animation-direction: alternate;
        animation-iteration-count: infinite;
    }

    @keyframes blink {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
