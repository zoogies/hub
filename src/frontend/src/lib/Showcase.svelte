<script>
    import IoIosPaper from 'svelte-icons/io/IoIosPaper.svelte'
    import FaSpotify from 'svelte-icons/fa/FaSpotify.svelte'
    import IoMdCodeDownload from 'svelte-icons/io/IoMdCodeDownload.svelte'
    import GoBeaker from 'svelte-icons/go/GoBeaker.svelte'
</script>
<main>
    <div class="showcase_top">
        <a href="https://zmuda.dev" class="block bg3 hvr-float hvr-fade slightshadow">
            <div class="icon">
                <IoIosPaper />
            </div>
            <p class="showcase_text">portfolio</p>
        </a>
        <a href="/spotiguess" class="block bg3 hvr-float hvr-fade slightshadow">
            <div class="icon">
                <FaSpotify />
            </div>
            <p class="showcase_text">spotiguess</p>
        </a>
        <a href="/gifapi" class="block bg3 hvr-float hvr-fade slightshadow">
            <div class="icon">
                <IoMdCodeDownload />
            </div>
            <p class="showcase_text">gif api</p>
        </a>
        <a href="/playground" class="block bg3 hvr-float hvr-fade slightshadow">
            <div class="icon">
                <GoBeaker />
            </div>
            <p class="showcase_text">playground</p>
        </a>
    </div>
</main>
<style>
    .showcase_text{
        margin: 0px;
        text-align: center;
    }
    .showcase_top{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        align-content: center;
        justify-content: center;
        width: 100%;
    }
    .block {
        border-radius: 10px;
        width: 45%;
        height: 100px;
        display: flex;
        margin: 7px;
        align-items: center;
        align-content: center;
        justify-content: center;
        flex-wrap: wrap;
    }
    .icon {
        color: rgb(255, 255, 255);
        width: 50px;
        height: 50px;
        margin: 10px;
    }
</style>