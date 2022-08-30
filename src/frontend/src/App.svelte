<!-- App.svelte -->
<script>
	import { Router, Route, Link } from "svelte-navigator";
import Clock from "./Components/Clock.svelte";
	import Main from "./Components/Main.svelte";
</script>
<main>
	<Router>
		<div id="header" class="bg2 shadow">
			<div class="title">
				<img id="header_logo" alt="logo" src="./assets/icon_256_trans.png"/>
				<h1 id="header_title">Zoogies</h1>
			</div>
			<div class="clock">
				<Clock/>
			</div>
		</div>
		<Route path="/" component="{Main}"/>
		<Route component="{Main}" />
		<!-- <footer id="footer">
			<p>Created by Ryan Zmuda</p>
		</footer> -->
	</Router>
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
	/* yeah  */
</style>