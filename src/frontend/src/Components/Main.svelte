<script>
    import HomePanel from "./HomePanel.svelte";
    import ServerStats from "./ServerStats.svelte";
</script>
<main>
    <div class="main_content">
        <HomePanel content={ServerStats}/>
    </div>
</main>
<style>
    .main_content{
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-evenly;
        margin: 30px;
    }
</style>