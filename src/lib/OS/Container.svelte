<div class="oscontainer">
	<div class="desktop">
		<!-- <button> <img src="svg/outlook.png" /> </button>
		<button> <img src="svg/MSPaint.png" /> </button> -->
		<button> <img src="svg/outlook.png" /> <span>Outlook</span> </button>
		<button> <img src="svg/MSPaint.png" /> <span>Paint</span> </button>
	</div>
	<div class="status">
		<div class="process">
			<button> <img src="svg/start.svg" /> </button>
			<button> <img src="svg/outlook.png" /> </button>
			<button> <img src="svg/MSPaint.png" /> </button>
		</div>
	</div>
</div>

<style lang="postcss">
	$processHeight: 6rem;

	.oscontainer {
		width: 100vw;
		height: calc(100vh);

		background-image: url('11.jpeg');
		background-size: cover;
		background-position-x: center;

		position: relative;
		display: flex;
		flex-direction: column;
	}

	.desktop {
		flex: 1;
		width: 0;
		height: calc(100% - $processHeight);
		/* background: purple; */
		display: flex;
		flex-direction: column;
		flex-wrap: wrap;
		gap: 3.5rem;
		padding: 2rem;

		button {
			$desktopIconSize: 6rem;
			height: $desktopIconSize;
			width: $desktopIconSize;

			img {
				height: 100%;
				padding: 1.1rem;
				display: inline;
			}
			span {
				color: white;
				font-size: 1.2rem;
				position: relative;
				bottom: 0.4rem;
			}
		}
	}

	.process {
		background: white;
		padding: 0 8rem;
		height: $processHeight;
		margin: auto;
		display: flex;
		border-radius: 10px 10px 0 0;
		position: absolute;
		bottom: 0;

		button {
			width: 7rem;

			img {
				height: 100%;
				padding: 1.1rem;
				display: inline;
			}
		}

		&:after {
			content: '';
			display: block;
			background: purple;
			height: 10px;
			width: 10px;
			position: absolute;
			bottom: calc($processHeight / 3);
			left: 0;
			transform: translateX(-100%);
		}
	}

	.status {
		position: relative;
		width: 100%;
		display: flex;
		justify-content: center;
		height: calc($processHeight / 3);
		background: white;
	}

	button {
		img {
			transition: 300ms;
		}
		&:hover {
			img {
				transform: scale(1.1);
				transition: 180ms;
			}
		}
		&:active {
			img {
				transform: scale(1.2);
				transition: 25ms;
			}
		}
	}
</style>
