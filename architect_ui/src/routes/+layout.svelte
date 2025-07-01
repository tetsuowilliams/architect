<script lang="ts">
	import '../app.css';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	let projects: Array<{
		id: number;
		name: string;
		description: string;
		title: string;
	}> = [];
	let loading = true;
	let error = false;
	let errorMessage = '';

	async function fetchProjects() {
		loading = true;
		error = false;
		errorMessage = '';
		
		try {
			console.log('Fetching projects from API...');
			const response = await fetch('http://localhost:8000/api/v1/get_all_projects', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
				},
			});
			
			console.log('Response status:', response.status);
			console.log('Response headers:', response.headers);
			
			if (response.ok) {
				const data = await response.json();
				console.log('Projects data:', data);
				projects = data;
			} else {
				error = true;
				errorMessage = `HTTP ${response.status}: ${response.statusText}`;
				console.error('API request failed:', response.status, response.statusText);
			}
		} catch (err) {
			error = true;
			errorMessage = err instanceof Error ? err.message : 'Network error';
			console.error('API request error:', err);
		} finally {
			loading = false;
		}
	}

	onMount(() => {
		fetchProjects();
	});
</script>

<div class="app">
	<!-- Sidebar -->
	<aside class="sidebar">
		<div class="sidebar-header">
			<h1 class="app-title">Architect</h1>
		</div>
		<nav class="sidebar-nav">
			<!-- Projects Section -->
			<div class="nav-section">
				<h3 class="nav-section-title">Projects</h3>
				{#if loading}
					<div class="nav-loading">
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M21 12a9 9 0 11-6.219-8.56"/>
						</svg>
						Loading...
					</div>
				{:else if error}
					<div class="nav-error" title={errorMessage}>
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<circle cx="12" cy="12" r="10"/>
							<line x1="15" y1="9" x2="9" y2="15"/>
							<line x1="9" y1="9" x2="15" y2="15"/>
						</svg>
						Failed to load
					</div>
					<button class="nav-retry" on:click={fetchProjects} aria-label="Retry loading projects">
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M21 12a9 9 0 11-6.219-8.56"/>
						</svg>
						Retry
					</button>
				{:else if projects.length === 0}
					<div class="nav-empty">
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
							<polyline points="14,2 14,8 20,8"/>
						</svg>
						No projects
					</div>
				{:else}
					{#each projects as project}
						<a 
							href="/project/{project.id}" 
							class="nav-item nav-project" 
							class:active={$page.url.pathname === `/project/${project.id}`}
						>
							<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
								<polyline points="14,2 14,8 20,8"/>
							</svg>
							<div class="nav-project-info">
								<span class="nav-project-name">{project.name}</span>
								<span class="nav-project-title">{project.title}</span>
							</div>
						</a>
					{/each}
				{/if}
			</div>
		</nav>
	</aside>

	<!-- Main content area -->
	<main class="main-content">
		<!-- Header -->
		<header class="header">
			<div class="header-content">
				<h2 class="page-title">
					{#if $page.url.pathname.startsWith('/project/')}
						Project
					{:else}
						Architect
					{/if}
				</h2>
				<div class="header-actions">
					<button class="btn btn-secondary" aria-label="Export">
						<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M15 17h5l-5 5v-5z"/>
							<path d="M4.19 4.19A4 4 0 0 0 6 3h10a4 4 0 0 1 4 4v10a3.97 3.97 0 0 1-1.172 2.828"/>
							<path d="M10.172 10.172a4 4 0 0 1 0 5.656"/>
							<rect x="2" y="2" width="20" height="20" rx="2.5"/>
						</svg>
					</button>
					<button class="btn btn-secondary" aria-label="Notifications">
						<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
							<path d="M13.73 21a2 2 0 0 1-3.46 0"/>
						</svg>
					</button>
					<div class="user-avatar" role="button" tabindex="0" aria-label="User menu">
						<svg class="avatar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
							<circle cx="12" cy="7" r="4"/>
						</svg>
					</div>
				</div>
			</div>
		</header>

		<!-- Page content -->
		<div class="page-content">
			<slot />
		</div>
	</main>
</div> 