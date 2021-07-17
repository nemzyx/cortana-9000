<script>
    import Camera from '$lib/Camera.svelte'
</script>

<svelte:head>
	<title>Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</svelte:head>

    
<div class="m-5" style="text-align: center">
    <h1>Setup vaccine</h1>

    <div class="card p-5">
        <h2 class="card-text">Cortana</h2>

        <form action="#" method="post" enctype="multipart/form-data">
            <div class="form-group" style="display:flex;">
                <label>🖊 Write here:</label>
                <input type="text" name="title" class="form-control" value="">
                <span class="invalid-feedback">Dab on the haters</span>
                <input type="submit" class="btn btn-primary" value="Submit">
            </form>
        </div>
        
    </div>
    <Camera />
    
<style>
</style>
