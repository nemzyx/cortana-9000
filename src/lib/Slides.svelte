<script>
	import { fade } from 'svelte/transition'
    import { debug } from '$lib/state.js'
	import { onMount } from 'svelte'

    // Slideshow variables
	let showGreet = false
	let greeting = ''
	let inputText = ''
	let inputUpdated = false
	let displayInput = false
	let inputField
	let utteranceOn = false

    let speedUp = true

    // Default time = time to show the slide
	function Slide(text, show, time = 1500) {
		return new Promise((resolve) => {
				setTimeout(() => {
					greeting = text
					showGreet = show
					resolve("resolved")
					console.log("Promise ran with: " + text)
					utteranceOn ? new SpeechSynthesisUtterance(text).speak() : console.log("Utterance off")
			}, (speedUp ? time * 0.1 : time))
		})
	}

	function timeout(ms) {
		return new Promise((resolve) => {
			setTimeout(() => {
				resolve("resolved")
			}, ms)
		})
	}

	function ShowInput() {
		inputField.value = ''
		displayInput = true
	}

	function HandleInput() {

	}

	async function AwaitUserInput() {
		console.log("Awaiting user input.")
		while(!inputUpdated) await timeout(50)
		inputUpdated = false
		displayInput = false
	}

	async function AwaitPermitCamera() {
		await Slide('', false, 4000)
		await Slide('it\'s just to check your answer', false)
		await Slide('', false, 6000)
		await Slide('please allow me to use the camera', false)
	}

	let slidesRun = async () => {
		await Slide('hello', true)
		await Slide('', false, 3000)
		await Slide('let\'s design your vaccine DNA', true)
		await Slide('', false, 5000)
		await Slide('I\'ll just ask some questions', true)
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
	slidesRun()
</script>

<button on:click={utteranceOn=!utteranceOn}>Sound {utteranceOn ? 'on' : 'off'}</button>
<img class="cortana" src="/cortana.gif" alt="Cortana"></img>
{#if showGreet}
    <div class="greet" transition:fade>{greeting}</div>
{:else}
    <div class="greet"></div>
{/if}
<input type="text" bind:this={inputField} style="display: {displayInput ? 'block' : 'none'};" name="title" class="form-control" bind:value={inputText} on:change={() => {inputUpdated=true; console.log("Input updated");}}>

<style lang="postcss">
    .greet {
        font-size: 6rem;
        line-height: 6rem;
        height: 10rem;
    }

    .cortana {
        width: 15%;
        height: auto;
    }

    input {
        background: #ffffff05;
        border: 1px #e7f3fd5b solid; 
        height: 3rem;
        width: 30rem;
        font-size: 2rem;
        text-align: center;
    }
</style>