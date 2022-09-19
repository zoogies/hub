<script>
	import Clock from '$lib/Clock.svelte'
	import logo from '$lib/assets/icon_256_trans.png'
	import '../styles/global.css'
</script>
<main>

    <div id="header" class="bg2 shadow">
        <a href="/" class="title hvr-grow-rotate">
            <img id="header_logo" alt="logo" src={logo}/>
            <h1 id="header_title">Zoogies</h1>
        </a>
        <div class="clock">
            <Clock/>
        </div>
    </div>

	<slot/>

	<div class="footer">
		<p>Beta Release 9.18.22</p>
		<p>Ryan Zmuda</p>
		<a href="https://github.com/Yoyolick/hub/issues">report an issue</a>
	</div>
</main>
<style>
	.footer{
		display: flex;
		width: 100%;
		flex-direction: column;
		margin: 0px;
		padding-bottom: 50px;
	}
	.footer > p {
		margin: 0px;
		text-align: center;
		color: rgb(138, 138, 138);
		font-weight: 300;
	}
	.footer > a {
		margin: 0px;
		text-align: center;
		color: rgb(255, 255, 255);
		text-decoration: underline;
		font-weight: 300;
	}
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