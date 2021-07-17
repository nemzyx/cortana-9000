<script context="module">
	export const prerender = true
</script>

<script>
	import { onMount } from 'svelte'
	import { clickStart, debug } from '$lib/state'
	import Slides from '$lib/Slides.svelte'
	
	debug.set(true)

	// Store variables
	let clickStart_tracker
	clickStart.subscribe((val) => clickStart_tracker = val)

</script>

<svelte:head>
	<title>Windows 11</title>
</svelte:head>

<section>

	<Slides />

	<div class="process-bar">
		<a href="#" on:click={() => {clickStart.set(!clickStart_tracker)}}><img src="windows-icon.jpg" alt="windows icon"/></a>
	</div>
</section>

<style lang="postcss">
	section {
		padding-top: 30vh;
		display: flex;
		flex-direction: column;
		align-items: flex-center;
		place-items: center;
		min-height: 100vh;
		background: #0E0E0E;
		text-align: center;
		color: #38ACC1;

		.process-bar {
			display: flex;
			bottom: 0px;
			height: 5vh;
			position: absolute;
			padding: 1vh;

			img {
				height: 4vh;
			}
		}
	}
</style>
