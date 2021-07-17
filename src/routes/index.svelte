<script context="module">
	export const prerender = true
</script>

<script>
	import { fade } from 'svelte/transition'

	let showGreet = false

	let greeting = ''

	const greet = (content, delay, time) => {
		setTimeout(() => {
			greeting = 'hello'
		}, delay * 10)
		setTimeout(() => {
			greeting = ''
		}, (delay + time) * 10)
	}
	
	// Default time = showtime
	function Slide(text, show, time = 1500) {
		setTimeout(() => {
			greeting = text
			showGreet = show
		}, time)
	}

	Slide('hello', true)
	Slide('', false, 3000)
	Slide('let\'s design your vaccine', true)
	Slide('', false, 6000)
	Slide('I\'ll just ask some questions', true)
	Slide('', false, 6000)
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<section>
	{#if showGreet}
		<div class="greet" transition:fade>{greeting}</div>
	{/if}
</section>

<style lang="postcss">
	section {
		display: grid;
		place-items: center;
		min-height: 100vh;
		background: #287dc7;
		color: white;

		.greet {
			font-size: 10rem;
		}
	}
</style>
