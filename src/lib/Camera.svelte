<script>
	// import Instacam from 'instacam'
	import { onMount } from 'svelte'
	let cameraRender
	onMount(async () => {
		const Instacam = await import('instacam').then((res) => res.default)
		new Instacam(cameraRender)
	})
</script>

<canvas bind:this={cameraRender} />