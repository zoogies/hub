<script>
import App from "../App.svelte";

    var loaded = false;
</script>

<div class="wrapper">
    {#if !loaded}
        <div class="spinner"></div>
    {:else}
        <p>loaded</p>
    {/if}
</div>

<style>
    .wrapper{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-content: center;
        align-items: center;
    }
    .spinner {
        width: 25%;
        height: 25%;
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