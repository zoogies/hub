<script>
    import Button from "../../lib/Button.svelte";
    import Error from "../../lib/Error.svelte";
    import Loading from "../../lib/Loading.svelte";
    import axios from 'axios';

    const ip = 'https://zoogies.live' //import.meta.env.VITE_SERVER_IP;

    var state = 'blank';
    var error = false;
    var loading = false;
    var gifs = 'unset';
    
    function getgifs(){
        state = 'display';
        loading = true;
        axios.get(ip + '/api/mitsuri/getgifs')
        .then(function (response) {
            gifs = response.data
            loading = false;
        })
        .catch(function (error) {
            error = true;
        });
    }
    function synctab(){
        state = 'sync';
    }
    function copytext(){
        document.getElementById('output').select(); // highlight the text from the hidden input element
        document.execCommand('copy'); // use some depracated copy command (the only one that works)
        alert('output copied!'); // generic alert
        document.getSelection().collapseToEnd(); // remove the selection so you cant see the hidden text
    }
    
</script>
<h1 style="text-align: center;">Ryan's Saved Gif Web Interface</h1>
<div class="top">
    <div style="margin: 20px;" on:click={getgifs}>
        <Button label={"Display gifs"}/>
    </div>
    <!-- <div style="margin: 20px;" on:click={synctab}>
        <Button label={"Sync gifs"}/>
    </div> -->
    <!-- TODO preview all gifs online big imageboard -->
</div>
{#if state === 'display'}
    {#if error}
        <Error message={"Error Loading Gifs"} description={"please try another time ;-;"}/>
    {:else if loading}
        <Loading/>
        <div class="spinner"></div>
    {:else}
        <div class="output_header">
            <h2 style="text-align: center;">Full output below:</h2>
                <div on:click={copytext} style="margin:20px">
                    <Button label={"Copy Output"}/>
                </div>
        </div>
        
        <div class="json_output bg2 slightshadow">
            <code>{JSON.stringify(gifs)}</code>
        </div>
        <input type="text" id="output" name="output" value={JSON.stringify(gifs)} readonly>
    {/if}
{:else if state === 'sync'}
        <!-- TODO LEFTOFF HERE -->
        <!-- submit button and way to add credentials to request -->
        <div class="bg2 slightshadow json_output">
            <h2>Paste json string below:</h2>
            <textarea></textarea>
        </div>
{/if}

<style>
    .output_header {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        text-align: center;
        justify-content: center;
    }
    .json_output{
        margin: 40px;
        border-radius: 15px;
        padding: 30px;
        overflow-wrap: break-word;
        margin-top: 20px;
    }
    .top{
        margin: 20px;
        display: flex;
        flex-direction: row;
        justify-items: center;
        justify-content: center;
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
    #output{
        outline: none;
        border:none;
        background-image:none;
        background-color:transparent;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;  
        color: #212121;
    }
</style>