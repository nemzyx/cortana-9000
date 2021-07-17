<script>
	import Camera from '$lib/Camera.svelte'
	import ML from '$lib/ML.svelte'
</script>

<svelte:head>
	<title>Home</title>
	<link
		rel="stylesheet"
		href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
		crossorigin="anonymous"
	/>
</svelte:head>

<div class="m-5" style="text-align: center">
	<h1>Setup vaccine</h1>

	<ML />
	<Camera />
</div>

<style>
</style>
