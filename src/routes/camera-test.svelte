<script context="module">
	export const prerender = true;
</script>

<script>
	import Camera from 'easy-js-camera';

    if(Camera.isCameraSupported()) {

        var video = document.getElementsByTagName('video')[0];
        var canvas = document.getElementsByTagName('canvas')[0];
        
        Camera
            .tryInvokePermission(video, canvas)
            .then(camera => {
                camera.start()
            })
            .catch(error => {
                // Mostly happens if the user blocks the camera or the media devices are not supported
                alert("Alright, no camera support.")
            });
    } else {
        alert("Webcam not supported!")
    }
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<section>
	<h1>YEET your way to success!</h1>

	<h2>You damn boi, here's some camera:</h2>

    <video autoplay playsinline></video>
    <canvas></canvas>


</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 1;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
