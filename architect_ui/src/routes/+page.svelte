<script lang="ts">
	// Welcome page component
</script>

<div class="welcome-page">
	<div class="welcome-content">
		<svg class="welcome-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
			<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
			<polyline points="14,2 14,8 20,8"/>
		</svg>
		<h1>Welcome to Architect</h1>
		<p>Select a project from the sidebar to get started.</p>
	</div>
</div>

<style>
	.welcome-page {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 60vh;
	}

	.welcome-content {
		text-align: center;
		max-width: 400px;
	}

	.welcome-icon {
		width: 80px;
		height: 80px;
		margin-bottom: 24px;
		color: #d1d5db;
	}

	.welcome-content h1 {
		margin: 0 0 16px 0;
		font-size: 32px;
		font-weight: 700;
		color: #111827;
	}

	.welcome-content p {
		margin: 0;
		font-size: 18px;
		color: #6b7280;
		line-height: 1.5;
	}
</style>
