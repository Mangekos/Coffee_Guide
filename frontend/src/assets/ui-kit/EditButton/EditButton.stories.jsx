import EditButton from './EditButton';

import '../../../index.scss';

export default {
	title: 'EditButton',
	tags: ['autodocs'],
	component: EditButton,
};

export const DefaultEditButton = {
	args: {
		theme: 'light',
		size: 'default',
	},
};

export const SmallEditButton = {
	args: {
		theme: 'light',
		size: 'small',
	},
};
