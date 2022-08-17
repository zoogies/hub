<script>
    export let content;
</script>
<main>
    <div class="bg2 slightshadow home_panel">
        <svelte:component class="fill" this={content}></svelte:component>
    </div>
</main>
<style>
    .home_panel{
        margin: 20px;
        max-width: 600px;
        max-height: 600px;
        min-width: 300px;
        min-height: 300px;
        border-radius: 10px;
        width: 70vw;
        height: 70vw;
    }
</style>