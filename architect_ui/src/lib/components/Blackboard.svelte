<script lang="ts">
	import type { Blackboard } from '$lib/types/project';
	
	export let blackboard: Blackboard;
	export let isRoot: boolean = false;
	export let selectedId: number | null = null;
	export let onSelect: (b: Blackboard) => void = () => {};
</script>

<div class="blackboard-tree">
	<div
		class="blackboard-card {selectedId === blackboard.id ? 'selected' : ''}"
		on:click={() => onSelect(blackboard)}
		tabindex="0"
		role="button"
		aria-pressed={selectedId === blackboard.id}
	>
		<p class="blackboard-title">{blackboard.title}</p>
		<p class="blackboard-content">{blackboard.content}</p>
	</div>
	{#if blackboard.child_blackboards && blackboard.child_blackboards.length > 0}
		<div class="blackboard-children">
			{#each blackboard.child_blackboards as childBlackboard (childBlackboard.id)}
				<svelte:self
					blackboard={childBlackboard}
					selectedId={selectedId}
					onSelect={onSelect}
				/>
			{/each}
		</div>
	{/if}
</div>

<style>
	.blackboard-tree {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		margin-bottom: 10px;
	}

	.blackboard-card {
		background: #fff;
		border: 1px solid #e5e7eb;
		border-radius: 12px;
		box-shadow: 0 1px 4px rgba(30, 41, 59, 0.06);
		padding: 8px 12px;
		min-width: 120px;
		max-width: 220px;
		text-align: left;
		z-index: 2;
		cursor: pointer;
		transition: box-shadow 0.15s, border-color 0.15s;
	}
	.blackboard-card.selected {
		border-color: #a78bfa;
		box-shadow: 0 0 0 2px #c7d2fe;
	}
	.blackboard-card:focus {
		outline: 2px solid #a78bfa;
	}

	.blackboard-title {
		margin: 0 0 4px 0;
		font-size: 13px;
		font-weight: 600;
		color: #4b2995;
		line-height: 1.2;
	}

	.blackboard-content {
		margin: 0;
		font-size: 12px;
		color: #6b7280;
		font-weight: 500;
		line-height: 1.4;
	}

	.blackboard-children {
		margin-left: 14px;
		margin-top: 4px;
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	@media (max-width: 600px) {
		.blackboard-card {
			padding: 6px 4px;
			min-width: 80px;
			max-width: 100%;
		}
		.blackboard-children {
			margin-left: 8px;
		}
	}
</style> 