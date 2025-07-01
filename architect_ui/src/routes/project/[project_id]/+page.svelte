<script lang="ts">
	import type { PageData } from './$types';
	import Blackboard from '$lib/components/Blackboard.svelte';
	import { writable, type Writable } from 'svelte/store';
	import type { Blackboard as BlackboardType } from '$lib/types/project';
	import { onDestroy } from 'svelte';

	export let data: PageData;

	$: projectId = data.projectId;
	$: project = data.project;
	$: error = data.error;

	// Selected blackboard state (id only)
	let selectedId: number | null = null;
	let selectedBlackboard: any = null;
	let loadingBlackboard = false;
	let blackboardError: string | null = null;
	let abortController: AbortController | null = null;

	async function fetchBlackboard(id: number) {
		loadingBlackboard = true;
		blackboardError = null;
		selectedBlackboard = null;
		if (abortController) abortController.abort();
		abortController = new AbortController();
		try {
			const res = await fetch(`http://localhost:8000/api/v1/get_blackboard_with_id?id=${id}`, {
				signal: abortController.signal
			});
			if (!res.ok) throw new Error('Failed to fetch blackboard');
			selectedBlackboard = await res.json();
		} catch (e) {
			if (e.name !== 'AbortError') blackboardError = e.message;
		} finally {
			loadingBlackboard = false;
		}
	}

	function handleSelect(blackboard) {
		selectedId = blackboard.id;
		fetchBlackboard(blackboard.id);
	}

	onDestroy(() => {
		if (abortController) abortController.abort();
	});
</script>

<div class="project-page-3col">
	{#if error}
		<div class="error-state">
			<svg class="error-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="12" cy="12" r="10"/>
				<line x1="15" y1="9" x2="9" y2="15"/>
				<line x1="9" y1="9" x2="15" y2="15"/>
			</svg>
			<h2>Failed to load project</h2>
			<p>{error}</p>
		</div>
	{:else if project}
		<div class="project-header">
			<h1>{project.name}</h1>
			<p class="project-title">{project.title}</p>
			<p class="project-description">{project.description}</p>
		</div>
		<div class="main-3col">
			<!-- Left: Blackboard tree -->
			<div class="tree-col">
				<Blackboard
					blackboard={project.root_blackboard}
					isRoot={true}
					selectedId={selectedId}
					onSelect={handleSelect}
				/>
			</div>
			<!-- Center: Blackboard content -->
			<div class="content-col">
				{#if loadingBlackboard}
					<div class="loading-state"><span>Loading blackboard...</span></div>
				{:else if blackboardError}
					<div class="error-state"><span>{blackboardError}</span></div>
				{:else if selectedBlackboard}
					<div class="blackboard-card-formal">
						<h2>{selectedBlackboard.title}</h2>
						<p>{selectedBlackboard.content}</p>
					</div>
				{:else}
					<div class="placeholder">Select a blackboard to view its content</div>
				{/if}
			</div>
			<!-- Right: Messages -->
			<div class="messages-col">
				{#if selectedBlackboard && selectedBlackboard.messages && selectedBlackboard.messages.length}
					<div class="messages-list">
						<h3>Messages</h3>
						<ul>
							{#each selectedBlackboard.messages as msg}
								<li class="message-item">
									<div class="msg-content">{msg.content}</div>
									<div class="msg-meta">{msg.sender.name} ({msg.sender.role})</div>
								</li>
							{/each}
						</ul>
					</div>
				{:else if selectedBlackboard}
					<div class="placeholder">No messages</div>
				{/if}
			</div>
		</div>
	{:else}
		<div class="loading-state">
			<svg class="loading-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M21 12a9 9 0 11-6.219-8.56"/>
			</svg>
			<h2>Loading project...</h2>
		</div>
	{/if}
</div>

<style>
	.project-page-3col {
		max-width: 1200px;
	}
	.main-3col {
		display: flex;
		gap: 32px;
		align-items: flex-start;
	}
	.tree-col {
		flex: 0 0 220px;
		min-width: 120px;
	}
	.content-col {
		flex: 1 1 0;
		max-width: 420px;
	}
	.messages-col {
		flex: 0 0 260px;
		min-width: 180px;
	}
	.blackboard-card-formal {
		background: #fff;
		border: 1.5px solid #e5e7eb;
		border-radius: 16px;
		box-shadow: 0 2px 8px 0 rgba(0,0,0,0.07);
		padding: 24px 28px;
		margin-bottom: 16px;
	}
	.blackboard-card-formal h2 {
		margin: 0 0 12px 0;
		font-size: 22px;
		font-weight: 700;
		color: #4b2995;
	}
	.blackboard-card-formal p {
		font-size: 16px;
		color: #22223b;
		margin: 0;
	}
	.messages-list {
		background: #f8f7fa;
		border-radius: 12px;
		padding: 16px 12px;
		box-shadow: 0 1px 3px 0 rgba(0,0,0,0.04);
	}
	.messages-list h3 {
		margin: 0 0 10px 0;
		font-size: 16px;
		font-weight: 600;
		color: #4b2995;
	}
	.messages-list ul {
		list-style: none;
		padding: 0;
		margin: 0;
	}
	.message-item {
		margin-bottom: 12px;
		padding-bottom: 8px;
		border-bottom: 1px solid #ececec;
	}
	.message-item:last-child {
		border-bottom: none;
	}
	.msg-content {
		font-size: 14px;
		color: #22223b;
	}
	.msg-meta {
		font-size: 12px;
		color: #6b7280;
		margin-top: 2px;
	}
	.placeholder {
		color: #b0b0b0;
		font-size: 15px;
		padding: 24px 0;
		text-align: center;
	}
	.project-header {
		margin-bottom: 32px;
	}
	.project-header h1 {
		margin: 0 0 8px 0;
		font-size: 32px;
		font-weight: 700;
		color: #111827;
	}
	.project-title {
		margin: 0 0 8px 0;
		font-size: 18px;
		font-weight: 600;
		color: #374151;
	}
	.project-description {
		margin: 0;
		color: #6b7280;
		font-size: 16px;
		line-height: 1.5;
	}
	.error-state,
	.loading-state {
		text-align: center;
		padding: 60px 20px;
		color: #6b7280;
	}
	.error-icon,
	.loading-icon {
		width: 64px;
		height: 64px;
		margin-bottom: 16px;
		color: #d1d5db;
	}
	.loading-icon {
		animation: spin 1s linear infinite;
	}
	@keyframes spin {
		from {
			transform: rotate(0deg);
		}
		to {
			transform: rotate(360deg);
		}
	}
	.error-state h2,
	.loading-state h2 {
		margin: 0 0 8px 0;
		font-size: 18px;
		font-weight: 600;
		color: #374151;
	}
	.error-state p {
		margin: 0;
		font-size: 14px;
	}
</style> 