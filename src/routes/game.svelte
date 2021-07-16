<script>
	import Button from '$lib/Button.svelte'
</script>

<div>
	<Button class="--btn">Load game</Button>
</div>

<style lang="postcss">
	div {
		@apply mt-[20rem];
	}

	:global(.--btn) {
		@apply block m-auto;
	}
</style>
