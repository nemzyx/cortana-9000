<script context="module">
	export const prerender = true
</script>

<script>
	import { fade } from 'svelte/transition'

	let showGreet = false

	let greeting = ''

	let greet = (content, delay, time) => {
		setTimeout(() => {
			greeting = 'hello'
			showGreet = true
		}, delay * 10)
		setTimeout(() => {
			greeting = ''
			showGreet = false
		}, (delay + time) * 10)
	}
	
	// Default time = showtime
	function Slide(text, show, time = 1500) {
		return new Promise((resolve) => {
				setTimeout(() => {
				greeting = text
				showGreet = show
				resolve("resolved")
				console.log("Promise ran with: " + text)
			}, time)
		})
	}

	let run = async () => {
		await Slide('hello', true)
		await Slide('', false, 3000)
		await Slide('let\'s design your vaccine', true)
		await Slide('', false, 5000)
		await Slide('I\'ll just ask some questions', true)
		await Slide('', false, 5000)
	}

	run()

</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<section>
	<img class="cortana" src="/cortana.gif" />
	{#if showGreet}
		<div class="greet" transition:fade>{greeting}</div>
	{/if}
	{#if !showGreet}
		<div class="greet"> </div>
	{/if}
</section>

<style lang="postcss">
	section {
		display: flex;
		flex-direction: column;
		align-items: flex-center;
		place-items: center;
		min-height: 100vh;
		background: #0E0E0E;
		color: white;
		text-align: center;
		
		.greet {
			color: #289CC1;
			font-size: 6rem;
			line-height: 6rem;
		}

		.cortana {
			width: 15%;
			height: auto;
		}
	}
</style>
