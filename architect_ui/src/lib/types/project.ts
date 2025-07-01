export interface Blackboard {
	id: number;
	title: string;
	content: string;
	parent_blackboard_id: number | null;
	child_blackboards: Blackboard[];
}

export interface Project {
	id: number;
	name: string;
	description: string;
	title: string;
	root_blackboard: Blackboard;
} 