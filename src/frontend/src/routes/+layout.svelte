<script>
	import Clock from '$lib/Clock.svelte'
	import logo from '$lib/assets/icon_256_trans.png'
	import '../styles/global.css'
</script>
<main>

    <div id="header" class="bg2 shadow">
        <div class="title">
            <img id="header_logo" alt="logo" src={logo}/>
            <h1 id="header_title">Zoogies</h1>
        </div>
        <div class="clock">
            <Clock/>
        </div>
    </div>

	<slot/>

</main>
<style>
	#header{
		width: 100%;
		height: 70px;
		margin: 0px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-between;
	}
	#header_title{
		margin: 0px;
		padding-left: 0px;
  		text-shadow: 2px 2px #000000;
	}
	#header_logo{
		width: 70px;
		height: 70px;
	}
	.title{
		display: flex;
		flex-direction: row;
		flex-wrap: nowrap;
		align-items: center;
	}
</style>