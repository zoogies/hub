<script>
    import axios from 'axios';
    const ip = import.meta.env.VITE_SERVER_IP;
    var loaded = false;
    var error = true;
    var serverdata;
    var uptime_stamp;

    function getstats(){
        axios.get(ip + '/api/hub/getstats')
        .then(function (response) {
            serverdata = response.data;
            error = false;
            loaded = true;
            var uptime_seconds = Math.round(new Date() / 1000) - serverdata['boot-time'];
            uptime_stamp = (Math.floor(uptime_seconds/86400) + ":" + (new Date(uptime_seconds * 1000)).toISOString().substr(11, 8)).split(":");
            
        })
        .catch(function (error) {
            error = true;
            loaded = true;
        });
        setTimeout(getstats,3000) //TODO LOWER THIS FOR PROD BUT 1 SECOND LOOKS COOLER
    }
    getstats()
</script>

<div class="wrapper">
    {#if !loaded}
        <div class="spinner"></div>
    {:else}
        {#if error}
            <div class="error-fit">
                <h1 style="color: red;">Server is offline</h1>
                <p style="color: gray;">If you are seeing this message, something is seriously wrong ;-;</p>
            </div>
        {:else}

        <!--PUT A CASE FOR ERROR HERE-->
            <div class="internal-fit">
                <h1 class="green text-fit">Server: {serverdata['ip']}</h1>
                <p class="text-fit">Up For: {(`${uptime_stamp[0]}d ${uptime_stamp[1]}h ${uptime_stamp[2]}m ${uptime_stamp[3]}s` )}</p>

                <p class="text-fit">Load Average: {serverdata['load-average']}%</p>
                <progress class="pbar" max="100" value={serverdata['load-average']}/>
                <!-- <CircularProgressBar progress={serverdata['disk']['percent'] / 100}/> -->
                <p class="text-fit">Disk Usage: {serverdata['disk']['used']}GB/{serverdata['disk']['total']}GB</p>
                <progress class="pbar" max="100" value={serverdata['disk']['percent']}/>
                <!-- <CircularProgressBar progress={serverdata['memory']['percent'] / 100}/> -->
                <p class="text-fit">RAM Usage: {serverdata['memory']['used']}GB/{serverdata['memory']['total']}GB</p>
                <progress class="pbar" max="100" value={serverdata['memory']['percent']}/>
                <!-- <CircularProgressBar progress={serverdata['swap']['percent'] / 100}/> -->
                <p class="text-fit">Swap Usage: {serverdata['swap']['used']}GB/{serverdata['swap']['total']}GB</p>
                <progress class="pbar" max="100" value={serverdata['swap']['percent']}/>
                <!-- <CircularProgressBar progress={serverdata['load-average'] / 100}/> -->
            </div>
        {/if}
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
    .internal-fit {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        max-height: 400px;
    }
    .text-fit{
        margin: 0px;
        font-weight: 600;
        font-size: 15px;
    }
    .pbar{
        width: 100%;
        margin: 6px;
        margin-left: 0px;
        margin-right: 0px;
    }
    .error-fit{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-align: center;
    }
    .green{
        color: rgb(0, 233, 19);
    }
</style>