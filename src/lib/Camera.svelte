<script>
	// import Instacam from 'instacam'
    import { onMount } from 'svelte'
	let cameraRender
	onMount(async () => {
		const Instacam = await import('instacam')
            // .then((res) => { console.log(res); return res.default; })
        
        let camera = new Instacam('camCanvas');
    })
</script>

<canvas id="camCanvas" />

<style>
    canvas {
        background-color: black;
    }

</style>