<script>
    import HomePanel from "./HomePanel.svelte";
    import ServerStats from "./ServerStats.svelte";
    import Showcase from "./Showcase.svelte";
</script>
<main>
    <div class="main_content">
        <HomePanel content={ServerStats}/>
        <HomePanel content={Showcase}/>
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