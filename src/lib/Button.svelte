<script>
	let clazz
	export { clazz as class }
</script>

<button class={clazz}>
	<slot />
</button>

<style lang="postcss" module>
	button {
		@apply bg-green-600 text-white px-6 py-3;
		&:hover:not(:active):not(:focus) {
			@apply bg-green-400;
		}

		@apply transform;
		&:active {
			@apply scale-[103%];
		}
	}
</style>
