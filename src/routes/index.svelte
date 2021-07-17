<script context="module">
	export const prerender = true
</script>

<script>
	import { fade } from 'svelte/transition'
	import { onMount } from 'svelte'

	let showGreet = false
	let greeting = ''
	let inputText = ''
	let inputUpdated = false
	let displayInput = false
	let speedUp = true
	let inputField
	let elem

	onMount(() => {
		/* Get the documentElement (<html>) to display the page in fullscreen */
		elem = document.documentElement

		/* View in fullscreen */
		function openFullscreen() {
			console.log(elem.requestFullscreen)
			if (elem.requestFullscreen) {
				elem.requestFullscreen()
			} else if (elem.webkitRequestFullscreen) {
				/* Safari */
				elem.webkitRequestFullscreen()
			} else if (elem.msRequestFullscreen) {
				/* IE11 */
				elem.msRequestFullscreen()
			}
		}

		openFullscreen()
	})

	// Default time = time to show the slide
	function Slide(text, show, time = 1500) {
		return new Promise((resolve) => {
			setTimeout(
				() => {
					greeting = text
					showGreet = show
					resolve('resolved')
					console.log('Promise ran with: ' + text)
				},
				speedUp ? time * 0.1 : time,
			)
		})
	}

	function timeout(ms) {
		return new Promise((resolve) => {
			setTimeout(() => {
				resolve('resolved')
			}, ms)
		})
	}

	function ShowInput() {
		// inputField.value = ''
		displayInput = true
	}

	function HandleInput() {}

	async function AwaitUserInput() {
		console.log('Awaiting user input.')
		while (!inputUpdated) await timeout(50)
		inputUpdated = false
		displayInput = false
	}

	async function AwaitPermitCamera() {
		await Slide('', false, 4000)
		await Slide("it's just to check your answer", false)
		await Slide('', false, 6000)
		await Slide('please allow me to use the camera', false)
	}

	let run = async () => {
		await Slide('hello', true)
		await Slide('', false, 3000)
		await Slide("let's design your vaccine DNA", true)
		await Slide('', false, 5000)
		await Slide("I'll just ask some questions", true)
		await Slide('', false, 5000)
		await Slide('I just need access to the camera', true)
		await AwaitPermitCamera()
		await Slide('', false, 100)
		await Slide('what is your age?', true)
		ShowInput()
		await AwaitUserInput()
		await HandleInput()
		await Slide('', false, 100)
		await Slide('what is your gender?', true)
		ShowInput()
		await AwaitUserInput()
	}

	run()
</script>

<svelte:head>
	<title>Windows 11</title>
</svelte:head>

<section>
	<img class="cortana" src="/cortana.gif" />
	{#if showGreet}
		<div class="greet" transition:fade>{greeting}</div>
	{:else}
		<div class="greet" />
	{/if}
	<input
		type="text"
		bind:this={inputField}
		style="display: {displayInput ? 'block' : 'none'};"
		name="title"
		class="form-control"
		bind:value={inputText}
		on:change={() => {
			inputUpdated = true
			console.log('Input updated')
		}}
	/>
</section>

<style lang="postcss">
	section {
		padding-top: 30vh;
		display: flex;
		flex-direction: column;
		align-items: flex-center;
		place-items: center;
		min-height: 100vh;
		background: #0e0e0e;
		text-align: center;
		color: #38acc1;

		.greet {
			font-size: 6rem;
			line-height: 6rem;
			height: 10rem;
		}

		.process-bar {
			display: flex;
			bottom: 0px;
			height: 5vh;
			position: absolute;
			padding: 1vh;

		input {
			background: #ffffff05;
			border: 1px #e7f3fd5b solid;
			height: 3rem;
			width: 30rem;
			font-size: 2rem;
			text-align: center;
		}
	}
</style>
