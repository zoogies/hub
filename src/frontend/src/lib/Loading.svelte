<!-- TODO idk why this shit so broke -->
<div class="wrapper">
    <div class="spinner">.</div>
</div>

<style>
    .wrapper{
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px;
    }
    .spinner {
        width: 100%;
        height: 100%;
        max-width: 100px;
        max-height: 100px;
        border-radius: 50%;
        background: radial-gradient(farthest-side,#ffffff 94%,#0000) top/9px 9px no-repeat,
                conic-gradient(#0000 30%,#ffffff);
        -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 9px),#000 0);
        animation: spinner-c7wet2 1s infinite linear;
        }

        @keyframes spinner-c7wet2 {
        100% {
            transform: rotate(1turn);
        }
    }
</style>