import CloseButton from './CloseButton';

import '../../../index.scss';

export default {
	title: 'CloseButton',
	tags: ['autodocs'],
	component: CloseButton,
};

export const DefaultCloseButton = {
	args: {
		theme: 'light',
		size: 'default',
	},
};

export const SmallCloseButton = {
	args: {
		theme: 'light',
		size: 'small',
	},
};
