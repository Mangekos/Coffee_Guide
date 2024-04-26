import TagButton from './TagButton';

import { BASE_TAGS } from '../../../utils/constants';

import '../../../index.scss';

export default {
	title: 'TagButton',
	tags: ['autodocs'],
	component: TagButton,
};

export const DefaultTagButton = {
	args: {
		text: 'Button',
		tag: 'alternative',
		theme: 'light',
		type: 'button',
		active: false,
	},
};

export const DefaultTagButtonActive = {
	args: {
		text: 'Button',
		tag: 'alternative',
		theme: 'light',
		type: 'button',
		active: true,
	},
};
