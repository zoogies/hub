<!-- YOINKED FROM: -->
<!-- https://svelte.dev/repl/f1437286b08d4890b9207180868ee37e?version=3.46.4 -->
<script>
	export let progress
	const angle = 360 * progress
	
	// Adapt the logic according to the approach
	const	background = `radial-gradient(white 50%, transparent 51%),
    conic-gradient(transparent 0deg ${angle}deg, gainsboro ${angle}deg 360deg),
    conic-gradient(orange 0deg, yellow 90deg, lightgreen 180deg, green);`;
	
	$: cssVarStyles = `--background:${background}`
</script>

<style>
#progress-circle {
  background: var(--background);
  border-radius: 50%;
  width: 120px;
  height: 120px;
	transition: all 500ms ease-in;
	will-change: transform;
}
</style>

<div id="progress-circle" style="{cssVarStyles}"></div>