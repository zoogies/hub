<!-- App.svelte -->
<script>
	import { Router, Route, Link } from "svelte-navigator";
	import Main from "./Components/Main.svelte";
</script>
<main>
	<Router>
		<div id="header" class="bg2 shadow">
			<h1 id="header_title">Zoogies</h1>
		</div>
		<Route path="/" component="{Main}"/>
		<Route component="{Main}" />
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
	}
	#header_title{
		margin: 0px;
		padding-left: 70px;
	}
</style>