<script>
    import App from "../App.svelte";
    import axios from 'axios';
    var loaded = false;
    var serverdata;
    var uptime_stamp;

    function getstats(){
        axios.get('server_address/api/getstats')
        .then(function (response) {
            serverdata = response.data;
            loaded = true;
            var uptime_seconds = Math.round(new Date() / 1000) - serverdata['boot-time'];
            uptime_stamp = (Math.floor(uptime_seconds/86400) + ":" + (new Date(uptime_seconds * 1000)).toISOString().substr(11, 8)).split(":");
            
        })
        .catch(function (error) {
            console.log(error);
        });
        setTimeout(getstats,1000) //TODO LOWER THIS FOR PROD BUT 1 SECOND LOOKS COOLER
    }
    getstats()

    

</script>

<div class="wrapper">
    {#if !loaded}
        <div class="spinner"></div>
    {:else}
        <div class="text-fit">
            <h1 class="text-fit">Server: {serverdata['ip']}</h1>
            <p class="text-fit">Up For: {(`${uptime_stamp[0]} days, ${uptime_stamp[1]} hours, ${uptime_stamp[2]} minutes, ${uptime_stamp[3]} seconds` )}</p>
        </div>
    {/if}
</div>

<style>
    .wrapper{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: flex-start;
        align-content: center;
        align-items: center;
        flex-direction: column;
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
    @media screen and (min-width: 700px) {

    .text-fit {

    font-size: 25px;

    }

    }
    @media screen and (max-width: 430px) {

    .text-fit {

    font-size: 15px;

    }

}
</style>