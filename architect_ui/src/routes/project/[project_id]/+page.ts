import type { PageLoad } from './$types';
import type { Project } from '$lib/types/project';

export const load: PageLoad = async ({ params, fetch }) => {
	const projectId = params.project_id;
	
	try {
		const response = await fetch(`http://localhost:8000/api/v1/get_project_tree_with_id?id=${projectId}`);
		
		if (response.ok) {
			const project: Project = await response.json();
			return {
				projectId,
				project
			};
		} else {
			throw new Error(`HTTP ${response.status}: ${response.statusText}`);
		}
	} catch (error) {
		console.error('Failed to fetch project:', error);
		return {
			projectId,
			project: null,
			error: error instanceof Error ? error.message : 'Failed to load project'
		};
	}
}; 