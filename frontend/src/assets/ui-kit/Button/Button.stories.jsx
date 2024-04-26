import Button from './Button';

export default {
	title: 'Button',
	tags: ['autodocs'],
	component: Button,
};

export const DefaultLargeButton = {
	args: {
		text: 'войти',
		type: 'button',
	},
};

export const DefaultMediumButton = {
	args: {
		text: 'добавить кофейню',
		type: 'button',
		size: 'medium',
	},
};

export const SearchButton = {
	args: {
		text: 'найти',
		type: 'button',
		size: 'small',
	},
};
